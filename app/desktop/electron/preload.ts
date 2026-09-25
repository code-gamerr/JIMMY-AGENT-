import { contextBridge, ipcRenderer, webFrame, webUtils } from 'electron'

// Which translucency the OS can back. Asked synchronously because the renderer
// needs it before its first paint, and answered by main because deciding it
// needs `os.release()` — a sandboxed preload may only require electron, events,
// timers and url, so importing node:os here throws before contextBridge runs
// and takes the ENTIRE bridge down with it (window.jimmyDesktop undefined =>
// "Desktop IPC bridge is unavailable"). No reply means no glass, which degrades
// to an ordinary opaque window rather than a page thinned over nothing.
const translucencySupport = ipcRenderer.sendSync('jimmy:translucency:support')

contextBridge.exposeInMainWorld('jimmyDesktop', {
  glassSupported: translucencySupport?.glass === true,
  translucencySupported: translucencySupport?.translucency === true,
  getConnection: profile => ipcRenderer.invoke('jimmy:connection', profile),
  // Registry-scoped backend resolution: { connectionId, profile } → descriptor.
  getConnectionFor: payload => ipcRenderer.invoke('jimmy:connection:for', payload),
  getProfileRoutes: profiles => ipcRenderer.invoke('jimmy:plugin-profile-routes', profiles),
  revalidateConnection: () => ipcRenderer.invoke('jimmy:connection:revalidate'),
  touchBackend: profile => ipcRenderer.invoke('jimmy:backend:touch', profile),
  getGatewayWsUrl: profile => ipcRenderer.invoke('jimmy:gateway:ws-url', profile),
  // Registry-scoped fresh WS URL: { connectionId, profile } → result shape of
  // getGatewayWsUrl, minted against that connection's backend.
  getGatewayWsUrlFor: payload => ipcRenderer.invoke('jimmy:gateway:ws-url-for', payload),
  // Union agent roster across every registered connection.
  getAgentRoster: () => ipcRenderer.invoke('jimmy:agents:roster'),
  openSessionWindow: (sessionId, opts) => ipcRenderer.invoke('jimmy:window:openSession', sessionId, opts),
  openSessionInTerminal: (sessionId, opts) => ipcRenderer.invoke('jimmy:window:openInTerminal', sessionId, opts),
  openWindow: () => ipcRenderer.invoke('jimmy:window:openInstance'),
  claimAmbientCue: key => ipcRenderer.invoke('jimmy:ambient:claim', key),
  wakeIndicator: {
    getState: () => ipcRenderer.invoke('jimmy:wake-indicator:get'),
    setState: state => ipcRenderer.send('jimmy:wake-indicator:set', state),
    onState: callback => {
      const listener = (_event, state) => callback(state)
      ipcRenderer.on('jimmy:wake-indicator:state', listener)

      return () => ipcRenderer.removeListener('jimmy:wake-indicator:state', listener)
    }
  },
  petOverlay: {
    // Main renderer → main process: window lifecycle + drag. `request` is
    // `{ bounds, screen }`; resolves with the screen bounds it actually used.
    open: request => ipcRenderer.invoke('jimmy:pet-overlay:open', request),
    close: () => ipcRenderer.invoke('jimmy:pet-overlay:close'),
    setBounds: bounds => ipcRenderer.send('jimmy:pet-overlay:set-bounds', bounds),
    setIgnoreMouse: ignore => ipcRenderer.send('jimmy:pet-overlay:ignore-mouse', ignore),
    // Flip the overlay focusable (and focus it) while the composer needs keys.
    setFocusable: focusable => ipcRenderer.send('jimmy:pet-overlay:set-focusable', focusable),
    // Main renderer → overlay (forwarded by main): push the latest pet state.
    pushState: payload => ipcRenderer.send('jimmy:pet-overlay:state', payload),
    // Overlay → main renderer (forwarded by main): pop back in / composer submit.
    control: payload => ipcRenderer.send('jimmy:pet-overlay:control', payload),
    // Overlay subscribes to state pushes.
    onState: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:pet-overlay:state', listener)

      return () => ipcRenderer.removeListener('jimmy:pet-overlay:state', listener)
    },
    // Main renderer subscribes to overlay control messages.
    onControl: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:pet-overlay:control', listener)

      return () => ipcRenderer.removeListener('jimmy:pet-overlay:control', listener)
    }
  },
  // HUD mode: the chrome-free floating chat. A full app renderer (own gateway)
  // sized as a floating bar, so it mounts the real composer. Main owns the
  // window; `onChanged` keeps every window's toggle truthful.
  hud: {
    open: request => ipcRenderer.invoke('jimmy:hud:open', request),
    close: () => ipcRenderer.invoke('jimmy:hud:close'),
    setIgnoreMouse: ignore => ipcRenderer.send('jimmy:hud:ignore-mouse', ignore),
    moveBy: delta => ipcRenderer.send('jimmy:hud:move-by', delta),
    setBounds: bounds => ipcRenderer.send('jimmy:hud:set-bounds', bounds),
    // Whether the band covers the window below the bar. Main pairs it with the
    // user's translucency setting to decide the native frost (macOS vibrancy /
    // Windows 11 DWM backdrop) — see hudFrostFor.
    setFrost: showing => ipcRenderer.invoke('jimmy:hud:frost', showing),
    // The HUD tells main which session it is on; main hands that back to the
    // app window when the HUD closes, so the app can re-home onto it.
    setSession: sessionId => ipcRenderer.send('jimmy:hud:session', sessionId),
    onGoto: callback => {
      const listener = (_event, sessionId) => callback(sessionId)
      ipcRenderer.on('jimmy:hud:goto', listener)

      return () => ipcRenderer.removeListener('jimmy:hud:goto', listener)
    },
    onChanged: callback => {
      const listener = (_event, state) => callback(state)
      ipcRenderer.on('jimmy:hud:changed', listener)

      return () => ipcRenderer.removeListener('jimmy:hud:changed', listener)
    },
    // Linux only, and silent elsewhere: where the cursor is, in page
    // coordinates, or null when it has left the window. Stands in for the
    // mousemove that `setIgnoreMouseEvents(true, { forward: true })` delivers on
    // macOS and Windows but not here.
    onCursor: callback => {
      const listener = (_event, point) => callback(point)
      ipcRenderer.on('jimmy:hud:cursor', listener)

      return () => ipcRenderer.removeListener('jimmy:hud:cursor', listener)
    }
  },
  // Quick Entry: the global-hotkey mini composer window. Main owns the OS
  // shortcut + the persisted preference; the quick window only captures text
  // and hands it back, and the primary renderer submits it through the normal
  // prompt path.
  quickEntry: {
    getSettings: () => ipcRenderer.invoke('jimmy:quick-entry:settings:get'),
    setSettings: patch => ipcRenderer.invoke('jimmy:quick-entry:settings:set', patch),
    submit: payload => ipcRenderer.send('jimmy:quick-entry:submit', payload),
    dismiss: () => ipcRenderer.send('jimmy:quick-entry:dismiss'),
    // Primary renderer → main → quick window: gateway connection state + the
    // recent-session options the target picker offers. Main caches the latest
    // payload so a freshly spawned quick window starts from truth.
    pushState: payload => ipcRenderer.send('jimmy:quick-entry:state', payload),
    // Quick window subscribes to those pushes.
    onState: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:quick-entry:state', listener)

      return () => ipcRenderer.removeListener('jimmy:quick-entry:state', listener)
    },
    // Main → primary renderer: a submit captured by the quick window.
    onSubmit: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:quick-entry:submit', listener)

      return () => ipcRenderer.removeListener('jimmy:quick-entry:submit', listener)
    },
    // Main → quick window: you were just summoned (reset draft + refocus).
    onShown: callback => {
      const listener = () => callback()
      ipcRenderer.on('jimmy:quick-entry:shown', listener)

      return () => ipcRenderer.removeListener('jimmy:quick-entry:shown', listener)
    }
  },
  getBootProgress: () => ipcRenderer.invoke('jimmy:boot-progress:get'),
  getConnectionConfig: profile => ipcRenderer.invoke('jimmy:connection-config:get', profile),
  saveConnectionConfig: payload => ipcRenderer.invoke('jimmy:connection-config:save', payload),
  applyConnectionConfig: payload => ipcRenderer.invoke('jimmy:connection-config:apply', payload),
  testConnectionConfig: payload => ipcRenderer.invoke('jimmy:connection-config:test', payload),
  // v2 multi-connection registry: named agent sources (local / remote / cloud / ssh).
  connections: {
    list: () => ipcRenderer.invoke('jimmy:connections:list'),
    save: payload => ipcRenderer.invoke('jimmy:connections:save', payload),
    remove: id => ipcRenderer.invoke('jimmy:connections:remove', id),
    setPrimary: id => ipcRenderer.invoke('jimmy:connections:set-primary', id),
    setLaunchMode: mode => ipcRenderer.invoke('jimmy:connections:set-launch-mode', mode),
    setLastUsed: id => ipcRenderer.invoke('jimmy:connections:set-last-used', id),
    test: id => ipcRenderer.invoke('jimmy:connections:test', id),
    // Fan out `jimmy update` to every eligible registered connection.
    // Optional excludeIds skips rows the caller updates through another path.
    updateAll: options => ipcRenderer.invoke('jimmy:connections:update-all', options),
    // Registry lifecycle push (main → renderer): a connection was removed or
    // materially edited, so secondaries scoped to it must be disposed (and,
    // for edits, re-dialed at the new target).
    onChanged: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:connections:changed', listener)

      return () => ipcRenderer.removeListener('jimmy:connections:changed', listener)
    }
  },
  sshConfigHosts: () => ipcRenderer.invoke('jimmy:ssh-config:hosts'),
  sshResolveHost: host => ipcRenderer.invoke('jimmy:ssh-config:resolve', host),
  probeConnectionConfig: remoteUrl => ipcRenderer.invoke('jimmy:connection-config:probe', remoteUrl),
  oauthLoginConnectionConfig: remoteUrl => ipcRenderer.invoke('jimmy:connection-config:oauth-login', remoteUrl),
  oauthLogoutConnectionConfig: remoteUrl => ipcRenderer.invoke('jimmy:connection-config:oauth-logout', remoteUrl),
  // Jimmy Cloud: one portal login powers discovery + silent per-agent sign-in
  // (cloud-auto-discovery Phase 3).
  cloud: {
    status: () => ipcRenderer.invoke('jimmy:cloud:status'),
    login: () => ipcRenderer.invoke('jimmy:cloud:login'),
    logout: () => ipcRenderer.invoke('jimmy:cloud:logout'),
    discover: org => ipcRenderer.invoke('jimmy:cloud:discover', org),
    agentSignIn: dashboardUrl => ipcRenderer.invoke('jimmy:cloud:agent-sign-in', dashboardUrl)
  },
  profile: {
    get: () => ipcRenderer.invoke('jimmy:profile:get'),
    set: name => ipcRenderer.invoke('jimmy:profile:set', name)
  },
  api: request => ipcRenderer.invoke('jimmy:api', request),
  notify: payload => ipcRenderer.invoke('jimmy:notify', payload),
  requestMicrophoneAccess: () => ipcRenderer.invoke('jimmy:requestMicrophoneAccess'),
  readWindowBelow: () => ipcRenderer.invoke('jimmy:window:readBelow'),
  readFileDataUrl: filePath => ipcRenderer.invoke('jimmy:readFileDataUrl', filePath),
  readFileDataUrlForAttach: filePath => ipcRenderer.invoke('jimmy:readFileDataUrlForAttach', filePath),
  dataUrlReadMax: {
    get: () => ipcRenderer.invoke('jimmy:data-url-read-max:get'),
    set: maxMb => ipcRenderer.invoke('jimmy:data-url-read-max:set', maxMb)
  },
  readFileText: filePath => ipcRenderer.invoke('jimmy:readFileText', filePath),
  selectPaths: options => ipcRenderer.invoke('jimmy:selectPaths', options),
  selectSavePath: options => ipcRenderer.invoke('jimmy:selectSavePath', options),
  writeClipboard: text => ipcRenderer.invoke('jimmy:writeClipboard', text),
  readClipboard: () => ipcRenderer.invoke('jimmy:readClipboard'),
  saveGatewayFile: payload => ipcRenderer.invoke('jimmy:saveGatewayFile', payload),
  saveImageFromUrl: url => ipcRenderer.invoke('jimmy:saveImageFromUrl', url),
  contextMenuEdit: command => ipcRenderer.invoke('jimmy:context-menu:edit', command),
  contextMenuCopyImage: () => ipcRenderer.invoke('jimmy:context-menu:copy-image'),
  contextMenuSpellcheck: action => ipcRenderer.invoke('jimmy:context-menu:spellcheck', action),
  contextMenuGuestAddWord: payload => ipcRenderer.invoke('jimmy:context-menu:guest-add-word', payload),
  onContextMenuSpellcheck: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:context-menu-spellcheck', listener)

    return () => ipcRenderer.removeListener('jimmy:context-menu-spellcheck', listener)
  },
  saveImageBuffer: (data, ext) => ipcRenderer.invoke('jimmy:saveImageBuffer', { data, ext }),
  saveClipboardImage: () => ipcRenderer.invoke('jimmy:saveClipboardImage'),
  getPathForFile: file => {
    try {
      return webUtils.getPathForFile(file) || ''
    } catch {
      return ''
    }
  },
  normalizePreviewTarget: (target, baseDir) => ipcRenderer.invoke('jimmy:normalizePreviewTarget', target, baseDir),
  watchPreviewFile: url => ipcRenderer.invoke('jimmy:watchPreviewFile', url),
  watchDirectory: dir => ipcRenderer.invoke('jimmy:watchDirectory', dir),
  stopPreviewFileWatch: id => ipcRenderer.invoke('jimmy:stopPreviewFileWatch', id),
  setActiveWork: payload => ipcRenderer.send('jimmy:active-work', payload),
  setTitleBarTheme: payload => ipcRenderer.send('jimmy:titlebar-theme', payload),
  setNativeTheme: mode => ipcRenderer.send('jimmy:native-theme', mode),
  setTranslucency: payload => ipcRenderer.send('jimmy:translucency', payload),
  setKeepAwake: on => ipcRenderer.send('jimmy:keep-awake', on),
  setDisableF12: blocked => ipcRenderer.send('jimmy:devtools:disable-f12', blocked),
  setPreviewShortcutActive: active => ipcRenderer.send('jimmy:previewShortcutActive', Boolean(active)),
  openExternal: url => ipcRenderer.invoke('jimmy:openExternal', url),
  openPreviewInBrowser: url => ipcRenderer.invoke('jimmy:openPreviewInBrowser', url),
  reachPreviewUrl: url => ipcRenderer.invoke('jimmy:preview:reach', url),
  fetchLinkTitle: url => ipcRenderer.invoke('jimmy:fetchLinkTitle', url),
  resolveFavicon: url => ipcRenderer.invoke('jimmy:resolveFavicon', url),
  sanitizeWorkspaceCwd: cwd => ipcRenderer.invoke('jimmy:workspace:sanitize', cwd),
  settings: {
    getDefaultProjectDir: () => ipcRenderer.invoke('jimmy:setting:defaultProjectDir:get'),
    setDefaultProjectDir: dir => ipcRenderer.invoke('jimmy:setting:defaultProjectDir:set', dir),
    pickDefaultProjectDir: () => ipcRenderer.invoke('jimmy:setting:defaultProjectDir:pick')
  },
  zoom: {
    // Current zoom of this window, as { level, percent }.
    get: () => ipcRenderer.invoke('jimmy:zoom:get'),
    // Synchronous zoom factor (1 = 100%). Coordinate math needs it in the
    // same tick as the event it converts, so no IPC round-trip here.
    factor: () => webFrame.getZoomFactor(),
    setPercent: percent => ipcRenderer.send('jimmy:zoom:set-percent', percent),
    // Fires on every zoom change, including the Ctrl/Cmd +/-/0 shortcuts,
    // so the settings UI can stay in sync with the keyboard.
    onChanged: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:zoom:changed', listener)

      return () => ipcRenderer.removeListener('jimmy:zoom:changed', listener)
    }
  },
  revealLogs: () => ipcRenderer.invoke('jimmy:logs:reveal'),
  getRecentLogs: () => ipcRenderer.invoke('jimmy:logs:recent'),
  // Fire-and-forget: persists a renderer error-boundary catch (with component
  // stack) to desktop.log so crashes survive the window (#79428).
  reportRendererError: report => ipcRenderer.send('jimmy:logs:renderer-error', report),
  readDir: dirPath => ipcRenderer.invoke('jimmy:fs:readDir', dirPath),
  gitRoot: startPath => ipcRenderer.invoke('jimmy:fs:gitRoot', startPath),
  revealPath: targetPath => ipcRenderer.invoke('jimmy:fs:reveal', targetPath),
  openDir: dirPath => ipcRenderer.invoke('jimmy:fs:openDir', dirPath),
  desktopPluginsRoot: () => ipcRenderer.invoke('jimmy:fs:desktopPluginsRoot'),
  agentPluginsRoot: () => ipcRenderer.invoke('jimmy:fs:agentPluginsRoot'),
  renamePath: (targetPath, newName) => ipcRenderer.invoke('jimmy:fs:rename', targetPath, newName),
  writeTextFile: (filePath, content) => ipcRenderer.invoke('jimmy:fs:writeText', filePath, content),
  trashPath: targetPath => ipcRenderer.invoke('jimmy:fs:trash', targetPath),
  git: {
    worktreeList: repoPath => ipcRenderer.invoke('jimmy:git:worktreeList', repoPath),
    worktreeAdd: (repoPath, options) => ipcRenderer.invoke('jimmy:git:worktreeAdd', repoPath, options),
    worktreeRemove: (repoPath, worktreePath, options) =>
      ipcRenderer.invoke('jimmy:git:worktreeRemove', repoPath, worktreePath, options),
    branchSwitch: (repoPath, branch) => ipcRenderer.invoke('jimmy:git:branchSwitch', repoPath, branch),
    branchList: repoPath => ipcRenderer.invoke('jimmy:git:branchList', repoPath),
    baseBranchList: repoPath => ipcRenderer.invoke('jimmy:git:baseBranchList', repoPath),
    repoStatus: repoPath => ipcRenderer.invoke('jimmy:git:repoStatus', repoPath),
    fileDiff: (repoPath, filePath) => ipcRenderer.invoke('jimmy:git:fileDiff', repoPath, filePath),
    scanRepos: (roots, options) => ipcRenderer.invoke('jimmy:git:scanRepos', roots, options),
    review: {
      list: (repoPath, scope, baseRef) => ipcRenderer.invoke('jimmy:git:review:list', repoPath, scope, baseRef),
      diff: (repoPath, filePath, scope, baseRef, staged) =>
        ipcRenderer.invoke('jimmy:git:review:diff', repoPath, filePath, scope, baseRef, staged),
      stage: (repoPath, filePath) => ipcRenderer.invoke('jimmy:git:review:stage', repoPath, filePath),
      unstage: (repoPath, filePath) => ipcRenderer.invoke('jimmy:git:review:unstage', repoPath, filePath),
      revert: (repoPath, filePath) => ipcRenderer.invoke('jimmy:git:review:revert', repoPath, filePath),
      revParse: (repoPath, ref) => ipcRenderer.invoke('jimmy:git:review:revParse', repoPath, ref),
      commit: (repoPath, message, push) => ipcRenderer.invoke('jimmy:git:review:commit', repoPath, message, push),
      commitContext: repoPath => ipcRenderer.invoke('jimmy:git:review:commitContext', repoPath),
      push: repoPath => ipcRenderer.invoke('jimmy:git:review:push', repoPath),
      shipInfo: repoPath => ipcRenderer.invoke('jimmy:git:review:shipInfo', repoPath),
      prList: (repoPath, branches, numbers) =>
        ipcRenderer.invoke('jimmy:git:review:prList', repoPath, branches, numbers),
      fetchPrComment: (repoPath, url) => ipcRenderer.invoke('jimmy:git:review:fetchPrComment', repoPath, url),
      createPr: repoPath => ipcRenderer.invoke('jimmy:git:review:createPr', repoPath)
    }
  },
  terminal: {
    cwd: id => ipcRenderer.invoke('jimmy:terminal:cwd', id),
    dispose: id => ipcRenderer.invoke('jimmy:terminal:dispose', id),
    resize: (id, size) => ipcRenderer.invoke('jimmy:terminal:resize', id, size),
    start: options => ipcRenderer.invoke('jimmy:terminal:start', options),
    write: (id, data) => ipcRenderer.invoke('jimmy:terminal:write', id, data),
    onData: (id, callback) => {
      const channel = `jimmy:terminal:${id}:data`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    },
    onExit: (id, callback) => {
      const channel = `jimmy:terminal:${id}:exit`
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on(channel, listener)

      return () => ipcRenderer.removeListener(channel, listener)
    }
  },
  onClosePreviewRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:close-preview-requested', listener)

    return () => ipcRenderer.removeListener('jimmy:close-preview-requested', listener)
  },
  onPreviewNav: callback => {
    const listener = (_event, command) => callback(command)
    ipcRenderer.on('jimmy:preview-nav', listener)

    return () => ipcRenderer.removeListener('jimmy:preview-nav', listener)
  },
  onOpenFolderRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:open-folder-requested', listener)

    return () => ipcRenderer.removeListener('jimmy:open-folder-requested', listener)
  },
  onOpenUpdatesRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:open-updates', listener)

    return () => ipcRenderer.removeListener('jimmy:open-updates', listener)
  },
  onDeepLink: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:deep-link', listener)

    return () => ipcRenderer.removeListener('jimmy:deep-link', listener)
  },
  signalDeepLinkReady: () => ipcRenderer.invoke('jimmy:deep-link-ready'),
  probePluginRepo: payload => ipcRenderer.invoke('jimmy:plugin:probe', payload),
  installDesktopPlugin: payload => ipcRenderer.invoke('jimmy:plugin:installDesktop', payload),
  onWindowStateChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:window-state-changed', listener)

    return () => ipcRenderer.removeListener('jimmy:window-state-changed', listener)
  },
  onFocusSession: callback => {
    const listener = (_event, sessionId) => callback(sessionId)
    ipcRenderer.on('jimmy:focus-session', listener)

    return () => ipcRenderer.removeListener('jimmy:focus-session', listener)
  },
  onNotificationAction: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:notification-action', listener)

    return () => ipcRenderer.removeListener('jimmy:notification-action', listener)
  },
  onNotificationActivate: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:notification-activate', listener)

    return () => ipcRenderer.removeListener('jimmy:notification-activate', listener)
  },
  onPreviewFileChanged: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:preview-file-changed', listener)

    return () => ipcRenderer.removeListener('jimmy:preview-file-changed', listener)
  },
  onBackendExit: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:backend-exit', listener)

    return () => ipcRenderer.removeListener('jimmy:backend-exit', listener)
  },
  // Soft gateway-mode apply finished tearing down the primary backend. Renderer
  // should wipe session lists + re-dial without a window reload.
  onConnectionApplied: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:connection:applied', listener)

    return () => ipcRenderer.removeListener('jimmy:connection:applied', listener)
  },
  onPowerResume: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:power-resume', listener)

    return () => ipcRenderer.removeListener('jimmy:power-resume', listener)
  },
  // AC ↔ battery transitions; renderers slow their backstop polls on battery.
  getOnBattery: () => ipcRenderer.invoke('jimmy:power-battery:get'),
  onBatteryChanged: callback => {
    const listener = (_event, onBattery) => callback(Boolean(onBattery))
    ipcRenderer.on('jimmy:power-battery', listener)

    return () => ipcRenderer.removeListener('jimmy:power-battery', listener)
  },
  onBootProgress: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:boot-progress', listener)

    return () => ipcRenderer.removeListener('jimmy:boot-progress', listener)
  },
  // First-launch bootstrap progress -- emitted by the install.ps1 stage
  // runner in main.ts (apps/desktop/electron/bootstrap-runner.ts).
  // Renderer's install overlay subscribes to live events and queries the
  // current snapshot via getBootstrapState() to recover after a devtools
  // reload mid-bootstrap.
  getBootstrapState: () => ipcRenderer.invoke('jimmy:bootstrap:get'),
  continueBootstrapLocal: () => ipcRenderer.invoke('jimmy:bootstrap:continue-local'),
  resetBootstrap: () => ipcRenderer.invoke('jimmy:bootstrap:reset'),
  repairBootstrap: () => ipcRenderer.invoke('jimmy:bootstrap:repair'),
  cancelBootstrap: () => ipcRenderer.invoke('jimmy:bootstrap:cancel'),
  onBootstrapEvent: callback => {
    const listener = (_event, payload) => callback(payload)
    ipcRenderer.on('jimmy:bootstrap:event', listener)

    return () => ipcRenderer.removeListener('jimmy:bootstrap:event', listener)
  },
  getVersion: () => ipcRenderer.invoke('jimmy:version'),
  getRemoteDisplayReason: () => ipcRenderer.invoke('jimmy:get-remote-display-reason'),
  uninstall: {
    summary: () => ipcRenderer.invoke('jimmy:uninstall:summary'),
    run: mode => ipcRenderer.invoke('jimmy:uninstall:run', { mode })
  },
  updates: {
    check: () => ipcRenderer.invoke('jimmy:updates:check'),
    apply: opts => ipcRenderer.invoke('jimmy:updates:apply', opts),
    getBranch: () => ipcRenderer.invoke('jimmy:updates:branch:get'),
    setBranch: name => ipcRenderer.invoke('jimmy:updates:branch:set', name),
    onProgress: callback => {
      const listener = (_event, payload) => callback(payload)
      ipcRenderer.on('jimmy:updates:progress', listener)

      return () => ipcRenderer.removeListener('jimmy:updates:progress', listener)
    }
  },
  themes: {
    fetchMarketplace: id => ipcRenderer.invoke('jimmy:vscode-theme:fetch', id),
    searchMarketplace: query => ipcRenderer.invoke('jimmy:vscode-theme:search', query)
  },
  // Find-in-page (Ctrl/Cmd+F): delegates to Electron's
  // webContents.findInPage on the IPC sender's window so a Cmd+F pressed
  // in a secondary session window searches THAT window, not the primary.
  // `onFoundInPage` returns the unsubscribe fn; the renderer wires it via
  // `initFindInPageListener` in store/find-in-page.ts and tears it down
  // when the FindBar unmounts.
  findInPage: (query, options) => ipcRenderer.invoke('jimmy:find-in-page', query, options),
  stopFindInPage: () => ipcRenderer.invoke('jimmy:stop-find-in-page'),
  onFoundInPage: callback => {
    const listener = (_event, result) => callback(result)
    ipcRenderer.on('jimmy:found-in-page', listener)

    return () => ipcRenderer.removeListener('jimmy:found-in-page', listener)
  },
  // Main-process `before-input-event` forwards Ctrl/Cmd+F here so renderer
  // can open the FindBar even when the GTK compositor has already grabbed
  // the chord at the windowing layer (#81727).
  onOpenFindBarRequested: callback => {
    const listener = () => callback()
    ipcRenderer.on('jimmy:open-find-bar', listener)

    return () => ipcRenderer.removeListener('jimmy:open-find-bar', listener)
  }
})
