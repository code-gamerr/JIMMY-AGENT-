# Graphy Codebase Analysis

## Project: c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main

### File Structure Summary
- Total Files: 9871
- Total Directories: 1001
- File Extensions: .md: 1545, .py: 4460, .example: 1, .txt: 10, .gz: 1, .yml: 3, .mjs: 155, .lock: 2, .nix: 18, .json: 105, .toml: 2, .sh: 37, .png: 54, .html: 11, .ts: 1729, .jpg: 4, .tsx: 735, .css: 13, .rs: 10, .manifest: 1, .icns: 2, .ico: 4, .plist: 2, .mts: 1, .webp: 4, .jsonl: 2, .woff2: 13, .js: 16, .com: 531, .xyz: 3, .cn: 10, .local: 34, .ai: 8, .dev: 7, .tr: 2, .io: 3, .cloud: 1, .il: 1, .net: 11, .au: 4, .se: 2, .no: 1, .me: 8, .lol: 1, .tw: 1, .br: 2, .co: 2, .de: 3, .group: 1, .gg: 1, .mesh: 1, .fr: 2, .jp: 1, .to: 2, .eu: 2, .uk: 2, .cc: 1, .tech: 1, .org: 5, .lan: 2, .ae: 1, .in: 1, .computer: 1, .inc: 2, .sg: 1, .pl: 1, .team: 1, .video: 1, .it: 2, .edu: 4, .kr: 1, .pw: 1, .id: 1, .Cloud: 1, .ca: 2, .ad: 1, .kitchen: 1, .club: 1, .online: 1, .fi: 1, .localdomain: 1, .top: 1, .yaml: 144, .pdf: 5, .c: 1, .h: 2, .tmpl: 3, .ps1: 9, .service: 1, .cmd: 1, .cnf: 1, .ini: 1, .tex: 11, .bib: 5, .bst: 5, .sty: 13, .wav: 1, .onnx: 1, .tflite: 1, .mdx: 5, .svg: 3, .mp4: 1

### Directory Tree
```
  ├── acp_adapter
   │  ├── auth.py
   │  ├── edit_approval.py
   │  ├── entry.py
   │  ├── events.py
   │  ├── permissions.py
   │  ├── provenance.py
   │  ├── server.py
   │  ├── session.py
   │  ├── tools.py
   │  ├── __init__.py
   │  └── __main__.py
  ├── agent
   │  ├── account_usage.py
   │  ├── agent_init.py
   │  ├── agent_runtime_helpers.py
   │  ├── anthropic_adapter.py
   │  ├── async_utils.py
   │  ├── auxiliary_client.py
   │  ├── aux_accounting.py
   │  ├── azure_identity_adapter.py
   │  ├── backend_identity.py
   │  ├── background_review.py
   │  ├── battery.py
   │  ├── bedrock_adapter.py
   │  ├── billing_links.py
   │  ├── billing_usage.py
   │  ├── billing_view.py
   │  ├── bounded_response.py
   │  ├── browser_provider.py
   │  ├── browser_registry.py
   │  ├── chat_completion_helpers.py
   │  ├── codex_responses_adapter.py
   │  ├── codex_runtime.py
   │  ├── coding_context.py
   │  ├── command_token_source.py
   │  ├── context_breakdown.py
   │  ├── context_compressor.py
   │  ├── context_engine.py
   │  ├── context_references.py
   │  ├── conversation_compression.py
   │  ├── conversation_loop.py
   │  ├── copilot_acp_client.py
   │  ├── credential_persistence.py
   │  ├── credential_pool.py
   │  ├── credential_sources.py
   │  ├── credits_tracker.py
   │  ├── curator.py
   │  ├── curator_backup.py
   │  ├── deadline.py
   │  ├── delegation_context.py
   │  ├── display.py
   │  ├── empty_response_guard.py
   │  ├── errors.py
   │  ├── error_classifier.py
   │  ├── estop.py
   │  ├── file_safety.py
   │  ├── gemini_native_adapter.py
   │  ├── gemini_schema.py
   │  ├── i18n.py
   │  ├── image_gen_provider.py
   │  ├── image_gen_registry.py
   │  ├── image_routing.py
   │  ├── insights.py
   │  ├── interrupt_compat.py
   │  ├── iteration_budget.py
   │  ├── jiter_preload.py
   │  ├── kanban_stop.py
   │  ├── learning_graph.py
   │  ├── learning_graph_render.py
   │  ├── learning_mutations.py
   │  ├── learn_prompt.py
   │  ├── lmstudio_reasoning.py
   │  ├── lsp
   │  │  ├── cli.py
   │  │  ├── client.py
   │  │  ├── eventlog.py
   │  │  ├── install.py
   │  │  ├── manager.py
   │  │  ├── protocol.py
   │  │  ├── range_shift.py
   │  │  ├── reporter.py
   │  │  ├── servers.py
   │  │  ├── workspace.py
   │  │  └── __init__.py
   │  ├── manual_compression_feedback.py
   │  ├── markdown_tables.py
   │  ├── memory_manager.py
   │  ├── memory_provider.py
   │  ├── message_content.py
   │  ├── message_metadata.py
   │  ├── message_sanitization.py
   │  ├── moa_loop.py
   │  ├── moa_trace.py
   │  ├── models_dev.py
   │  ├── model_metadata.py
   │  ├── monitoring
   │  │  ├── cron_health.py
   │  │  ├── emitter.py
   │  │  ├── events.py
   │  │  ├── gateway_health.py
   │  │  ├── gateway_health_export.py
   │  │  ├── otlp_exporter.py
   │  │  ├── policy.py
   │  │  ├── redaction.py
   │  │  └── __init__.py
   │  ├── moonshot_schema.py
   │  ├── native_compaction.py
   │  ├── nous_rate_guard.py
   │  ├── onboarding.py
   │  ├── oneshot.py
   │  ├── outbound_webhooks.py
   │  ├── pet
   │  │  ├── constants.py
   │  │  ├── generate
   │  │  │  ├── atlas.py
   │  │  │  ├── imagegen.py
   │  │  │  ├── orchestrate.py
   │  │  │  ├── prompts.py
   │  │  │  └── __init__.py
   │  │  ├── manifest.py
   │  │  ├── render.py
   │  │  ├── state.py
   │  │  ├── store.py
   │  │  └── __init__.py
   │  ├── plugin_llm.py
   │  ├── plugin_stream_hooks.py
   │  ├── portal_tags.py
   │  ├── process_bootstrap.py
   │  ├── prompt_builder.py
   │  ├── prompt_cache_boundary.py
   │  ├── prompt_cache_scope.py
   │  ├── prompt_caching.py
   │  ├── proxy_sources
   │  │  ├── iron_proxy.py
   │  │  └── __init__.py
   │  ├── rate_limit_tracker.py
   │  ├── reactions.py
   │  ├── reasoning_effort.py
   │  ├── reasoning_summaries.py
   │  ├── reasoning_timeouts.py
   │  ├── redact.py
   │  ├── relay_llm.py
   │  ├── relay_runtime.py
   │  ├── relay_tools.py
   │  ├── repetition_guard.py
   │  ├── replay_cleanup.py
   │  ├── retry_utils.py
   │  ├── runtime_cwd.py
   │  ├── secret_scope.py
   │  ├── secret_sources
   │  │  ├── base.py
   │  │  ├── bitwarden.py
   │  │  ├── command.py
   │  │  ├── onepassword.py
   │  │  ├── registry.py
   │  │  ├── _cache.py
   │  │  └── __init__.py
   │  ├── session_activity.py
   │  ├── shell_hooks.py
   │  ├── skill_bundles.py
   │  ├── skill_commands.py
   │  ├── skill_preprocessing.py
   │  ├── skill_utils.py
   │  ├── ssl_guard.py
   │  ├── ssl_verify.py
   │  ├── stream_diag.py
   │  ├── stream_single_writer.py
   │  ├── subagent_lifecycle.py
   │  ├── subdirectory_hints.py
   │  ├── subscription_view.py
   │  ├── system_prompt.py
   │  ├── thinking_timeout_guidance.py
   │  ├── think_scrubber.py
   │  ├── thread_scoped_output.py
   │  ├── title_generator.py
   │  ├── tool_dispatch_helpers.py
   │  ├── tool_executor.py
   │  ├── tool_guardrails.py
   │  ├── tool_result_classification.py
   │  ├── trace_upload.py
   │  ├── trajectory.py
   │  ├── transcription_provider.py
   │  ├── transcription_registry.py
   │  ├── transports
   │  │  ├── anthropic.py
   │  │  ├── base.py
   │  │  ├── bedrock.py
   │  │  ├── chat_completions.py
   │  │  ├── codex.py
   │  │  ├── codex_app_server.py
   │  │  ├── codex_app_server_session.py
   │  │  ├── codex_event_projector.py
   │  │  ├── jimmy_tools_mcp_server.py
   │  │  ├── types.py
   │  │  └── __init__.py
   │  ├── tts_provider.py
   │  ├── tts_registry.py
   │  ├── turn_context.py
   │  ├── turn_finalizer.py
   │  ├── turn_retry_state.py
   │  ├── turn_summary.py
   │  ├── usage_pricing.py
   │  ├── verification_evidence.py
   │  ├── verification_stop.py
   │  ├── verify
   │  │  ├── environment.py
   │  │  ├── recipes.py
   │  │  ├── runner.py
   │  │  └── __init__.py
   │  ├── verify_hooks.py
   │  ├── vertex_adapter.py
   │  ├── video_gen_provider.py
   │  ├── video_gen_registry.py
   │  ├── web_search_provider.py
   │  ├── web_search_registry.py
   │  └── __init__.py
  ├── AGENTS.md
  ├── apps
   │  ├── bootstrap-installer
   │  │  ├── eslint.config.mjs
   │  │  ├── index.html
   │  │  ├── package.json
   │  │  ├── public
   │  │  │  └── nous-girl.jpg
   │  │  ├── src
   │  │  │  ├── app.tsx
   │  │  │  ├── components
   │  │  │  │  ├── brand-mark.tsx
   │  │  │  │  ├── button.tsx
   │  │  │  │  ├── hackery-button.tsx
   │  │  │  │  └── loader.tsx
   │  │  │  ├── lib
   │  │  │  │  ├── format.ts
   │  │  │  │  └── utils.ts
   │  │  │  ├── main.tsx
   │  │  │  ├── routes
   │  │  │  │  ├── failure.tsx
   │  │  │  │  ├── progress.tsx
   │  │  │  │  ├── success.tsx
   │  │  │  │  └── welcome.tsx
   │  │  │  ├── store.ts
   │  │  │  ├── styles.css
   │  │  │  ├── theme.ts
   │  │  │  └── vite-env.d.ts
   │  │  ├── src-tauri
   │  │  │  ├── build.rs
   │  │  │  ├── capabilities
   │  │  │  │  └── default.json
   │  │  │  ├── Cargo.toml
   │  │  │  ├── jimmy-setup.manifest
   │  │  │  ├── icons
   │  │  │  │  ├── 128x128.png
   │  │  │  │  ├── 128x128@2x.png
   │  │  │  │  ├── 32x32.png
   │  │  │  │  ├── icon.icns
   │  │  │  │  └── icon.ico
   │  │  │  ├── src
   │  │  │  │  ├── bootstrap.rs
   │  │  │  │  ├── events.rs
   │  │  │  │  ├── install_script.rs
   │  │  │  │  ├── lib.rs
   │  │  │  │  ├── main.rs
   │  │  │  │  ├── paths.rs
   │  │  │  │  ├── powershell.rs
   │  │  │  │  └── update.rs
   │  │  │  └── tauri.conf.json
   │  │  ├── tsconfig.json
   │  │  ├── tsconfig.node.json
   │  │  └── vite.config.ts
   │  ├── desktop
   │  │  ├── AGENTS.md
   │  │  ├── assets
   │  │  │  ├── icon.icns
   │  │  │  ├── icon.ico
   │  │  │  └── icon.png
   │  │  ├── components.json
   │  │  ├── DESIGN.md
   │  │  ├── e2e
   │  │  │  ├── at-rest-connection-token.spec.ts
   │  │  │  ├── batch-clarify.spec.ts
   │  │  │  ├── boot-failure.spec.ts
   │  │  │  ├── boot.spec.ts
   │  │  │  ├── chat.spec.ts
   │  │  │  ├── context-menu-editables.spec.ts
   │  │  │  ├── correction-session-switch.spec.ts
   │  │  │  ├── fix-electron-tracing.ts
   │  │  │  ├── fixtures.ts
   │  │  │  ├── hidden-history-messages.spec.ts
   │  │  │  ├── image-attachment-resume.spec.ts
   │  │  │  ├── interim-messages.spec.ts
   │  │  │  ├── large-session-resume.spec.ts
   │  │  │  ├── launch-packaged-app.spec.ts
   │  │  │  ├── mock-backend-setup.spec.ts
   │  │  │  ├── mock-server.ts
   │  │  │  ├── onboarding.spec.ts
   │  │  │  ├── queue-turn-boundary.spec.ts
   │  │  │  ├── real-session-builder.ts
   │  │  │  ├── right-pane.spec.ts
   │  │  │  ├── session-compression-and-queue-stop.spec.ts
   │  │  │  ├── sidebar-states.spec.ts
   │  │  │  ├── submit-drift.spec.ts
   │  │  │  ├── task-panel-clearance.spec.ts
   │  │  │  ├── test.ts
   │  │  │  ├── tile-unread-bug.spec.ts
   │  │  │  ├── unread-dot-restart.spec.ts
   │  │  │  ├── visual-snapshot.ts
   │  │  │  ├── warm-resume-jitter.spec.ts
   │  │  │  └── worktree-branch-status.spec.ts
   │  │  ├── electron
   │  │  │  ├── active-runtime-state.test.ts
   │  │  │  ├── active-runtime-state.ts
   │  │  │  ├── backend-child.ts
   │  │  │  ├── backend-command.test.ts
   │  │  │  ├── backend-command.ts
   │  │  │  ├── backend-connection-state.test.ts
   │  │  │  ├── backend-connection-state.ts
   │  │  │  ├── backend-env.test.ts
   │  │  │  ├── backend-env.ts
   │  │  │  ├── backend-health.test.ts
   │  │  │  ├── backend-health.ts
   │  │  │  ├── backend-ownership.test.ts
   │  │  │  ├── backend-ownership.ts
   │  │  │  ├── backend-probes.test.ts
   │  │  │  ├── backend-probes.ts
   │  │  │  ├── backend-ready.test.ts
   │  │  │  ├── backend-ready.ts
   │  │  │  ├── backend-start-failure.test.ts
   │  │  │  ├── backend-start-failure.ts
   │  │  │  ├── bootstrap-platform.test.ts
   │  │  │  ├── bootstrap-platform.ts
   │  │  │  ├── bootstrap-repair-guard.test.ts
   │  │  │  ├── bootstrap-repair-guard.ts
   │  │  │  ├── bootstrap-runner.test.ts
   │  │  │  ├── bootstrap-runner.ts
   │  │  │  ├── bundle-skew.test.ts
   │  │  │  ├── bundle-skew.ts
   │  │  │  ├── connection-apply.test.ts
   │  │  │  ├── connection-apply.ts
   │  │  │  ├── connection-config.test.ts
   │  │  │  ├── connection-config.ts
   │  │  │  ├── connection-registry.test.ts
   │  │  │  ├── connection-registry.ts
   │  │  │  ├── crash-forensics.test.ts
   │  │  │  ├── crash-forensics.ts
   │  │  │  ├── dashboard-token.test.ts
   │  │  │  ├── dashboard-token.ts
   │  │  │  ├── desktop-electron-pin.test.ts
   │  │  │  ├── desktop-installation.test.ts
   │  │  │  ├── desktop-installation.ts
   │  │  │  ├── desktop-log-line.test.ts
   │  │  │  ├── desktop-log-line.ts
   │  │  │  ├── desktop-plugin-install.test.ts
   │  │  │  ├── desktop-plugin-install.ts
   │  │  │  ├── desktop-remote-route.test.ts
   │  │  │  ├── desktop-remote-route.ts
   │  │  │  ├── desktop-uninstall.test.ts
   │  │  │  ├── desktop-uninstall.ts
   │  │  │  ├── dev-cdp.test.ts
   │  │  │  ├── dev-cdp.ts
   │  │  │  ├── embed-referer.ts
   │  │  │  ├── entitlements.mac.inherit.plist
   │  │  │  ├── entitlements.mac.plist
   │  │  │  ├── event-dedupe.test.ts
   │  │  │  ├── event-dedupe.ts
   │  │  │  ├── external-terminal.test.ts
   │  │  │  ├── external-terminal.ts
   │  │  │  ├── favicon.test.ts
   │  │  │  ├── favicon.ts
   │  │  │  ├── find-git-bash.test.ts
   │  │  │  ├── find-git-bash.ts
   │  │  │  ├── find-in-page-native-fixture
   │  │  │  │  └── package.json
   │  │  │  ├── find-in-page-native.test.mjs
   │  │  │  ├── find-in-page.test.ts
   │  │  │  ├── find-in-page.ts
   │  │  │  ├── first-run-setup-gate.test.ts
   │  │  │  ├── first-run-setup-gate.ts
   │  │  │  ├── first-run-setup-main-process.test.ts
   │  │  │  ├── fs-ipc.ts
   │  │  │  ├── fs-read-dir.test.ts
   │  │  │  ├── fs-read-dir.ts
   │  │  │  ├── gateway-file-download-transport.test.ts
   │  │  │  ├── gateway-file-download.test.ts
   │  │  │  ├── gateway-file-download.ts
   │  │  │  ├── gateway-ws-probe.test.ts
   │  │  │  ├── gateway-ws-probe.ts
   │  │  │  ├── get-windows.d.ts
   │  │  │  ├── git-ipc.ts
   │  │  │  ├── git-repo-scan.test.ts
   │  │  │  ├── git-repo-scan.ts
   │  │  │  ├── git-review-ops.test.ts
   │  │  │  ├── git-review-ops.ts
   │  │  │  ├── git-root.test.ts
   │  │  │  ├── git-root.ts
   │  │  │  ├── git-worktree-ops.test.ts
   │  │  │  ├── git-worktree-ops.ts
   │  │  │  ├── gitlock.test.ts
   │  │  │  ├── gitlock.ts
   │  │  │  ├── handoff-result.test.ts
   │  │  │  ├── handoff-result.ts
   │  │  │  ├── hardening.test.ts
   │  │  │  ├── hardening.ts
   │  │  │  ├── hud-cursor.test.ts
   │  │  │  ├── hud-cursor.ts
   │  │  │  ├── hud-ipc.ts
   │  │  │  ├── hud-snap-shortcut.test.ts
   │  │  │  ├── hud-snap-shortcut.ts
   │  │  │  ├── hud-snap.test.ts
   │  │  │  ├── hud-snap.ts
   │  │  │  ├── hud-url.test.ts
   │  │  │  ├── hud-url.ts
   │  │  │  ├── hyprland.test.ts
   │  │  │  ├── hyprland.ts
   │  │  │  ├── link-title-window.test.ts
   │  │  │  ├── link-title-window.ts
   │  │  │  ├── main-window-lifecycle.test.ts
   │  │  │  ├── main-window-lifecycle.ts
   │  │  │  ├── main.ts
   │  │  │  ├── media-protocol.test.ts
   │  │  │  ├── media-protocol.ts
   │  │  │  ├── native-auth-decisions.test.ts
   │  │  │  ├── native-auth-decisions.ts
   │  │  │  ├── native-oauth-login.test.ts
   │  │  │  ├── native-oauth-login.ts
   │  │  │  ├── native-oauth.test.ts
   │  │  │  ├── native-oauth.ts
   │  │  │  ├── native-token-store.test.ts
   │  │  │  ├── native-token-store.ts
   │  │  │  ├── oauth-net-request.test.ts
   │  │  │  ├── oauth-net-request.ts
   │  │  │  ├── parent-process-identity.test.ts
   │  │  │  ├── parent-process-identity.ts
   │  │  │  ├── pet-overlay-ipc.ts
   │  │  │  ├── plugin-profile-routes.test.ts
   │  │  │  ├── plugin-profile-routes.ts
   │  │  │  ├── pool-eviction.test.ts
   │  │  │  ├── pool-eviction.ts
   │  │  │  ├── pool-stop.test.ts
   │  │  │  ├── pool-stop.ts
   │  │  │  ├── pool-touch-scope.test.ts
   │  │  │  ├── pool-touch-scope.ts
   │  │  │  ├── power-save.test.ts
   │  │  │  ├── power-save.ts
   │  │  │  ├── preload.ts
   │  │  │  ├── preview-reach.e2e.mts
   │  │  │  ├── preview-reach.test.ts
   │  │  │  ├── preview-reach.ts
   │  │  │  ├── primary-backend-startup.test.ts
   │  │  │  ├── primary-backend-startup.ts
   │  │  │  ├── primary-connection-rehome.ts
   │  │  │  ├── profile-delete-routing.test.ts
   │  │  │  ├── profile-delete-routing.ts
   │  │  │  ├── profile-rename-routing.test.ts
   │  │  │  ├── profile-rename-routing.ts
   │  │  │  ├── profile-session-routing.test.ts
   │  │  │  ├── profile-session-routing.ts
   │  │  │  ├── quick-entry.test.ts
   │  │  │  ├── quick-entry.ts
   │  │  │  ├── quit-guard.test.ts
   │  │  │  ├── quit-guard.ts
   │  │  │  ├── remote-lifecycle.test.ts
   │  │  │  ├── remote-lifecycle.ts
   │  │  │  ├── remote-liveness.test.ts
   │  │  │  ├── remote-liveness.ts
   │  │  │  ├── renderer-bundle.test.ts
   │  │  │  ├── renderer-bundle.ts
   │  │  │  ├── renderer-log.test.ts
   │  │  │  ├── renderer-log.ts
   │  │  │  ├── session-windows.test.ts
   │  │  │  ├── session-windows.ts
   │  │  │  ├── shell-path.test.ts
   │  │  │  ├── shell-path.ts
   │  │  │  ├── spawn-helper-perms.test.ts
   │  │  │  ├── spawn-helper-perms.ts
   │  │  │  ├── ssh-bootstrap-coordinator.test.ts
   │  │  │  ├── ssh-bootstrap-coordinator.ts
   │  │  │  ├── ssh-config.test.ts
   │  │  │  ├── ssh-config.ts
   │  │  │  ├── ssh-connection.test.ts
   │  │  │  ├── ssh-connection.ts
   │  │  │  ├── stream-throttle.test.ts
   │  │  │  ├── stream-throttle.ts
   │  │  │  ├── terminal-ipc.ts
   │  │  │  ├── titlebar-overlay-width.test.ts
   │  │  │  ├── titlebar-overlay-width.ts
   │  │  │  ├── translucency.test.ts
   │  │  │  ├── translucency.ts
   │  │  │  ├── update-count.test.ts
   │  │  │  ├── update-count.ts
   │  │  │  ├── update-gate.test.ts
   │  │  │  ├── update-gate.ts
   │  │  │  ├── update-handoff-marker.test.ts
   │  │  │  ├── update-marker.test.ts
   │  │  │  ├── update-marker.ts
   │  │  │  ├── update-remote.test.ts
   │  │  │  ├── update-remote.ts
   │  │  │  ├── updater-process.test.ts
   │  │  │  ├── updater-process.ts
   │  │  │  ├── venv-blocker-scan.test.ts
   │  │  │  ├── venv-blocker-scan.ts
   │  │  │  ├── vscode-marketplace.test.ts
   │  │  │  ├── vscode-marketplace.ts
   │  │  │  ├── wake-indicator-window.ts
   │  │  │  ├── wake-indicator.test.ts
   │  │  │  ├── wake-indicator.ts
   │  │  │  ├── window-below.test.ts
   │  │  │  ├── window-below.ts
   │  │  │  ├── window-renderer-lifecycle.test.ts
   │  │  │  ├── window-renderer-lifecycle.ts
   │  │  │  ├── window-reveal.test.ts
   │  │  │  ├── window-reveal.ts
   │  │  │  ├── window-state.test.ts
   │  │  │  ├── window-state.ts
   │  │  │  ├── windows-child-options.test.ts
   │  │  │  ├── windows-child-options.ts
   │  │  │  ├── windows-jimmy-path.test.ts
   │  │  │  ├── windows-jimmy-path.ts
   │  │  │  ├── windows-remote-lifecycle.test.ts
   │  │  │  ├── windows-remote-lifecycle.ts
   │  │  │  ├── windows-remote-live.test.ts
   │  │  │  ├── windows-sandbox-fallback.test.ts
   │  │  │  ├── windows-sandbox-fallback.ts
   │  │  │  ├── windows-system-ca.test.ts
   │  │  │  ├── windows-system-ca.ts
   │  │  │  ├── windows-user-env.test.ts
   │  │  │  ├── windows-user-env.ts
   │  │  │  ├── workspace-cwd.test.ts
   │  │  │  ├── workspace-cwd.ts
   │  │  │  ├── wsl-clipboard-image.test.ts
   │  │  │  ├── wsl-clipboard-image.ts
   │  │  │  ├── wsl-path-bridge.test.ts
   │  │  │  ├── wsl-path-bridge.ts
   │  │  │  ├── zoom.test.ts
   │  │  │  └── zoom.ts
   │  │  ├── eslint.config.mjs
   │  │  ├── index.html
   │  │  ├── package.json
   │  │  ├── playwright.config.ts
   │  │  ├── pr-assets
   │  │  │  └── session-source-folders.png
   │  │  ├── preview-demo.html
   │  │  ├── public
   │  │  │  ├── apple-touch-icon.png
   │  │  │  ├── ds-assets
   │  │  │  │  └── filler-bg0.jpg
   │  │  │  ├── jimmy-frames
   │  │  │  │  ├── jimmy-frame-0.png
   │  │  │  │  ├── jimmy-frame-1.png
   │  │  │  │  ├── jimmy-frame-2.png
   │  │  │  │  ├── jimmy-frame-3.png
   │  │  │  │  ├── jimmy-frame-4.png
   │  │  │  │  ├── jimmy-frame-5.png
   │  │  │  │  ├── jimmy-frame-6.png
   │  │  │  │  └── jimmy-frame-7.png
   │  │  │  ├── jimmy-sprite.png
   │  │  │  ├── jimmy.png
   │  │  │  └── nous-girl.jpg
   │  │  ├── README.md
   │  │  ├── scripts
   │  │  │  ├── after-pack.mjs
   │  │  │  ├── assert-dist-built.mjs
   │  │  │  ├── assert-dist-built.test.mjs
   │  │  │  ├── assert-root-install.mjs
   │  │  │  ├── before-build.mjs
   │  │  │  ├── before-pack.mjs
   │  │  │  ├── before-pack.test.mjs
   │  │  │  ├── bundle-electron-main.mjs
   │  │  │  ├── click-session.mjs
   │  │  │  ├── dev-mock.mjs
   │  │  │  ├── dev-no-hmr.mjs
   │  │  │  ├── diag-code-live.mjs
   │  │  │  ├── diag-drag-churn.mjs
   │  │  │  ├── diag-drag-trace.mjs
   │  │  │  ├── diag-jump.mjs
   │  │  │  ├── diag-key-latency.mjs
   │  │  │  ├── diag-live-state.mjs
   │  │  │  ├── diag-overlay-ab.mjs
   │  │  │  ├── diag-overlay-churn.mjs
   │  │  │  ├── diag-overlay-full.mjs
   │  │  │  ├── diag-overlay-sweep.mjs
   │  │  │  ├── diag-real-loop.mjs
   │  │  │  ├── diag-ro-storm.mjs
   │  │  │  ├── diag-scroll-reset.mjs
   │  │  │  ├── diag-sidebar-dom.mjs
   │  │  │  ├── diag-switch-autopsy.mjs
   │  │  │  ├── diag-switch-trace.mjs
   │  │  │  ├── eval.mjs
   │  │  │  ├── gen-share-codes.ts
   │  │  │  ├── live-drive.mjs
   │  │  │  ├── local-pack-publish.test.mjs
   │  │  │  ├── notarize-artifact.mjs
   │  │  │  ├── notarize.mjs
   │  │  │  ├── patch-electron-builder-mac-binary.mjs
   │  │  │  ├── perf
   │  │  │  │  ├── baseline.json
   │  │  │  │  ├── gateway_attach_bench.py
   │  │  │  │  ├── image-attach-bench.mjs
   │  │  │  │  ├── lib
   │  │  │  │  │  ├── baseline.mjs
   │  │  │  │  │  ├── cdp.mjs
   │  │  │  │  │  ├── launch.mjs
   │  │  │  │  │  └── stats.mjs
   │  │  │  │  ├── README.md
   │  │  │  │  ├── run.mjs
   │  │  │  │  ├── scenarios
   │  │  │  │  │  ├── cold-start.mjs
   │  │  │  │  │  ├── first-token.mjs
   │  │  │  │  │  ├── idle-cost.mjs
   │  │  │  │  │  ├── index.mjs
   │  │  │  │  │  ├── keystroke.mjs
   │  │  │  │  │  ├── multitab.mjs
   │  │  │  │  │  ├── profile-switch.mjs
   │  │  │  │  │  ├── render-churn.mjs
   │  │  │  │  │  ├── right-pane.mjs
   │  │  │  │  │  ├── session-load.mjs
   │  │  │  │  │  ├── session-switch.mjs
   │  │  │  │  │  ├── stream-history.mjs
   │  │  │  │  │  ├── stream.mjs
   │  │  │  │  │  ├── submit.mjs
   │  │  │  │  │  └── transcript.mjs
   │  │  │  │  └── serve.mjs
   │  │  │  ├── probe-command-palette.mjs
   │  │  │  ├── probe-model-picker.mjs
   │  │  │  ├── probe-renderer.mjs
   │  │  │  ├── probe-thread.mjs
   │  │  │  ├── profile-model-picker.mjs
   │  │  │  ├── profile-typing-lag.md
   │  │  │  ├── rebuild-native.mjs
   │  │  │  ├── reload-renderer.mjs
   │  │  │  ├── reload.mjs
   │  │  │  ├── run-electron-builder.mjs
   │  │  │  ├── run-short-session-hang-repro.mjs
   │  │  │  ├── run-short-session-hang-repro.test.mjs
   │  │  │  ├── run-ui-shard.mjs
   │  │  │  ├── set-exe-identity.mjs
   │  │  │  ├── stage-native-deps.mjs
   │  │  │  ├── stage-native-deps.test.mjs
   │  │  │  ├── test-desktop.mjs
   │  │  │  ├── utils.mjs
   │  │  │  ├── write-build-stamp.mjs
   │  │  │  └── write-build-stamp.test.mjs
   │  │  ├── src
   │  │  │  ├── api
   │  │  │  │  ├── client.ts
   │  │  │  │  ├── config.ts
   │  │  │  │  ├── cron.ts
   │  │  │  │  ├── mcp.ts
   │  │  │  │  ├── messaging.ts
   │  │  │  │  ├── models.ts
   │  │  │  │  ├── plugins.ts
   │  │  │  │  ├── profiles.ts
   │  │  │  │  ├── sessions.ts
   │  │  │  │  ├── skills.ts
   │  │  │  │  ├── system.ts
   │  │  │  │  └── toolsets.ts
   │  │  │  ├── app
   │  │  │  │  ├── agents
   │  │  │  │  │  └── index.tsx
   │  │  │  │  ├── artifacts
   │  │  │  │  │  ├── artifact-utils.ts
   │  │  │  │  │  ├── index.test.ts
   │  │  │  │  │  └── index.tsx
   │  │  │  │  ├── chat
   │  │  │  │  │  ├── chat-drop-overlay.tsx
   │  │  │  │  │  ├── chat-swap-overlay.tsx
   │  │  │  │  │  ├── close-tab.test.ts
   │  │  │  │  │  ├── close-tab.ts
   │  │  │  │  │  ├── composer
   │  │  │  │  │  │  ├── at-folder-navigation.test.tsx
   │  │  │  │  │  │  ├── attachments.test.tsx
   │  │  │  │  │  │  ├── attachments.tsx
   │  │  │  │  │  │  ├── completion-drawer.tsx
   │  │  │  │  │  │  ├── composer-text-guard.test.tsx
   │  │  │  │  │  │  ├── composer-utils.test.ts
   │  │  │  │  │  │  ├── composer-utils.ts
   │  │  │  │  │  │  ├── context-menu.tsx
   │  │  │  │  │  │  ├── contrib.test.ts
   │  │  │  │  │  │  ├── contrib.ts
   │  │  │  │  │  │  ├── control-classes.ts
   │  │  │  │  │  │  ├── controls.test.tsx
   │  │  │  │  │  │  ├── controls.tsx
   │  │  │  │  │  │  ├── directive-actions.test.tsx
   │  │  │  │  │  │  ├── directive-actions.tsx
   │  │  │  │  │  │  ├── directive-label.test.ts
   │  │  │  │  │  │  ├── directive-scope.test.ts
   │  │  │  │  │  │  ├── drop-affordance.ts
   │  │  │  │  │  │  ├── empty-composer.test.ts
   │  │  │  │  │  │  ├── enter-stale-ime-flag.test.tsx
   │  │  │  │  │  │  ├── enter-submit-dom-race.test.tsx
   │  │  │  │  │  │  ├── focus.test.ts
   │  │  │  │  │  │  ├── focus.ts
   │  │  │  │  │  │  ├── help-hint.tsx
   │  │  │  │  │  │  ├── hooks
   │  │  │  │  │  │  │  ├── use-at-completions-contrib.test.tsx
   │  │  │  │  │  │  │  ├── use-at-completions.test.ts
   │  │  │  │  │  │  │  ├── use-at-completions.ts
   │  │  │  │  │  │  │  ├── use-auto-speak-replies.ts
   │  │  │  │  │  │  │  ├── use-composer-branch.ts
   │  │  │  │  │  │  │  ├── use-composer-draft.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-draft.ts
   │  │  │  │  │  │  │  ├── use-composer-drop.ts
   │  │  │  │  │  │  │  ├── use-composer-esc-cancel.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-esc-cancel.ts
   │  │  │  │  │  │  │  ├── use-composer-metrics.ts
   │  │  │  │  │  │  │  ├── use-composer-placeholder.ts
   │  │  │  │  │  │  │  ├── use-composer-popout.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-popout.ts
   │  │  │  │  │  │  │  ├── use-composer-queue.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-queue.ts
   │  │  │  │  │  │  │  ├── use-composer-submit.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-submit.ts
   │  │  │  │  │  │  │  ├── use-composer-trigger.test.ts
   │  │  │  │  │  │  │  ├── use-composer-trigger.ts
   │  │  │  │  │  │  │  ├── use-composer-undo.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-undo.ts
   │  │  │  │  │  │  │  ├── use-composer-url-dialog.test.tsx
   │  │  │  │  │  │  │  ├── use-composer-url-dialog.ts
   │  │  │  │  │  │  │  ├── use-composer-voice.ts
   │  │  │  │  │  │  │  ├── use-emoji-completions.ts
   │  │  │  │  │  │  │  ├── use-live-completion-adapter.ts
   │  │  │  │  │  │  │  ├── use-mic-recorder.ts
   │  │  │  │  │  │  │  ├── use-micro-actions.ts
   │  │  │  │  │  │  │  ├── use-popout-drag.test.tsx
   │  │  │  │  │  │  │  ├── use-popout-drag.ts
   │  │  │  │  │  │  │  ├── use-slash-completions.test.tsx
   │  │  │  │  │  │  │  ├── use-slash-completions.ts
   │  │  │  │  │  │  │  ├── use-status-presence.ts
   │  │  │  │  │  │  │  ├── use-voice-conversation-rearm.test.tsx
   │  │  │  │  │  │  │  ├── use-voice-conversation.test.tsx
   │  │  │  │  │  │  │  ├── use-voice-conversation.ts
   │  │  │  │  │  │  │  └── use-voice-recorder.ts
   │  │  │  │  │  │  ├── ime-composition-dom-repro.test.tsx
   │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  ├── inline-references.test.ts
   │  │  │  │  │  │  ├── inline-refs.ts
   │  │  │  │  │  │  ├── micro-actions.tsx
   │  │  │  │  │  │  ├── model-pill.test.tsx
   │  │  │  │  │  │  ├── model-pill.tsx
   │  │  │  │  │  │  ├── paste-to-focus.test.ts
   │  │  │  │  │  │  ├── paste-to-focus.ts
   │  │  │  │  │  │  ├── path-refs.test.ts
   │  │  │  │  │  │  ├── path-refs.ts
   │  │  │  │  │  │  ├── queue-panel.tsx
   │  │  │  │  │  │  ├── rich-editor.test.ts
   │  │  │  │  │  │  ├── rich-editor.ts
   │  │  │  │  │  │  ├── scope.tsx
   │  │  │  │  │  │  ├── slash-nav-dom-repro.test.tsx
   │  │  │  │  │  │  ├── slash-refs.test.ts
   │  │  │  │  │  │  ├── slash-refs.ts
   │  │  │  │  │  │  ├── status-stack
   │  │  │  │  │  │  │  ├── coding-row.test.tsx
   │  │  │  │  │  │  │  ├── coding-row.tsx
   │  │  │  │  │  │  │  ├── collapsed-indicator.test.tsx
   │  │  │  │  │  │  │  ├── goal-indicator.test.tsx
   │  │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  │  ├── preview-row.test.tsx
   │  │  │  │  │  │  │  ├── preview-row.tsx
   │  │  │  │  │  │  │  └── status-row.tsx
   │  │  │  │  │  │  ├── suggestion-pills.test.tsx
   │  │  │  │  │  │  ├── suggestion-pills.tsx
   │  │  │  │  │  │  ├── test-utils.ts
   │  │  │  │  │  │  ├── text-utils.test.ts
   │  │  │  │  │  │  ├── text-utils.ts
   │  │  │  │  │  │  ├── trigger-popover-parity.test.tsx
   │  │  │  │  │  │  ├── trigger-popover.test.tsx
   │  │  │  │  │  │  ├── trigger-popover.tsx
   │  │  │  │  │  │  ├── types.ts
   │  │  │  │  │  │  ├── undo-history.test.ts
   │  │  │  │  │  │  ├── undo-history.ts
   │  │  │  │  │  │  ├── url-dialog.tsx
   │  │  │  │  │  │  ├── url-refs.test.ts
   │  │  │  │  │  │  ├── url-refs.ts
   │  │  │  │  │  │  ├── voice-activity.tsx
   │  │  │  │  │  │  └── voice-menu.tsx
   │  │  │  │  │  ├── hooks
   │  │  │  │  │  │  ├── use-composer-actions.test.ts
   │  │  │  │  │  │  ├── use-composer-actions.ts
   │  │  │  │  │  │  └── use-file-drop-zone.ts
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── intro-visibility.test.ts
   │  │  │  │  │  ├── intro-visibility.ts
   │  │  │  │  │  ├── pane-mirror.ts
   │  │  │  │  │  ├── perf-probe.tsx
   │  │  │  │  │  ├── pr-tag.tsx
   │  │  │  │  │  ├── preview-tile.tsx
   │  │  │  │  │  ├── profile-tag.test.tsx
   │  │  │  │  │  ├── profile-tag.tsx
   │  │  │  │  │  ├── right-rail
   │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  ├── preview-act.test.ts
   │  │  │  │  │  │  ├── preview-act.ts
   │  │  │  │  │  │  ├── preview-artifact.test.tsx
   │  │  │  │  │  │  ├── preview-artifact.tsx
   │  │  │  │  │  │  ├── preview-browser-bar.test.tsx
   │  │  │  │  │  │  ├── preview-browser-bar.tsx
   │  │  │  │  │  │  ├── preview-console-state.ts
   │  │  │  │  │  │  ├── preview-console-store.ts
   │  │  │  │  │  │  ├── preview-console.tsx
   │  │  │  │  │  │  ├── preview-drive.ts
   │  │  │  │  │  │  ├── preview-file.test.tsx
   │  │  │  │  │  │  ├── preview-file.tsx
   │  │  │  │  │  │  ├── preview-input.ts
   │  │  │  │  │  │  ├── preview-mind.ts
   │  │  │  │  │  │  ├── preview-nav.test.ts
   │  │  │  │  │  │  ├── preview-nav.ts
   │  │  │  │  │  │  ├── preview-nudge.ts
   │  │  │  │  │  │  ├── preview-pane.test.tsx
   │  │  │  │  │  │  ├── preview-pane.tsx
   │  │  │  │  │  │  ├── preview-reader.test.ts
   │  │  │  │  │  │  ├── preview-reader.ts
   │  │  │  │  │  │  ├── preview-script-runner.ts
   │  │  │  │  │  │  ├── preview-tour.ts
   │  │  │  │  │  │  └── preview.tsx
   │  │  │  │  │  ├── route-session-state.test.ts
   │  │  │  │  │  ├── route-session-state.ts
   │  │  │  │  │  ├── route-tile.tsx
   │  │  │  │  │  ├── runtime-repository.test.ts
   │  │  │  │  │  ├── runtime-repository.ts
   │  │  │  │  │  ├── scroll-to-bottom-button.test.tsx
   │  │  │  │  │  ├── scroll-to-bottom-button.tsx
   │  │  │  │  │  ├── session-draft-title.tsx
   │  │  │  │  │  ├── session-drag.test.ts
   │  │  │  │  │  ├── session-drag.ts
   │  │  │  │  │  ├── session-status-dot.tsx
   │  │  │  │  │  ├── session-tile-actions.test.ts
   │  │  │  │  │  ├── session-tile-actions.ts
   │  │  │  │  │  ├── session-tile-attachments.test.tsx
   │  │  │  │  │  ├── session-tile-row.test.ts
   │  │  │  │  │  ├── session-tile.tsx
   │  │  │  │  │  ├── session-view.test.ts
   │  │  │  │  │  ├── session-view.tsx
   │  │  │  │  │  ├── short-session-hang-repro.tsx
   │  │  │  │  │  ├── sidebar
   │  │  │  │  │  │  ├── chrome.tsx
   │  │  │  │  │  │  ├── connection-switcher.test.tsx
   │  │  │  │  │  │  ├── connection-switcher.tsx
   │  │  │  │  │  │  ├── cron-jobs-section.tsx
   │  │  │  │  │  │  ├── filter-menu.tsx
   │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  ├── load-more-row.test.tsx
   │  │  │  │  │  │  ├── load-more-row.tsx
   │  │  │  │  │  │  ├── order.test.ts
   │  │  │  │  │  │  ├── order.ts
   │  │  │  │  │  │  ├── profile-rail-connect.test.tsx
   │  │  │  │  │  │  ├── profile-scope.test.ts
   │  │  │  │  │  │  ├── profile-scope.ts
   │  │  │  │  │  │  ├── profile-switcher.tsx
   │  │  │  │  │  │  ├── project-dialog.test.tsx
   │  │  │  │  │  │  ├── project-dialog.tsx
   │  │  │  │  │  │  ├── projects
   │  │  │  │  │  │  │  ├── base-branch-picker.tsx
   │  │  │  │  │  │  │  ├── entered-content.tsx
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── model.test.ts
   │  │  │  │  │  │  │  ├── model.ts
   │  │  │  │  │  │  │  ├── overview-row.test.tsx
   │  │  │  │  │  │  │  ├── overview-row.tsx
   │  │  │  │  │  │  │  ├── project-appearance.tsx
   │  │  │  │  │  │  │  ├── project-menu.test.tsx
   │  │  │  │  │  │  │  ├── project-menu.tsx
   │  │  │  │  │  │  │  ├── workspace-group.tsx
   │  │  │  │  │  │  │  ├── workspace-groups.test.ts
   │  │  │  │  │  │  │  ├── workspace-groups.ts
   │  │  │  │  │  │  │  ├── workspace-header.test.tsx
   │  │  │  │  │  │  │  ├── workspace-header.tsx
   │  │  │  │  │  │  │  └── worktree-dialog.tsx
   │  │  │  │  │  │  ├── reorderable-list.tsx
   │  │  │  │  │  │  ├── section-states.tsx
   │  │  │  │  │  │  ├── session-actions-menu.test.ts
   │  │  │  │  │  │  ├── session-actions-menu.test.tsx
   │  │  │  │  │  │  ├── session-actions-menu.tsx
   │  │  │  │  │  │  ├── session-index.test.ts
   │  │  │  │  │  │  ├── session-index.ts
   │  │  │  │  │  │  ├── session-row-details.test.ts
   │  │  │  │  │  │  ├── session-row-details.ts
   │  │  │  │  │  │  ├── session-row-gesture.test.ts
   │  │  │  │  │  │  ├── session-row-gesture.ts
   │  │  │  │  │  │  ├── session-row.test.tsx
   │  │  │  │  │  │  ├── session-row.tsx
   │  │  │  │  │  │  ├── sessions-section.test.tsx
   │  │  │  │  │  │  ├── sessions-section.tsx
   │  │  │  │  │  │  ├── split-submenu.tsx
   │  │  │  │  │  │  ├── strip-fts-markers.test.ts
   │  │  │  │  │  │  ├── use-profile-prewarm.ts
   │  │  │  │  │  │  ├── use-profile-rail-refresh-on-active.test.ts
   │  │  │  │  │  │  ├── use-profile-rail-refresh-on-active.ts
   │  │  │  │  │  │  ├── virtual-session-list.test.tsx
   │  │  │  │  │  │  └── virtual-session-list.tsx
   │  │  │  │  │  ├── surface-vars.test.ts
   │  │  │  │  │  ├── surface-vars.ts
   │  │  │  │  │  ├── thread-loading.test.ts
   │  │  │  │  │  ├── thread-loading.ts
   │  │  │  │  │  ├── transcript-backfill.test.ts
   │  │  │  │  │  ├── transcript-backfill.ts
   │  │  │  │  │  ├── transcript-window.test.ts
   │  │  │  │  │  └── transcript-window.ts
   │  │  │  │  ├── command-center
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  └── maintenance.tsx
   │  │  │  │  ├── command-palette
   │  │  │  │  │  ├── contrib.ts
   │  │  │  │  │  ├── highlight-watcher.test.tsx
   │  │  │  │  │  ├── highlight-watcher.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── marketplace-theme-page.tsx
   │  │  │  │  │  ├── pet-palette-page.tsx
   │  │  │  │  │  └── status-row.tsx
   │  │  │  │  ├── context-menu
   │  │  │  │  │  ├── app-context-menu.test.tsx
   │  │  │  │  │  ├── app-context-menu.tsx
   │  │  │  │  │  ├── store.ts
   │  │  │  │  │  └── target.ts
   │  │  │  │  ├── contrib
   │  │  │  │  │  ├── context.tsx
   │  │  │  │  │  ├── controller.tsx
   │  │  │  │  │  ├── dev
   │  │  │  │  │  │  └── credits-notice-demo.ts
   │  │  │  │  │  ├── hooks
   │  │  │  │  │  │  ├── live-status-reap.test.ts
   │  │  │  │  │  │  ├── live-status-spinner.test.ts
   │  │  │  │  │  │  ├── use-background-sync.test.ts
   │  │  │  │  │  │  ├── use-background-sync.test.tsx
   │  │  │  │  │  │  ├── use-background-sync.ts
   │  │  │  │  │  │  ├── use-desktop-integrations.test.tsx
   │  │  │  │  │  │  ├── use-desktop-integrations.ts
   │  │  │  │  │  │  ├── use-pet-bridge.ts
   │  │  │  │  │  │  ├── use-quick-entry-bridge.ts
   │  │  │  │  │  │  ├── use-session-tile-delegate.test.ts
   │  │  │  │  │  │  └── use-session-tile-delegate.ts
   │  │  │  │  │  ├── index.ts
   │  │  │  │  │  ├── latest-actions.test.ts
   │  │  │  │  │  ├── latest-actions.ts
   │  │  │  │  │  ├── mcp-install-deeplink-dialog.tsx
   │  │  │  │  │  ├── panes.tsx
   │  │  │  │  │  ├── surfaces.test.tsx
   │  │  │  │  │  ├── surfaces.tsx
   │  │  │  │  │  ├── types.ts
   │  │  │  │  │  └── wiring.tsx
   │  │  │  │  ├── cron
   │  │  │  │  │  ├── blueprints.test.ts
   │  │  │  │  │  ├── blueprints.tsx
   │  │  │  │  │  ├── cron-actions.test.ts
   │  │  │  │  │  ├── cron-actions.ts
   │  │  │  │  │  ├── cron-job-model.test.ts
   │  │  │  │  │  ├── cron-job-model.ts
   │  │  │  │  │  ├── deliver-checkboxes.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  └── job-state.ts
   │  │  │  │  ├── floating-hud.ts
   │  │  │  │  ├── gateway
   │  │  │  │  │  └── hooks
   │  │  │  │  │    ├── gateway-hmr-survivor.test.ts
   │  │  │  │  │    ├── gateway-hmr-survivor.ts
   │  │  │  │  │    ├── use-gateway-boot.test.tsx
   │  │  │  │  │    ├── use-gateway-boot.ts
   │  │  │  │  │    ├── use-gateway-request.test.ts
   │  │  │  │  │    └── use-gateway-request.ts
   │  │  │  │  ├── hooks
   │  │  │  │  │  ├── use-config-record.ts
   │  │  │  │  │  ├── use-debounced.ts
   │  │  │  │  │  ├── use-keybinds.ts
   │  │  │  │  │  ├── use-on-profile-switch.ts
   │  │  │  │  │  ├── use-refresh-hotkey.ts
   │  │  │  │  │  ├── use-route-enum-param.ts
   │  │  │  │  │  └── use-route-overlay-active.ts
   │  │  │  │  ├── hud
   │  │  │  │  │  ├── click-through.test.ts
   │  │  │  │  │  ├── click-through.ts
   │  │  │  │  │  ├── composer-drag.test.ts
   │  │  │  │  │  ├── composer-drag.ts
   │  │  │  │  │  ├── glass.ts
   │  │  │  │  │  ├── handoff.ts
   │  │  │  │  │  ├── hud-shell.tsx
   │  │  │  │  │  ├── layout.test.ts
   │  │  │  │  │  ├── layout.ts
   │  │  │  │  │  ├── resize-handle.ts
   │  │  │  │  │  └── thread-focus.ts
   │  │  │  │  ├── index.tsx
   │  │  │  │  ├── layout-constants.ts
   │  │  │  │  ├── learning
   │  │  │  │  │  └── archive-skill-confirm-dialog.tsx
   │  │  │  │  ├── master-detail.tsx
   │  │  │  │  ├── messaging
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  └── platform-icon.tsx
   │  │  │  │  ├── model-picker-overlay.tsx
   │  │  │  │  ├── model-visibility-overlay.tsx
   │  │  │  │  ├── open-session.test.ts
   │  │  │  │  ├── open-session.ts
   │  │  │  │  ├── overlays
   │  │  │  │  │  ├── overlay-chrome.tsx
   │  │  │  │  │  ├── overlay-split-layout.tsx
   │  │  │  │  │  ├── overlay-view.tsx
   │  │  │  │  │  ├── panel.test.tsx
   │  │  │  │  │  ├── panel.tsx
   │  │  │  │  │  └── peek-scope.test.ts
   │  │  │  │  ├── page-search-shell.tsx
   │  │  │  │  ├── pet-generate
   │  │  │  │  │  ├── components
   │  │  │  │  │  │  ├── draft-grid.tsx
   │  │  │  │  │  │  ├── empty-hint.tsx
   │  │  │  │  │  │  ├── generate-unavailable.tsx
   │  │  │  │  │  │  ├── hatch-preview.tsx
   │  │  │  │  │  │  ├── hatching-view.tsx
   │  │  │  │  │  │  ├── provider-picker.tsx
   │  │  │  │  │  │  └── reference-chip.tsx
   │  │  │  │  │  ├── lib
   │  │  │  │  │  │  ├── frame-count.ts
   │  │  │  │  │  │  └── read-reference-image.ts
   │  │  │  │  │  ├── pet-generate-content.tsx
   │  │  │  │  │  └── pet-generate-overlay.tsx
   │  │  │  │  ├── pet-overlay
   │  │  │  │  │  ├── overlay-root.tsx
   │  │  │  │  │  └── pet-overlay-app.tsx
   │  │  │  │  ├── profiles
   │  │  │  │  │  ├── create-profile-dialog.tsx
   │  │  │  │  │  ├── delete-profile-dialog.tsx
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── rename-profile-dialog.test.tsx
   │  │  │  │  │  └── rename-profile-dialog.tsx
   │  │  │  │  ├── quick-entry
   │  │  │  │  │  ├── quick-entry-app.tsx
   │  │  │  │  │  └── quick-entry-root.tsx
   │  │  │  │  ├── right-sidebar
   │  │  │  │  │  ├── file-actions.tsx
   │  │  │  │  │  ├── files
   │  │  │  │  │  │  ├── dnd-manager.ts
   │  │  │  │  │  │  ├── ipc.test.ts
   │  │  │  │  │  │  ├── ipc.ts
   │  │  │  │  │  │  ├── remote-picker.tsx
   │  │  │  │  │  │  ├── tree-sizing.test.ts
   │  │  │  │  │  │  ├── tree.tsx
   │  │  │  │  │  │  ├── use-project-tree.test.ts
   │  │  │  │  │  │  └── use-project-tree.ts
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── review
   │  │  │  │  │  │  ├── churn-bar.tsx
   │  │  │  │  │  │  ├── file-tree.test.tsx
   │  │  │  │  │  │  ├── file-tree.tsx
   │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  ├── ship-bar.tsx
   │  │  │  │  │  │  ├── tree-data.test.ts
   │  │  │  │  │  │  └── tree-data.ts
   │  │  │  │  │  ├── store.ts
   │  │  │  │  │  └── terminal
   │  │  │  │  │    ├── active-resize.test.ts
   │  │  │  │  │    ├── active-resize.ts
   │  │  │  │  │    ├── agent-terminal-stream.ts
   │  │  │  │  │    ├── buffer.ts
   │  │  │  │  │    ├── chrome.tsx
   │  │  │  │  │    ├── clipboard.test.ts
   │  │  │  │  │    ├── clipboard.ts
   │  │  │  │  │    ├── instance.tsx
   │  │  │  │  │    ├── links.test.ts
   │  │  │  │  │    ├── links.ts
   │  │  │  │  │    ├── persistent.test.tsx
   │  │  │  │  │    ├── persistent.tsx
   │  │  │  │  │    ├── rail.test.tsx
   │  │  │  │  │    ├── rail.tsx
   │  │  │  │  │    ├── revive-buffer.test.ts
   │  │  │  │  │    ├── selection.ts
   │  │  │  │  │    ├── terminal-context-menu.ts
   │  │  │  │  │    ├── terminal-font.test.ts
   │  │  │  │  │    ├── terminal-font.ts
   │  │  │  │  │    ├── terminals.test.ts
   │  │  │  │  │    ├── terminals.ts
   │  │  │  │  │    ├── use-agent-terminal.test.tsx
   │  │  │  │  │    ├── use-agent-terminal.ts
   │  │  │  │  │    ├── use-terminal-font.test.tsx
   │  │  │  │  │    ├── use-terminal-font.ts
   │  │  │  │  │    ├── use-terminal-session.ts
   │  │  │  │  │    └── workspace.tsx
   │  │  │  │  ├── routes.test.ts
   │  │  │  │  ├── routes.ts
   │  │  │  │  ├── routes.workspace-reveal.test.ts
   │  │  │  │  ├── session
   │  │  │  │  │  ├── hooks
   │  │  │  │  │  │  ├── preview-open.test.tsx
   │  │  │  │  │  │  ├── session-context-drift.test.ts
   │  │  │  │  │  │  ├── session-context-drift.ts
   │  │  │  │  │  │  ├── use-background-queue-drain.test.tsx
   │  │  │  │  │  │  ├── use-background-queue-drain.ts
   │  │  │  │  │  │  ├── use-context-suggestions.ts
   │  │  │  │  │  │  ├── use-cwd-actions.test.tsx
   │  │  │  │  │  │  ├── use-cwd-actions.ts
   │  │  │  │  │  │  ├── use-jimmy-config.test.ts
   │  │  │  │  │  │  ├── use-jimmy-config.ts
   │  │  │  │  │  │  ├── use-message-stream
   │  │  │  │  │  │  │  ├── agent-init-error.test.tsx
   │  │  │  │  │  │  │  ├── approval-mode-event.test.tsx
   │  │  │  │  │  │  │  ├── clarify-hydration.test.tsx
   │  │  │  │  │  │  │  ├── compaction-event.test.tsx
   │  │  │  │  │  │  │  ├── composer-model-event.test.tsx
   │  │  │  │  │  │  │  ├── delta-flush.test.tsx
   │  │  │  │  │  │  │  ├── gateway-event
   │  │  │  │  │  │  │  │  ├── desktop-bridge.ts
   │  │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  │  ├── input-requests.ts
   │  │  │  │  │  │  │  │  ├── lifecycle.ts
   │  │  │  │  │  │  │  │  ├── message-stream.ts
   │  │  │  │  │  │  │  │  ├── session-info.ts
   │  │  │  │  │  │  │  │  ├── status.ts
   │  │  │  │  │  │  │  │  ├── tools.ts
   │  │  │  │  │  │  │  │  └── types.ts
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── interim-sealing.test.tsx
   │  │  │  │  │  │  │  ├── moa-progress-event.test.tsx
   │  │  │  │  │  │  │  ├── moa-reference-event.test.tsx
   │  │  │  │  │  │  │  ├── pet-tool-failure-event.test.tsx
   │  │  │  │  │  │  │  ├── provider-wait-event.test.tsx
   │  │  │  │  │  │  │  ├── session-info-side-effects.test.tsx
   │  │  │  │  │  │  │  ├── session-reclaimed.test.tsx
   │  │  │  │  │  │  │  ├── stale-pending-settle.test.tsx
   │  │  │  │  │  │  │  ├── steer-arrival-order.test.tsx
   │  │  │  │  │  │  │  ├── stream-flush.test.tsx
   │  │  │  │  │  │  │  ├── terminal-error-frame.test.tsx
   │  │  │  │  │  │  │  ├── test-harness.tsx
   │  │  │  │  │  │  │  ├── timeline-events.test.tsx
   │  │  │  │  │  │  │  ├── todo-cleanup.test.tsx
   │  │  │  │  │  │  │  ├── tool-drafting-event.test.tsx
   │  │  │  │  │  │  │  ├── usage.test.tsx
   │  │  │  │  │  │  │  ├── utils.test.ts
   │  │  │  │  │  │  │  └── utils.ts
   │  │  │  │  │  │  ├── use-model-controls.test.tsx
   │  │  │  │  │  │  ├── use-model-controls.ts
   │  │  │  │  │  │  ├── use-preview-routing.ts
   │  │  │  │  │  │  ├── use-prompt-actions
   │  │  │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── resolve-target-session.test.ts
   │  │  │  │  │  │  │  ├── resolve-target-session.ts
   │  │  │  │  │  │  │  ├── rewind.test.ts
   │  │  │  │  │  │  │  ├── rewind.ts
   │  │  │  │  │  │  │  ├── slash.ts
   │  │  │  │  │  │  │  ├── submit.ts
   │  │  │  │  │  │  │  ├── utils.test.ts
   │  │  │  │  │  │  │  └── utils.ts
   │  │  │  │  │  │  ├── use-route-resume.test.tsx
   │  │  │  │  │  │  ├── use-route-resume.ts
   │  │  │  │  │  │  ├── use-session-actions
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── remove-archived-session.test.tsx
   │  │  │  │  │  │  │  ├── resolve-stored-session.test.ts
   │  │  │  │  │  │  │  ├── resume-structural-parts.test.ts
   │  │  │  │  │  │  │  ├── utils.test.ts
   │  │  │  │  │  │  │  └── utils.ts
   │  │  │  │  │  │  ├── use-session-actions.test.tsx
   │  │  │  │  │  │  ├── use-session-list-actions.test.tsx
   │  │  │  │  │  │  ├── use-session-list-actions.ts
   │  │  │  │  │  │  ├── use-session-state-cache.test.tsx
   │  │  │  │  │  │  └── use-session-state-cache.ts
   │  │  │  │  │  ├── session-state-cache.test.ts
   │  │  │  │  │  ├── session-state-cache.ts
   │  │  │  │  │  ├── workspace-session-target.test.ts
   │  │  │  │  │  └── workspace-session-target.ts
   │  │  │  │  ├── session-picker-overlay.tsx
   │  │  │  │  ├── session-switcher.tsx
   │  │  │  │  ├── settings
   │  │  │  │  │  ├── about-settings.tsx
   │  │  │  │  │  ├── appearance-settings.tsx
   │  │  │  │  │  ├── billing
   │  │  │  │  │  │  ├── account-row-value.tsx
   │  │  │  │  │  │  ├── api.test.ts
   │  │  │  │  │  │  ├── api.ts
   │  │  │  │  │  │  ├── auto-reload-row.tsx
   │  │  │  │  │  │  ├── billing-amounts.ts
   │  │  │  │  │  │  ├── current-plan-card.tsx
   │  │  │  │  │  │  ├── dev-fixtures.ts
   │  │  │  │  │  │  ├── errors.test.ts
   │  │  │  │  │  │  ├── errors.ts
   │  │  │  │  │  │  ├── fixtures.test-util.ts
   │  │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  ├── inline-feedback.tsx
   │  │  │  │  │  │  ├── open-external.ts
   │  │  │  │  │  │  ├── plans-view.tsx
   │  │  │  │  │  │  ├── simulated-api.test.ts
   │  │  │  │  │  │  ├── simulated-api.ts
   │  │  │  │  │  │  ├── tier-art.test.ts
   │  │  │  │  │  │  ├── tier-art.tsx
   │  │  │  │  │  │  ├── types.test.ts
   │  │  │  │  │  │  ├── types.ts
   │  │  │  │  │  │  ├── use-billing-state.test.ts
   │  │  │  │  │  │  ├── use-billing-state.ts
   │  │  │  │  │  │  ├── use-charge-poller.test.ts
   │  │  │  │  │  │  ├── use-charge-poller.ts
   │  │  │  │  │  │  ├── use-step-up.test.tsx
   │  │  │  │  │  │  ├── use-step-up.ts
   │  │  │  │  │  │  ├── use-subscription-change.test.tsx
   │  │  │  │  │  │  └── use-subscription-change.ts
   │  │  │  │  │  ├── combobox-input.tsx
   │  │  │  │  │  ├── computer-use-panel.tsx
   │  │  │  │  │  ├── config-field.tsx
   │  │  │  │  │  ├── config-settings.tsx
   │  │  │  │  │  ├── connections-registry.test.tsx
   │  │  │  │  │  ├── connections-registry.tsx
   │  │  │  │  │  ├── constants.ts
   │  │  │  │  │  ├── credential-key-ui.tsx
   │  │  │  │  │  ├── custom-endpoints-settings.tsx
   │  │  │  │  │  ├── env-credentials.tsx
   │  │  │  │  │  ├── env-var-actions-menu.tsx
   │  │  │  │  │  ├── fallback-models-field.test.tsx
   │  │  │  │  │  ├── fallback-models-field.tsx
   │  │  │  │  │  ├── field-copy.ts
   │  │  │  │  │  ├── gateway-settings.test.ts
   │  │  │  │  │  ├── gateway-settings.test.tsx
   │  │  │  │  │  ├── gateway-settings.tsx
   │  │  │  │  │  ├── helpers.test.ts
   │  │  │  │  │  ├── helpers.ts
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── keybind-settings.tsx
   │  │  │  │  │  ├── keys-settings.test.tsx
   │  │  │  │  │  ├── keys-settings.tsx
   │  │  │  │  │  ├── memory
   │  │  │  │  │  │  ├── connect.tsx
   │  │  │  │  │  │  ├── field-control.tsx
   │  │  │  │  │  │  ├── provider-config-modal.test.tsx
   │  │  │  │  │  │  ├── provider-config-modal.tsx
   │  │  │  │  │  │  ├── provider-config-panel.test.tsx
   │  │  │  │  │  │  └── provider-config-panel.tsx
   │  │  │  │  │  ├── model-settings.test.tsx
   │  │  │  │  │  ├── model-settings.tsx
   │  │  │  │  │  ├── notifications-settings.tsx
   │  │  │  │  │  ├── pet-settings.tsx
   │  │  │  │  │  ├── plugin-install-modal.tsx
   │  │  │  │  │  ├── plugins-settings.test.tsx
   │  │  │  │  │  ├── plugins-settings.tsx
   │  │  │  │  │  ├── primitives.tsx
   │  │  │  │  │  ├── profile-scope.test.tsx
   │  │  │  │  │  ├── profile-scope.tsx
   │  │  │  │  │  ├── providers-settings.test.tsx
   │  │  │  │  │  ├── providers-settings.tsx
   │  │  │  │  │  ├── quick-entry-settings.tsx
   │  │  │  │  │  ├── searchable-select.test.tsx
   │  │  │  │  │  ├── searchable-select.tsx
   │  │  │  │  │  ├── sessions-settings.tsx
   │  │  │  │  │  ├── settings-search.test.ts
   │  │  │  │  │  ├── settings-search.ts
   │  │  │  │  │  ├── ssh-host-selection.test.ts
   │  │  │  │  │  ├── ssh-host-selection.ts
   │  │  │  │  │  ├── terminal-backend-panel.test.tsx
   │  │  │  │  │  ├── terminal-backend-panel.tsx
   │  │  │  │  │  ├── terminal-font-setting.test.tsx
   │  │  │  │  │  ├── terminal-font-setting.tsx
   │  │  │  │  │  ├── test-utils.ts
   │  │  │  │  │  ├── toolset-config-panel.test.tsx
   │  │  │  │  │  ├── toolset-config-panel.tsx
   │  │  │  │  │  ├── types.ts
   │  │  │  │  │  ├── uninstall-section.tsx
   │  │  │  │  │  ├── use-deep-link-highlight.ts
   │  │  │  │  │  ├── use-settings-search.ts
   │  │  │  │  │  ├── voice-field-visible.test.ts
   │  │  │  │  │  ├── voice-provider-fields.test.ts
   │  │  │  │  │  ├── voice-provider-fields.tsx
   │  │  │  │  │  └── with-active.test.ts
   │  │  │  │  ├── shell
   │  │  │  │  │  ├── approval-mode-menu.test.tsx
   │  │  │  │  │  ├── approval-mode-menu.tsx
   │  │  │  │  │  ├── context-usage-panel.test.tsx
   │  │  │  │  │  ├── context-usage-panel.tsx
   │  │  │  │  │  ├── gateway-menu-panel.test.tsx
   │  │  │  │  │  ├── gateway-menu-panel.tsx
   │  │  │  │  │  ├── group-setter.ts
   │  │  │  │  │  ├── hooks
   │  │  │  │  │  │  ├── use-context-breakdown.ts
   │  │  │  │  │  │  ├── use-overlay-routing.ts
   │  │  │  │  │  │  ├── use-status-snapshot.test.ts
   │  │  │  │  │  │  ├── use-status-snapshot.ts
   │  │  │  │  │  │  ├── use-statusbar-items.tsx
   │  │  │  │  │  │  └── use-window-controls-overlay-width.ts
   │  │  │  │  │  ├── model-catalog-menu.test.tsx
   │  │  │  │  │  ├── model-catalog-menu.tsx
   │  │  │  │  │  ├── model-edit-submenu.test.tsx
   │  │  │  │  │  ├── model-edit-submenu.tsx
   │  │  │  │  │  ├── model-menu-panel.test.tsx
   │  │  │  │  │  ├── model-menu-panel.tsx
   │  │  │  │  │  ├── sidebar-label.tsx
   │  │  │  │  │  ├── statusbar-context-menu.test.tsx
   │  │  │  │  │  ├── statusbar-controls.tsx
   │  │  │  │  │  ├── statusbar-visibility.test.tsx
   │  │  │  │  │  ├── titlebar-controls.tsx
   │  │  │  │  │  ├── titlebar-icon.tsx
   │  │  │  │  │  ├── titlebar.test.ts
   │  │  │  │  │  └── titlebar.ts
   │  │  │  │  ├── skills
   │  │  │  │  │  ├── embedded-hub-picker.tsx
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── mcp-tab.tsx
   │  │  │  │  │  └── store.ts
   │  │  │  │  ├── starmap
   │  │  │  │  │  ├── color.ts
   │  │  │  │  │  ├── constants.ts
   │  │  │  │  │  ├── geometry.ts
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  ├── node-context-menu.tsx
   │  │  │  │  │  ├── render.ts
   │  │  │  │  │  ├── share-code.test.ts
   │  │  │  │  │  ├── share-code.ts
   │  │  │  │  │  ├── share-controls.test.tsx
   │  │  │  │  │  ├── share-controls.tsx
   │  │  │  │  │  ├── simulation.ts
   │  │  │  │  │  ├── star-map.tsx
   │  │  │  │  │  ├── text.ts
   │  │  │  │  │  ├── time-axis.ts
   │  │  │  │  │  ├── timeline.tsx
   │  │  │  │  │  └── types.ts
   │  │  │  │  ├── types.ts
   │  │  │  │  ├── updates-overlay.blockers.test.tsx
   │  │  │  │  ├── updates-overlay.tsx
   │  │  │  │  ├── wake-indicator
   │  │  │  │  │  ├── wake-indicator-app.tsx
   │  │  │  │  │  ├── wake-indicator-root.tsx
   │  │  │  │  │  └── wake-indicator.css
   │  │  │  │  └── webhooks
   │  │  │  │    └── index.tsx
   │  │  │  ├── assets
   │  │  │  │  └── tiers
   │  │  │  │    ├── feature-automation.webp
   │  │  │  │    ├── feature-connect.webp
   │  │  │  │    ├── feature-memory.webp
   │  │  │  │    └── feature-sandbox.webp
   │  │  │  ├── components
   │  │  │  │  ├── assistant-ui
   │  │  │  │  │  ├── ansi-text.tsx
   │  │  │  │  │  ├── artifact-card.tsx
   │  │  │  │  │  ├── clarify-tool.test.tsx
   │  │  │  │  │  ├── clarify-tool.tsx
   │  │  │  │  │  ├── directive-text.test.ts
   │  │  │  │  │  ├── directive-text.tsx
   │  │  │  │  │  ├── embeds
   │  │  │  │  │  │  ├── alert.test.tsx
   │  │  │  │  │  │  ├── alert.tsx
   │  │  │  │  │  │  ├── embed-consent.tsx
   │  │  │  │  │  │  ├── embed-size.ts
   │  │  │  │  │  │  ├── escape-html.ts
   │  │  │  │  │  │  ├── fail.tsx
   │  │  │  │  │  │  ├── frame-embed.tsx
   │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  ├── mermaid-embed.tsx
   │  │  │  │  │  │  ├── providers
   │  │  │  │  │  │  │  ├── detect.test.ts
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── instagram.ts
   │  │  │  │  │  │  │  ├── maps.ts
   │  │  │  │  │  │  │  ├── pinterest.ts
   │  │  │  │  │  │  │  ├── spotify.ts
   │  │  │  │  │  │  │  ├── tiktok.ts
   │  │  │  │  │  │  │  ├── twitter.ts
   │  │  │  │  │  │  │  ├── types.ts
   │  │  │  │  │  │  │  ├── vimeo.ts
   │  │  │  │  │  │  │  └── youtube.ts
   │  │  │  │  │  │  ├── registry.tsx
   │  │  │  │  │  │  ├── rich-boundary.tsx
   │  │  │  │  │  │  ├── scroll-gate.tsx
   │  │  │  │  │  │  ├── social-embed.tsx
   │  │  │  │  │  │  ├── spotify-embed.tsx
   │  │  │  │  │  │  ├── svg-embed.tsx
   │  │  │  │  │  │  ├── types.ts
   │  │  │  │  │  │  ├── url-embed.tsx
   │  │  │  │  │  │  ├── use-is-dark.ts
   │  │  │  │  │  │  └── youtube-embed.tsx
   │  │  │  │  │  ├── inline-preview-directive.test.ts
   │  │  │  │  │  ├── inline-preview-directive.tsx
   │  │  │  │  │  ├── markdown-table.tsx
   │  │  │  │  │  ├── markdown-text.artifacts.test.tsx
   │  │  │  │  │  ├── markdown-text.filelinks.test.tsx
   │  │  │  │  │  ├── markdown-text.media-md.test.tsx
   │  │  │  │  │  ├── markdown-text.media.test.tsx
   │  │  │  │  │  ├── markdown-text.overflow.test.tsx
   │  │  │  │  │  ├── markdown-text.session.test.tsx
   │  │  │  │  │  ├── markdown-text.test.ts
   │  │  │  │  │  ├── markdown-text.tsx
   │  │  │  │  │  ├── mcp-setup-tool.tsx
   │  │  │  │  │  ├── message-render-boundary.test.tsx
   │  │  │  │  │  ├── message-render-boundary.tsx
   │  │  │  │  │  ├── reference-kinds.ts
   │  │  │  │  │  ├── session-ref-open.test.tsx
   │  │  │  │  │  ├── test-utils.tsx
   │  │  │  │  │  ├── thread
   │  │  │  │  │  │  ├── agent-delivery.test.tsx
   │  │  │  │  │  │  ├── agent-delivery.tsx
   │  │  │  │  │  │  ├── agent-message.test.tsx
   │  │  │  │  │  │  ├── assistant-message.test.tsx
   │  │  │  │  │  │  ├── assistant-message.tsx
   │  │  │  │  │  │  ├── block-direction.test.tsx
   │  │  │  │  │  │  ├── changed-files-card.tsx
   │  │  │  │  │  │  ├── changed-files.ts
   │  │  │  │  │  │  ├── content.test.ts
   │  │  │  │  │  │  ├── content.ts
   │  │  │  │  │  │  ├── double-click-reaction.test.tsx
   │  │  │  │  │  │  ├── duplicate-activity-indicator.test.tsx
   │  │  │  │  │  │  ├── edit-context.test.tsx
   │  │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  │  ├── list.test.ts
   │  │  │  │  │  │  ├── list.tsx
   │  │  │  │  │  │  ├── message-parts.tsx
   │  │  │  │  │  │  ├── message-reactions.tsx
   │  │  │  │  │  │  ├── status-tail-only.test.tsx
   │  │  │  │  │  │  ├── status.test.tsx
   │  │  │  │  │  │  ├── status.tsx
   │  │  │  │  │  │  ├── streaming.test.tsx
   │  │  │  │  │  │  ├── system-message.test.tsx
   │  │  │  │  │  │  ├── system-message.tsx
   │  │  │  │  │  │  ├── timeline-data.test.ts
   │  │  │  │  │  │  ├── timeline-data.ts
   │  │  │  │  │  │  ├── timeline-idle.test.tsx
   │  │  │  │  │  │  ├── timeline-timestamp.test.tsx
   │  │  │  │  │  │  ├── timeline-timestamp.tsx
   │  │  │  │  │  │  ├── timeline.test.ts
   │  │  │  │  │  │  ├── timeline.tsx
   │  │  │  │  │  │  ├── timestamp.test.ts
   │  │  │  │  │  │  ├── timestamp.ts
   │  │  │  │  │  │  ├── transcript-window.test.ts
   │  │  │  │  │  │  ├── transcript-window.tsx
   │  │  │  │  │  │  ├── turn-activity.test.ts
   │  │  │  │  │  │  ├── turn-activity.ts
   │  │  │  │  │  │  ├── turn-gap-indicator.test.tsx
   │  │  │  │  │  │  ├── types.ts
   │  │  │  │  │  │  ├── use-message-reactions.ts
   │  │  │  │  │  │  ├── user-edit-composer.tsx
   │  │  │  │  │  │  ├── user-message-edit-gesture.test.tsx
   │  │  │  │  │  │  ├── user-message-edit.test.tsx
   │  │  │  │  │  │  ├── user-message-selection.test.ts
   │  │  │  │  │  │  ├── user-message-text.test.tsx
   │  │  │  │  │  │  ├── user-message-text.tsx
   │  │  │  │  │  │  └── user-message.tsx
   │  │  │  │  │  ├── thread-remount.test.tsx
   │  │  │  │  │  ├── tool
   │  │  │  │  │  │  ├── approval.test.tsx
   │  │  │  │  │  │  ├── approval.tsx
   │  │  │  │  │  │  ├── delegate-model.test.ts
   │  │  │  │  │  │  ├── delegate-model.ts
   │  │  │  │  │  │  ├── delegate.tsx
   │  │  │  │  │  │  ├── fallback-model
   │  │  │  │  │  │  │  ├── format.ts
   │  │  │  │  │  │  │  ├── index.ts
   │  │  │  │  │  │  │  ├── targets.ts
   │  │  │  │  │  │  │  └── types.ts
   │  │  │  │  │  │  ├── fallback-model.test.ts
   │  │  │  │  │  │  ├── fallback-preview-scope.test.tsx
   │  │  │  │  │  │  ├── fallback.test.ts
   │  │  │  │  │  │  ├── fallback.tsx
   │  │  │  │  │  │  ├── run-summary.test.ts
   │  │  │  │  │  │  ├── run-summary.ts
   │  │  │  │  │  │  ├── run-ticker.tsx
   │  │  │  │  │  │  └── tool-group.test.tsx
   │  │  │  │  │  ├── tooltip-icon-button.tsx
   │  │  │  │  │  ├── transcript-directive.test.tsx
   │  │  │  │  │  └── transcript-directive.tsx
   │  │  │  │  ├── Backdrop.tsx
   │  │  │  │  ├── billing-banner.tsx
   │  │  │  │  ├── boot-failure-overlay.test.tsx
   │  │  │  │  ├── boot-failure-overlay.tsx
   │  │  │  │  ├── boot-failure-reauth.test.ts
   │  │  │  │  ├── boot-failure-reauth.ts
   │  │  │  │  ├── brand-mark.tsx
   │  │  │  │  ├── chat
   │  │  │  │  │  ├── activity-timer-text.tsx
   │  │  │  │  │  ├── activity-timer.test.tsx
   │  │  │  │  │  ├── activity-timer.ts
   │  │  │  │  │  ├── code-card.tsx
   │  │  │  │  │  ├── code-editor-theme.ts
   │  │  │  │  │  ├── code-editor.tsx
   │  │  │  │  │  ├── compact-markdown.tsx
   │  │  │  │  │  ├── composer-dock.ts
   │  │  │  │  │  ├── diff-lines.tsx
   │  │  │  │  │  ├── disclosure-row.tsx
   │  │  │  │  │  ├── expandable-block.test.tsx
   │  │  │  │  │  ├── expandable-block.tsx
   │  │  │  │  │  ├── fixed-row-window.ts
   │  │  │  │  │  ├── generated-image-result.tsx
   │  │  │  │  │  ├── image-generation-placeholder.test.tsx
   │  │  │  │  │  ├── image-generation-placeholder.tsx
   │  │  │  │  │  ├── intro-copy.jsonl
   │  │  │  │  │  ├── intro.tsx
   │  │  │  │  │  ├── json-document-editor.tsx
   │  │  │  │  │  ├── log-tail.tsx
   │  │  │  │  │  ├── preview-attachment.tsx
   │  │  │  │  │  ├── scaffold-row.tsx
   │  │  │  │  │  ├── shiki-block.tsx
   │  │  │  │  │  ├── shiki-highlighter.test.ts
   │  │  │  │  │  ├── shiki-highlighter.tsx
   │  │  │  │  │  ├── skeletons.tsx
   │  │  │  │  │  ├── stable-text.tsx
   │  │  │  │  │  ├── status-row.tsx
   │  │  │  │  │  ├── status-section.tsx
   │  │  │  │  │  ├── syntax-diff.tsx
   │  │  │  │  │  ├── terminal-output.tsx
   │  │  │  │  │  ├── vibe-hearts.tsx
   │  │  │  │  │  ├── widget-shell.ts
   │  │  │  │  │  └── zoomable-image.tsx
   │  │  │  │  ├── confirm-host.test.tsx
   │  │  │  │  ├── confirm-host.tsx
   │  │  │  │  ├── desktop-install-overlay.test.tsx
   │  │  │  │  ├── desktop-install-overlay.tsx
   │  │  │  │  ├── error-boundary.test.tsx
   │  │  │  │  ├── error-boundary.tsx
   │  │  │  │  ├── find-bar.test.tsx
   │  │  │  │  ├── find-bar.tsx
   │  │  │  │  ├── first-run-remote-form.tsx
   │  │  │  │  ├── gateway-connecting-overlay.test.tsx
   │  │  │  │  ├── gateway-connecting-overlay.tsx
   │  │  │  │  ├── haptics-provider.tsx
   │  │  │  │  ├── idle-mount.test.tsx
   │  │  │  │  ├── idle-mount.tsx
   │  │  │  │  ├── language-switcher.test.tsx
   │  │  │  │  ├── language-switcher.tsx
   │  │  │  │  ├── model-picker.tsx
   │  │  │  │  ├── model-visibility-dialog.tsx
   │  │  │  │  ├── notifications.test.tsx
   │  │  │  │  ├── notifications.tsx
   │  │  │  │  ├── onboarding
   │  │  │  │  │  ├── flow.tsx
   │  │  │  │  │  ├── glyph.tsx
   │  │  │  │  │  ├── index.test.tsx
   │  │  │  │  │  ├── index.tsx
   │  │  │  │  │  └── providers.tsx
   │  │  │  │  ├── page-loader.tsx
   │  │  │  │  ├── pane-shell
   │  │  │  │  │  ├── edit-mode.tsx
   │  │  │  │  │  ├── geometry.ts
   │  │  │  │  │  ├── index.ts
   │  │  │  │  │  ├── pane-lifecycle.test.ts
   │  │  │  │  │  ├── pane-lifecycle.ts
   │  │  │  │  │  ├── pane-visibility.test.ts
   │  │  │  │  │  ├── pane-visibility.ts
   │  │  │  │  │  └── tree
   │  │  │  │  │    ├── dock-enforce.test.ts
   │  │  │  │  │    ├── floating-adoption.test.ts
   │  │  │  │  │    ├── focus-tab-hijack.test.ts
   │  │  │  │  │    ├── focused-session-tab.test.ts
   │  │  │  │  │    ├── grid-model.ts
   │  │  │  │  │    ├── grid-to-tree.ts
   │  │  │  │  │    ├── hide-only-strip-tabs.test.ts
   │  │  │  │  │    ├── hovered-zone-tabs.test.ts
   │  │  │  │  │    ├── model.ts
   │  │  │  │  │    ├── multi-tab-drag.test.ts
   │  │  │  │  │    ├── pane-reload.test.ts
   │  │  │  │  │    ├── pane-share-memory.test.ts
   │  │  │  │  │    ├── pane-toggle-visibility.test.ts
   │  │  │  │  │    ├── plugin-pane-close.test.ts
   │  │  │  │  │    ├── presets.ts
   │  │  │  │  │    ├── reactive-unhide.test.ts
   │  │  │  │  │    ├── remove-pane.test.ts
   │  │  │  │  │    ├── renderer
   │  │  │  │  │     │  ├── drag-session.ts
   │  │  │  │  │     │  ├── edit-bar.tsx
   │  │  │  │  │     │  ├── floating-panes.test.tsx
   │  │  │  │  │     │  ├── floating-panes.tsx
   │  │  │  │  │     │  ├── floating-rect.test.ts
   │  │  │  │  │     │  ├── floating-rect.ts
   │  │  │  │  │     │  ├── index.tsx
   │  │  │  │  │     │  ├── layout-picker.tsx
   │  │  │  │  │     │  ├── lone-header.test.ts
   │  │  │  │  │     │  ├── lone-header.ts
   │  │  │  │  │     │  ├── narrow-overlays.test.tsx
   │  │  │  │  │     │  ├── narrow-overlays.tsx
   │  │  │  │  │     │  ├── tab-strip-scroll.test.ts
   │  │  │  │  │     │  ├── tab-strip-scroll.ts
   │  │  │  │  │     │  ├── tool-panel-close.test.tsx
   │  │  │  │  │     │  ├── track-model-absorber.test.ts
   │  │  │  │  │     │  ├── track-model.ts
   │  │  │  │  │     │  ├── tree-group.test.tsx
   │  │  │  │  │     │  ├── tree-group.tsx
   │  │  │  │  │     │  ├── tree-node.tsx
   │  │  │  │  │     │  └── tree-split.tsx
   │  │  │  │  │    ├── store.ts
   │  │  │  │  │    ├── tab-selection.ts
   │  │  │  │  │    ├── tab-slot-shown.test.ts
   │  │  │  │  │    ├── tool-pane-toggle.test.ts
   │  │  │  │  │    ├── zone-editor.tsx
   │  │  │  │  │    └── zones-engine.ts
   │  │  │  │  ├── particles
   │  │  │  │  │  ├── particle-field.css
   │  │  │  │  │  └── particle-field.tsx
   │  │  │  │  ├── pet
   │  │  │  │  │  ├── floating-pet-poll.test.ts
   │  │  │  │  │  ├── floating-pet.tsx
   │  │  │  │  │  ├── pet-bubble.tsx
   │  │  │  │  │  ├── pet-egg-hatch.tsx
   │  │  │  │  │  ├── pet-egg-sheet.png
   │  │  │  │  │  ├── pet-info-poll.ts
   │  │  │  │  │  ├── pet-sprite.test.tsx
   │  │  │  │  │  ├── pet-sprite.tsx
   │  │  │  │  │  ├── pet-star-shower.tsx
   │  │  │  │  │  ├── pet-thumb.tsx
   │  │  │  │  │  ├── pixel-egg-sprite.test.tsx
   │  │  │  │  │  ├── pixel-egg-sprite.tsx
   │  │  │  │  │  ├── roam-behavior.test.ts
   │  │  │  │  │  ├── roam-behavior.ts
   │  │  │  │  │  ├── roam-geometry.test.ts
   │  │  │  │  │  ├── roam-geometry.ts
   │  │  │  │  │  ├── use-pet-roam.test.tsx
   │  │  │  │  │  ├── use-pet-roam.ts
   │  │  │  │  │  └── use-pet-zoom-gesture.ts
   │  │  │  │  ├── prompt-overlays.test.tsx
   │  │  │  │  ├── prompt-overlays.tsx
   │  │  │  │  ├── remote-display-banner.tsx
   │  │  │  │  ├── session-picker.tsx
   │  │  │  │  ├── status-dot.tsx
   │  │  │  │  └── ui
   │  │  │  │    ├── action-status.tsx
   │  │  │  │    ├── actions-menu.tsx
   │  │  │  │    ├── alert.tsx
   │  │  │  │    ├── avatar-chip.test.tsx
   │  │  │  │    ├── avatar-chip.tsx
   │  │  │  │    ├── badge.tsx
   │  │  │  │    ├── button.tsx
   │  │  │  │    ├── checkbox.test.tsx
   │  │  │  │    ├── checkbox.tsx
   │  │  │  │    ├── codicon.tsx
   │  │  │  │    ├── color-swatches.tsx
   │  │  │  │    ├── command.tsx
   │  │  │  │    ├── confirm-dialog.test.tsx
   │  │  │  │    ├── confirm-dialog.tsx
   │  │  │  │    ├── connector-card.test.tsx
   │  │  │  │    ├── connector-card.tsx
   │  │  │  │    ├── connector-logo.tsx
   │  │  │  │    ├── context-menu.tsx
   │  │  │  │    ├── control.ts
   │  │  │  │    ├── copy-button.test.tsx
   │  │  │  │    ├── copy-button.tsx
   │  │  │  │    ├── decode-text.tsx
   │  │  │  │    ├── dialog-dismiss-repro.test.tsx
   │  │  │  │    ├── dialog-portal-context.ts
   │  │  │  │    ├── dialog.test.tsx
   │  │  │  │    ├── dialog.tsx
   │  │  │  │    ├── diff-count.tsx
   │  │  │  │    ├── disclosure-caret.tsx
   │  │  │  │    ├── drop-affordance.tsx
   │  │  │  │    ├── dropdown-menu.tsx
   │  │  │  │    ├── empty-state.tsx
   │  │  │  │    ├── error-state.tsx
   │  │  │  │    ├── fade-scroll.test.ts
   │  │  │  │    ├── fade-scroll.tsx
   │  │  │  │    ├── fade-text.tsx
   │  │  │  │    ├── favicon.tsx
   │  │  │  │    ├── field.tsx
   │  │  │  │    ├── file-type-icon.tsx
   │  │  │  │    ├── generate-button.tsx
   │  │  │  │    ├── glyph-spinner.test.tsx
   │  │  │  │    ├── glyph-spinner.tsx
   │  │  │  │    ├── highlight-matches.test.tsx
   │  │  │  │    ├── highlight-matches.tsx
   │  │  │  │    ├── input.test.tsx
   │  │  │  │    ├── input.tsx
   │  │  │  │    ├── kbd.tsx
   │  │  │  │    ├── keyboard-first.test.ts
   │  │  │  │    ├── keyboard-first.ts
   │  │  │  │    ├── loader.tsx
   │  │  │  │    ├── log-view.tsx
   │  │  │  │    ├── pagination.tsx
   │  │  │  │    ├── pane-tab.test.tsx
   │  │  │  │    ├── pane-tab.tsx
   │  │  │  │    ├── popover.tsx
   │  │  │  │    ├── profile-glyph.tsx
   │  │  │  │    ├── progress.tsx
   │  │  │  │    ├── row-button.test.tsx
   │  │  │  │    ├── row-button.tsx
   │  │  │  │    ├── sanitized-input.tsx
   │  │  │  │    ├── scroll-area.tsx
   │  │  │  │    ├── search-field.tsx
   │  │  │  │    ├── segmented-control.tsx
   │  │  │  │    ├── select.tsx
   │  │  │  │    ├── separator.tsx
   │  │  │  │    ├── sheet.tsx
   │  │  │  │    ├── sidebar.tsx
   │  │  │  │    ├── skeleton.tsx
   │  │  │  │    ├── split-button.tsx
   │  │  │  │    ├── status-pulse.test.tsx
   │  │  │  │    ├── status-pulse.tsx
   │  │  │  │    ├── switch.tsx
   │  │  │  │    ├── tab-dropdown.tsx
   │  │  │  │    ├── tabs.tsx
   │  │  │  │    ├── text-tab.tsx
   │  │  │  │    ├── textarea.tsx
   │  │  │  │    ├── title-menu-trigger.tsx
   │  │  │  │    ├── tool-icon.tsx
   │  │  │  │    ├── tooltip.test.tsx
   │  │  │  │    ├── tooltip.tsx
   │  │  │  │    ├── use-zoom-pan.ts
   │  │  │  │    ├── zoomable.test.tsx
   │  │  │  │    ├── zoomable.tsx
   │  │  │  │    └── __tests__
   │  │  │  │       └── no-native-title.test.ts
   │  │  │  ├── contrib
   │  │  │  │  ├── events.ts
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── plugin.test.ts
   │  │  │  │  ├── plugin.ts
   │  │  │  │  ├── plugins-store.ts
   │  │  │  │  ├── plugins.ts
   │  │  │  │  ├── react
   │  │  │  │  │  ├── boundary.tsx
   │  │  │  │  │  ├── contribute.tsx
   │  │  │  │  │  ├── slot.test.tsx
   │  │  │  │  │  ├── slot.tsx
   │  │  │  │  │  └── use-contributions.ts
   │  │  │  │  ├── registry.ts
   │  │  │  │  ├── runtime-loader.test.ts
   │  │  │  │  ├── runtime-loader.ts
   │  │  │  │  └── types.ts
   │  │  │  ├── debug
   │  │  │  │  ├── atom-churn.ts
   │  │  │  │  ├── dev-only.noop.ts
   │  │  │  │  ├── dev-only.ts
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── perf-live.ts
   │  │  │  │  ├── README.md
   │  │  │  │  ├── render-counter.ts
   │  │  │  │  ├── right-pane-events.ts
   │  │  │  │  ├── right-pane-probe.ts
   │  │  │  │  └── watched-atoms.ts
   │  │  │  ├── fonts
   │  │  │  │  ├── JetBrainsMono-Bold.woff2
   │  │  │  │  ├── JetBrainsMono-Italic.woff2
   │  │  │  │  └── JetBrainsMono-Regular.woff2
   │  │  │  ├── global.d.ts
   │  │  │  ├── jimmy-capability-scope.test.ts
   │  │  │  ├── jimmy-cron-scope.test.ts
   │  │  │  ├── jimmy-parity.test.ts
   │  │  │  ├── jimmy-profile-scope.test.ts
   │  │  │  ├── jimmy.test.ts
   │  │  │  ├── jimmy.ts
   │  │  │  ├── hooks
   │  │  │  │  ├── use-delayed-true.ts
   │  │  │  │  ├── use-grab-scroll.ts
   │  │  │  │  ├── use-image-download.test.ts
   │  │  │  │  ├── use-image-download.ts
   │  │  │  │  ├── use-media-query.ts
   │  │  │  │  ├── use-mobile.ts
   │  │  │  │  ├── use-resize-observer.ts
   │  │  │  │  ├── use-theme-epoch.ts
   │  │  │  │  └── use-viewed-interval.ts
   │  │  │  ├── i18n
   │  │  │  │  ├── ar.ts
   │  │  │  │  ├── catalog.ts
   │  │  │  │  ├── context.test.tsx
   │  │  │  │  ├── context.tsx
   │  │  │  │  ├── define-locale.ts
   │  │  │  │  ├── en.ts
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── ja.ts
   │  │  │  │  ├── languages.test.ts
   │  │  │  │  ├── languages.ts
   │  │  │  │  ├── plugin-i18n.test.tsx
   │  │  │  │  ├── plugin-i18n.ts
   │  │  │  │  ├── runtime.test.ts
   │  │  │  │  ├── runtime.ts
   │  │  │  │  ├── types.ts
   │  │  │  │  ├── zh-hant.ts
   │  │  │  │  └── zh.ts
   │  │  │  ├── lib
   │  │  │  │  ├── ansi.test.ts
   │  │  │  │  ├── ansi.ts
   │  │  │  │  ├── artifact-detect.test.ts
   │  │  │  │  ├── artifact-detect.ts
   │  │  │  │  ├── audio-context.ts
   │  │  │  │  ├── brand-icon.test.ts
   │  │  │  │  ├── brand-icon.ts
   │  │  │  │  ├── budgeted-loop.test.ts
   │  │  │  │  ├── budgeted-loop.ts
   │  │  │  │  ├── chat-messages
   │  │  │  │  │  ├── hydration.ts
   │  │  │  │  │  ├── index.ts
   │  │  │  │  │  ├── parts.ts
   │  │  │  │  │  ├── reconciliation.ts
   │  │  │  │  │  ├── tool-parts.ts
   │  │  │  │  │  └── types.ts
   │  │  │  │  ├── chat-messages.test.ts
   │  │  │  │  ├── chat-runtime.test.ts
   │  │  │  │  ├── chat-runtime.ts
   │  │  │  │  ├── clipboard.ts
   │  │  │  │  ├── commit-changelog.test.ts
   │  │  │  │  ├── commit-changelog.ts
   │  │  │  │  ├── completion-sound.ts
   │  │  │  │  ├── composer-input-sanitize.test.ts
   │  │  │  │  ├── composer-input-sanitize.ts
   │  │  │  │  ├── connection-display.test.ts
   │  │  │  │  ├── connection-display.ts
   │  │  │  │  ├── connection-scoped.ts
   │  │  │  │  ├── deeplink-routes.test.ts
   │  │  │  │  ├── deeplink-routes.ts
   │  │  │  │  ├── desktop-fs.test.ts
   │  │  │  │  ├── desktop-fs.ts
   │  │  │  │  ├── desktop-git.test.ts
   │  │  │  │  ├── desktop-git.ts
   │  │  │  │  ├── desktop-remote-auth.test.ts
   │  │  │  │  ├── desktop-remote-auth.ts
   │  │  │  │  ├── desktop-slash-commands.test.ts
   │  │  │  │  ├── desktop-slash-commands.ts
   │  │  │  │  ├── desktop-toolsets.test.ts
   │  │  │  │  ├── desktop-toolsets.ts
   │  │  │  │  ├── display-path.test.ts
   │  │  │  │  ├── display-path.ts
   │  │  │  │  ├── download-text.ts
   │  │  │  │  ├── draft-title.ts
   │  │  │  │  ├── drag-ghost.ts
   │  │  │  │  ├── embedded-images.test.ts
   │  │  │  │  ├── embedded-images.ts
   │  │  │  │  ├── escape-layers.test.ts
   │  │  │  │  ├── escape-layers.ts
   │  │  │  │  ├── excluded-paths.ts
   │  │  │  │  ├── external-link.test.tsx
   │  │  │  │  ├── external-link.tsx
   │  │  │  │  ├── file-preview-math.render.test.tsx
   │  │  │  │  ├── find-in-page-scope.test.ts
   │  │  │  │  ├── find-in-page-scope.ts
   │  │  │  │  ├── find-in-page.ts
   │  │  │  │  ├── format.ts
   │  │  │  │  ├── gateway-events.test.ts
   │  │  │  │  ├── gateway-events.ts
   │  │  │  │  ├── gateway-rpc.test.ts
   │  │  │  │  ├── gateway-rpc.ts
   │  │  │  │  ├── gateway-ws-url.test.ts
   │  │  │  │  ├── generated-images.test.ts
   │  │  │  │  ├── generated-images.ts
   │  │  │  │  ├── guest-pointer-guard.ts
   │  │  │  │  ├── haptics.ts
   │  │  │  │  ├── jimmy-open-target.test.ts
   │  │  │  │  ├── jimmy-open-target.ts
   │  │  │  │  ├── icons.ts
   │  │  │  │  ├── image-resize.test.ts
   │  │  │  │  ├── image-resize.ts
   │  │  │  │  ├── incremental-external-store-runtime.test.ts
   │  │  │  │  ├── incremental-external-store-runtime.ts
   │  │  │  │  ├── inflight-turn-journal.test.ts
   │  │  │  │  ├── inflight-turn-journal.ts
   │  │  │  │  ├── input-modality.test.ts
   │  │  │  │  ├── input-modality.ts
   │  │  │  │  ├── json-format.test.ts
   │  │  │  │  ├── json-format.ts
   │  │  │  │  ├── json-rpc-gateway-url-guard.test.ts
   │  │  │  │  ├── katex-memo.ts
   │  │  │  │  ├── keybinds
   │  │  │  │  │  ├── actions.test.ts
   │  │  │  │  │  ├── actions.ts
   │  │  │  │  │  ├── combo.test.ts
   │  │  │  │  │  ├── combo.ts
   │  │  │  │  │  ├── composer-focus-keys.test.ts
   │  │  │  │  │  ├── composer-focus-keys.ts
   │  │  │  │  │  ├── contributed-actions.test.ts
   │  │  │  │  │  └── use-keybind-hint.ts
   │  │  │  │  ├── keyed-timeouts.ts
   │  │  │  │  ├── loadout.ts
   │  │  │  │  ├── local-preview.test.ts
   │  │  │  │  ├── local-preview.ts
   │  │  │  │  ├── markdown-blocks.test.ts
   │  │  │  │  ├── markdown-blocks.ts
   │  │  │  │  ├── markdown-code.test.ts
   │  │  │  │  ├── markdown-code.ts
   │  │  │  │  ├── markdown-html-depth.test.ts
   │  │  │  │  ├── markdown-html-depth.ts
   │  │  │  │  ├── markdown-preprocess.file-preview.test.ts
   │  │  │  │  ├── markdown-preprocess.ts
   │  │  │  │  ├── markdown-table-widths.ts
   │  │  │  │  ├── mcp-brands.tsx
   │  │  │  │  ├── mcp-cost.test.ts
   │  │  │  │  ├── mcp-cost.ts
   │  │  │  │  ├── mcp-dashboard-oauth.test.ts
   │  │  │  │  ├── mcp-dashboard-oauth.ts
   │  │  │  │  ├── mcp-deeplink.test.ts
   │  │  │  │  ├── mcp-deeplink.ts
   │  │  │  │  ├── mcp-directory.ts
   │  │  │  │  ├── mcp-import.test.ts
   │  │  │  │  ├── mcp-import.ts
   │  │  │  │  ├── mcp-probe-cache.test.ts
   │  │  │  │  ├── mcp-probe-cache.ts
   │  │  │  │  ├── mcp-servers.ts
   │  │  │  │  ├── mcp-tool-filter.test.ts
   │  │  │  │  ├── mcp-tool-filter.ts
   │  │  │  │  ├── media.remote.test.ts
   │  │  │  │  ├── media.ts
   │  │  │  │  ├── middle-click.test.tsx
   │  │  │  │  ├── middle-click.ts
   │  │  │  │  ├── model-options.test.ts
   │  │  │  │  ├── model-options.ts
   │  │  │  │  ├── model-search-text.ts
   │  │  │  │  ├── model-status-label.test.ts
   │  │  │  │  ├── model-status-label.ts
   │  │  │  │  ├── mutable-ref.ts
   │  │  │  │  ├── oneshot.ts
   │  │  │  │  ├── path-compare.test.ts
   │  │  │  │  ├── path-compare.ts
   │  │  │  │  ├── persisted.test.ts
   │  │  │  │  ├── persisted.ts
   │  │  │  │  ├── personalities.ts
   │  │  │  │  ├── platform.ts
   │  │  │  │  ├── plugin-source-urls.test.ts
   │  │  │  │  ├── plugin-source-urls.ts
   │  │  │  │  ├── pointer-drag.ts
   │  │  │  │  ├── pool.test.ts
   │  │  │  │  ├── pool.ts
   │  │  │  │  ├── preview-act
   │  │  │  │  │  ├── act-in-page.test.ts
   │  │  │  │  │  ├── act-in-page.ts
   │  │  │  │  │  ├── identity.ts
   │  │  │  │  │  ├── naming.test.ts
   │  │  │  │  │  ├── naming.ts
   │  │  │  │  │  ├── types.ts
   │  │  │  │  │  ├── visibility.ts
   │  │  │  │  │  ├── watch-in-page.test.ts
   │  │  │  │  │  └── watch-in-page.ts
   │  │  │  │  ├── preview-reach.test.ts
   │  │  │  │  ├── preview-reach.ts
   │  │  │  │  ├── preview-targets.test.ts
   │  │  │  │  ├── preview-targets.ts
   │  │  │  │  ├── profile-color.ts
   │  │  │  │  ├── project-idea-templates.ts
   │  │  │  │  ├── provider-setup-errors.test.ts
   │  │  │  │  ├── provider-setup-errors.ts
   │  │  │  │  ├── query-client.test.ts
   │  │  │  │  ├── query-client.ts
   │  │  │  │  ├── raf-coalesce.ts
   │  │  │  │  ├── reasoning-blocks.test.ts
   │  │  │  │  ├── reasoning-blocks.ts
   │  │  │  │  ├── reasoning-effort.test.ts
   │  │  │  │  ├── reasoning-effort.ts
   │  │  │  │  ├── reconnect-backoff.test.ts
   │  │  │  │  ├── reconnect-backoff.ts
   │  │  │  │  ├── remote-url.test.ts
   │  │  │  │  ├── remote-url.ts
   │  │  │  │  ├── render-weight.test.ts
   │  │  │  │  ├── render-weight.ts
   │  │  │  │  ├── renderer-loop-pause.test.ts
   │  │  │  │  ├── renderer-loop-pause.ts
   │  │  │  │  ├── reorder.ts
   │  │  │  │  ├── runtime-readiness.test.ts
   │  │  │  │  ├── runtime-readiness.ts
   │  │  │  │  ├── sanitize.test.ts
   │  │  │  │  ├── sanitize.ts
   │  │  │  │  ├── selectable-card.ts
   │  │  │  │  ├── session-branch-tree.test.ts
   │  │  │  │  ├── session-branch-tree.ts
   │  │  │  │  ├── session-date-groups.test.ts
   │  │  │  │  ├── session-date-groups.ts
   │  │  │  │  ├── session-export.ts
   │  │  │  │  ├── session-ids.test.ts
   │  │  │  │  ├── session-ids.ts
   │  │  │  │  ├── session-link-title.test.ts
   │  │  │  │  ├── session-link-title.ts
   │  │  │  │  ├── session-project-label.ts
   │  │  │  │  ├── session-refs.test.ts
   │  │  │  │  ├── session-refs.ts
   │  │  │  │  ├── session-search.test.ts
   │  │  │  │  ├── session-search.ts
   │  │  │  │  ├── session-signatures.test.ts
   │  │  │  │  ├── session-signatures.ts
   │  │  │  │  ├── session-source.test.ts
   │  │  │  │  ├── session-source.ts
   │  │  │  │  ├── slash-completion-cache.ts
   │  │  │  │  ├── speech-text.test.ts
   │  │  │  │  ├── speech-text.ts
   │  │  │  │  ├── spoken-reply.test.ts
   │  │  │  │  ├── spoken-reply.ts
   │  │  │  │  ├── stable-array.ts
   │  │  │  │  ├── statusbar.tsx
   │  │  │  │  ├── steered-turn-hydration-order.test.ts
   │  │  │  │  ├── storage.test.ts
   │  │  │  │  ├── storage.ts
   │  │  │  │  ├── summarize-command.test.ts
   │  │  │  │  ├── summarize-command.ts
   │  │  │  │  ├── svg-image.test.ts
   │  │  │  │  ├── svg-image.ts
   │  │  │  │  ├── text.ts
   │  │  │  │  ├── thinking-sound.test.ts
   │  │  │  │  ├── thinking-sound.ts
   │  │  │  │  ├── time.test.ts
   │  │  │  │  ├── time.ts
   │  │  │  │  ├── todos.test.ts
   │  │  │  │  ├── todos.ts
   │  │  │  │  ├── tool-render-class.ts
   │  │  │  │  ├── tool-result-summary.test.ts
   │  │  │  │  ├── tool-result-summary.ts
   │  │  │  │  ├── tool-run-continuity.test.ts
   │  │  │  │  ├── tour
   │  │  │  │  │  ├── app-tour.css
   │  │  │  │  │  ├── collect-targets.ts
   │  │  │  │  │  ├── engine.test.ts
   │  │  │  │  │  ├── engine.ts
   │  │  │  │  │  ├── index.ts
   │  │  │  │  │  ├── run-tour.ts
   │  │  │  │  │  └── spotlight-blur.ts
   │  │  │  │  ├── trackpad-gestures.ts
   │  │  │  │  ├── transcript-directives.test.ts
   │  │  │  │  ├── transcript-directives.ts
   │  │  │  │  ├── update-copy.test.ts
   │  │  │  │  ├── update-copy.ts
   │  │  │  │  ├── use-enter-animation.test.tsx
   │  │  │  │  ├── use-enter-animation.ts
   │  │  │  │  ├── use-session-slice.ts
   │  │  │  │  ├── utils.ts
   │  │  │  │  ├── version-status.test.ts
   │  │  │  │  ├── version-status.ts
   │  │  │  │  ├── voice-barge-in.ts
   │  │  │  │  ├── voice-playback.ts
   │  │  │  │  ├── voice-stop-word.test.ts
   │  │  │  │  ├── voice-stop-word.ts
   │  │  │  │  ├── wake-client-capture.ts
   │  │  │  │  ├── wake-indicator.test.ts
   │  │  │  │  ├── wake-indicator.ts
   │  │  │  │  ├── wake-sound.test.ts
   │  │  │  │  ├── wake-sound.ts
   │  │  │  │  └── yolo-session.ts
   │  │  │  ├── main.tsx
   │  │  │  ├── pairing-scope.test.ts
   │  │  │  ├── plugin-socket-scope.test.ts
   │  │  │  ├── plugins
   │  │  │  │  ├── accent
   │  │  │  │  │  ├── picker.tsx
   │  │  │  │  │  └── plugin.tsx
   │  │  │  │  ├── hello-runtime
   │  │  │  │  │  └── plugin.runtime.js
   │  │  │  │  ├── jimmy-bots
   │  │  │  │  │  ├── LICENSE
   │  │  │  │  │  ├── plugin.js
   │  │  │  │  │  └── tests
   │  │  │  │  │    ├── active-now-strip.test.mjs
   │  │  │  │  │    ├── activity-toasts.test.mjs
   │  │  │  │  │    ├── blobatar-shapes.test.mjs
   │  │  │  │  │    ├── bot-delete.test.mjs
   │  │  │  │  │    ├── bot-meta-asset-sync.test.mjs
   │  │  │  │  │    ├── bot-meta-hydrate.test.mjs
   │  │  │  │  │    ├── bot-meta-persistence.test.mjs
   │  │  │  │  │    ├── bot-meta-sync.test.mjs
   │  │  │  │  │    ├── bots-search.test.mjs
   │  │  │  │  │    ├── canonical-chat-adopt-before-mint.test.mjs
   │  │  │  │  │    ├── canonical-chat-creation.test.mjs
   │  │  │  │  │    ├── canonical-chat-empty-recovery.test.mjs
   │  │  │  │  │    ├── canonical-chat-identity.test.mjs
   │  │  │  │  │    ├── canonical-chat-pin.test.mjs
   │  │  │  │  │    ├── create-agent-clone-default.test.mjs
   │  │  │  │  │    ├── create-agent-mcp-setup.test.mjs
   │  │  │  │  │    ├── create-group-chat.test.mjs
   │  │  │  │  │    ├── cross-connection-bots.test.mjs
   │  │  │  │  │    ├── draft-agent-discard.test.mjs
   │  │  │  │  │    ├── duplicate-bot.test.mjs
   │  │  │  │  │    ├── embed-real-capabilities.test.mjs
   │  │  │  │  │    ├── embed-skills-view.test.mjs
   │  │  │  │  │    ├── face-catchlight.test.mjs
   │  │  │  │  │    ├── face-clock.test.mjs
   │  │  │  │  │    ├── focused-bot-highlight.test.mjs
   │  │  │  │  │    ├── group-activity.test.mjs
   │  │  │  │  │    ├── group-chat-attachments.test.mjs
   │  │  │  │  │    ├── group-chat-identity-edit.test.mjs
   │  │  │  │  │    ├── group-chat.test.mjs
   │  │  │  │  │    ├── group-mention-composer.test.mjs
   │  │  │  │  │    ├── hide-bot-chats.test.mjs
   │  │  │  │  │    ├── hide-bots.test.mjs
   │  │  │  │  │    ├── hub-picker-guard.test.mjs
   │  │  │  │  │    ├── legacy-sdk-compat.test.mjs
   │  │  │  │  │    ├── mention-completions.test.mjs
   │  │  │  │  │    ├── mention-handoff-quoting.test.mjs
   │  │  │  │  │    ├── mention-renamed-bots.test.mjs
   │  │  │  │  │    ├── model-inherit.test.mjs
   │  │  │  │  │    ├── multi-source-roster.test.mjs
   │  │  │  │  │    ├── new-compact-guard.test.mjs
   │  │  │  │  │    ├── pane-dock-layout.test.mjs
   │  │  │  │  │    ├── pet-fetch.test.mjs
   │  │  │  │  │    ├── profile-prewarm.test.mjs
   │  │  │  │  │    ├── remote-dm-delivery.test.mjs
   │  │  │  │  │    ├── roster-groups.test.mjs
   │  │  │  │  │    ├── roster-preview.test.mjs
   │  │  │  │  │    ├── routine-owner.test.mjs
   │  │  │  │  │    ├── routine-prompt.test.mjs
   │  │  │  │  │    ├── routines-error.test.mjs
   │  │  │  │  │    ├── routines-filter-hint.test.mjs
   │  │  │  │  │    ├── routines-pause-failure.test.mjs
   │  │  │  │  │    ├── routines-profile-scope.test.mjs
   │  │  │  │  │    ├── routines-selected-bot.test.mjs
   │  │  │  │  │    ├── single-flight.test.mjs
   │  │  │  │  │    └── soul-protocol-backfill.test.mjs
   │  │  │  │  ├── kanban
   │  │  │  │  │  ├── api.ts
   │  │  │  │  │  ├── board-switcher.tsx
   │  │  │  │  │  ├── board.tsx
   │  │  │  │  │  ├── completion-notify.test.ts
   │  │  │  │  │  ├── completion-notify.ts
   │  │  │  │  │  ├── drawer.tsx
   │  │  │  │  │  ├── i18n.ts
   │  │  │  │  │  ├── kanban.css
   │  │  │  │  │  ├── model-override.test.tsx
   │  │  │  │  │  ├── model-override.tsx
   │  │  │  │  │  ├── orchestration.tsx
   │  │  │  │  │  ├── plugin.tsx
   │  │  │  │  │  ├── types.ts
   │  │  │  │  │  └── ui.tsx
   │  │  │  │  └── README.md
   │  │  │  ├── sdk
   │  │  │  │  ├── host-state.test.ts
   │  │  │  │  ├── index.test.ts
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── plugin-open-session-plan.test.ts
   │  │  │  │  ├── plugin-open-session-plan.ts
   │  │  │  │  ├── profile-routing.test.ts
   │  │  │  │  └── runtime.ts
   │  │  │  ├── store
   │  │  │  │  ├── active-work.test.ts
   │  │  │  │  ├── active-work.ts
   │  │  │  │  ├── activity.ts
   │  │  │  │  ├── agent-notices.test.ts
   │  │  │  │  ├── agent-notices.ts
   │  │  │  │  ├── agent-plugins.ts
   │  │  │  │  ├── ambient.ts
   │  │  │  │  ├── approval-mode.test.ts
   │  │  │  │  ├── approval-mode.ts
   │  │  │  │  ├── artifacts.test.ts
   │  │  │  │  ├── artifacts.ts
   │  │  │  │  ├── backdrop.ts
   │  │  │  │  ├── background-delegation.test.ts
   │  │  │  │  ├── background-delegation.ts
   │  │  │  │  ├── billing-block.test.ts
   │  │  │  │  ├── billing-block.ts
   │  │  │  │  ├── boot.ts
   │  │  │  │  ├── clarify.test.ts
   │  │  │  │  ├── clarify.ts
   │  │  │  │  ├── coding-status.test.ts
   │  │  │  │  ├── coding-status.ts
   │  │  │  │  ├── command-palette.ts
   │  │  │  │  ├── compaction.test.ts
   │  │  │  │  ├── compaction.ts
   │  │  │  │  ├── completion-sound.ts
   │  │  │  │  ├── composer-actions.ts
   │  │  │  │  ├── composer-input-history.test.ts
   │  │  │  │  ├── composer-input-history.ts
   │  │  │  │  ├── composer-popout-preference.test.ts
   │  │  │  │  ├── composer-popout.test.ts
   │  │  │  │  ├── composer-popout.ts
   │  │  │  │  ├── composer-queue.test.ts
   │  │  │  │  ├── composer-queue.ts
   │  │  │  │  ├── composer-status.test.ts
   │  │  │  │  ├── composer-status.ts
   │  │  │  │  ├── composer-suggestions.test.ts
   │  │  │  │  ├── composer-suggestions.ts
   │  │  │  │  ├── composer.test.ts
   │  │  │  │  ├── composer.ts
   │  │  │  │  ├── confirm.ts
   │  │  │  │  ├── connections.test.ts
   │  │  │  │  ├── connections.ts
   │  │  │  │  ├── cron-model-impact-scope.test.ts
   │  │  │  │  ├── cron-model-impact-scope.ts
   │  │  │  │  ├── cron-model-impact.test.ts
   │  │  │  │  ├── cron-model-impact.ts
   │  │  │  │  ├── cron.test.ts
   │  │  │  │  ├── cron.ts
   │  │  │  │  ├── data-url-read-max.test.ts
   │  │  │  │  ├── data-url-read-max.ts
   │  │  │  │  ├── disable-f12.ts
   │  │  │  │  ├── display-timestamps.ts
   │  │  │  │  ├── embed-consent.ts
   │  │  │  │  ├── file-actions.test.ts
   │  │  │  │  ├── file-actions.ts
   │  │  │  │  ├── find-in-page.ts
   │  │  │  │  ├── gateway-activation-prune-lease.test.ts
   │  │  │  │  ├── gateway-agent-scope.test.ts
   │  │  │  │  ├── gateway-connection-lifecycle.test.ts
   │  │  │  │  ├── gateway-connection-scope.test.ts
   │  │  │  │  ├── gateway-profile-request.test.ts
   │  │  │  │  ├── gateway-reconnect.test.ts
   │  │  │  │  ├── gateway-reconnect.ts
   │  │  │  │  ├── gateway-shared-remote.test.ts
   │  │  │  │  ├── gateway-switch.test.ts
   │  │  │  │  ├── gateway-switch.ts
   │  │  │  │  ├── gateway.ts
   │  │  │  │  ├── goals.test.ts
   │  │  │  │  ├── goals.ts
   │  │  │  │  ├── haptics.ts
   │  │  │  │  ├── hub-actions.test.ts
   │  │  │  │  ├── hub-actions.ts
   │  │  │  │  ├── hud.test.ts
   │  │  │  │  ├── hud.ts
   │  │  │  │  ├── intro-splash.ts
   │  │  │  │  ├── keep-awake.test.ts
   │  │  │  │  ├── keep-awake.ts
   │  │  │  │  ├── keybinds.ts
   │  │  │  │  ├── layout-connection-scope.test.ts
   │  │  │  │  ├── layout-dismissed-projects.test.ts
   │  │  │  │  ├── layout-pinned-order.test.ts
   │  │  │  │  ├── layout-sidebar-view.test.ts
   │  │  │  │  ├── layout.ts
   │  │  │  │  ├── live-sync.ts
   │  │  │  │  ├── mcp-deeplink-install.ts
   │  │  │  │  ├── mcp-health.test.ts
   │  │  │  │  ├── mcp-health.ts
   │  │  │  │  ├── mcp-setup.ts
   │  │  │  │  ├── model-presets.test.ts
   │  │  │  │  ├── model-presets.ts
   │  │  │  │  ├── model-visibility.test.ts
   │  │  │  │  ├── model-visibility.ts
   │  │  │  │  ├── nanostores-batch-guard.test.ts
   │  │  │  │  ├── native-notifications.test.ts
   │  │  │  │  ├── native-notifications.ts
   │  │  │  │  ├── notifications.test.ts
   │  │  │  │  ├── notifications.ts
   │  │  │  │  ├── notify-baseline.ts
   │  │  │  │  ├── onboarding.test.ts
   │  │  │  │  ├── onboarding.ts
   │  │  │  │  ├── pane-focus.test.ts
   │  │  │  │  ├── pane-focus.ts
   │  │  │  │  ├── panes.test.ts
   │  │  │  │  ├── panes.ts
   │  │  │  │  ├── pet-gallery.test.ts
   │  │  │  │  ├── pet-gallery.ts
   │  │  │  │  ├── pet-generate.ts
   │  │  │  │  ├── pet-overlay.ts
   │  │  │  │  ├── pet.test.ts
   │  │  │  │  ├── pet.ts
   │  │  │  │  ├── plugin-install-request.ts
   │  │  │  │  ├── power.ts
   │  │  │  │  ├── preview-edit.ts
   │  │  │  │  ├── preview-open-browser.test.ts
   │  │  │  │  ├── preview-persistence.test.ts
   │  │  │  │  ├── preview-status.test.ts
   │  │  │  │  ├── preview-status.ts
   │  │  │  │  ├── preview.test.ts
   │  │  │  │  ├── preview.ts
   │  │  │  │  ├── profile-agent-activation.test.ts
   │  │  │  │  ├── profile-share.test.ts
   │  │  │  │  ├── profile-share.ts
   │  │  │  │  ├── profile.test.ts
   │  │  │  │  ├── profile.ts
   │  │  │  │  ├── projects.test.ts
   │  │  │  │  ├── projects.ts
   │  │  │  │  ├── prompts.test.ts
   │  │  │  │  ├── prompts.ts
   │  │  │  │  ├── provider-collapse.ts
   │  │  │  │  ├── provider-wait.ts
   │  │  │  │  ├── pull-requests.ts
   │  │  │  │  ├── quick-entry.test.ts
   │  │  │  │  ├── quick-entry.ts
   │  │  │  │  ├── reactions-enabled.ts
   │  │  │  │  ├── reactions-local.ts
   │  │  │  │  ├── reactions.test.ts
   │  │  │  │  ├── reactions.ts
   │  │  │  │  ├── reasoning-disclosure.ts
   │  │  │  │  ├── review.test.ts
   │  │  │  │  ├── review.ts
   │  │  │  │  ├── route-tiles.ts
   │  │  │  │  ├── session-color.test.ts
   │  │  │  │  ├── session-color.ts
   │  │  │  │  ├── session-dot-state.test.ts
   │  │  │  │  ├── session-dot-state.ts
   │  │  │  │  ├── session-list-density.test.ts
   │  │  │  │  ├── session-list-density.ts
   │  │  │  │  ├── session-pin-sync.test.ts
   │  │  │  │  ├── session-pin-sync.ts
   │  │  │  │  ├── session-request-router.test.ts
   │  │  │  │  ├── session-request-router.ts
   │  │  │  │  ├── session-states-eviction.test.ts
   │  │  │  │  ├── session-states-scopes.test.ts
   │  │  │  │  ├── session-states.test.ts
   │  │  │  │  ├── session-states.ts
   │  │  │  │  ├── session-switcher.test.ts
   │  │  │  │  ├── session-switcher.ts
   │  │  │  │  ├── session-sync.ts
   │  │  │  │  ├── session-unread-remote.test.ts
   │  │  │  │  ├── session-unread-remote.ts
   │  │  │  │  ├── session-unread-tile.test.ts
   │  │  │  │  ├── session-unread.test.ts
   │  │  │  │  ├── session-unread.ts
   │  │  │  │  ├── session-watchdog.test.ts
   │  │  │  │  ├── session.test.ts
   │  │  │  │  ├── session.ts
   │  │  │  │  ├── settings-scope.test.ts
   │  │  │  │  ├── settings-scope.ts
   │  │  │  │  ├── sidebar-archive.ts
   │  │  │  │  ├── sidebar-collapse-persistence.test.ts
   │  │  │  │  ├── sidebar-sort.test.ts
   │  │  │  │  ├── sidebar-sort.ts
   │  │  │  │  ├── starmap.ts
   │  │  │  │  ├── statusbar-prefs.ts
   │  │  │  │  ├── subagents.test.ts
   │  │  │  │  ├── subagents.ts
   │  │  │  │  ├── suggestion-providers
   │  │  │  │  │  ├── cron.test.ts
   │  │  │  │  │  ├── cron.ts
   │  │  │  │  │  ├── github.test.ts
   │  │  │  │  │  ├── github.ts
   │  │  │  │  │  ├── mcp.test.ts
   │  │  │  │  │  ├── mcp.ts
   │  │  │  │  │  ├── repair.test.ts
   │  │  │  │  │  ├── repair.ts
   │  │  │  │  │  ├── skill.test.ts
   │  │  │  │  │  └── skill.ts
   │  │  │  │  ├── system-actions.ts
   │  │  │  │  ├── thread-scroll.ts
   │  │  │  │  ├── todos.test.ts
   │  │  │  │  ├── todos.ts
   │  │  │  │  ├── tool-diffs.test.ts
   │  │  │  │  ├── tool-diffs.ts
   │  │  │  │  ├── tool-dismiss.ts
   │  │  │  │  ├── tool-drafting.ts
   │  │  │  │  ├── tool-view.ts
   │  │  │  │  ├── transcript-tail-cache.test.ts
   │  │  │  │  ├── transcript-tail-cache.ts
   │  │  │  │  ├── transcript-tail.ts
   │  │  │  │  ├── translucency.test.ts
   │  │  │  │  ├── translucency.ts
   │  │  │  │  ├── updates.test.ts
   │  │  │  │  ├── updates.ts
   │  │  │  │  ├── voice-playback.ts
   │  │  │  │  ├── voice-prefs.test.ts
   │  │  │  │  ├── voice-prefs.ts
   │  │  │  │  ├── wake-word.test.ts
   │  │  │  │  ├── wake-word.ts
   │  │  │  │  ├── windows.test.ts
   │  │  │  │  ├── windows.ts
   │  │  │  │  ├── working-ids-stored-id.test.ts
   │  │  │  │  ├── workspace-events.ts
   │  │  │  │  └── zoom.ts
   │  │  │  ├── styles.css
   │  │  │  ├── test
   │  │  │  │  ├── deferred.ts
   │  │  │  │  ├── jsdom.ts
   │  │  │  │  ├── oauth-provider.ts
   │  │  │  │  ├── react-root.ts
   │  │  │  │  ├── session-info.ts
   │  │  │  │  └── window-state.ts
   │  │  │  ├── themes
   │  │  │  │  ├── accent-override.ts
   │  │  │  │  ├── backend-sync.test.ts
   │  │  │  │  ├── backend-sync.ts
   │  │  │  │  ├── color.ts
   │  │  │  │  ├── context.test.tsx
   │  │  │  │  ├── context.tsx
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── install.test.ts
   │  │  │  │  ├── install.ts
   │  │  │  │  ├── presets.test.ts
   │  │  │  │  ├── presets.ts
   │  │  │  │  ├── profile-theme.test.ts
   │  │  │  │  ├── request.test.tsx
   │  │  │  │  ├── request.ts
   │  │  │  │  ├── retint.test.ts
   │  │  │  │  ├── retint.ts
   │  │  │  │  ├── skin.test.ts
   │  │  │  │  ├── skin.ts
   │  │  │  │  ├── types.ts
   │  │  │  │  ├── use-skin-command.ts
   │  │  │  │  ├── user-themes.test.ts
   │  │  │  │  ├── user-themes.ts
   │  │  │  │  ├── vscode.test.ts
   │  │  │  │  └── vscode.ts
   │  │  │  ├── types
   │  │  │  │  └── jimmy.ts
   │  │  │  ├── vite-env.d.ts
   │  │  │  └── webhooks-rest.test.ts
   │  │  ├── tsconfig.e2e.json
   │  │  ├── tsconfig.electron.json
   │  │  ├── tsconfig.json
   │  │  ├── vite.config.ts
   │  │  ├── vitest.config.ts
   │  │  └── vitest.setup.ts
   │  └── shared
   │    ├── eslint.config.mjs
   │    ├── package.json
   │    ├── src
   │     │  ├── backend-scope.ts
   │     │  ├── billing-payment-method.test-d.ts
   │     │  ├── billing-policy.ts
   │     │  ├── billing-types.ts
   │     │  ├── charge-settlement.ts
   │     │  ├── cron-trigger-controller.ts
   │     │  ├── data-url-read-max.ts
   │     │  ├── index.ts
   │     │  ├── json-rpc-gateway.ts
   │     │  ├── skill-scaffold.test.ts
   │     │  ├── skill-scaffold.ts
   │     │  ├── skin.ts
   │     │  ├── translucency.ts
   │     │  └── websocket-url.ts
   │    └── tsconfig.json
  ├── assets
   │  └── banner.png
  ├── batch_runner.py
  ├── cli-config.yaml.example
  ├── cli.py
  ├── constraints-termux.txt
  ├── CONTRIBUTING.es.md
  ├── CONTRIBUTING.md
  ├── contributors
   │  ├── emails
   │  │  ├── 0301chris@gmail.com
   │  │  ├── 0xarkstar@users.noreply.github.com
   │  │  ├── 0xprincess@nuconstruct.xyz
   │  │  ├── 1051445024@qq.com
   │  │  ├── 114367649+knoal@users.noreply.github.com
   │  │  ├── 116476090+JeffStone69@users.noreply.github.com
   │  │  ├── 1265291278@qq.com
   │  │  ├── 1347825413@qq.com
   │  │  ├── 1373636680@qq.com
   │  │  ├── 15167896+2001Y@users.noreply.github.com
   │  │  ├── 155588579+spiky02plateau@users.noreply.github.com
   │  │  ├── 1759158233@qq.com
   │  │  ├── 1762459322@qq.com
   │  │  ├── 1940428933@qq.com
   │  │  ├── 203146215+monerostar@users.noreply.github.com
   │  │  ├── 225291640+camaleonidas@users.noreply.github.com
   │  │  ├── 232201106@qq.com
   │  │  ├── 2418548+markoub@users.noreply.github.com
   │  │  ├── 2436887475@qq.com
   │  │  ├── 260355617@qq.com
   │  │  ├── 262373281+vexclawx31@users.noreply.github.com
   │  │  ├── 269728612+metamon-p@users.noreply.github.com
   │  │  ├── 275831447+maff-t2b@users.noreply.github.com
   │  │  ├── 285329547+xaviersudre@users.noreply.github.com
   │  │  ├── 286182457+Da7-Tech@users.noreply.github.com
   │  │  ├── 3115763429@qq.com
   │  │  ├── 314574126@qq.com
   │  │  ├── 3Nya3@users.noreply.github.com
   │  │  ├── 445481611@qq.com
   │  │  ├── 46404230+peetteerr@users.noreply.github.com
   │  │  ├── 48723787+chuenchen309@users.noreply.github.com
   │  │  ├── 50810385+tigercraft4@users.noreply.github.com
   │  │  ├── 55nx954gn6-debug@users.noreply.github.com
   │  │  ├── 56281588+LevSky22@users.noreply.github.com
   │  │  ├── 582149912@qq.com
   │  │  ├── 602028@ky-tech.com.cn
   │  │  ├── 604maestro@protonmail.com
   │  │  ├── 619963502@qq.com
   │  │  ├── 807847218@qq.com
   │  │  ├── 840596168@qq.com
   │  │  ├── 87degrees@87ui-Macmini.local
   │  │  ├── a.neyman17@gmail.com
   │  │  ├── a.weiker@sap.com
   │  │  ├── a9@A9deMac-mini.local
   │  │  ├── a@l
   │  │  ├── aakash@plasticlabs.ai
   │  │  ├── aameobius@gmail.com
   │  │  ├── abcdjmm970703@gmail.com
   │  │  ├── abdulsalamalotaibi86@gmail.com
   │  │  ├── adam@exo.ai
   │  │  ├── admin@diaoan.xyz
   │  │  ├── adrian.soto6@gmail.com
   │  │  ├── adybag14@gmail.com
   │  │  ├── afgl_mk93@icloud.com
   │  │  ├── afournier@nvidia.com
   │  │  ├── agent@jimmy.dev
   │  │  ├── agent@openclaw.local
   │  │  ├── agents@joinsensie.com
   │  │  ├── ahamoudhy@gmail.com
   │  │  ├── ahmedmoro@gmail.com
   │  │  ├── ahmetsonersancak@anadolu.edu.tr
   │  │  ├── ajzrva@gmail.com
   │  │  ├── akitani@akitaninoMac-mini.local
   │  │  ├── akshankrithick305@gmail.com
   │  │  ├── akulayash1996@gmail.com
   │  │  ├── alanrbox@gmail.com
   │  │  ├── alcibiades.eth@protonmail.com
   │  │  ├── aleks.clark@gmail.com
   │  │  ├── alex-secure@tuta.io
   │  │  ├── alex.moreno161100@gmail.com
   │  │  ├── alexgong7@outlook.com
   │  │  ├── almurat@Almurats-MacBook-Pro.local
   │  │  ├── alvaro.sanchez-mariscal@oracle.com
   │  │  ├── alzilla22@gmail.com
   │  │  ├── amdnative@gmail.com
   │  │  ├── anatolij.laptev.1991@gmail.com
   │  │  ├── and@appz.cloud
   │  │  ├── andrew.lg.ford@gmail.com
   │  │  ├── andrexibiza@gmail.com
   │  │  ├── andy.loafoe@gmail.com
   │  │  ├── andy@andydeMac-mini-2.local
   │  │  ├── angeon922@gmail.com
   │  │  ├── anoop.mehendale@gmail.com
   │  │  ├── anthony.ai.assistant@gmail.com
   │  │  ├── arccat114@gmail.com
   │  │  ├── ariel@vortexradar.com
   │  │  ├── armaandhawan61@gmail.com
   │  │  ├── asscan@189.cn
   │  │  ├── assiri@gmail.com
   │  │  ├── at@aisec.co.il
   │  │  ├── atakan1705@hotmail.com
   │  │  ├── austinpickett@users.noreply.github.com
   │  │  ├── awain7@gmail.com
   │  │  ├── Axmr1@users.noreply.github.com
   │  │  ├── ayoub@gmail.com
   │  │  ├── ayushnangia16@gmail.com
   │  │  ├── azureuser@Main.n1l05aasmpie5onxhehb5y5gra.lx.internal.cloudapp.net
   │  │  ├── a_espinosa@live.com
   │  │  ├── baslam@users.noreply.github.com
   │  │  ├── bb@users.noreply.github.com
   │  │  ├── bbasketballer75@gmail.com
   │  │  ├── bedirhancode@users.noreply.github.com
   │  │  ├── beingsabundant@gmail.com
   │  │  ├── ben.ross@moov.io
   │  │  ├── ben@ben-phillips.net
   │  │  ├── ben@whetstone.com.au
   │  │  ├── benjamin-liang@outlook.com
   │  │  ├── benjamin2026-dot@users.noreply.github.com
   │  │  ├── bennybuoy@users.noreply.github.com
   │  │  ├── bensheridanedwards@gmail.com
   │  │  ├── betodepaola@meta.com
   │  │  ├── biz@topherross.com
   │  │  ├── bkashjee@users.noreply.github.com
   │  │  ├── borje@dqsverige.se
   │  │  ├── bot@bkstock.dev
   │  │  ├── boumagent@gmail.com
   │  │  ├── brdpedroo@gmail.com
   │  │  ├── brian717fr@gmail.com
   │  │  ├── brian@bsweatt.com
   │  │  ├── brice@brice.net
   │  │  ├── brunopira@gmail.com
   │  │  ├── cad@arcabot.ai
   │  │  ├── caleb.deleeuw@gmail.com
   │  │  ├── carl@carltaylor.com.au
   │  │  ├── carl@sempervirens.no
   │  │  ├── carlotestor@users.noreply.github.com
   │  │  ├── carnie-bot@openclaw.local
   │  │  ├── carrion256@proton.me
   │  │  ├── cassie@omg.lol
   │  │  ├── cation98@yahoo.com
   │  │  ├── centerid@naver.com
   │  │  ├── chancelu@users.noreply.github.com
   │  │  ├── chaosxinglong@gmail.com
   │  │  ├── checo520@outlook.com
   │  │  ├── chelsealong@126.com
   │  │  ├── chengxizhou6@gmail.com
   │  │  ├── chenjin@jimmy.local
   │  │  ├── chenyang.yl@alibaba-inc.com
   │  │  ├── chris@scalelean.com
   │  │  ├── cicav@users.noreply.github.com
   │  │  ├── citizendev9c@users.noreply.github.com
   │  │  ├── cjwang@sowork.tw
   │  │  ├── ckorhonen@gmail.com
   │  │  ├── cluster2@Cluster2s-Mac-Studio.local
   │  │  ├── cmoiccool@users.noreply.github.com
   │  │  ├── coder@trevhome.local
   │  │  ├── coe0718+tuck@gmail.com
   │  │  ├── coe0718@icloud.com
   │  │  ├── coffee@coffeebot.dev
   │  │  ├── colin@colingreig.com
   │  │  ├── connorjosephblack@gmail.com
   │  │  ├── contact@eliebruno.com
   │  │  ├── contact@grahfmusic.com
   │  │  ├── contact@nytemode.com
   │  │  ├── contato@webtecnica.com.br
   │  │  ├── content@tyfpro.com
   │  │  ├── copii.list@gmail.com
   │  │  ├── core@lfdm.co
   │  │  ├── craig@shotflame.local
   │  │  ├── cto@phrase.local
   │  │  ├── cursoragent@cursor.com
   │  │  ├── cwt@users.noreply.github.com
   │  │  ├── Cyrus@ThreeSixs-Mac-Mini.local
   │  │  ├── d@rko.rs
   │  │  ├── dai.suzuki.829@gmail.com
   │  │  ├── damian.kluk.92@gmail.com
   │  │  ├── dan.brunsdon@gmail.com
   │  │  ├── daniel.blank@reportsolution.de
   │  │  ├── daniel21436@hotmail.com
   │  │  ├── danielrpike9@gmail.com
   │  │  ├── dasilva.daniel6@gmail.com
   │  │  ├── david@lexgenius.ai
   │  │  ├── DavidMetcalfe@users.noreply.github.com
   │  │  ├── deepujain@gmail.com
   │  │  ├── degensmoke@gmail.com
   │  │  ├── deusyu@users.noreply.github.com
   │  │  ├── dev@redeyesolutions.dev
   │  │  ├── devops@sycamore.group
   │  │  ├── dhravya@supermemory.com
   │  │  ├── dhruv.modi2345@gmail.com
   │  │  ├── dhruv.raajjeev@gmail.com
   │  │  ├── dhruvkejri9@gmail.com
   │  │  ├── diamantejc87@gmail.com
   │  │  ├── dickson.neoh@gmail.com
   │  │  ├── dillontownsel@gmail.com
   │  │  ├── dinmail@gmail.com
   │  │  ├── dixit.tanmay1995@gmail.com
   │  │  ├── dnethusahan.h05@gmail.com
   │  │  ├── dombejar@users.noreply.github.com
   │  │  ├── dominicbejar@gmail.com
   │  │  ├── dongjiang1989@126.com
   │  │  ├── dqdung205@gmail.com
   │  │  ├── drew@kainotomic.com
   │  │  ├── drissman@gmail.com
   │  │  ├── dstkwll@users.noreply.github.com
   │  │  ├── dustin.persek@protonmail.com
   │  │  ├── eagleyouxiang@gmail.com
   │  │  ├── eapwrk@gmail.com
   │  │  ├── eazye19@users.noreply.github.com
   │  │  ├── ebablick@hpc-gridware.com
   │  │  ├── egilewski@egilewski.com
   │  │  ├── elco@thedaoist.gg
   │  │  ├── eleanor@intellectronica.net
   │  │  ├── elisam@nvidia.com
   │  │  ├── ella@cincin.mesh
   │  │  ├── eman1369a@gmail.com
   │  │  ├── emilio.jesus.lasheras.romero@nttdata.com
   │  │  ├── emodoteth@gmail.com
   │  │  ├── emopilot@163.com
   │  │  ├── Enough1122@users.noreply.github.com
   │  │  ├── ergorburak33@gmail.com
   │  │  ├── eri@plasticlabs.ai
   │  │  ├── eric@erickornacki.com
   │  │  ├── erick@kinnee.net
   │  │  ├── esther@feedmob.com
   │  │  ├── evangonggyf@gmail.com
   │  │  ├── executus.ahli@gmail.com
   │  │  ├── ezell.matt@gmail.com
   │  │  ├── f1aggo_macair@f1aggo-macairdeMacBook-Air.local
   │  │  ├── f4lko@pm.me
   │  │  ├── fangliquan@oppo.com
   │  │  ├── fangliquan@qq.com
   │  │  ├── fanyu@moonshot.cn
   │  │  ├── fatbigpig979@gmail.com
   │  │  ├── fattchris@users.noreply.github.com
   │  │  ├── fazerluga@gmail.com
   │  │  ├── fboutboul@free.fr
   │  │  ├── felipe.cavalcanti.rj@gmail.com
   │  │  ├── fengtianyu_danny@163.com
   │  │  ├── floatingrain@yeah.net
   │  │  ├── florianvalade@Florians-Mac-mini.local
   │  │  ├── fmy3@qq.com
   │  │  ├── fraser.humphries@gmail.com
   │  │  ├── fred.vanwagenen@gmail.com
   │  │  ├── fukutake@convi.ne.jp
   │  │  ├── g.atkinson112@gmail.com
   │  │  ├── gabriel@gabotronics.com
   │  │  ├── geoffreybutler94@gmail.com
   │  │  ├── gercamjr.dev@gmail.com
   │  │  ├── gh.chiller@pm.me
   │  │  ├── ghislain.lemeur@gmail.com
   │  │  ├── gigakun@agentmail.to
   │  │  ├── gijs@digitalbase.eu
   │  │  ├── git@gottz.de
   │  │  ├── git@hode.co.uk
   │  │  ├── git@lunarnexus.com
   │  │  ├── github.commits@widow.cc
   │  │  ├── github@00b.tech
   │  │  ├── githubespresso407@users.noreply.github.com
   │  │  ├── gitong@gmail.com
   │  │  ├── gkd2323c@users.noreply.github.com
   │  │  ├── gkgibeau@gmail.com
   │  │  ├── gnani.nutakki@gmail.com
   │  │  ├── gokhansarapevi@gmail.com
   │  │  ├── goktugvatandas@gmail.com
   │  │  ├── gonzalofrancoceballos@Gonzalos-Mac-mini.local
   │  │  ├── greg@border0.com
   │  │  ├── gshall@pm.me
   │  │  ├── guilherme@guilhermeaguiar.com
   │  │  ├── guillaumepeypin@hotmail.fr
   │  │  ├── guoyu.li@lcfuturecenter.com
   │  │  ├── h-chenbin@voyah.com.cn
   │  │  ├── halaprix@users.noreply.github.com
   │  │  ├── halldrix@users.noreply.github.com
   │  │  ├── handnew@hotmail.com
   │  │  ├── handnewb@users.noreply.github.com
   │  │  ├── hang.li@tcredit.com
   │  │  ├── hanqshih@gmail.com
   │  │  ├── hans@groupg.org
   │  │  ├── haowang@HaodeMac-mini.lan
   │  │  ├── harp@hermz580.dev
   │  │  ├── harrison@medmetricsrx.com
   │  │  ├── harshkamdar67@gmail.com
   │  │  ├── hbasheer@student.42abudhabi.ae
   │  │  ├── hej@romell.se
   │  │  ├── hello@ianks.com
   │  │  ├── hello@jeromeiveson.com
   │  │  ├── hello@jpanganiban.com
   │  │  ├── hellofrommorgan@users.noreply.github.com
   │  │  ├── henrino3@gmail.com
   │  │  ├── hereicq@users.noreply.github.com
   │  │  ├── jimmy-agent@nous.local
   │  │  ├── jimmy-agent@jimmy-agent.com
   │  │  ├── jimmy-agent@users.noreply.local
   │  │  ├── jimmy@kortify.local
   │  │  ├── jimmy@server.local
   │  │  ├── jimmyagent424@gmail.com
   │  │  ├── hfsearcy@gmail.com
   │  │  ├── hi@tairasim.com
   │  │  ├── hill.chitsanupong@gmail.com
   │  │  ├── hinablue@gmail.com
   │  │  ├── hotragn.pettugani_2024@woxsen.edu.in
   │  │  ├── hubin-ll@foxmail.com
   │  │  ├── hukla25@gmail.com
   │  │  ├── hunter.c.yeagley@outlook.com
   │  │  ├── hunter@mail.com
   │  │  ├── hustwkr@users.noreply.github.com
   │  │  ├── iammotivated@gmail.com
   │  │  ├── idrisalmalki@Idriss-MacBook-Air.local
   │  │  ├── ilovethevikings@yahoo.com
   │  │  ├── info@datachainsystems.com
   │  │  ├── iniak@iniakdeMac-mini.local
   │  │  ├── ipkharitonov@gmail.com
   │  │  ├── isak@ialogics.com
   │  │  ├── isheng-eqi@users.noreply.github.com
   │  │  ├── iskysun96@gmail.com
   │  │  ├── israel.lot@gmail.com
   │  │  ├── itzhak.pan@gmail.com
   │  │  ├── jaap20035@outlook.com
   │  │  ├── jackoconner55@icloud.com
   │  │  ├── jake.tracey@noice.net.au
   │  │  ├── jakub.wolniewicz@gmail.com
   │  │  ├── james@terminaloutcomes.com
   │  │  ├── janig88@gmail.com
   │  │  ├── jaretbottoms@gmail.com
   │  │  ├── jasmine@smfworks.com
   │  │  ├── jason@webdevtoday.com
   │  │  ├── jasonfang1993@users.noreply.github.com
   │  │  ├── jazzwu@163.com
   │  │  ├── jdgg777@users.noreply.github.com
   │  │  ├── jeff.mettel@gmail.com
   │  │  ├── jeffrey.ying86@live.com
   │  │  ├── jerry.ytp@gmail.com
   │  │  ├── jerry@jimmy.local
   │  │  ├── jesse.casco@gmail.com
   │  │  ├── jethachan@gmail.com
   │  │  ├── jevin@jevin.org
   │  │  ├── jfduarte09@gmail.com
   │  │  ├── jfmusa2024@gmail.com
   │  │  ├── jinglun010@gmail.com
   │  │  ├── jinshi.zjs@antgroup.com
   │  │  ├── joaomarcosdias444@gmail.com
   │  │  ├── jodybagdonas@gmail.com
   │  │  ├── joezhang@outlook.com
   │  │  ├── johann@Mac.lan
   │  │  ├── john.kattenhorn.personal@gmail.com
   │  │  ├── johnsonafuye@gmail.com
   │  │  ├── jonathan@wolftacdigital.com
   │  │  ├── jordan.mymail@gmail.com
   │  │  ├── jordanh@nvidia.com
   │  │  ├── jordyelfferich15@gmail.com
   │  │  ├── jorkeyliu@gmail.com
   │  │  ├── joshua@amokk.net
   │  │  ├── jquesnelle@gmail.com
   │  │  ├── jr.razmus@gmail.com
   │  │  ├── jrcrittenden@gmail.com
   │  │  ├── jrfbch@gmail.com
   │  │  ├── jskang@lablup.com
   │  │  ├── jun@junho.co
   │  │  ├── junhaowanggg@gmail.com
   │  │  ├── justin@actual.computer
   │  │  ├── justin@actual.inc
   │  │  ├── justin@bowes.org
   │  │  ├── kaiyisg@yahoo.com.sg
   │  │  ├── kamon@gao-ai.com
   │  │  ├── kascorp@gmail.com
   │  │  ├── kelsia014@gmail.com
   │  │  ├── keviea@gmail.com
   │  │  ├── kevin@fleetsmarts.net
   │  │  ├── kevinbanjo@gmail.com
   │  │  ├── khanhngoo3116@gmail.com
   │  │  ├── kingdomwarrior23@gmail.com
   │  │  ├── kinsonnee@gmail.com
   │  │  ├── konrad.stawiski@umed.lodz.pl
   │  │  ├── konsisumer@users.noreply.github.com
   │  │  ├── kosta963@gmail.com
   │  │  ├── kray@block.xyz
   │  │  ├── kritcha.b+github@dgtpsn.com
   │  │  ├── ksatha113@gmail.com
   │  │  ├── kshitij@k4poor.dev
   │  │  ├── kshitij@users.noreply.github.com
   │  │  ├── kshitijkapoor0611@gmail.com
   │  │  ├── kuangmi@deeparchi.com
   │  │  ├── kuangmi@nudge.com.cn
   │  │  ├── kubolko@users.noreply.github.com
   │  │  ├── kudi3699@gmail.com
   │  │  ├── laithweinberger@gmail.com
   │  │  ├── lakshya.agarwal@tavily.com
   │  │  ├── lamjj622009225@gmail.com
   │  │  ├── landaun@gmail.com
   │  │  ├── lanyusea@gmail.com
   │  │  ├── laura@localhost
   │  │  ├── LauraGPT@users.noreply.github.com
   │  │  ├── lavie@local
   │  │  ├── lavinia.beghini@genialcare.com.br
   │  │  ├── lazy-idler@users.noreply.github.com
   │  │  ├── leo@gtmcore.ai
   │  │  ├── lepetitprince716-prog@users.noreply.github.com
   │  │  ├── lepetitprince716@gmail.com
   │  │  ├── lesbetes28@gmail.com
   │  │  ├── lexharddrive69@gmail.com
   │  │  ├── lg_329@163.com
   │  │  ├── lidangjiang@gmail.com
   │  │  ├── linhk8@mail2.sysu.edu.cn
   │  │  ├── linux2011@qq.com
   │  │  ├── liqiping@msh.team
   │  │  ├── liruixinch@outlook.com
   │  │  ├── liyunlong@nemo.video
   │  │  ├── lucas.fernandes.df@gmail.com
   │  │  ├── lucas@policastromd.com
   │  │  ├── lucaskvasir@duck.com
   │  │  ├── lucasxavier926@gmail.com
   │  │  ├── lumina@douno.it
   │  │  ├── luna@jimmy.local
   │  │  ├── luoxiao6645@gmail.com
   │  │  ├── ly-wang19@users.noreply.github.com
   │  │  ├── m.varnskuehler@gmail.com
   │  │  ├── m296064@rohpccpu21.mayo.edu
   │  │  ├── maartendormenatteysen@hotmail.com
   │  │  ├── magnus919@pm.me
   │  │  ├── mail.liangyang@gmail.com
   │  │  ├── maly.dan@gmail.com
   │  │  ├── mannnrachman@users.noreply.github.com
   │  │  ├── marcolivier@gmail.com
   │  │  ├── mariobgsp@gmail.com
   │  │  ├── mariobgsp@users.noreply.github.com
   │  │  ├── marketing@cflow.co.kr
   │  │  ├── markmnl@fmsg.io
   │  │  ├── markvlcek@gmail.com
   │  │  ├── martin@tinetwork.com
   │  │  ├── marzukia@users.noreply.github.com
   │  │  ├── mason@masontanguay.com
   │  │  ├── materemias@gmail.com
   │  │  ├── matt.strawbridge@lotuscollective.ai
   │  │  ├── mattmiller@comfy.org
   │  │  ├── mattshapsss@gmail.com
   │  │  ├── matvey.sakhnenko03@icloud.com
   │  │  ├── MaxFreedomPollard@users.noreply.github.com
   │  │  ├── mbrooks@slack-corp.com
   │  │  ├── mcjimmy@edu.dreamcatcher.ai
   │  │  ├── mcjoys@users.noreply.github.com
   │  │  ├── megusta52@proton.me
   │  │  ├── mehmet.kar@std.yildiz.edu.tr
   │  │  ├── mehrzad.karami@gmail.com
   │  │  ├── menglipeng@gmail.com
   │  │  ├── menhguin@users.noreply.github.com
   │  │  ├── metamind@kakao.com
   │  │  ├── michael@example.com
   │  │  ├── michael@smfworks.com
   │  │  ├── michaelsam00@yahoo.com
   │  │  ├── mihaly.schroth@gmail.com
   │  │  ├── mike@mlsmith.net
   │  │  ├── miniadmin@skshim-mini.local
   │  │  ├── mjolley9@gmail.com
   │  │  ├── mkoduri73@gmail.com
   │  │  ├── moeadham@gmail.com
   │  │  ├── mohamed.origami@gmail.com
   │  │  ├── moisesvs84@gmail.com
   │  │  ├── mollusk@users.noreply.github.com
   │  │  ├── motoblurr@users.noreply.github.com
   │  │  ├── mpetrelli@gmail.com
   │  │  ├── mrabsaroka@gmail.com
   │  │  ├── mrgraphitem@gmail.com
   │  │  ├── mromano3@ad.engr.wisc.edu
   │  │  ├── mrz@mrzlab630.pw
   │  │  ├── mudreac@gmail.com
   │  │  ├── muhammadfurqan0100@gmail.com
   │  │  ├── mvalentin@valensys.net
   │  │  ├── mycodeisbad@gmail.com
   │  │  ├── namredips@gmail.com
   │  │  ├── naqerl@users.noreply.github.com
   │  │  ├── nawfal.fardana@dana.id
   │  │  ├── necipaksahin056@gmail.com
   │  │  ├── netease@pricegov.local
   │  │  ├── nformenton@gmail.com
   │  │  ├── nformenton@Nicolass-MacBook-Air.local
   │  │  ├── nguyentien01634@gmail.com
   │  │  ├── nicholas.mariani@hotmail.it
   │  │  ├── nickkarhan@users.noreply.github.com
   │  │  ├── nicochase@users.noreply.github.com
   │  │  ├── nicolasdmolina76@gmail.com
   │  │  ├── nikita.barkov@jetbrains.com
   │  │  ├── Nikola@PlayForm.Cloud
   │  │  ├── nkreadly@gmail.com
   │  │  ├── nnqbao@gmail.com
   │  │  ├── nolanchic@gmail.com
   │  │  ├── noreply@anthropic.com
   │  │  ├── normanking@me.com
   │  │  ├── nsovipgl@gmail.com
   │  │  ├── nwadwa@gmail.com
   │  │  ├── nyaruko@jimmy
   │  │  ├── nypyouxiang@163.com
   │  │  ├── ohs2251@naver.com
   │  │  ├── ojassharma16@gmail.com
   │  │  ├── okalentiev@gmail.com
   │  │  ├── Olympus.roots@outlook.com
   │  │  ├── omid3098@gmail.com
   │  │  ├── opsdownn@gmail.com
   │  │  ├── pa.sen@outlook.com
   │  │  ├── pan.luo@ubc.ca
   │  │  ├── panding99@outlook.com
   │  │  ├── pantinor@redhat.com
   │  │  ├── Paolo@Dylans-Mac-Studio.local
   │  │  ├── patrickmuller@outlook.com
   │  │  ├── paul.lesyuk@gmail.com
   │  │  ├── paul@21million.ad
   │  │  ├── PavelTajdus@users.noreply.github.com
   │  │  ├── peace@trippyogi.com
   │  │  ├── phixxation@gmail.com
   │  │  ├── phm543@gmail.com
   │  │  ├── phull@phullcutz.de
   │  │  ├── pink@macmini-jimmy.local
   │  │  ├── piyushbag4@gmail.com
   │  │  ├── pooyan6@gmail.com
   │  │  ├── pouya.ataei.7@gmail.com
   │  │  ├── praneshnikhar@gmail.com
   │  │  ├── professorpalmer9@gmail.com
   │  │  ├── prontsevich@gmail.com
   │  │  ├── punyko8@users.noreply.github.com
   │  │  ├── qlskssk@gmail.com
   │  │  ├── qlyf@QLYFdeMacBook-Air.local
   │  │  ├── rain@synth.kitchen
   │  │  ├── randy@heroictek.com
   │  │  ├── razsoc.01@gmail.com
   │  │  ├── razultull@gmail.com
   │  │  ├── redpiggy-cyber@users.noreply.github.com
   │  │  ├── reinbeumer@gmail.com
   │  │  ├── reneisaipa@gmail.com
   │  │  ├── rg@replygirl.club
   │  │  ├── rgerrish@outlook.com
   │  │  ├── richard.ham@live.com
   │  │  ├── richard@workflowgroup.com
   │  │  ├── RichardGuan1@users.noreply.github.com
   │  │  ├── richardhojunjang@gmail.com
   │  │  ├── rickard@kumobits.com
   │  │  ├── rjhilgefort@gmail.com
   │  │  ├── rkfshakti@gmail.com
   │  │  ├── rkt.2@hotmail.com
   │  │  ├── rmk799@outlook.com
   │  │  ├── rob@cocodelivery.com
   │  │  ├── rob@zolkos.com
   │  │  ├── robbyczgw@gmail.com
   │  │  ├── robertsryan_21@icloud.com
   │  │  ├── rod.boev@gmail.com
   │  │  ├── rod@nxtlevel.dev
   │  │  ├── rodrigo@nxtlevelsaas.com
   │  │  ├── roger.hanhong@gmail.com
   │  │  ├── royzhrxy-glitch@users.noreply.github.com
   │  │  ├── rsayar@uvic.ca
   │  │  ├── rsherman@velocityinteractive.com
   │  │  ├── rsk-731@users.noreply.github.com
   │  │  ├── rt.cms012@gmail.com
   │  │  ├── rudimar@outlook.com
   │  │  ├── ruizanthony@users.noreply.github.com
   │  │  ├── ruslan.vasylev.vfx@gmail.com
   │  │  ├── ryan.kelln@gmail.com
   │  │  ├── RyderFreeman4Logos@gmail.com
   │  │  ├── s0xn1ck@proton.me
   │  │  ├── s@Ss-MacBook-Pro.local
   │  │  ├── sahabatheri@gmail.com
   │  │  ├── saitama@saitamas-MacBook-Pro.local
   │  │  ├── sascha.haase@textiletsg.com
   │  │  ├── schattenan@kagaku.eu
   │  │  ├── sdevinarayanan@asymbl.com
   │  │  ├── seashore.shi@gmail.com
   │  │  ├── sebastian@mause.online
   │  │  ├── sergey.veys@gmail.com
   │  │  ├── sergey@3dacademysoftware.com
   │  │  ├── seth@rapchat.com
   │  │  ├── seze@andrew.cmu.edu
   │  │  ├── shag@agentmail.to
   │  │  ├── shellybotmoyer@users.noreply.github.com
   │  │  ├── shikanga-jimmy@shikanga.co.uk
   │  │  ├── shiqiming.sqm@taobao.com
   │  │  ├── shubhambc09@gmail.com
   │  │  ├── siage@139.com
   │  │  ├── simon@everythingmma.com.au
   │  │  ├── simonmmafs@users.noreply.github.com
   │  │  ├── simonvanlaak@users.noreply.github.com
   │  │  ├── sjq15251852316@gmail.com
   │  │  ├── sjungwon03@gmail.com
   │  │  ├── skool@doctablade.com
   │  │  ├── skywind5487@gmail.com
   │  │  ├── soheil.fakour@gmail.com
   │  │  ├── songotenukraine@gmail.com
   │  │  ├── sophia@jimmy.local
   │  │  ├── sora.bluesky.dev@gmail.com
   │  │  ├── soundbrokaz@kakao.com
   │  │  ├── spark@channel.inc
   │  │  ├── spfcraze@users.noreply.github.com
   │  │  ├── ssahaun19@gmail.com
   │  │  ├── sswdarius@gmail.com
   │  │  ├── stanislav@local
   │  │  ├── StanleyStetson@users.noreply.github.com
   │  │  ├── stephenlopez2030@gmail.com
   │  │  ├── steve.darlow@gmail.com
   │  │  ├── Steven.Leath@gmail.com
   │  │  ├── stoltemberg@users.noreply.github.com
   │  │  ├── strnadchristopher@gmail.com
   │  │  ├── subhoya@gmail.com
   │  │  ├── sun.guoen0@gmail.com
   │  │  ├── suparious@users.noreply.github.com
   │  │  ├── support@captureclient.net
   │  │  ├── sylbae@users.noreply.github.com
   │  │  ├── szzhoujiarui@users.noreply.github.com
   │  │  ├── takumisatojpn@gmail.com
   │  │  ├── taneli.mielikainen@iki.fi
   │  │  ├── tangyi@DESKTOP-2U4MD8Q
   │  │  ├── tars@users.noreply.github.com
   │  │  ├── tbsonline@protonmail.com
   │  │  ├── team@williepeacock.com
   │  │  ├── texasich@users.noreply.github.com
   │  │  ├── the3asic@users.noreply.github.com
   │  │  ├── theone139344@users.noreply.github.com
   │  │  ├── theunathi@gmail.com
   │  │  ├── tikkanadityajyothi@gmail.com
   │  │  ├── tobiassafaie@MacBook-Air-von-Tobias-3.local
   │  │  ├── TomAce7@users.noreply.github.com
   │  │  ├── topazd2@gmail.com
   │  │  ├── toprakeker@users.noreply.github.com
   │  │  ├── trkim@vms-solutions.com
   │  │  ├── tron@chriswykel.com
   │  │  ├── tugrulgunr@gmail.com
   │  │  ├── turgut.kural@gmail.com
   │  │  ├── tusharanshu18@gmail.com
   │  │  ├── tutors1997@outlook.com
   │  │  ├── Ufonik88@users.noreply.github.com
   │  │  ├── ulises.millanguerrero@gmail.com
   │  │  ├── unashamed366@gmail.com
   │  │  ├── universeszym@mail.ustc.edu.cn
   │  │  ├── unixwzrd.register@mac.com
   │  │  ├── uperLu@users.noreply.github.com
   │  │  ├── upicat@users.noreply.github.com
   │  │  ├── uplink.punks-1k@icloud.com
   │  │  ├── vadelma-agent@users.noreply.github.com
   │  │  ├── vadelma@agenttiklubi.org
   │  │  ├── vaibhavs362@gmail.com
   │  │  ├── valda68k@gmail.com
   │  │  ├── vanshgilhotra8885@gmail.com
   │  │  ├── venkatbalaji2004@gmail.com
   │  │  ├── veryverybigdog@gmail.com
   │  │  ├── victor@jimmy-agent.com
   │  │  ├── vikyw89@gmail.com
   │  │  ├── vinoth12940@users.noreply.github.com
   │  │  ├── viteballoons@gmail.com
   │  │  ├── vitor@vitorcepedalopes.com
   │  │  ├── vittoria3103.123@gmail.com
   │  │  ├── voodoo-pixels@Mac.localdomain
   │  │  ├── vovik-assistant@proton.me
   │  │  ├── wangs.coder@gmail.com
   │  │  ├── wangyunyou@leoao.com
   │  │  ├── wayne1992127@gmail.com
   │  │  ├── webtecnica@gmail.com
   │  │  ├── webtecnica@users.noreply.github.com
   │  │  ├── wen0531@gmail.com
   │  │  ├── wenzel.james.r@gmail.com
   │  │  ├── wernerhp@users.noreply.github.com
   │  │  ├── whisky0809@users.noreply.github.com
   │  │  ├── wilgefortz@gmail.com
   │  │  ├── will@startupbros.com
   │  │  ├── william.reed@acquia.com
   │  │  ├── williamchastain2005@gmail.com
   │  │  ├── WojtekMR3@users.noreply.github.com
   │  │  ├── wrjie@msn.cn
   │  │  ├── wubu.bounty.hunter@users.noreply.github.com
   │  │  ├── wykim777@naver.com
   │  │  ├── xaydinoktay@gmail.com
   │  │  ├── XiaoZAZA@users.noreply.github.com
   │  │  ├── xiehong@xinjikang.cn
   │  │  ├── xinyu@starfie1d.top
   │  │  ├── xiongyue_hnu@163.com
   │  │  ├── xqdwww@qq.com
   │  │  ├── xrwang8@gmail.com
   │  │  ├── xwlyy1991@163.com
   │  │  ├── yemi@lagosinternationalmarket.com
   │  │  ├── yflmq001@users.noreply.github.com
   │  │  ├── yingwaizhiying@gmail.com
   │  │  ├── YLChen-007@users.noreply.github.com
   │  │  ├── yukinomon@users.noreply.github.com
   │  │  ├── yuntianqing@yahoo.com
   │  │  ├── yuri@sparkroad.com
   │  │  ├── yuzilong.leif@gmail.com
   │  │  ├── yy28@vip.sina.com
   │  │  ├── z23@users.noreply.github.com
   │  │  ├── zabih.mosafer@gmail.com
   │  │  ├── zcj1122@example.com
   │  │  ├── zehuaw@mit.edu
   │  │  ├── zgzczzw@users.noreply.github.com
   │  │  ├── zhangcw1989@gmail.com
   │  │  ├── zhangk1985@gmail.com
   │  │  ├── zhangyingliang@outlook.com
   │  │  ├── zhjay@stu.xjtu.edu.cn
   │  │  ├── zhouou6@users.noreply.github.com
   │  │  ├── zhu2mu@qq.com
   │  │  ├── zhunyunjiang@gmail.com
   │  │  ├── Zioywishing@users.noreply.github.com
   │  │  ├── zkgit.substance129@passmail.com
   │  │  ├── zombopanda@gmail.com
   │  │  ├── zqw3719222@163.com
   │  │  ├── ZundamonnoVRChatkaisetu@users.noreply.github.com
   │  │  ├── [email protected]
   │  │  └── {ID}+{username}@users.noreply.github.com
   │  └── README.md
  ├── cron
   │  ├── blueprint_catalog.py
   │  ├── executions.py
   │  ├── jobs.py
   │  ├── lifecycle_guard.py
   │  ├── monitor.py
   │  ├── notepad.py
   │  ├── scheduler.py
   │  ├── scheduler_provider.py
   │  ├── scripts
   │  │  ├── classify_items.py
   │  │  └── __init__.py
   │  ├── suggestions.py
   │  ├── suggestion_catalog.py
   │  └── __init__.py
  ├── datagen-config-examples
   │  ├── example_browser_tasks.jsonl
   │  ├── run_browser_tasks.sh
   │  ├── trajectory_compression.yaml
   │  └── web_research.yaml
  ├── default.tar.gz
  ├── docker
   │  ├── cont-init.d
   │  │  ├── 015-supervise-perms
   │  │  └── 02-reconcile-profiles
   │  ├── entrypoint-dispatch.sh
   │  ├── entrypoint.sh
   │  ├── jimmy-exec-shim.sh
   │  ├── main-wrapper.sh
   │  ├── s6-rc.d
   │  │  ├── dashboard
   │  │  │  ├── dependencies.d
   │  │  │  │  └── base
   │  │  │  ├── finish
   │  │  │  ├── run
   │  │  │  └── type
   │  │  ├── main-jimmy
   │  │  │  ├── dependencies.d
   │  │  │  │  └── base
   │  │  │  ├── run
   │  │  │  └── type
   │  │  └── user
   │  │    └── contents.d
   │  │       ├── dashboard
   │  │       └── main-jimmy
   │  ├── SOUL.md
   │  ├── stage2-hook.sh
   │  └── tini-shim.sh
  ├── docker-compose.windows.yml
  ├── docker-compose.yml
  ├── Dockerfile
  ├── docs
   │  ├── ADR.md
   │  ├── billing-lifecycle.md
   │  ├── chronos-managed-cron-contract.md
   │  ├── design
   │  │  ├── kanban-dialogs
   │  │  │  └── index.html
   │  │  └── profile-builder.md
   │  ├── jimmy-kanban-v1-spec.pdf
   │  ├── kanban
   │  │  └── multi-gateway.md
   │  ├── micro-compaction.md
   │  ├── middleware
   │  │  └── README.md
   │  ├── observability
   │  │  ├── monitoring.md
   │  │  ├── README.md
   │  │  └── relay-shared-metrics.md
   │  ├── profile-routing.md
   │  ├── rca-ssl-cacert-post-git-pull.md
   │  ├── relay-connector-contract.md
   │  ├── rfcs
   │  │  ├── 2026-07-plugin-architecture-lessons-pi-opencode.md
   │  │  └── plugin-config-state-bridge.md
   │  ├── security
   │  │  └── network-egress-isolation.md
   │  ├── session-lifecycle.md
   │  └── streaming-tts.md
  ├── eslint.config.shared.mjs
  ├── evals
   │  ├── browser_use
   │  │  ├── orchestrate.py
   │  │  ├── orchestrate_cloud.py
   │  │  ├── README.md
   │  │  ├── report.py
   │  │  ├── results
   │  │  ├── single_run.py
   │  │  └── tasks
   │  │    ├── easy.json
   │  │    └── hard.json
   │  ├── compaction
   │  │  ├── fixtures.py
   │  │  ├── policies.py
   │  │  ├── README.md
   │  │  ├── report.py
   │  │  ├── results
   │  │  │  ├── codex-arm-2026-08-15
   │  │  │  │  ├── acp.json
   │  │  │  │  ├── gui.json
   │  │  │  │  ├── prmerge.json
   │  │  │  │  └── sweep.json
   │  │  │  └── SCORECARD-2026-08-15.md
   │  │  ├── runner.py
   │  │  ├── scripts
   │  │  │  ├── build_html_report.py
   │  │  │  ├── codex_arm.py
   │  │  │  ├── reconstruct_lineage.py
   │  │  │  └── replay_lineage.py
   │  │  └── test_region_scoping.py
   │  └── readtool
   │    ├── fixtures.py
   │    ├── README.md
   │    ├── report.py
   │    ├── results
   │     │  └── SUMMARY.md
   │    ├── runner.py
   │    └── tasks.py
  ├── flake.lock
  ├── flake.nix
  ├── gateway
   │  ├── agent_cache_pressure.py
   │  ├── assets
   │  │  ├── status_phrases.yaml
   │  │  └── telegram-botfather-threads-settings.jpg
   │  ├── authz_mixin.py
   │  ├── builtin_hooks
   │  │  └── __init__.py
   │  ├── cgroup_cleanup.py
   │  ├── channel_directory.py
   │  ├── code_skew.py
   │  ├── config.py
   │  ├── cwd_placeholder.py
   │  ├── dead_targets.py
   │  ├── delivery.py
   │  ├── delivery_ledger.py
   │  ├── disk_status.py
   │  ├── display_config.py
   │  ├── drain_control.py
   │  ├── hooks.py
   │  ├── kanban_watchers.py
   │  ├── lifecycle_ledger.py
   │  ├── media_policy.py
   │  ├── memory_monitor.py
   │  ├── memory_status.py
   │  ├── message_timestamps.py
   │  ├── mirror.py
   │  ├── pairing.py
   │  ├── platforms
   │  │  ├── ADDING_A_PLATFORM.md
   │  │  ├── api_server.py
   │  │  ├── base.py
   │  │  ├── bluebubbles.py
   │  │  ├── helpers.py
   │  │  ├── media_cache.py
   │  │  ├── msgraph_webhook.py
   │  │  ├── qqbot
   │  │  │  ├── adapter.py
   │  │  │  ├── chunked_upload.py
   │  │  │  ├── constants.py
   │  │  │  ├── crypto.py
   │  │  │  ├── keyboards.py
   │  │  │  ├── onboard.py
   │  │  │  ├── utils.py
   │  │  │  └── __init__.py
   │  │  ├── signal.py
   │  │  ├── signal_format.py
   │  │  ├── signal_rate_limit.py
   │  │  ├── webhook.py
   │  │  ├── webhook_filters.py
   │  │  ├── weixin.py
   │  │  ├── whatsapp_cloud.py
   │  │  ├── whatsapp_common.py
   │  │  ├── yuanbao.py
   │  │  ├── yuanbao_media.py
   │  │  ├── yuanbao_proto.py
   │  │  ├── yuanbao_sticker.py
   │  │  ├── _http_client_limits.py
   │  │  └── __init__.py
   │  ├── platform_registry.py
   │  ├── profile_routing.py
   │  ├── readiness.py
   │  ├── relay
   │  │  ├── adapter.py
   │  │  ├── auth.py
   │  │  ├── command_manifest.py
   │  │  ├── descriptor.py
   │  │  ├── media.py
   │  │  ├── transport.py
   │  │  ├── ws_transport.py
   │  │  └── __init__.py
   │  ├── response_filters.py
   │  ├── restart.py
   │  ├── restart_loop_guard.py
   │  ├── rich_sent_store.py
   │  ├── run.py
   │  ├── runtime_footer.py
   │  ├── scale_to_zero.py
   │  ├── session.py
   │  ├── session_context.py
   │  ├── session_stall.py
   │  ├── session_state.py
   │  ├── shutdown_flush.py
   │  ├── shutdown_forensics.py
   │  ├── shutdown_watchdog.py
   │  ├── slash_access.py
   │  ├── slash_commands.py
   │  ├── status.py
   │  ├── status_phrases.py
   │  ├── sticker_cache.py
   │  ├── streaming_tts_consumer.py
   │  ├── stream_consumer.py
   │  ├── stream_dispatch.py
   │  ├── stream_events.py
   │  ├── systemd_notify.py
   │  ├── turn_context.py
   │  ├── turn_lease.py
   │  ├── wake.py
   │  ├── whatsapp_identity.py
   │  └── __init__.py
  ├── jimmy
  ├── jimmy_bootstrap.py
  ├── jimmy_cli
   │  ├── active_sessions.py
   │  ├── agent_import.py
   │  ├── agent_plugins.py
   │  ├── approvals_suggest.py
   │  ├── approvals_test.py
   │  ├── approval_mode.py
   │  ├── approval_transport.py
   │  ├── auth.py
   │  ├── auth_commands.py
   │  ├── azure_detect.py
   │  ├── backup.py
   │  ├── bang_shell.py
   │  ├── banner.py
   │  ├── blueprint_cmd.py
   │  ├── browser_connect.py
   │  ├── build_info.py
   │  ├── bundles.py
   │  ├── callbacks.py
   │  ├── checkpoints.py
   │  ├── claw.py
   │  ├── clipboard.py
   │  ├── cli_agent_setup_mixin.py
   │  ├── cli_billing_mixin.py
   │  ├── cli_commands_mixin.py
   │  ├── cli_output.py
   │  ├── codex_models.py
   │  ├── codex_runtime_plugin_migration.py
   │  ├── codex_runtime_switch.py
   │  ├── colors.py
   │  ├── commands.py
   │  ├── completion.py
   │  ├── config.py
   │  ├── config_defaults.py
   │  ├── config_migrations.py
   │  ├── console_engine.py
   │  ├── container_boot.py
   │  ├── context_switch_guard.py
   │  ├── copilot_auth.py
   │  ├── credential_lifecycle.py
   │  ├── cron.py
   │  ├── curator.py
   │  ├── curses_ui.py
   │  ├── dashboard_auth
   │  │  ├── audit.py
   │  │  ├── base.py
   │  │  ├── cookies.py
   │  │  ├── login_page.py
   │  │  ├── middleware.py
   │  │  ├── native_flow.py
   │  │  ├── prefix.py
   │  │  ├── public_paths.py
   │  │  ├── registry.py
   │  │  ├── routes.py
   │  │  ├── token_auth.py
   │  │  ├── ws_tickets.py
   │  │  └── __init__.py
   │  ├── dashboard_procs.py
   │  ├── dashboard_register.py
   │  ├── data
   │  │  └── plugin_index.json
   │  ├── debug.py
   │  ├── default_soul.py
   │  ├── dep_ensure.py
   │  ├── diagnostics_upload.py
   │  ├── dingtalk_auth.py
   │  ├── doctor.py
   │  ├── doctor_live.py
   │  ├── dump.py
   │  ├── env_loader.py
   │  ├── fallback_cmd.py
   │  ├── fallback_config.py
   │  ├── focus_view.py
   │  ├── foreign_sessions.py
   │  ├── gateway.py
   │  ├── gateway_enroll.py
   │  ├── gateway_windows.py
   │  ├── gitlock.py
   │  ├── goals.py
   │  ├── gui_uninstall.py
   │  ├── heartbeat.py
   │  ├── hooks.py
   │  ├── init_command.py
   │  ├── input_sanitize.py
   │  ├── inventory.py
   │  ├── journey.py
   │  ├── kanban.py
   │  ├── kanban_db.py
   │  ├── kanban_decompose.py
   │  ├── kanban_diagnostics.py
   │  ├── kanban_specify.py
   │  ├── kanban_swarm.py
   │  ├── lifecycle.py
   │  ├── linux_desktop_entry.py
   │  ├── logs.py
   │  ├── loops.py
   │  ├── main.py
   │  ├── managed_scope.py
   │  ├── managed_uv.py
   │  ├── mcp_catalog.py
   │  ├── mcp_config.py
   │  ├── mcp_picker.py
   │  ├── mcp_security.py
   │  ├── mcp_startup.py
   │  ├── memory_oauth.py
   │  ├── memory_setup.py
   │  ├── mem_trim.py
   │  ├── middleware.py
   │  ├── migrate.py
   │  ├── moa_cmd.py
   │  ├── moa_config.py
   │  ├── models.py
   │  ├── model_catalog.py
   │  ├── model_cost_guard.py
   │  ├── model_data_policy_guard.py
   │  ├── model_normalize.py
   │  ├── model_search.py
   │  ├── model_selection_guards.py
   │  ├── model_setup_flows.py
   │  ├── model_switch.py
   │  ├── nous_account.py
   │  ├── nous_auth_keepalive.py
   │  ├── nous_billing.py
   │  ├── nous_subscription.py
   │  ├── npm_engine.py
   │  ├── observability
   │  │  ├── relay_runtime.py
   │  │  ├── relay_shared_metrics.py
   │  │  ├── schemas
   │  │  │  ├── jimmy.shared_metrics.v1.schema.json
   │  │  │  └── jimmy.shared_metrics.v2.schema.json
   │  │  ├── shared_metrics.py
   │  │  ├── shared_metrics_contract.py
   │  │  ├── shared_metrics_subscriber.py
   │  │  └── __init__.py
   │  ├── onepassword_secrets_cli.py
   │  ├── oneshot.py
   │  ├── pairing.py
   │  ├── partial_compress.py
   │  ├── personality.py
   │  ├── pets.py
   │  ├── platforms.py
   │  ├── platform_actions.py
   │  ├── plugins.py
   │  ├── plugins_cmd.py
   │  ├── plugin_capabilities.py
   │  ├── plugin_dev.py
   │  ├── plugin_index.py
   │  ├── plugin_packs.py
   │  ├── portal_cli.py
   │  ├── process_identity.py
   │  ├── profiles.py
   │  ├── profile_describer.py
   │  ├── profile_distribution.py
   │  ├── projects_cmd.py
   │  ├── projects_db.py
   │  ├── prompt_size.py
   │  ├── prompt_stash.py
   │  ├── providers.py
   │  ├── provider_catalog.py
   │  ├── proxy
   │  │  ├── adapters
   │  │  │  ├── base.py
   │  │  │  ├── nous_portal.py
   │  │  │  ├── xai.py
   │  │  │  └── __init__.py
   │  │  ├── cli.py
   │  │  ├── server.py
   │  │  └── __init__.py
   │  ├── proxy_cli.py
   │  ├── psutil_android.py
   │  ├── pty_bridge.py
   │  ├── pty_session.py
   │  ├── pt_input_extras.py
   │  ├── relaunch.py
   │  ├── relay_plugin_cutover.py
   │  ├── resource_limits.py
   │  ├── route_identity.py
   │  ├── runtime_provider.py
   │  ├── secrets_cli.py
   │  ├── secret_prompt.py
   │  ├── security_advisories.py
   │  ├── security_audit.py
   │  ├── security_audit_startup.py
   │  ├── send_cmd.py
   │  ├── service_manager.py
   │  ├── sessions_cmd.py
   │  ├── session_export.py
   │  ├── session_export_html.py
   │  ├── session_export_md.py
   │  ├── session_filters.py
   │  ├── session_listing.py
   │  ├── session_lost_and_found.py
   │  ├── session_recap.py
   │  ├── session_recovery.py
   │  ├── setup.py
   │  ├── setup_hidden_env.py
   │  ├── setup_whatsapp_cloud.py
   │  ├── sizefmt.py
   │  ├── skills_config.py
   │  ├── skills_hub.py
   │  ├── skin_cmd.py
   │  ├── skin_engine.py
   │  ├── slack_cli.py
   │  ├── slash_exec.py
   │  ├── sqlite_runtime.py
   │  ├── sqlite_safe_read.py
   │  ├── sqlite_util.py
   │  ├── status.py
   │  ├── stderr_timestamp.py
   │  ├── stdio.py
   │  ├── subcommands
   │  │  ├── acp.py
   │  │  ├── approvals.py
   │  │  ├── auth.py
   │  │  ├── backup.py
   │  │  ├── claw.py
   │  │  ├── config.py
   │  │  ├── console.py
   │  │  ├── cron.py
   │  │  ├── dashboard.py
   │  │  ├── debug.py
   │  │  ├── doctor.py
   │  │  ├── dump.py
   │  │  ├── gateway.py
   │  │  ├── gui.py
   │  │  ├── hooks.py
   │  │  ├── import_agent.py
   │  │  ├── import_cmd.py
   │  │  ├── insights.py
   │  │  ├── login.py
   │  │  ├── logout.py
   │  │  ├── logs.py
   │  │  ├── mcp.py
   │  │  ├── memory.py
   │  │  ├── model.py
   │  │  ├── monitoring.py
   │  │  ├── pairing.py
   │  │  ├── pause.py
   │  │  ├── peer.py
   │  │  ├── plugins.py
   │  │  ├── profile.py
   │  │  ├── prompt_size.py
   │  │  ├── security.py
   │  │  ├── setup.py
   │  │  ├── skills.py
   │  │  ├── skin.py
   │  │  ├── slack.py
   │  │  ├── status.py
   │  │  ├── sync.py
   │  │  ├── tools.py
   │  │  ├── uninstall.py
   │  │  ├── update.py
   │  │  ├── verify.py
   │  │  ├── webhook.py
   │  │  ├── whatsapp.py
   │  │  ├── _shared.py
   │  │  └── __init__.py
   │  ├── suggestions_cmd.py
   │  ├── telegram_managed_bot.py
   │  ├── terminal_breadcrumbs.py
   │  ├── timefmt.py
   │  ├── timeouts.py
   │  ├── tips.py
   │  ├── toolset_validation.py
   │  ├── tools_config.py
   │  ├── uninstall.py
   │  ├── update_cmd.py
   │  ├── update_lock.py
   │  ├── urllib_security.py
   │  ├── vercel_auth.py
   │  ├── verify_cmd.py
   │  ├── voice.py
   │  ├── webhook.py
   │  ├── web_deps.py
   │  ├── web_git.py
   │  ├── web_models.py
   │  ├── web_routers
   │  │  ├── cron.py
   │  │  ├── git.py
   │  │  ├── mcp.py
   │  │  ├── profiles.py
   │  │  ├── sessions.py
   │  │  ├── skills.py
   │  │  ├── tools.py
   │  │  └── __init__.py
   │  ├── web_server.py
   │  ├── windows_ssh_runtime.py
   │  ├── win_pty_bridge.py
   │  ├── worktree_cmd.py
   │  ├── worktree_gc.py
   │  ├── write_approval_commands.py
   │  ├── xai_retirement.py
   │  ├── _early_recovery.py
   │  ├── _install_repair.py
   │  ├── _parser.py
   │  ├── _scan_venv_blockers.py
   │  ├── _startup_fast.py
   │  ├── _subprocess_compat.py
   │  └── __init__.py
  ├── jimmy_constants.py
  ├── jimmy_logging.py
  ├── jimmy_state.py
  ├── jimmy_state_common.py
  ├── jimmy_state_portability.py
  ├── jimmy_state_schema.py
  ├── jimmy_state_search.py
  ├── jimmy_time.py
  ├── LICENSE
  ├── locales
   │  ├── af.yaml
   │  ├── ar.yaml
   │  ├── de.yaml
   │  ├── en.yaml
   │  ├── es.yaml
   │  ├── fr.yaml
   │  ├── ga.yaml
   │  ├── hu.yaml
   │  ├── it.yaml
   │  ├── ja.yaml
   │  ├── ko.yaml
   │  ├── pt.yaml
   │  ├── ru.yaml
   │  ├── tr.yaml
   │  ├── uk.yaml
   │  ├── zh-hant.yaml
   │  └── zh.yaml
  ├── log.txt
  ├── mcp-research-data
   │  ├── ue_bench_rows.json
   │  ├── ue_bench_summary.json
   │  ├── ue_discovery_rows.json
   │  ├── ue_hard_haiku_rows.json
   │  └── ue_hard_rows.json
  ├── mcp_serve.py
  ├── mini_swe_runner.py
  ├── model_tools.py
  ├── native
   │  └── fts5_cjk
   │    ├── build.sh
   │    ├── fts5_cjk.c
   │    ├── README.md
   │    └── vendor
   │       ├── sqlite3.h
   │       └── sqlite3ext.h
  ├── nix
   │  ├── checks.nix
   │  ├── configMergeScript.nix
   │  ├── desktop.nix
   │  ├── devShell.nix
   │  ├── jimmy-agent.nix
   │  ├── homeManagerModules.nix
   │  ├── lib.nix
   │  ├── moduleCommon.nix
   │  ├── nixosModules.nix
   │  ├── node-gyp-11-4-0-package-lock.json
   │  ├── node-gyp-11-4-0.nix
   │  ├── npm-12-0-2.nix
   │  ├── overlays.nix
   │  ├── packages.nix
   │  ├── python.nix
   │  ├── sandbox.nix
   │  ├── tui.nix
   │  └── web.nix
  ├── optional-mcps
   │  ├── airtable
   │  │  └── manifest.yaml
   │  ├── asana
   │  │  └── manifest.yaml
   │  ├── atlassian
   │  │  └── manifest.yaml
   │  ├── comfy-cloud
   │  │  └── manifest.yaml
   │  ├── datadog
   │  │  └── manifest.yaml
   │  ├── figma
   │  │  └── manifest.yaml
   │  ├── hugging_face
   │  │  └── manifest.yaml
   │  ├── intercom
   │  │  └── manifest.yaml
   │  ├── linear
   │  │  └── manifest.yaml
   │  ├── n8n
   │  │  └── manifest.yaml
   │  ├── netlify
   │  │  └── manifest.yaml
   │  ├── notion
   │  │  └── manifest.yaml
   │  ├── paypal
   │  │  └── manifest.yaml
   │  ├── sentry
   │  │  └── manifest.yaml
   │  ├── square
   │  │  └── manifest.yaml
   │  ├── stripe
   │  │  └── manifest.yaml
   │  ├── supabase
   │  │  └── manifest.yaml
   │  ├── unreal-engine
   │  │  └── manifest.yaml
   │  ├── vercel
   │  │  └── manifest.yaml
   │  └── webflow
   │    └── manifest.yaml
  ├── optional-skills
   │  ├── autonomous-ai-agents
   │  │  ├── antigravity-cli
   │  │  │  ├── references
   │  │  │  │  └── cli-docs.md
   │  │  │  └── SKILL.md
   │  │  ├── blackbox
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── grok
   │  │  │  └── SKILL.md
   │  │  ├── honcho
   │  │  │  └── SKILL.md
   │  │  └── openhands
   │  │    └── SKILL.md
   │  ├── blockchain
   │  │  ├── evm
   │  │  │  ├── scripts
   │  │  │  │  └── evm_client.py
   │  │  │  └── SKILL.md
   │  │  ├── hyperliquid
   │  │  │  ├── scripts
   │  │  │  │  └── hyperliquid_client.py
   │  │  │  └── SKILL.md
   │  │  └── solana
   │  │    ├── scripts
   │  │     │  └── solana_client.py
   │  │    └── SKILL.md
   │  ├── communication
   │  │  ├── DESCRIPTION.md
   │  │  └── one-three-one-rule
   │  │    └── SKILL.md
   │  ├── creative
   │  │  ├── audiocraft-audio-generation
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── baoyu-article-illustrator
   │  │  │  ├── PORT_NOTES.md
   │  │  │  ├── prompts
   │  │  │  │  └── system.md
   │  │  │  ├── references
   │  │  │  │  ├── palettes
   │  │  │  │  │  ├── macaron.md
   │  │  │  │  │  ├── mono-ink.md
   │  │  │  │  │  ├── neon.md
   │  │  │  │  │  └── warm.md
   │  │  │  │  ├── prompt-construction.md
   │  │  │  │  ├── style-presets.md
   │  │  │  │  ├── styles
   │  │  │  │  │  ├── blueprint.md
   │  │  │  │  │  ├── chalkboard.md
   │  │  │  │  │  ├── editorial.md
   │  │  │  │  │  ├── elegant.md
   │  │  │  │  │  ├── fantasy-animation.md
   │  │  │  │  │  ├── flat-doodle.md
   │  │  │  │  │  ├── flat.md
   │  │  │  │  │  ├── ink-notes.md
   │  │  │  │  │  ├── intuition-machine.md
   │  │  │  │  │  ├── minimal.md
   │  │  │  │  │  ├── nature.md
   │  │  │  │  │  ├── notion.md
   │  │  │  │  │  ├── pixel-art.md
   │  │  │  │  │  ├── playful.md
   │  │  │  │  │  ├── retro.md
   │  │  │  │  │  ├── scientific.md
   │  │  │  │  │  ├── screen-print.md
   │  │  │  │  │  ├── sketch-notes.md
   │  │  │  │  │  ├── sketch.md
   │  │  │  │  │  ├── vector-illustration.md
   │  │  │  │  │  ├── vintage.md
   │  │  │  │  │  ├── warm.md
   │  │  │  │  │  └── watercolor.md
   │  │  │  │  ├── styles.md
   │  │  │  │  ├── usage.md
   │  │  │  │  └── workflow.md
   │  │  │  └── SKILL.md
   │  │  ├── baoyu-comic
   │  │  │  ├── PORT_NOTES.md
   │  │  │  ├── references
   │  │  │  │  ├── analysis-framework.md
   │  │  │  │  ├── art-styles
   │  │  │  │  │  ├── chalk.md
   │  │  │  │  │  ├── ink-brush.md
   │  │  │  │  │  ├── ligne-claire.md
   │  │  │  │  │  ├── manga.md
   │  │  │  │  │  ├── minimalist.md
   │  │  │  │  │  └── realistic.md
   │  │  │  │  ├── auto-selection.md
   │  │  │  │  ├── base-prompt.md
   │  │  │  │  ├── character-template.md
   │  │  │  │  ├── layouts
   │  │  │  │  │  ├── cinematic.md
   │  │  │  │  │  ├── dense.md
   │  │  │  │  │  ├── four-panel.md
   │  │  │  │  │  ├── mixed.md
   │  │  │  │  │  ├── splash.md
   │  │  │  │  │  ├── standard.md
   │  │  │  │  │  └── webtoon.md
   │  │  │  │  ├── ohmsha-guide.md
   │  │  │  │  ├── partial-workflows.md
   │  │  │  │  ├── presets
   │  │  │  │  │  ├── concept-story.md
   │  │  │  │  │  ├── four-panel.md
   │  │  │  │  │  ├── ohmsha.md
   │  │  │  │  │  ├── shoujo.md
   │  │  │  │  │  └── wuxia.md
   │  │  │  │  ├── storyboard-template.md
   │  │  │  │  ├── tones
   │  │  │  │  │  ├── action.md
   │  │  │  │  │  ├── dramatic.md
   │  │  │  │  │  ├── energetic.md
   │  │  │  │  │  ├── neutral.md
   │  │  │  │  │  ├── romantic.md
   │  │  │  │  │  ├── vintage.md
   │  │  │  │  │  └── warm.md
   │  │  │  │  └── workflow.md
   │  │  │  └── SKILL.md
   │  │  ├── concept-diagrams
   │  │  │  ├── examples
   │  │  │  │  ├── apartment-floor-plan-conversion.md
   │  │  │  │  ├── automated-password-reset-flow.md
   │  │  │  │  ├── autonomous-llm-research-agent-flow.md
   │  │  │  │  ├── banana-journey-tree-to-smoothie.md
   │  │  │  │  ├── commercial-aircraft-structure.md
   │  │  │  │  ├── cpu-ooo-microarchitecture.md
   │  │  │  │  ├── electricity-grid-flow.md
   │  │  │  │  ├── feature-film-production-pipeline.md
   │  │  │  │  ├── hospital-emergency-department-flow.md
   │  │  │  │  ├── ml-benchmark-grouped-bar-chart.md
   │  │  │  │  ├── place-order-uml-sequence.md
   │  │  │  │  ├── smart-city-infrastructure.md
   │  │  │  │  ├── smartphone-layer-anatomy.md
   │  │  │  │  ├── sn2-reaction-mechanism.md
   │  │  │  │  └── wind-turbine-structure.md
   │  │  │  ├── references
   │  │  │  │  ├── dashboard-patterns.md
   │  │  │  │  ├── infrastructure-patterns.md
   │  │  │  │  └── physical-shape-cookbook.md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── template.html
   │  │  ├── creative-ideation
   │  │  │  ├── references
   │  │  │  │  ├── anti-slop.md
   │  │  │  │  ├── exercises.md
   │  │  │  │  ├── full-prompt-library.md
   │  │  │  │  ├── heuristics.md
   │  │  │  │  ├── method-catalog.md
   │  │  │  │  └── methods
   │  │  │  │    ├── affinity-diagrams.md
   │  │  │  │    ├── analogy-and-blending.md
   │  │  │  │    ├── biomimicry.md
   │  │  │  │    ├── chance-and-remix.md
   │  │  │  │    ├── compression-progress.md
   │  │  │  │    ├── creative-discipline.md
   │  │  │  │    ├── defamiliarization.md
   │  │  │  │    ├── derive-and-mapping.md
   │  │  │  │    ├── first-principles.md
   │  │  │  │    ├── jobs-to-be-done.md
   │  │  │  │    ├── lateral-provocations.md
   │  │  │  │    ├── leverage-points.md
   │  │  │  │    ├── oblique-strategies.md
   │  │  │  │    ├── oulipo.md
   │  │  │  │    ├── pataphysics.md
   │  │  │  │    ├── pattern-languages.md
   │  │  │  │    ├── polya.md
   │  │  │  │    ├── premortem-and-inversion.md
   │  │  │  │    ├── scamper.md
   │  │  │  │    ├── story-skeletons.md
   │  │  │  │    ├── triz-principles.md
   │  │  │  │    └── volume-generation.md
   │  │  │  └── SKILL.md
   │  │  ├── draw-your-font
   │  │  │  ├── references
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── heartmula
   │  │  │  └── SKILL.md
   │  │  ├── hyperframes
   │  │  │  ├── references
   │  │  │  │  ├── cli.md
   │  │  │  │  ├── composition.md
   │  │  │  │  ├── features.md
   │  │  │  │  ├── gsap.md
   │  │  │  │  ├── troubleshooting.md
   │  │  │  │  └── website-to-video.md
   │  │  │  ├── scripts
   │  │  │  │  └── setup.sh
   │  │  │  └── SKILL.md
   │  │  ├── kanban-video-orchestrator
   │  │  │  ├── assets
   │  │  │  │  ├── brief.md.tmpl
   │  │  │  │  ├── setup.sh.tmpl
   │  │  │  │  └── soul.md.tmpl
   │  │  │  ├── references
   │  │  │  │  ├── examples.md
   │  │  │  │  ├── intake.md
   │  │  │  │  ├── kanban-setup.md
   │  │  │  │  ├── monitoring.md
   │  │  │  │  ├── role-archetypes.md
   │  │  │  │  └── tool-matrix.md
   │  │  │  ├── scripts
   │  │  │  │  ├── bootstrap_pipeline.py
   │  │  │  │  └── monitor.py
   │  │  │  └── SKILL.md
   │  │  ├── meme-generation
   │  │  │  ├── EXAMPLES.md
   │  │  │  ├── scripts
   │  │  │  │  ├── generate_meme.py
   │  │  │  │  └── templates.json
   │  │  │  └── SKILL.md
   │  │  ├── pixel-art
   │  │  │  ├── ATTRIBUTION.md
   │  │  │  ├── references
   │  │  │  │  └── palettes.md
   │  │  │  ├── scripts
   │  │  │  │  ├── palettes.py
   │  │  │  │  ├── pixel_art.py
   │  │  │  │  ├── pixel_art_video.py
   │  │  │  │  └── __init__.py
   │  │  │  └── SKILL.md
   │  │  ├── simple-english
   │  │  │  ├── references
   │  │  │  │  ├── checklist.md
   │  │  │  │  └── use-cases.md
   │  │  │  └── SKILL.md
   │  │  ├── social-media-content-calendar
   │  │  │  └── SKILL.md
   │  │  ├── tldraw-offline
   │  │  │  ├── scripts
   │  │  │  │  ├── counter.js
   │  │  │  │  ├── main.js
   │  │  │  │  └── validate_shapes.mjs
   │  │  │  └── SKILL.md
   │  │  └── unreal-mcp
   │  │    ├── references
   │  │     │  ├── advanced-workflows.md
   │  │     │  ├── pitfalls.md
   │  │     │  ├── recipes.md
   │  │     │  ├── scene-craft.md
   │  │     │  └── tool-surface.md
   │  │    └── SKILL.md
   │  ├── data-science
   │  │  ├── DESCRIPTION.md
   │  │  └── jupyter-notebook
   │  │    └── SKILL.md
   │  ├── DESCRIPTION.md
   │  ├── devops
   │  │  ├── actual-setup
   │  │  │  ├── references
   │  │  │  │  └── opencode.md
   │  │  │  └── SKILL.md
   │  │  ├── docker-management
   │  │  │  └── SKILL.md
   │  │  ├── jimmy-s6-container-supervision
   │  │  │  └── SKILL.md
   │  │  ├── inference-sh-cli
   │  │  │  ├── references
   │  │  │  │  ├── app-discovery.md
   │  │  │  │  ├── authentication.md
   │  │  │  │  ├── cli-reference.md
   │  │  │  │  └── running-apps.md
   │  │  │  └── SKILL.md
   │  │  ├── pinggy-tunnel
   │  │  │  └── SKILL.md
   │  │  └── watchers
   │  │    ├── scripts
   │  │     │  ├── watch_github.py
   │  │     │  ├── watch_http_json.py
   │  │     │  ├── watch_rss.py
   │  │     │  └── _watermark.py
   │  │    └── SKILL.md
   │  ├── dogfood
   │  │  ├── adversarial-ux-test
   │  │  │  └── SKILL.md
   │  │  └── DESCRIPTION.md
   │  ├── email
   │  │  └── agentmail
   │  │    └── SKILL.md
   │  ├── finance
   │  │  ├── 3-statement-model
   │  │  │  ├── references
   │  │  │  │  ├── formatting.md
   │  │  │  │  ├── formulas.md
   │  │  │  │  └── sec-filings.md
   │  │  │  └── SKILL.md
   │  │  ├── comps-analysis
   │  │  │  └── SKILL.md
   │  │  ├── dcf-model
   │  │  │  ├── requirements.txt
   │  │  │  ├── scripts
   │  │  │  │  └── validate_dcf.py
   │  │  │  ├── SKILL.md
   │  │  │  └── TROUBLESHOOTING.md
   │  │  ├── excel-author
   │  │  │  ├── scripts
   │  │  │  │  └── recalc.py
   │  │  │  └── SKILL.md
   │  │  ├── lbo-model
   │  │  │  └── SKILL.md
   │  │  ├── merger-model
   │  │  │  └── SKILL.md
   │  │  ├── polymarket
   │  │  │  ├── references
   │  │  │  │  └── api-endpoints.md
   │  │  │  ├── scripts
   │  │  │  │  └── polymarket.py
   │  │  │  └── SKILL.md
   │  │  ├── pptx-author
   │  │  │  └── SKILL.md
   │  │  └── stocks
   │  │    ├── scripts
   │  │     │  └── stocks_client.py
   │  │    └── SKILL.md
   │  ├── gaming
   │  │  ├── DESCRIPTION.md
   │  │  ├── minecraft-modpack-server
   │  │  │  └── SKILL.md
   │  │  └── pokemon-player
   │  │    └── SKILL.md
   │  ├── health
   │  │  ├── DESCRIPTION.md
   │  │  ├── fitness-nutrition
   │  │  │  ├── references
   │  │  │  │  └── FORMULAS.md
   │  │  │  ├── scripts
   │  │  │  │  ├── body_calc.py
   │  │  │  │  └── nutrition_search.py
   │  │  │  └── SKILL.md
   │  │  └── neuroskill-bci
   │  │    ├── references
   │  │     │  ├── api.md
   │  │     │  ├── metrics.md
   │  │     │  └── protocols.md
   │  │    └── SKILL.md
   │  ├── mcp
   │  │  ├── DESCRIPTION.md
   │  │  ├── fastmcp
   │  │  │  ├── references
   │  │  │  │  └── fastmcp-cli.md
   │  │  │  ├── scripts
   │  │  │  │  └── scaffold_fastmcp.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── api_wrapper.py
   │  │  │    ├── database_server.py
   │  │  │    └── file_processor.py
   │  │  ├── mcp-oauth-remote-gateway
   │  │  │  ├── references
   │  │  │  │  └── stripe-mcp-oauth-revocation.md
   │  │  │  ├── scripts
   │  │  │  │  └── diagnose-oauth-mcp.py
   │  │  │  └── SKILL.md
   │  │  └── mcporter
   │  │    └── SKILL.md
   │  ├── migration
   │  │  ├── DESCRIPTION.md
   │  │  └── openclaw-migration
   │  │    ├── scripts
   │  │     │  └── openclaw_to_jimmy.py
   │  │    └── SKILL.md
   │  ├── mlops
   │  │  ├── accelerate
   │  │  │  ├── references
   │  │  │  │  ├── custom-plugins.md
   │  │  │  │  ├── megatron-integration.md
   │  │  │  │  └── performance.md
   │  │  │  └── SKILL.md
   │  │  ├── chroma
   │  │  │  ├── references
   │  │  │  │  └── integration.md
   │  │  │  └── SKILL.md
   │  │  ├── clip
   │  │  │  ├── references
   │  │  │  │  └── applications.md
   │  │  │  └── SKILL.md
   │  │  ├── faiss
   │  │  │  ├── references
   │  │  │  │  └── index_types.md
   │  │  │  └── SKILL.md
   │  │  ├── flash-attention
   │  │  │  ├── references
   │  │  │  │  ├── benchmarks.md
   │  │  │  │  └── transformers-integration.md
   │  │  │  └── SKILL.md
   │  │  ├── guidance
   │  │  │  ├── references
   │  │  │  │  ├── backends.md
   │  │  │  │  ├── constraints.md
   │  │  │  │  └── examples.md
   │  │  │  └── SKILL.md
   │  │  ├── huggingface-tokenizers
   │  │  │  ├── references
   │  │  │  │  ├── algorithms.md
   │  │  │  │  ├── integration.md
   │  │  │  │  ├── pipeline.md
   │  │  │  │  └── training.md
   │  │  │  └── SKILL.md
   │  │  ├── inference
   │  │  │  └── outlines
   │  │  │    ├── references
   │  │  │     │  ├── backends.md
   │  │  │     │  ├── examples.md
   │  │  │     │  └── json_generation.md
   │  │  │    └── SKILL.md
   │  │  ├── instructor
   │  │  │  ├── references
   │  │  │  │  ├── examples.md
   │  │  │  │  ├── providers.md
   │  │  │  │  └── validation.md
   │  │  │  └── SKILL.md
   │  │  ├── lambda-labs
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── llava
   │  │  │  ├── references
   │  │  │  │  └── training.md
   │  │  │  └── SKILL.md
   │  │  ├── modal
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── models
   │  │  │  └── segment-anything-model
   │  │  │    ├── references
   │  │  │     │  ├── advanced-usage.md
   │  │  │     │  └── troubleshooting.md
   │  │  │    └── SKILL.md
   │  │  ├── nemo-curator
   │  │  │  ├── references
   │  │  │  │  ├── deduplication.md
   │  │  │  │  └── filtering.md
   │  │  │  └── SKILL.md
   │  │  ├── obliteratus
   │  │  │  ├── references
   │  │  │  │  ├── analysis-modules.md
   │  │  │  │  └── methods-guide.md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── abliteration-config.yaml
   │  │  │    ├── analysis-study.yaml
   │  │  │    └── batch-abliteration.yaml
   │  │  ├── peft
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── pinecone
   │  │  │  ├── references
   │  │  │  │  └── deployment.md
   │  │  │  └── SKILL.md
   │  │  ├── pytorch-fsdp
   │  │  │  ├── references
   │  │  │  │  ├── common-patterns.md
   │  │  │  │  ├── index.md
   │  │  │  │  └── other.md
   │  │  │  └── SKILL.md
   │  │  ├── pytorch-lightning
   │  │  │  ├── references
   │  │  │  │  ├── callbacks.md
   │  │  │  │  ├── distributed.md
   │  │  │  │  └── hyperparameter-tuning.md
   │  │  │  └── SKILL.md
   │  │  ├── qdrant
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── research
   │  │  │  ├── DESCRIPTION.md
   │  │  │  └── dspy
   │  │  │    ├── references
   │  │  │     │  ├── examples.md
   │  │  │     │  ├── modules.md
   │  │  │     │  └── optimizers.md
   │  │  │    └── SKILL.md
   │  │  ├── saelens
   │  │  │  ├── references
   │  │  │  │  ├── api.md
   │  │  │  │  ├── README.md
   │  │  │  │  └── tutorials.md
   │  │  │  └── SKILL.md
   │  │  ├── simpo
   │  │  │  ├── references
   │  │  │  │  ├── datasets.md
   │  │  │  │  ├── hyperparameters.md
   │  │  │  │  └── loss-functions.md
   │  │  │  └── SKILL.md
   │  │  ├── slime
   │  │  │  ├── references
   │  │  │  │  ├── api-reference.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── stable-diffusion
   │  │  │  ├── references
   │  │  │  │  ├── advanced-usage.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── tensorrt-llm
   │  │  │  ├── references
   │  │  │  │  ├── multi-gpu.md
   │  │  │  │  ├── optimization.md
   │  │  │  │  └── serving.md
   │  │  │  └── SKILL.md
   │  │  ├── torchtitan
   │  │  │  ├── references
   │  │  │  │  ├── checkpoint.md
   │  │  │  │  ├── custom-models.md
   │  │  │  │  ├── float8.md
   │  │  │  │  └── fsdp.md
   │  │  │  └── SKILL.md
   │  │  ├── training
   │  │  │  ├── axolotl
   │  │  │  │  ├── references
   │  │  │  │  │  ├── api.md
   │  │  │  │  │  ├── dataset-formats.md
   │  │  │  │  │  ├── index.md
   │  │  │  │  │  └── other.md
   │  │  │  │  └── SKILL.md
   │  │  │  ├── trl-fine-tuning
   │  │  │  │  ├── references
   │  │  │  │  │  ├── dpo-variants.md
   │  │  │  │  │  ├── grpo-training.md
   │  │  │  │  │  ├── online-rl.md
   │  │  │  │  │  ├── reward-modeling.md
   │  │  │  │  │  └── sft-training.md
   │  │  │  │  ├── SKILL.md
   │  │  │  │  └── templates
   │  │  │  │    └── basic_grpo_training.py
   │  │  │  └── unsloth
   │  │  │    ├── references
   │  │  │     │  ├── index.md
   │  │  │     │  ├── llms-full.md
   │  │  │     │  ├── llms-txt.md
   │  │  │     │  └── llms.md
   │  │  │    └── SKILL.md
   │  │  └── whisper
   │  │    ├── references
   │  │     │  └── languages.md
   │  │    └── SKILL.md
   │  ├── payments
   │  │  ├── mpp-agent
   │  │  │  └── SKILL.md
   │  │  ├── stripe-link-cli
   │  │  │  └── SKILL.md
   │  │  └── stripe-projects
   │  │    └── SKILL.md
   │  ├── productivity
   │  │  ├── canvas
   │  │  │  ├── scripts
   │  │  │  │  └── canvas_api.py
   │  │  │  └── SKILL.md
   │  │  ├── here-now
   │  │  │  ├── scripts
   │  │  │  │  ├── drive.sh
   │  │  │  │  └── publish.sh
   │  │  │  └── SKILL.md
   │  │  ├── memento-flashcards
   │  │  │  ├── scripts
   │  │  │  │  ├── memento_cards.py
   │  │  │  │  └── youtube_quiz.py
   │  │  │  └── SKILL.md
   │  │  ├── shop
   │  │  │  ├── references
   │  │  │  │  ├── catalog-mcp.md
   │  │  │  │  ├── direct-api.md
   │  │  │  │  ├── legal.md
   │  │  │  │  └── safety.md
   │  │  │  └── SKILL.md
   │  │  ├── shopify
   │  │  │  └── SKILL.md
   │  │  ├── siyuan
   │  │  │  └── SKILL.md
   │  │  └── telephony
   │  │    ├── scripts
   │  │     │  └── telephony.py
   │  │    └── SKILL.md
   │  ├── research
   │  │  ├── bioinformatics
   │  │  │  └── SKILL.md
   │  │  ├── darwinian-evolver
   │  │  │  ├── scripts
   │  │  │  │  ├── parrot_openrouter.py
   │  │  │  │  └── show_snapshot.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── custom_problem_template.py
   │  │  ├── domain-intel
   │  │  │  ├── scripts
   │  │  │  │  └── domain_intel.py
   │  │  │  └── SKILL.md
   │  │  ├── drug-discovery
   │  │  │  ├── references
   │  │  │  │  └── ADMET_REFERENCE.md
   │  │  │  ├── scripts
   │  │  │  │  ├── chembl_target.py
   │  │  │  │  └── ro5_screen.py
   │  │  │  └── SKILL.md
   │  │  ├── duckduckgo-search
   │  │  │  ├── scripts
   │  │  │  │  └── duckduckgo.sh
   │  │  │  └── SKILL.md
   │  │  ├── gitnexus-explorer
   │  │  │  ├── scripts
   │  │  │  │  └── proxy.mjs
   │  │  │  └── SKILL.md
   │  │  ├── osint-investigation
   │  │  │  ├── references
   │  │  │  │  └── sources
   │  │  │  │    ├── courtlistener.md
   │  │  │  │    ├── gdelt.md
   │  │  │  │    ├── icij-offshore.md
   │  │  │  │    ├── nyc-acris.md
   │  │  │  │    ├── ofac-sdn.md
   │  │  │  │    ├── opencorporates.md
   │  │  │  │    ├── sec-edgar.md
   │  │  │  │    ├── senate-ld.md
   │  │  │  │    ├── usaspending.md
   │  │  │  │    ├── wayback.md
   │  │  │  │    └── wikipedia.md
   │  │  │  ├── scripts
   │  │  │  │  ├── build_findings.py
   │  │  │  │  ├── entity_resolution.py
   │  │  │  │  ├── fetch_courtlistener.py
   │  │  │  │  ├── fetch_gdelt.py
   │  │  │  │  ├── fetch_icij_offshore.py
   │  │  │  │  ├── fetch_nyc_acris.py
   │  │  │  │  ├── fetch_ofac_sdn.py
   │  │  │  │  ├── fetch_opencorporates.py
   │  │  │  │  ├── fetch_sec_edgar.py
   │  │  │  │  ├── fetch_senate_ld.py
   │  │  │  │  ├── fetch_usaspending.py
   │  │  │  │  ├── fetch_wayback.py
   │  │  │  │  ├── fetch_wikipedia.py
   │  │  │  │  ├── timing_analysis.py
   │  │  │  │  ├── _http.py
   │  │  │  │  └── _normalize.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── source-template.md
   │  │  ├── parallel-cli
   │  │  │  └── SKILL.md
   │  │  ├── pinecone-research
   │  │  │  ├── scripts
   │  │  │  │  ├── memory_manager.py
   │  │  │  │  └── rag_pipeline.py
   │  │  │  └── SKILL.md
   │  │  ├── qmd
   │  │  │  └── SKILL.md
   │  │  ├── scrapling
   │  │  │  └── SKILL.md
   │  │  └── searxng-search
   │  │    ├── scripts
   │  │     │  └── searxng.sh
   │  │    └── SKILL.md
   │  ├── security
   │  │  ├── 1password
   │  │  │  ├── references
   │  │  │  │  ├── cli-examples.md
   │  │  │  │  └── get-started.md
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── godmode
   │  │  │  ├── references
   │  │  │  │  ├── jailbreak-templates.md
   │  │  │  │  └── refusal-detection.md
   │  │  │  ├── scripts
   │  │  │  │  ├── auto_jailbreak.py
   │  │  │  │  ├── godmode_race.py
   │  │  │  │  ├── load_godmode.py
   │  │  │  │  └── parseltongue.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── prefill-subtle.json
   │  │  │    └── prefill.json
   │  │  ├── oss-forensics
   │  │  │  ├── references
   │  │  │  │  ├── evidence-types.md
   │  │  │  │  ├── github-archive-guide.md
   │  │  │  │  ├── investigation-templates.md
   │  │  │  │  └── recovery-techniques.md
   │  │  │  ├── scripts
   │  │  │  │  └── evidence-store.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── forensic-report.md
   │  │  │    └── malicious-package-report.md
   │  │  ├── sherlock
   │  │  │  └── SKILL.md
   │  │  ├── unbroker
   │  │  │  ├── assets
   │  │  │  │  └── unbroker.png
   │  │  │  ├── README.md
   │  │  │  ├── references
   │  │  │  │  ├── brokers
   │  │  │  │  │  ├── addresses.json
   │  │  │  │  │  ├── advancedbackgroundchecks.json
   │  │  │  │  │  ├── beenverified.json
   │  │  │  │  │  ├── clustal.json
   │  │  │  │  │  ├── clustrmaps.json
   │  │  │  │  │  ├── cyberbackgroundchecks.json
   │  │  │  │  │  ├── familytreenow.json
   │  │  │  │  │  ├── fastpeoplesearch.json
   │  │  │  │  │  ├── intelius.json
   │  │  │  │  │  ├── mylife.json
   │  │  │  │  │  ├── nuwber.json
   │  │  │  │  │  ├── peekyou.json
   │  │  │  │  │  ├── peoplefinders.json
   │  │  │  │  │  ├── radaris.json
   │  │  │  │  │  ├── rehold.json
   │  │  │  │  │  ├── searchpeoplefree.json
   │  │  │  │  │  ├── socialcatfish.json
   │  │  │  │  │  ├── spokeo.json
   │  │  │  │  │  ├── thatsthem.json
   │  │  │  │  │  ├── truepeoplesearch.json
   │  │  │  │  │  ├── usphonebook.json
   │  │  │  │  │  └── whitepages.json
   │  │  │  │  ├── legal
   │  │  │  │  │  ├── ccpa.md
   │  │  │  │  │  ├── drop.md
   │  │  │  │  │  └── gdpr.md
   │  │  │  │  ├── methods.md
   │  │  │  │  ├── site-playbooks.md
   │  │  │  │  └── state-machine.md
   │  │  │  ├── scripts
   │  │  │  │  ├── autopilot.py
   │  │  │  │  ├── badbool.py
   │  │  │  │  ├── brokers.py
   │  │  │  │  ├── cdp.py
   │  │  │  │  ├── config.py
   │  │  │  │  ├── crypto.py
   │  │  │  │  ├── dossier.py
   │  │  │  │  ├── emailer.py
   │  │  │  │  ├── email_modes.py
   │  │  │  │  ├── ledger.py
   │  │  │  │  ├── legal.py
   │  │  │  │  ├── paths.py
   │  │  │  │  ├── pdd.py
   │  │  │  │  ├── registry.py
   │  │  │  │  ├── report.py
   │  │  │  │  ├── scan.py
   │  │  │  │  ├── storage.py
   │  │  │  │  ├── tiers.py
   │  │  │  │  └── vectors.py
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── consent
   │  │  │     │  └── authorization.md
   │  │  │    └── emails
   │  │  │       ├── ccpa-authorized-agent.txt
   │  │  │       ├── ccpa-deletion.txt
   │  │  │       ├── ccpa-indirect-deletion.txt
   │  │  │       ├── gdpr-erasure.txt
   │  │  │       └── generic-optout.txt
   │  │  └── web-pentest
   │  │    ├── references
   │  │     │  ├── bypass-techniques.md
   │  │     │  ├── exploitation-techniques.md
   │  │     │  ├── scope-enforcement.md
   │  │     │  └── vuln-taxonomy.md
   │  │    ├── scripts
   │  │     │  └── recon-scan.sh
   │  │    ├── SKILL.md
   │  │    └── templates
   │  │       ├── authorization.md
   │  │       ├── exploitation-queue.json
   │  │       └── pentest-report.md
   │  ├── software-development
   │  │  ├── ast-grep
   │  │  │  ├── install.ps1
   │  │  │  ├── install.sh
   │  │  │  ├── LICENSE
   │  │  │  ├── references
   │  │  │  │  ├── cli.md
   │  │  │  │  ├── install.md
   │  │  │  │  ├── patterns.md
   │  │  │  │  ├── pitfalls.md
   │  │  │  │  ├── recipes.md
   │  │  │  │  ├── sgconfig.md
   │  │  │  │  └── yaml-rules.md
   │  │  │  ├── scripts
   │  │  │  │  └── ast_grep_helper.py
   │  │  │  ├── SKILL.md
   │  │  │  └── tests
   │  │  │    ├── smoke.ps1
   │  │  │    └── smoke.sh
   │  │  ├── code-wiki
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── architecture.md
   │  │  │    ├── getting-started.md
   │  │  │    ├── module.md
   │  │  │    └── README.md
   │  │  ├── rest-graphql-debug
   │  │  │  └── SKILL.md
   │  │  └── subagent-driven-development
   │  │    ├── references
   │  │     │  ├── context-budget-discipline.md
   │  │     │  └── gates-taxonomy.md
   │  │    └── SKILL.md
   │  ├── web-development
   │  │  ├── cloudflare-temporary-deploy
   │  │  │  ├── scripts
   │  │  │  │  └── parse_deploy_output.py
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── har-derived-api-client
   │  │  │  ├── scripts
   │  │  │  │  ├── har_capture.py
   │  │  │  │  ├── har_capture_cdp.py
   │  │  │  │  └── har_to_client.py
   │  │  │  └── SKILL.md
   │  │  └── page-agent
   │  │    └── SKILL.md
   │  └── yuanbao
   │    └── SKILL.md
  ├── package-lock.json
  ├── package.json
  ├── plugins
   │  ├── browser
   │  │  ├── browserbase
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── browser_use
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  └── firecrawl
   │  │    ├── plugin.yaml
   │  │    ├── provider.py
   │  │    └── __init__.py
   │  ├── context_engine
   │  │  └── __init__.py
   │  ├── cron_providers
   │  │  ├── chronos
   │  │  │  ├── plugin.yaml
   │  │  │  ├── verify.py
   │  │  │  ├── _nas_client.py
   │  │  │  └── __init__.py
   │  │  └── __init__.py
   │  ├── dashboard_auth
   │  │  ├── basic
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── drain
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── nous
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  └── self_hosted
   │  │    ├── plugin.yaml
   │  │    └── __init__.py
   │  ├── disk-cleanup
   │  │  ├── disk_cleanup.py
   │  │  ├── plugin.yaml
   │  │  ├── README.md
   │  │  └── __init__.py
   │  ├── google_meet
   │  │  ├── audio_bridge.py
   │  │  ├── cli.py
   │  │  ├── meet_bot.py
   │  │  ├── node
   │  │  │  ├── cli.py
   │  │  │  ├── client.py
   │  │  │  ├── protocol.py
   │  │  │  ├── registry.py
   │  │  │  ├── server.py
   │  │  │  └── __init__.py
   │  │  ├── plugin.yaml
   │  │  ├── process_manager.py
   │  │  ├── README.md
   │  │  ├── realtime
   │  │  │  ├── openai_client.py
   │  │  │  └── __init__.py
   │  │  ├── SKILL.md
   │  │  ├── tools.py
   │  │  └── __init__.py
   │  ├── jimmy-achievements
   │  │  ├── dashboard
   │  │  │  ├── dist
   │  │  │  │  ├── index.js
   │  │  │  │  └── style.css
   │  │  │  ├── manifest.json
   │  │  │  └── plugin_api.py
   │  │  ├── docs
   │  │  │  └── assets
   │  │  │    ├── achievements-dashboard-hd.png
   │  │  │    └── achievements-tier-showcase-hd.png
   │  │  ├── LICENSE
   │  │  ├── README.md
   │  │  └── tests
   │  │    └── test_achievement_engine.py
   │  ├── image_gen
   │  │  ├── deepinfra
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── fal
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── krea
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── openai
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── openai-codex
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── openrouter
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  └── xai
   │  │    ├── plugin.yaml
   │  │    └── __init__.py
   │  ├── kanban
   │  │  ├── dashboard
   │  │  │  ├── dist
   │  │  │  │  ├── index.js
   │  │  │  │  └── style.css
   │  │  │  ├── manifest.json
   │  │  │  └── plugin_api.py
   │  │  └── systemd
   │  │    └── jimmy-kanban-dispatcher.service
   │  ├── memory
   │  │  ├── byterover
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  └── __init__.py
   │  │  ├── config_schema.py
   │  │  ├── hindsight
   │  │  │  ├── config_schema.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  ├── templates.py
   │  │  │  └── __init__.py
   │  │  ├── holographic
   │  │  │  ├── holographic.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  ├── retrieval.py
   │  │  │  ├── store.py
   │  │  │  └── __init__.py
   │  │  ├── honcho
   │  │  │  ├── cli.py
   │  │  │  ├── client.py
   │  │  │  ├── config_schema.py
   │  │  │  ├── oauth.py
   │  │  │  ├── oauth_flow.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  ├── session.py
   │  │  │  └── __init__.py
   │  │  ├── mem0
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  ├── _backend.py
   │  │  │  ├── _oss_providers.py
   │  │  │  ├── _setup.py
   │  │  │  └── __init__.py
   │  │  ├── openviking
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  └── __init__.py
   │  │  ├── query_rewrite.py
   │  │  ├── retaindb
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  └── __init__.py
   │  │  ├── supermemory
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  └── __init__.py
   │  │  └── __init__.py
   │  ├── model-providers
   │  │  ├── actual
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── ai-gateway
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── alibaba
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── alibaba-coding-plan
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── anthropic
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── arcee
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── azure-foundry
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── bedrock
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── commandcode
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── copilot
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── copilot-acp
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── custom
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── deepinfra
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── deepseek
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── fireworks
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── gemini
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── gmi
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── huggingface
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── kilocode
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── kimi-coding
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── meta-ai
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── minimax
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── nous
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── novita
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── nvidia
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── ollama-cloud
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── openai-codex
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── opencode-zen
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── openrouter
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── qwen-oauth
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── README.md
   │  │  ├── stepfun
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── upstage
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── vertex
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── xai
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── xiaomi
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  └── zai
   │  │    ├── plugin.yaml
   │  │    └── __init__.py
   │  ├── observability
   │  │  └── langfuse
   │  │    ├── plugin.yaml
   │  │    ├── README.md
   │  │    └── __init__.py
   │  ├── platforms
   │  │  ├── a2a
   │  │  │  ├── adapter.py
   │  │  │  ├── DESIGN.md
   │  │  │  ├── plugin.yaml
   │  │  │  ├── protocol.py
   │  │  │  ├── README.md
   │  │  │  ├── security.py
   │  │  │  ├── tools.py
   │  │  │  └── __init__.py
   │  │  ├── buzz
   │  │  │  ├── adapter.py
   │  │  │  ├── nostr_auth.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── dingtalk
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── discord
   │  │  │  ├── adapter.py
   │  │  │  ├── ffmpeg_utils.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── recovery.py
   │  │  │  ├── voice_mixer.py
   │  │  │  └── __init__.py
   │  │  ├── email
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── feishu
   │  │  │  ├── adapter.py
   │  │  │  ├── feishu_comment.py
   │  │  │  ├── feishu_comment_rules.py
   │  │  │  ├── feishu_meeting_invite.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── google_chat
   │  │  │  ├── adapter.py
   │  │  │  ├── oauth.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── homeassistant
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── irc
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── line
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── matrix
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── mattermost
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── ntfy
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── photon
   │  │  │  ├── adapter.py
   │  │  │  ├── auth.py
   │  │  │  ├── cli.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── README.md
   │  │  │  ├── sidecar
   │  │  │  │  ├── index.mjs
   │  │  │  │  ├── package-lock.json
   │  │  │  │  ├── package.json
   │  │  │  │  ├── patch-spectrum-mixed-attachments.mjs
   │  │  │  │  ├── README.md
   │  │  │  │  ├── send-format.mjs
   │  │  │  │  └── stream-staleness.mjs
   │  │  │  ├── sidecar_paths.py
   │  │  │  └── __init__.py
   │  │  ├── raft
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── simplex
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── slack
   │  │  │  ├── adapter.py
   │  │  │  ├── block_kit.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── sms
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── teams
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── telegram
   │  │  │  ├── adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── telegram_ids.py
   │  │  │  ├── telegram_network.py
   │  │  │  └── __init__.py
   │  │  ├── wecom
   │  │  │  ├── adapter.py
   │  │  │  ├── callback_adapter.py
   │  │  │  ├── plugin.yaml
   │  │  │  ├── wecom_crypto.py
   │  │  │  └── __init__.py
   │  │  └── whatsapp
   │  │    ├── adapter.py
   │  │    ├── plugin.yaml
   │  │    └── __init__.py
   │  ├── plugin_storage.py
   │  ├── plugin_utils.py
   │  ├── security-guidance
   │  │  ├── LICENSE
   │  │  ├── NOTICE
   │  │  ├── patterns.py
   │  │  ├── plugin.yaml
   │  │  ├── README.md
   │  │  └── __init__.py
   │  ├── spotify
   │  │  ├── client.py
   │  │  ├── plugin.yaml
   │  │  ├── tools.py
   │  │  └── __init__.py
   │  ├── teams_pipeline
   │  │  ├── cli.py
   │  │  ├── meetings.py
   │  │  ├── models.py
   │  │  ├── pipeline.py
   │  │  ├── plugin.yaml
   │  │  ├── runtime.py
   │  │  ├── store.py
   │  │  ├── subscriptions.py
   │  │  └── __init__.py
   │  ├── video_gen
   │  │  ├── deepinfra
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  ├── fal
   │  │  │  ├── plugin.yaml
   │  │  │  └── __init__.py
   │  │  └── xai
   │  │    ├── plugin.yaml
   │  │    └── __init__.py
   │  ├── web
   │  │  ├── brave_free
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── ddgs
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  ├── _search_worker.py
   │  │  │  └── __init__.py
   │  │  ├── exa
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── firecrawl
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── keenable
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── keyless_mcp.py
   │  │  ├── parallel
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── searxng
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── tavily
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  ├── xai
   │  │  │  ├── plugin.yaml
   │  │  │  ├── provider.py
   │  │  │  └── __init__.py
   │  │  └── __init__.py
   │  └── __init__.py
  ├── providers
   │  ├── base.py
   │  ├── README.md
   │  └── __init__.py
  ├── pyproject.toml
  ├── README.es.md
  ├── README.md
  ├── README.ur-pk.md
  ├── README.zh-CN.md
  ├── registration_lifecycle.py
  ├── run_agent.py
  ├── scripts
   │  ├── add_contributor.py
   │  ├── analyze_livetest.py
   │  ├── audit_pr_attribution.py
   │  ├── benchmark_browser_eval.py
   │  ├── build_model_catalog.py
   │  ├── build_skills_index.py
   │  ├── capture-cage-terminal.sh
   │  ├── check-windows-footguns.py
   │  ├── check_subprocess_stdin.py
   │  ├── ci
   │  │  ├── assemble_review_comment.py
   │  │  ├── classify_changes.py
   │  │  ├── e2e_screenshot_status.py
   │  │  ├── emit_review_status.py
   │  │  ├── list_os_marked_tests.py
   │  │  ├── live_comment.py
   │  │  ├── lockfile_diff.py
   │  │  ├── publish_e2e_evidence.py
   │  │  ├── test_install_ps1_path_migration.ps1
   │  │  └── timings_report.py
   │  ├── contributor_audit.py
   │  ├── desktop-update
   │  │  ├── posix.sh
   │  │  ├── repro.sh
   │  │  ├── serve-ui.py
   │  │  ├── ui.html
   │  │  └── windows.ps1
   │  ├── desktop-update.ps1
   │  ├── dev-sandbox.sh
   │  ├── discord-voice-doctor.py
   │  ├── docker_config_migrate.py
   │  ├── docker_rebootstrap_nous_session.py
   │  ├── generate_conformance_vectors.py
   │  ├── jimmy-gateway
   │  ├── install.cmd
   │  ├── install.ps1
   │  ├── install.sh
   │  ├── install_psutil_android.py
   │  ├── iso-certify.py
   │  ├── keystroke_diagnostic.py
   │  ├── kill_modal.sh
   │  ├── lib
   │  │  └── node-bootstrap.sh
   │  ├── lint_diff.py
   │  ├── LIVETEST_README.md
   │  ├── micro_compaction_report.py
   │  ├── observability
   │  │  ├── gateway_health_export_probe.py
   │  │  └── otel_capture_collector.py
   │  ├── profile-tui.py
   │  ├── release.py
   │  ├── run_tests.sh
   │  ├── run_tests_parallel.py
   │  ├── sample_and_compress.py
   │  ├── sandbox
   │  │  ├── openssl.cnf
   │  │  ├── pick-release-tags.sh
   │  │  ├── proxy.py
   │  │  ├── ssh-shim.sh
   │  │  └── stage2-run.sh
   │  ├── smoke_nemo_relay_shared_metrics.py
   │  ├── tests
   │  │  ├── test-install-ps1-gitbash-compatibility.ps1
   │  │  ├── test-install-ps1-longpath.ps1
   │  │  └── test-install-ps1-stage-protocol.ps1
   │  ├── toolperf_abeval
   │  │  ├── ab_eval.py
   │  │  ├── README.md
   │  │  └── run_all.sh
   │  ├── tool_search_livetest.py
   │  ├── tool_search_livetest2.py
   │  ├── tool_search_livetest_ue.py
   │  ├── tool_search_livetest_ue_disc.py
   │  ├── tool_search_livetest_ue_hard.py
   │  └── whatsapp-bridge
   │    ├── allowlist.js
   │    ├── allowlist.test.mjs
   │    ├── bridge.js
   │    ├── bridge.native.test.mjs
   │    ├── bridge.reconnect.test.mjs
   │    ├── bridge.sendqueue.test.mjs
   │    ├── bridge_helpers.js
   │    ├── outbound_ids.js
   │    ├── outbound_ids.test.mjs
   │    ├── owner_message_gate.js
   │    ├── owner_message_gate.test.mjs
   │    ├── package-lock.json
   │    └── package.json
  ├── SECURITY.es.md
  ├── SECURITY.md
  ├── setup-jimmy.sh
  ├── setup.py
  ├── skills
   │  ├── apple
   │  │  ├── apple-notes
   │  │  │  └── SKILL.md
   │  │  ├── apple-reminders
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── findmy
   │  │  │  └── SKILL.md
   │  │  └── imessage
   │  │    └── SKILL.md
   │  ├── autonomous-ai-agents
   │  │  ├── claude-code
   │  │  │  └── SKILL.md
   │  │  ├── codex
   │  │  │  └── SKILL.md
   │  │  ├── computer-use
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── jimmy-agent
   │  │  │  ├── references
   │  │  │  │  ├── background-systems.md
   │  │  │  │  ├── cli-reference.md
   │  │  │  │  ├── configuration.md
   │  │  │  │  ├── contributor-guide.md
   │  │  │  │  ├── delegate-task-concurrency-diagnosis.md
   │  │  │  │  ├── desktop-plugins.md
   │  │  │  │  ├── native-mcp.md
   │  │  │  │  ├── petdex.md
   │  │  │  │  ├── portal-auth-for-third-party-apps.md
   │  │  │  │  ├── project-context-files.md
   │  │  │  │  ├── providers-and-models.md
   │  │  │  │  ├── security-privacy.md
   │  │  │  │  ├── slash-commands.md
   │  │  │  │  ├── themes.md
   │  │  │  │  ├── troubleshooting.md
   │  │  │  │  ├── tui-widgets.md
   │  │  │  │  ├── webhooks.md
   │  │  │  │  └── windows-quirks.md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── clock.mjs
   │  │  │    ├── plugin.js
   │  │  │    └── skin.yaml
   │  │  ├── merge-reconciler
   │  │  │  └── SKILL.md
   │  │  └── opencode
   │  │    └── SKILL.md
   │  ├── creative
   │  │  ├── architecture-diagram
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── template.html
   │  │  ├── ascii-art
   │  │  │  └── SKILL.md
   │  │  ├── ascii-video
   │  │  │  ├── README.md
   │  │  │  ├── references
   │  │  │  │  ├── architecture.md
   │  │  │  │  ├── composition.md
   │  │  │  │  ├── effects.md
   │  │  │  │  ├── inputs.md
   │  │  │  │  ├── optimization.md
   │  │  │  │  ├── scenes.md
   │  │  │  │  ├── shaders.md
   │  │  │  │  └── troubleshooting.md
   │  │  │  └── SKILL.md
   │  │  ├── baoyu-infographic
   │  │  │  ├── PORT_NOTES.md
   │  │  │  ├── references
   │  │  │  │  ├── analysis-framework.md
   │  │  │  │  ├── base-prompt.md
   │  │  │  │  ├── layouts
   │  │  │  │  │  ├── bento-grid.md
   │  │  │  │  │  ├── binary-comparison.md
   │  │  │  │  │  ├── bridge.md
   │  │  │  │  │  ├── circular-flow.md
   │  │  │  │  │  ├── comic-strip.md
   │  │  │  │  │  ├── comparison-matrix.md
   │  │  │  │  │  ├── dashboard.md
   │  │  │  │  │  ├── dense-modules.md
   │  │  │  │  │  ├── funnel.md
   │  │  │  │  │  ├── hierarchical-layers.md
   │  │  │  │  │  ├── hub-spoke.md
   │  │  │  │  │  ├── iceberg.md
   │  │  │  │  │  ├── isometric-map.md
   │  │  │  │  │  ├── jigsaw.md
   │  │  │  │  │  ├── linear-progression.md
   │  │  │  │  │  ├── periodic-table.md
   │  │  │  │  │  ├── story-mountain.md
   │  │  │  │  │  ├── structural-breakdown.md
   │  │  │  │  │  ├── tree-branching.md
   │  │  │  │  │  ├── venn-diagram.md
   │  │  │  │  │  └── winding-roadmap.md
   │  │  │  │  ├── structured-content-template.md
   │  │  │  │  └── styles
   │  │  │  │    ├── aged-academia.md
   │  │  │  │    ├── bold-graphic.md
   │  │  │  │    ├── chalkboard.md
   │  │  │  │    ├── claymation.md
   │  │  │  │    ├── corporate-memphis.md
   │  │  │  │    ├── craft-handmade.md
   │  │  │  │    ├── cyberpunk-neon.md
   │  │  │  │    ├── hand-drawn-edu.md
   │  │  │  │    ├── ikea-manual.md
   │  │  │  │    ├── kawaii.md
   │  │  │  │    ├── knolling.md
   │  │  │  │    ├── lego-brick.md
   │  │  │  │    ├── morandi-journal.md
   │  │  │  │    ├── origami.md
   │  │  │  │    ├── pixel-art.md
   │  │  │  │    ├── pop-laboratory.md
   │  │  │  │    ├── retro-pop-grid.md
   │  │  │  │    ├── storybook-watercolor.md
   │  │  │  │    ├── subway-map.md
   │  │  │  │    ├── technical-schematic.md
   │  │  │  │    └── ui-wireframe.md
   │  │  │  └── SKILL.md
   │  │  ├── claude-design
   │  │  │  └── SKILL.md
   │  │  ├── comfyui
   │  │  │  ├── references
   │  │  │  │  ├── official-cli.md
   │  │  │  │  ├── rest-api.md
   │  │  │  │  ├── template-integrity.md
   │  │  │  │  └── workflow-format.md
   │  │  │  ├── scripts
   │  │  │  │  ├── auto_fix_deps.py
   │  │  │  │  ├── check_deps.py
   │  │  │  │  ├── comfyui_setup.sh
   │  │  │  │  ├── extract_schema.py
   │  │  │  │  ├── fetch_logs.py
   │  │  │  │  ├── hardware_check.py
   │  │  │  │  ├── health_check.py
   │  │  │  │  ├── run_batch.py
   │  │  │  │  ├── run_workflow.py
   │  │  │  │  ├── ws_monitor.py
   │  │  │  │  └── _common.py
   │  │  │  ├── SKILL.md
   │  │  │  ├── tests
   │  │  │  │  ├── conftest.py
   │  │  │  │  ├── pytest.ini
   │  │  │  │  ├── README.md
   │  │  │  │  ├── test_check_deps.py
   │  │  │  │  ├── test_cloud_integration.py
   │  │  │  │  ├── test_common.py
   │  │  │  │  ├── test_extract_schema.py
   │  │  │  │  └── test_run_workflow.py
   │  │  │  └── workflows
   │  │  │    ├── animatediff_video.json
   │  │  │    ├── flux_dev_txt2img.json
   │  │  │    ├── README.md
   │  │  │    ├── sd15_txt2img.json
   │  │  │    ├── sdxl_img2img.json
   │  │  │    ├── sdxl_inpaint.json
   │  │  │    ├── sdxl_txt2img.json
   │  │  │    ├── upscale_4x.json
   │  │  │    └── wan_video_t2v.json
   │  │  ├── DESCRIPTION.md
   │  │  ├── design-md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── starter.md
   │  │  ├── excalidraw
   │  │  │  ├── references
   │  │  │  │  ├── colors.md
   │  │  │  │  ├── dark-mode.md
   │  │  │  │  └── examples.md
   │  │  │  ├── scripts
   │  │  │  │  └── upload.py
   │  │  │  └── SKILL.md
   │  │  ├── humanizer
   │  │  │  ├── LICENSE
   │  │  │  └── SKILL.md
   │  │  ├── manim-video
   │  │  │  ├── README.md
   │  │  │  ├── references
   │  │  │  │  ├── animation-design-thinking.md
   │  │  │  │  ├── animations.md
   │  │  │  │  ├── camera-and-3d.md
   │  │  │  │  ├── decorations.md
   │  │  │  │  ├── equations.md
   │  │  │  │  ├── graphs-and-data.md
   │  │  │  │  ├── mobjects.md
   │  │  │  │  ├── paper-explainer.md
   │  │  │  │  ├── production-quality.md
   │  │  │  │  ├── rendering.md
   │  │  │  │  ├── scene-planning.md
   │  │  │  │  ├── troubleshooting.md
   │  │  │  │  ├── updaters-and-trackers.md
   │  │  │  │  └── visual-design.md
   │  │  │  ├── scripts
   │  │  │  │  └── setup.sh
   │  │  │  └── SKILL.md
   │  │  ├── p5js
   │  │  │  ├── README.md
   │  │  │  ├── references
   │  │  │  │  ├── animation.md
   │  │  │  │  ├── color-systems.md
   │  │  │  │  ├── core-api.md
   │  │  │  │  ├── export-pipeline.md
   │  │  │  │  ├── interaction.md
   │  │  │  │  ├── shapes-and-geometry.md
   │  │  │  │  ├── troubleshooting.md
   │  │  │  │  ├── typography.md
   │  │  │  │  ├── visual-effects.md
   │  │  │  │  └── webgl-and-3d.md
   │  │  │  ├── scripts
   │  │  │  │  ├── export-frames.js
   │  │  │  │  ├── render.sh
   │  │  │  │  ├── serve.sh
   │  │  │  │  └── setup.sh
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    └── viewer.html
   │  │  ├── popular-web-designs
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── airbnb.md
   │  │  │    ├── airtable.md
   │  │  │    ├── apple.md
   │  │  │    ├── bmw.md
   │  │  │    ├── cal.md
   │  │  │    ├── claude.md
   │  │  │    ├── clay.md
   │  │  │    ├── clickhouse.md
   │  │  │    ├── cohere.md
   │  │  │    ├── coinbase.md
   │  │  │    ├── composio.md
   │  │  │    ├── cursor.md
   │  │  │    ├── elevenlabs.md
   │  │  │    ├── expo.md
   │  │  │    ├── figma.md
   │  │  │    ├── framer.md
   │  │  │    ├── hashicorp.md
   │  │  │    ├── ibm.md
   │  │  │    ├── intercom.md
   │  │  │    ├── kraken.md
   │  │  │    ├── linear.app.md
   │  │  │    ├── lovable.md
   │  │  │    ├── minimax.md
   │  │  │    ├── mintlify.md
   │  │  │    ├── miro.md
   │  │  │    ├── mistral.ai.md
   │  │  │    ├── mongodb.md
   │  │  │    ├── notion.md
   │  │  │    ├── nvidia.md
   │  │  │    ├── ollama.md
   │  │  │    ├── opencode.ai.md
   │  │  │    ├── pinterest.md
   │  │  │    ├── posthog.md
   │  │  │    ├── raycast.md
   │  │  │    ├── replicate.md
   │  │  │    ├── resend.md
   │  │  │    ├── revolut.md
   │  │  │    ├── runwayml.md
   │  │  │    ├── sanity.md
   │  │  │    ├── sentry.md
   │  │  │    ├── spacex.md
   │  │  │    ├── spotify.md
   │  │  │    ├── stripe.md
   │  │  │    ├── supabase.md
   │  │  │    ├── superhuman.md
   │  │  │    ├── together.ai.md
   │  │  │    ├── uber.md
   │  │  │    ├── vercel.md
   │  │  │    ├── voltagent.md
   │  │  │    ├── warp.md
   │  │  │    ├── webflow.md
   │  │  │    ├── wise.md
   │  │  │    ├── x.ai.md
   │  │  │    └── zapier.md
   │  │  ├── pretext
   │  │  │  ├── references
   │  │  │  │  └── patterns.md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── donut-orbit.html
   │  │  │    └── hello-orb-flow.html
   │  │  ├── sketch
   │  │  │  └── SKILL.md
   │  │  ├── songwriting-and-ai-music
   │  │  │  └── SKILL.md
   │  │  └── touchdesigner-mcp
   │  │    ├── references
   │  │     │  ├── 3d-scene.md
   │  │     │  ├── animation.md
   │  │     │  ├── audio-reactive.md
   │  │     │  ├── dat-scripting.md
   │  │     │  ├── external-data.md
   │  │     │  ├── geometry-comp.md
   │  │     │  ├── glsl.md
   │  │     │  ├── layout-compositor.md
   │  │     │  ├── mcp-tools.md
   │  │     │  ├── midi-osc.md
   │  │     │  ├── network-patterns.md
   │  │     │  ├── operator-tips.md
   │  │     │  ├── operators.md
   │  │     │  ├── panel-ui.md
   │  │     │  ├── particles.md
   │  │     │  ├── pitfalls.md
   │  │     │  ├── postfx.md
   │  │     │  ├── projection-mapping.md
   │  │     │  ├── python-api.md
   │  │     │  ├── replicator.md
   │  │     │  └── troubleshooting.md
   │  │    ├── scripts
   │  │     │  └── setup.sh
   │  │    └── SKILL.md
   │  ├── devops
   │  │  └── sdlc-review
   │  │    └── SKILL.md
   │  ├── email
   │  │  ├── DESCRIPTION.md
   │  │  ├── email-inbox-triage
   │  │  │  └── SKILL.md
   │  │  └── himalaya
   │  │    ├── references
   │  │     │  ├── configuration.md
   │  │     │  └── message-composition.md
   │  │    └── SKILL.md
   │  ├── github
   │  │  ├── codebase-inspection
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── github-auth
   │  │  │  ├── scripts
   │  │  │  │  ├── gh-env.sh
   │  │  │  │  └── git-credential-token.py
   │  │  │  └── SKILL.md
   │  │  ├── github-code-review
   │  │  │  ├── references
   │  │  │  │  └── review-output-template.md
   │  │  │  └── SKILL.md
   │  │  ├── github-issue-to-pr
   │  │  │  └── SKILL.md
   │  │  ├── github-issues
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── bug-report.md
   │  │  │    └── feature-request.md
   │  │  ├── github-pr-workflow
   │  │  │  ├── references
   │  │  │  │  ├── ci-troubleshooting.md
   │  │  │  │  └── conventional-commits.md
   │  │  │  ├── SKILL.md
   │  │  │  └── templates
   │  │  │    ├── pr-body-bugfix.md
   │  │  │    └── pr-body-feature.md
   │  │  └── github-repo-management
   │  │    ├── references
   │  │     │  └── github-api-cheatsheet.md
   │  │    └── SKILL.md
   │  ├── index-cache
   │  │  ├── anthropics_skills_skills_.json
   │  │  ├── lobehub_index.json
   │  │  └── openai_skills_skills_.json
   │  ├── media
   │  │  ├── DESCRIPTION.md
   │  │  ├── gif-search
   │  │  │  └── SKILL.md
   │  │  ├── songsee
   │  │  │  └── SKILL.md
   │  │  └── youtube-content
   │  │    ├── references
   │  │     │  └── output-formats.md
   │  │    ├── scripts
   │  │     │  └── fetch_transcript.py
   │  │    └── SKILL.md
   │  ├── mlops
   │  │  ├── DESCRIPTION.md
   │  │  ├── evaluation
   │  │  │  ├── DESCRIPTION.md
   │  │  │  ├── evaluating-llms-harness
   │  │  │  │  ├── references
   │  │  │  │  │  ├── api-evaluation.md
   │  │  │  │  │  ├── benchmark-guide.md
   │  │  │  │  │  ├── custom-tasks.md
   │  │  │  │  │  └── distributed-eval.md
   │  │  │  │  └── SKILL.md
   │  │  │  └── weights-and-biases
   │  │  │    ├── references
   │  │  │     │  ├── artifacts.md
   │  │  │     │  ├── integrations.md
   │  │  │     │  └── sweeps.md
   │  │  │    └── SKILL.md
   │  │  ├── huggingface-hub
   │  │  │  └── SKILL.md
   │  │  ├── inference
   │  │  │  ├── DESCRIPTION.md
   │  │  │  ├── llama-cpp
   │  │  │  │  ├── references
   │  │  │  │  │  ├── advanced-usage.md
   │  │  │  │  │  ├── hub-discovery.md
   │  │  │  │  │  ├── optimization.md
   │  │  │  │  │  ├── quantization.md
   │  │  │  │  │  ├── server.md
   │  │  │  │  │  └── troubleshooting.md
   │  │  │  │  └── SKILL.md
   │  │  │  └── serving-llms-vllm
   │  │  │    ├── references
   │  │  │     │  ├── optimization.md
   │  │  │     │  ├── quantization.md
   │  │  │     │  ├── server-deployment.md
   │  │  │     │  └── troubleshooting.md
   │  │  │    └── SKILL.md
   │  │  └── models
   │  │    └── DESCRIPTION.md
   │  ├── note-taking
   │  │  ├── DESCRIPTION.md
   │  │  └── obsidian
   │  │    └── SKILL.md
   │  ├── productivity
   │  │  ├── airtable
   │  │  │  └── SKILL.md
   │  │  ├── box
   │  │  │  ├── references
   │  │  │  │  ├── bulk-operations.md
   │  │  │  │  ├── cli-guide.md
   │  │  │  │  ├── content-workflows.md
   │  │  │  │  ├── hubs.md
   │  │  │  │  ├── oauth-setup.md
   │  │  │  │  ├── rest-api.md
   │  │  │  │  ├── sdk-development.md
   │  │  │  │  ├── search-and-ai.md
   │  │  │  │  ├── troubleshooting.md
   │  │  │  │  └── webhooks-and-events.md
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── document-to-action-items
   │  │  │  └── SKILL.md
   │  │  ├── docx
   │  │  │  ├── LICENSE
   │  │  │  ├── references
   │  │  │  │  └── revisions-and-comments.md
   │  │  │  ├── scripts
   │  │  │  │  ├── docx_comments.py
   │  │  │  │  ├── docx_common.py
   │  │  │  │  ├── docx_create.py
   │  │  │  │  ├── docx_edit.py
   │  │  │  │  ├── docx_read.py
   │  │  │  │  ├── docx_revisions.py
   │  │  │  │  ├── docx_template.py
   │  │  │  │  └── docx_validate.py
   │  │  │  ├── SKILL.md
   │  │  │  └── tests
   │  │  │    └── test_docx_skill.py
   │  │  ├── google-workspace
   │  │  │  ├── references
   │  │  │  │  ├── daily-brief.md
   │  │  │  │  └── gmail-search-syntax.md
   │  │  │  ├── scripts
   │  │  │  │  ├── google_api.py
   │  │  │  │  ├── gws_bridge.py
   │  │  │  │  ├── setup.py
   │  │  │  │  └── _jimmy_home.py
   │  │  │  └── SKILL.md
   │  │  ├── maps
   │  │  │  ├── scripts
   │  │  │  │  └── maps_client.py
   │  │  │  └── SKILL.md
   │  │  ├── meeting-action-items
   │  │  │  └── SKILL.md
   │  │  ├── nano-pdf
   │  │  │  └── SKILL.md
   │  │  ├── notion
   │  │  │  ├── references
   │  │  │  │  └── block-types.md
   │  │  │  └── SKILL.md
   │  │  ├── ocr-and-documents
   │  │  │  ├── DESCRIPTION.md
   │  │  │  ├── scripts
   │  │  │  │  ├── extract_marker.py
   │  │  │  │  └── extract_pymupdf.py
   │  │  │  └── SKILL.md
   │  │  ├── pdf
   │  │  │  ├── LICENSE
   │  │  │  ├── references
   │  │  │  │  └── forms.md
   │  │  │  ├── scripts
   │  │  │  │  ├── pdf_create.py
   │  │  │  │  ├── pdf_fill_form.py
   │  │  │  │  ├── pdf_form_layout.py
   │  │  │  │  ├── pdf_make_form.py
   │  │  │  │  ├── pdf_merge.py
   │  │  │  │  ├── pdf_meta.py
   │  │  │  │  ├── pdf_page_image.py
   │  │  │  │  ├── pdf_read.py
   │  │  │  │  ├── pdf_secure.py
   │  │  │  │  ├── pdf_split.py
   │  │  │  │  ├── pdf_stamp.py
   │  │  │  │  ├── pdf_watermark.py
   │  │  │  │  └── _raster.py
   │  │  │  ├── SKILL.md
   │  │  │  └── tests
   │  │  │    └── test_pdf_skill.py
   │  │  ├── powerpoint
   │  │  │  ├── LICENSE
   │  │  │  ├── scripts
   │  │  │  │  ├── pptx_create.py
   │  │  │  │  ├── pptx_edit.py
   │  │  │  │  ├── pptx_from_template.py
   │  │  │  │  ├── pptx_read.py
   │  │  │  │  └── pptx_render.py
   │  │  │  ├── SKILL.md
   │  │  │  └── tests
   │  │  │    └── test_powerpoint_skill.py
   │  │  ├── product-price-monitor
   │  │  │  └── SKILL.md
   │  │  ├── session-librarian
   │  │  │  └── SKILL.md
   │  │  ├── teams-meeting-pipeline
   │  │  │  └── SKILL.md
   │  │  ├── weekly-review-planning
   │  │  │  └── SKILL.md
   │  │  └── xlsx
   │  │    ├── LICENSE
   │  │    ├── references
   │  │     │  └── restructuring.md
   │  │    ├── scripts
   │  │     │  ├── csv_to_xlsx.py
   │  │     │  ├── xlsx_create.py
   │  │     │  ├── xlsx_edit.py
   │  │     │  ├── xlsx_read.py
   │  │     │  ├── xlsx_recalc.py
   │  │     │  ├── xlsx_restructure.py
   │  │     │  └── xlsx_to_csv.py
   │  │    ├── SKILL.md
   │  │    └── tests
   │  │       └── test_xlsx_skill.py
   │  ├── research
   │  │  ├── arxiv
   │  │  │  ├── scripts
   │  │  │  │  └── search_arxiv.py
   │  │  │  └── SKILL.md
   │  │  ├── blocked-page-recovery
   │  │  │  ├── scripts
   │  │  │  │  └── recover_page.py
   │  │  │  └── SKILL.md
   │  │  ├── blogwatcher
   │  │  │  └── SKILL.md
   │  │  ├── competitor-news-monitor
   │  │  │  └── SKILL.md
   │  │  ├── DESCRIPTION.md
   │  │  ├── grounded-citations
   │  │  │  ├── references
   │  │  │  │  ├── citation-formats.md
   │  │  │  │  └── grounding-rationale.md
   │  │  │  ├── scripts
   │  │  │  │  ├── sources.py
   │  │  │  │  └── _jimmy_home.py
   │  │  │  └── SKILL.md
   │  │  ├── llm-wiki
   │  │  │  └── SKILL.md
   │  │  └── research-paper-writing
   │  │    ├── references
   │  │     │  ├── autoreason-methodology.md
   │  │     │  ├── checklists.md
   │  │     │  ├── citation-workflow.md
   │  │     │  ├── experiment-patterns.md
   │  │     │  ├── human-evaluation.md
   │  │     │  ├── paper-types.md
   │  │     │  ├── phase5-paper-drafting.md
   │  │     │  ├── reviewer-guidelines.md
   │  │     │  ├── sources.md
   │  │     │  └── writing-guide.md
   │  │    ├── SKILL.md
   │  │    └── templates
   │  │       ├── aaai2026
   │  │        │  ├── aaai2026-unified-supp.tex
   │  │        │  ├── aaai2026-unified-template.tex
   │  │        │  ├── aaai2026.bib
   │  │        │  ├── aaai2026.bst
   │  │        │  ├── aaai2026.sty
   │  │        │  └── README.md
   │  │       ├── acl
   │  │        │  ├── acl.sty
   │  │        │  ├── acl_latex.tex
   │  │        │  ├── acl_lualatex.tex
   │  │        │  ├── acl_natbib.bst
   │  │        │  ├── anthology.bib.txt
   │  │        │  ├── custom.bib
   │  │        │  ├── formatting.md
   │  │        │  └── README.md
   │  │       ├── colm2025
   │  │        │  ├── colm2025_conference.bib
   │  │        │  ├── colm2025_conference.bst
   │  │        │  ├── colm2025_conference.pdf
   │  │        │  ├── colm2025_conference.sty
   │  │        │  ├── colm2025_conference.tex
   │  │        │  ├── fancyhdr.sty
   │  │        │  ├── math_commands.tex
   │  │        │  ├── natbib.sty
   │  │        │  └── README.md
   │  │       ├── iclr2026
   │  │        │  ├── fancyhdr.sty
   │  │        │  ├── iclr2026_conference.bib
   │  │        │  ├── iclr2026_conference.bst
   │  │        │  ├── iclr2026_conference.pdf
   │  │        │  ├── iclr2026_conference.sty
   │  │        │  ├── iclr2026_conference.tex
   │  │        │  ├── math_commands.tex
   │  │        │  └── natbib.sty
   │  │       ├── icml2026
   │  │        │  ├── algorithm.sty
   │  │        │  ├── algorithmic.sty
   │  │        │  ├── example_paper.bib
   │  │        │  ├── example_paper.pdf
   │  │        │  ├── example_paper.tex
   │  │        │  ├── fancyhdr.sty
   │  │        │  ├── icml2026.bst
   │  │        │  ├── icml2026.sty
   │  │        │  └── icml_numpapers.pdf
   │  │       ├── neurips2025
   │  │        │  ├── extra_pkgs.tex
   │  │        │  ├── main.tex
   │  │        │  ├── Makefile
   │  │        │  └── neurips.sty
   │  │       └── README.md
   │  ├── smart-home
   │  │  ├── DESCRIPTION.md
   │  │  └── openhue
   │  │    └── SKILL.md
   │  ├── social-media
   │  │  ├── DESCRIPTION.md
   │  │  └── xurl
   │  │    └── SKILL.md
   │  └── software-development
   │    ├── dogfood
   │     │  ├── references
   │     │  │  └── issue-taxonomy.md
   │     │  ├── SKILL.md
   │     │  └── templates
   │     │    └── dogfood-report-template.md
   │    ├── jimmy-agent-skill-authoring
   │     │  └── SKILL.md
   │    ├── inspecting-jimmy-desktop-dom
   │     │  └── SKILL.md
   │    ├── node-inspect-debugger
   │     │  └── SKILL.md
   │    ├── plan
   │     │  └── SKILL.md
   │    ├── python-debugpy
   │     │  └── SKILL.md
   │    ├── requesting-code-review
   │     │  └── SKILL.md
   │    ├── simplify-code
   │     │  └── SKILL.md
   │    ├── spike
   │     │  └── SKILL.md
   │    ├── systematic-debugging
   │     │  └── SKILL.md
   │    └── test-driven-development
   │       └── SKILL.md
  ├── sqlite_leak_fix.png
  ├── tests
   │  ├── acp
   │  │  ├── conftest.py
   │  │  ├── test_approval_isolation.py
   │  │  ├── test_auth.py
   │  │  ├── test_edit_approval.py
   │  │  ├── test_entry.py
   │  │  ├── test_events.py
   │  │  ├── test_mcp_e2e.py
   │  │  ├── test_named_provider_catalogs.py
   │  │  ├── test_permissions.py
   │  │  ├── test_ping_suppression.py
   │  │  ├── test_server.py
   │  │  ├── test_session.py
   │  │  ├── test_session_db_private_access.py
   │  │  ├── test_session_provenance.py
   │  │  ├── test_tools.py
   │  │  └── __init__.py
   │  ├── acp_adapter
   │  │  ├── test_acp_commands.py
   │  │  ├── test_acp_images.py
   │  │  ├── test_acp_logging_redaction.py
   │  │  ├── test_acp_mcp_discovery.py
   │  │  └── test_detect_provider_entra.py
   │  ├── agent
   │  │  ├── lsp
   │  │  │  ├── test_backend_gate.py
   │  │  │  ├── test_broken_set.py
   │  │  │  ├── test_client_e2e.py
   │  │  │  ├── test_delta_key.py
   │  │  │  ├── test_diagnostics_field.py
   │  │  │  ├── test_eventlog.py
   │  │  │  ├── test_install_and_lint_fixes.py
   │  │  │  ├── test_lifecycle.py
   │  │  │  ├── test_powershell_server.py
   │  │  │  ├── test_protocol.py
   │  │  │  ├── test_reporter.py
   │  │  │  ├── test_service.py
   │  │  │  ├── test_shell_linter_lsp_skip.py
   │  │  │  ├── test_stale_diagnostics.py
   │  │  │  ├── test_workspace.py
   │  │  │  ├── _mock_lsp_server.py
   │  │  │  └── __init__.py
   │  │  ├── test_account_usage.py
   │  │  ├── test_anthropic_adapter.py
   │  │  ├── test_anthropic_billing_guidance.py
   │  │  ├── test_anthropic_keychain.py
   │  │  ├── test_anthropic_kimi_signed_thinking_replay.py
   │  │  ├── test_anthropic_kwargs_sanitize.py
   │  │  ├── test_anthropic_mcp_prefix_strip.py
   │  │  ├── test_anthropic_oauth_pkce.py
   │  │  ├── test_anthropic_oauth_ua_prefix.py
   │  │  ├── test_anthropic_output_field_leak.py
   │  │  ├── test_anthropic_request_blank_block_guard.py
   │  │  ├── test_anthropic_request_client_reuse.py
   │  │  ├── test_anthropic_structured_output.py
   │  │  ├── test_anthropic_thinking_block_order.py
   │  │  ├── test_anthropic_thinking_disable.py
   │  │  ├── test_anthropic_token_scope_isolation.py
   │  │  ├── test_anthropic_whitespace_text_blocks.py
   │  │  ├── test_api_content_sidecar.py
   │  │  ├── test_arcee_trinity_overrides.py
   │  │  ├── test_async_token_accounting.py
   │  │  ├── test_async_utils.py
   │  │  ├── test_auxiliary_anthropic_pool_fallback_regression.py
   │  │  ├── test_auxiliary_client.py
   │  │  ├── test_auxiliary_client_anthropic_custom.py
   │  │  ├── test_auxiliary_client_azure_foundry.py
   │  │  ├── test_auxiliary_client_base_url_host_validation_52608.py
   │  │  ├── test_auxiliary_client_bootstrap_skew.py
   │  │  ├── test_auxiliary_client_proxy_env.py
   │  │  ├── test_auxiliary_client_resolve_dedup.py
   │  │  ├── test_auxiliary_client_ssl_verify.py
   │  │  ├── test_auxiliary_client_xai_oauth_recovery.py
   │  │  ├── test_auxiliary_compression_timeout_floor.py
   │  │  ├── test_auxiliary_concurrency.py
   │  │  ├── test_auxiliary_config_bridge.py
   │  │  ├── test_auxiliary_explicit_base_anthropic.py
   │  │  ├── test_auxiliary_explicit_cancellation.py
   │  │  ├── test_auxiliary_main_first.py
   │  │  ├── test_auxiliary_named_custom_providers.py
   │  │  ├── test_auxiliary_relay.py
   │  │  ├── test_auxiliary_runtime_cache_key.py
   │  │  ├── test_auxiliary_transient_retry.py
   │  │  ├── test_auxiliary_transport_autodetect.py
   │  │  ├── test_auxiliary_user_default_headers.py
   │  │  ├── test_aux_progress_streaming.py
   │  │  ├── test_azure_identity_adapter.py
   │  │  ├── test_backend_identity.py
   │  │  ├── test_background_review_usage.py
   │  │  ├── test_battery.py
   │  │  ├── test_bedrock_1m_context.py
   │  │  ├── test_bedrock_adapter.py
   │  │  ├── test_bedrock_empty_text_blocks.py
   │  │  ├── test_bedrock_integration.py
   │  │  ├── test_bedrock_interrupt_post_worker.py
   │  │  ├── test_billing_links.py
   │  │  ├── test_billing_unverified_carrythrough.py
   │  │  ├── test_billing_usage.py
   │  │  ├── test_billing_view.py
   │  │  ├── test_bot_profile_prompt_isolation.py
   │  │  ├── test_bounded_response.py
   │  │  ├── test_budget_reasoning_details_exclusion.py
   │  │  ├── test_builtin_memory_disabled_surface.py
   │  │  ├── test_cache_disabled_on_stubs.py
   │  │  ├── test_canon_args_memo_parity.py
   │  │  ├── test_cascading_interrupt_6600.py
   │  │  ├── test_chat_completion_helpers_provider_sort.py
   │  │  ├── test_cjk_token_estimation.py
   │  │  ├── test_close_interrupted_tool_sequence.py
   │  │  ├── test_codex_app_server_event_bridge.py
   │  │  ├── test_codex_app_server_persist.py
   │  │  ├── test_codex_cloudflare_headers.py
   │  │  ├── test_codex_gpt55_autoraise_notice.py
   │  │  ├── test_codex_request_transport_diagnostics.py
   │  │  ├── test_codex_responses_adapter.py
   │  │  ├── test_codex_runtime_live_events.py
   │  │  ├── test_codex_ttfb_watchdog.py
   │  │  ├── test_coding_context.py
   │  │  ├── test_command_token_source.py
   │  │  ├── test_compaction_anti_thrash.py
   │  │  ├── test_compaction_redaction_boundaries.py
   │  │  ├── test_compressed_summary_metadata.py
   │  │  ├── test_compression_adoption_preserves_live_tail.py
   │  │  ├── test_compression_anti_thrash_persistence.py
   │  │  ├── test_compression_anti_thrash_recovery.py
   │  │  ├── test_compression_attempt_telemetry.py
   │  │  ├── test_compression_concurrent_fork.py
   │  │  ├── test_compression_count_warning_36908.py
   │  │  ├── test_compression_fallback_budget.py
   │  │  ├── test_compression_interrupt_protection.py
   │  │  ├── test_compression_logging_session_context.py
   │  │  ├── test_compression_max_attempts_config.py
   │  │  ├── test_compression_orphan_recovery.py
   │  │  ├── test_compression_progress.py
   │  │  ├── test_compression_review_76354.py
   │  │  ├── test_compression_rotation_state.py
   │  │  ├── test_compression_small_ctx_threshold_floor.py
   │  │  ├── test_compression_worker_isolation_76354.py
   │  │  ├── test_compressor_actionable_tail_anchor.py
   │  │  ├── test_compressor_assistant_tail_anchor.py
   │  │  ├── test_compressor_historical_media.py
   │  │  ├── test_compressor_image_tokens.py
   │  │  ├── test_compressor_media_stripping.py
   │  │  ├── test_compressor_tail_cut_oob_fix.py
   │  │  ├── test_compressor_tail_cut_tool_pair_floor.py
   │  │  ├── test_compressor_tool_call_budget.py
   │  │  ├── test_compressor_zero_user_guard.py
   │  │  ├── test_compress_context_progress_timeout.py
   │  │  ├── test_compress_focus.py
   │  │  ├── test_compress_signal_leak.py
   │  │  ├── test_context_breakdown.py
   │  │  ├── test_context_compressor.py
   │  │  ├── test_context_compressor_cross_session_guard.py
   │  │  ├── test_context_compressor_session_end_clears_state.py
   │  │  ├── test_context_compressor_summary_continuity.py
   │  │  ├── test_context_compressor_temporal_anchoring.py
   │  │  ├── test_context_compressor_zero_user_provenance.py
   │  │  ├── test_context_engine.py
   │  │  ├── test_context_engine_host_contract.py
   │  │  ├── test_context_engine_on_turn_complete_usage.py
   │  │  ├── test_context_engine_select_context.py
   │  │  ├── test_context_references.py
   │  │  ├── test_context_refs_concurrent.py
   │  │  ├── test_context_route_mismatch.py
   │  │  ├── test_copilot_acp_client.py
   │  │  ├── test_copilot_acp_deprecation.py
   │  │  ├── test_credential_pool.py
   │  │  ├── test_credential_pool_deferred_refresh.py
   │  │  ├── test_credential_pool_key_rotation.py
   │  │  ├── test_credential_pool_lease_refresh_reselect.py
   │  │  ├── test_credential_pool_no_entries_log_throttle.py
   │  │  ├── test_credential_pool_oat_authtype.py
   │  │  ├── test_credential_pool_oauth_writethrough.py
   │  │  ├── test_credential_pool_provider_boundary.py
   │  │  ├── test_credential_pool_quarantine_locking.py
   │  │  ├── test_credential_pool_routing.py
   │  │  ├── test_credential_pool_sole_cooldown.py
   │  │  ├── test_credential_pool_unmatched_rotation_bound.py
   │  │  ├── test_credits_cold_start.py
   │  │  ├── test_credits_fixture_snapshot.py
   │  │  ├── test_credits_policy.py
   │  │  ├── test_credits_tracker.py
   │  │  ├── test_credits_view.py
   │  │  ├── test_cron_inline_api_call_62151.py
   │  │  ├── test_crossloop_client_cache.py
   │  │  ├── test_curator.py
   │  │  ├── test_curator_activity.py
   │  │  ├── test_curator_backup.py
   │  │  ├── test_curator_classification.py
   │  │  ├── test_curator_reports.py
   │  │  ├── test_cursor_optimizations_parity.py
   │  │  ├── test_custom_pool_mismatch_guard.py
   │  │  ├── test_custom_providers_vision.py
   │  │  ├── test_custom_provider_ca_probes.py
   │  │  ├── test_custom_provider_extra_body.py
   │  │  ├── test_custom_provider_extra_body_matching.py
   │  │  ├── test_deadline.py
   │  │  ├── test_deepseek_anthropic_thinking.py
   │  │  ├── test_direct_provider_url_detection.py
   │  │  ├── test_display.py
   │  │  ├── test_display_emoji.py
   │  │  ├── test_display_todo_progress.py
   │  │  ├── test_display_tool_failure.py
   │  │  ├── test_empty_response_guard.py
   │  │  ├── test_empty_tool_name_loop_dampening.py
   │  │  ├── test_endpoint_blackhole.py
   │  │  ├── test_engine_preflight_wire.py
   │  │  ├── test_error_classifier.py
   │  │  ├── test_external_skills.py
   │  │  ├── test_external_skills_dirs_cache.py
   │  │  ├── test_failover_identity.py
   │  │  ├── test_file_safety.py
   │  │  ├── test_file_safety_container_mirror.py
   │  │  ├── test_file_safety_credentials.py
   │  │  ├── test_file_safety_cross_profile.py
   │  │  ├── test_file_safety_sandbox_mirror.py
   │  │  ├── test_file_safety_session_state.py
   │  │  ├── test_gateway_turn_sidecar.py
   │  │  ├── test_gemini_fast_fallback.py
   │  │  ├── test_gemini_free_tier_gate.py
   │  │  ├── test_gemini_native_adapter.py
   │  │  ├── test_gemini_schema.py
   │  │  ├── test_gemini_standard_key_guidance.py
   │  │  ├── test_ghost_skill_pruning.py
   │  │  ├── test_hygiene_timeout_cooldown_isolation.py
   │  │  ├── test_i18n.py
   │  │  ├── test_idle_compaction.py
   │  │  ├── test_idle_compaction_lock_and_guards.py
   │  │  ├── test_image_gen_registry.py
   │  │  ├── test_image_routing.py
   │  │  ├── test_insights.py
   │  │  ├── test_intent_ack_continuation.py
   │  │  ├── test_interrupt_compat.py
   │  │  ├── test_jiter_preload.py
   │  │  ├── test_kanban_stop.py
   │  │  ├── test_kimi_coding_anthropic_thinking.py
   │  │  ├── test_last_total_tokens.py
   │  │  ├── test_learning_graph.py
   │  │  ├── test_learning_graph_render.py
   │  │  ├── test_learning_mutations.py
   │  │  ├── test_learn_prompt.py
   │  │  ├── test_lmstudio_reasoning.py
   │  │  ├── test_local_probe_disk_cache.py
   │  │  ├── test_local_stream_timeout.py
   │  │  ├── test_manual_compression_feedback.py
   │  │  ├── test_manual_compression_refusal_feedback.py
   │  │  ├── test_markdown_tables.py
   │  │  ├── test_memory_async_sync.py
   │  │  ├── test_memory_boundary_commit.py
   │  │  ├── test_memory_provider.py
   │  │  ├── test_memory_provider_unavailable_warning.py
   │  │  ├── test_memory_recall_indicator.py
   │  │  ├── test_memory_session_switch.py
   │  │  ├── test_memory_skill_scaffolding.py
   │  │  ├── test_memory_user_id.py
   │  │  ├── test_memory_write_bridge.py
   │  │  ├── test_message_content.py
   │  │  ├── test_message_metadata.py
   │  │  ├── test_message_sanitization_policy.py
   │  │  ├── test_meta_agent_init.py
   │  │  ├── test_meta_usage_cache_reporting.py
   │  │  ├── test_micro_compaction.py
   │  │  ├── test_minimax_auxiliary_url.py
   │  │  ├── test_minimax_provider.py
   │  │  ├── test_moa_aggregator_cache_control.py
   │  │  ├── test_moa_aggregator_cost_slot.py
   │  │  ├── test_moa_cold_start_cache_66793.py
   │  │  ├── test_moa_context_max_tokens.py
   │  │  ├── test_moa_observability_bridge.py
   │  │  ├── test_moa_prepared_request_client_swap.py
   │  │  ├── test_moa_progress.py
   │  │  ├── test_moa_quiet_reference_output.py
   │  │  ├── test_moa_reasoning_effort.py
   │  │  ├── test_moa_reference_system_prompt.py
   │  │  ├── test_moa_slot_api_mode.py
   │  │  ├── test_moa_slot_max_tokens.py
   │  │  ├── test_moa_switch_api_mode.py
   │  │  ├── test_moa_trace_streamed_capture.py
   │  │  ├── test_models_dev.py
   │  │  ├── test_models_dev_meta_mapping.py
   │  │  ├── test_model_extra_type_guard.py
   │  │  ├── test_model_metadata.py
   │  │  ├── test_model_metadata_local_ctx.py
   │  │  ├── test_model_metadata_ssl.py
   │  │  ├── test_moonshot_schema.py
   │  │  ├── test_none_deref_guards.py
   │  │  ├── test_non_stream_stale_timeout.py
   │  │  ├── test_nous_credits_gauge.py
   │  │  ├── test_nous_credits_snapshot.py
   │  │  ├── test_nous_oauth_401_guidance.py
   │  │  ├── test_nous_portal_anthropic_wire.py
   │  │  ├── test_nous_rate_guard.py
   │  │  ├── test_onboarding.py
   │  │  ├── test_oneshot.py
   │  │  ├── test_openrouter_response_cache.py
   │  │  ├── test_org_skill_namespace.py
   │  │  ├── test_outbound_webhooks.py
   │  │  ├── test_pet_engine.py
   │  │  ├── test_pet_generate.py
   │  │  ├── test_platform_hint_desktop.py
   │  │  ├── test_platform_hint_overrides.py
   │  │  ├── test_plugin_context_references.py
   │  │  ├── test_plugin_llm.py
   │  │  ├── test_plugin_llm_task_routing.py
   │  │  ├── test_plugin_prompt_sections.py
   │  │  ├── test_portal_tags.py
   │  │  ├── test_post_compression_trim.py
   │  │  ├── test_preflight_compression_gate.py
   │  │  ├── test_preflight_lock_defer.py
   │  │  ├── test_pre_compress_memory_context.py
   │  │  ├── test_proactive_prune_config.py
   │  │  ├── test_proactive_prune_restart_safety.py
   │  │  ├── test_proactive_tool_result_pruning.py
   │  │  ├── test_probe_cache_followups.py
   │  │  ├── test_profile_home_override_precedence.py
   │  │  ├── test_project_skills.py
   │  │  ├── test_prompt_builder.py
   │  │  ├── test_prompt_cache_boundary.py
   │  │  ├── test_prompt_cache_scope.py
   │  │  ├── test_prompt_cache_ttl_propagation.py
   │  │  ├── test_prompt_caching.py
   │  │  ├── test_protected_tail_pressure_61932.py
   │  │  ├── test_proxy_and_url_validation.py
   │  │  ├── test_pydantic_dump_warning_leak.py
   │  │  ├── test_rate_limit_tracker.py
   │  │  ├── test_reactions.py
   │  │  ├── test_reasoning_effort_module.py
   │  │  ├── test_reasoning_effort_wire_translation.py
   │  │  ├── test_reasoning_stale_timeout_floor.py
   │  │  ├── test_reasoning_summaries.py
   │  │  ├── test_redact.py
   │  │  ├── test_reference_handoff_active_turn.py
   │  │  ├── test_refine_focus.py
   │  │  ├── test_relay_llm.py
   │  │  ├── test_relay_nested_execution.py
   │  │  ├── test_relay_runtime_bounded_scope_ops.py
   │  │  ├── test_relay_runtime_plugins.py
   │  │  ├── test_relay_scope_pop_metadata.py
   │  │  ├── test_relay_session_segments.py
   │  │  ├── test_relay_tools.py
   │  │  ├── test_repetition_guard.py
   │  │  ├── test_replay_budget_accounting.py
   │  │  ├── test_replay_cleanup.py
   │  │  ├── test_request_client_reuse.py
   │  │  ├── test_restore_primary_pool_reselect.py
   │  │  ├── test_resume_stale_active_task.py
   │  │  ├── test_rotation_flush_persisted_boundary_68196.py
   │  │  ├── test_runtime_cwd.py
   │  │  ├── test_run_budget.py
   │  │  ├── test_salvage_grown_transcript.py
   │  │  ├── test_save_url_image.py
   │  │  ├── test_secret_scope.py
   │  │  ├── test_secret_scope_tier1_migration.py
   │  │  ├── test_send_path_history_isolation.py
   │  │  ├── test_sequential_tool_interrupt.py
   │  │  ├── test_session_activity.py
   │  │  ├── test_session_rotation_flush_cold_resume_68454.py
   │  │  ├── test_set_runtime_main_custom_provider.py
   │  │  ├── test_shell_hooks.py
   │  │  ├── test_shell_hooks_consent.py
   │  │  ├── test_shell_hooks_tree_kill.py
   │  │  ├── test_skills_guidance_content_filter.py
   │  │  ├── test_skill_bundles.py
   │  │  ├── test_skill_commands.py
   │  │  ├── test_skill_commands_reload.py
   │  │  ├── test_skill_invocation_description.py
   │  │  ├── test_skill_todo_retention_parity.py
   │  │  ├── test_skill_utils.py
   │  │  ├── test_skip_background_review.py
   │  │  ├── test_skip_memory_store_65429.py
   │  │  ├── test_soul_md_profile_isolation.py
   │  │  ├── test_ssl_ca_guard.py
   │  │  ├── test_ssl_verify.py
   │  │  ├── test_stale_replay_prune.py
   │  │  ├── test_stall_guards.py
   │  │  ├── test_streaming_context_scrubber.py
   │  │  ├── test_stream_chunk_byte_estimate.py
   │  │  ├── test_stream_read_timeout_floor.py
   │  │  ├── test_stream_single_writer_guard.py
   │  │  ├── test_structured_output_rejection_retry.py
   │  │  ├── test_subagent_lifecycle.py
   │  │  ├── test_subagent_progress.py
   │  │  ├── test_subagent_stop_hook.py
   │  │  ├── test_subdirectory_hints.py
   │  │  ├── test_subdirectory_hints_tilde.py
   │  │  ├── test_subprocess_env_guard.py
   │  │  ├── test_subscription_view.py
   │  │  ├── test_summarize_tool_result_type_safety.py
   │  │  ├── test_summary_prefix_semantics.py
   │  │  ├── test_summary_prefix_tool_use.py
   │  │  ├── test_summary_role_template_alternation.py
   │  │  ├── test_surrogate_chokepoints.py
   │  │  ├── test_synthetic_turn_display_kind.py
   │  │  ├── test_system_prompt.py
   │  │  ├── test_system_prompt_restore.py
   │  │  ├── test_thinking_timeout_guidance.py
   │  │  ├── test_think_scrubber.py
   │  │  ├── test_thread_scoped_output.py
   │  │  ├── test_title_generator.py
   │  │  ├── test_tool_call_arg_no_redaction.py
   │  │  ├── test_tool_dispatch_helpers.py
   │  │  ├── test_tool_executor_checkpoint_paths.py
   │  │  ├── test_tool_guardrails.py
   │  │  ├── test_tool_result_classification.py
   │  │  ├── test_trace_upload.py
   │  │  ├── test_transcription_registry.py
   │  │  ├── test_tts_registry.py
   │  │  ├── test_turn_context.py
   │  │  ├── test_turn_context_overflow_warning.py
   │  │  ├── test_turn_finalizer_cleanup_guard.py
   │  │  ├── test_turn_finalizer_final_response_persistence.py
   │  │  ├── test_turn_finalizer_interrupt_alternation.py
   │  │  ├── test_turn_finalizer_iteration_limit_exit.py
   │  │  ├── test_turn_overlap_tripwire.py
   │  │  ├── test_turn_retry_state.py
   │  │  ├── test_turn_summary.py
   │  │  ├── test_uncompressed_context_guardrail.py
   │  │  ├── test_unsupported_parameter_retry.py
   │  │  ├── test_unsupported_temperature_retry.py
   │  │  ├── test_usage_pricing.py
   │  │  ├── test_verification_evidence.py
   │  │  ├── test_verification_evidence_fd_leak.py
   │  │  ├── test_verification_stop.py
   │  │  ├── test_verification_stop_caching.py
   │  │  ├── test_verify_hooks.py
   │  │  ├── test_vertex_adapter.py
   │  │  ├── test_video_gen_registry.py
   │  │  ├── test_vision_resolved_args.py
   │  │  ├── test_vision_routing_31179.py
   │  │  ├── transports
   │  │  │  ├── test_bedrock_transport.py
   │  │  │  ├── test_chat_completions.py
   │  │  │  ├── test_chat_completions_empty_tool_calls.py
   │  │  │  ├── test_codex_app_server_runtime.py
   │  │  │  ├── test_codex_app_server_session.py
   │  │  │  ├── test_codex_event_projector.py
   │  │  │  ├── test_codex_transport.py
   │  │  │  ├── test_jimmy_tools_mcp_server.py
   │  │  │  ├── test_meta_codex_cache.py
   │  │  │  ├── test_reasoning_effort_sibling_sites.py
   │  │  │  ├── test_transport.py
   │  │  │  ├── test_types.py
   │  │  │  └── __init__.py
   │  │  └── __init__.py
   │  ├── ci
   │  │  ├── test_assemble_review_comment.py
   │  │  ├── test_classify_changes.py
   │  │  ├── test_e2e_screenshot_status.py
   │  │  ├── test_emit_review_status.py
   │  │  ├── test_list_os_marked_tests.py
   │  │  ├── test_live_comment.py
   │  │  ├── test_lockfile_diff.py
   │  │  ├── test_publish_e2e_evidence.py
   │  │  └── test_timings_report.py
   │  ├── cli
   │  │  ├── conftest.py
   │  │  ├── test_bang_shell_mode.py
   │  │  ├── test_bracketed_paste_timeout.py
   │  │  ├── test_branch_command.py
   │  │  ├── test_busy_input_mode_command.py
   │  │  ├── test_chat_q_exit_clear.py
   │  │  ├── test_cli_active_agent_ref_wiring.py
   │  │  ├── test_cli_approval_ui.py
   │  │  ├── test_cli_async_delegation_delivery.py
   │  │  ├── test_cli_background_busy_path.py
   │  │  ├── test_cli_background_status_indicator.py
   │  │  ├── test_cli_background_tui_refresh.py
   │  │  ├── test_cli_bracketed_paste_sanitizer.py
   │  │  ├── test_cli_browser_connect.py
   │  │  ├── test_cli_clarify_batch.py
   │  │  ├── test_cli_cmd_backspace.py
   │  │  ├── test_cli_codex_context_reference.py
   │  │  ├── test_cli_context_warning.py
   │  │  ├── test_cli_copy_command.py
   │  │  ├── test_cli_delegate_background_notice.py
   │  │  ├── test_cli_extension_hooks.py
   │  │  ├── test_cli_external_editor.py
   │  │  ├── test_cli_file_drop.py
   │  │  ├── test_cli_first_run_setup.py
   │  │  ├── test_cli_force_redraw.py
   │  │  ├── test_cli_goal_interrupt.py
   │  │  ├── test_cli_image_command.py
   │  │  ├── test_cli_init.py
   │  │  ├── test_cli_insights_command.py
   │  │  ├── test_cli_interrupt_ack_race.py
   │  │  ├── test_cli_interrupt_drain_regression.py
   │  │  ├── test_cli_interrupt_subagent.py
   │  │  ├── test_cli_light_mode.py
   │  │  ├── test_cli_loading_indicator.py
   │  │  ├── test_cli_markdown_rendering.py
   │  │  ├── test_cli_mcp_config_watch.py
   │  │  ├── test_cli_new_session.py
   │  │  ├── test_cli_pet_pane.py
   │  │  ├── test_cli_prefix_matching.py
   │  │  ├── test_cli_preloaded_skills.py
   │  │  ├── test_cli_provider_resolution.py
   │  │  ├── test_cli_queue_paste.py
   │  │  ├── test_cli_reload_skills.py
   │  │  ├── test_cli_resume_command.py
   │  │  ├── test_cli_retry.py
   │  │  ├── test_cli_save_config_value.py
   │  │  ├── test_cli_secret_capture.py
   │  │  ├── test_cli_shift_enter_newline.py
   │  │  ├── test_cli_shutdown_memory_messages.py
   │  │  ├── test_cli_skin_integration.py
   │  │  ├── test_cli_status_bar.py
   │  │  ├── test_cli_status_bar_goal.py
   │  │  ├── test_cli_status_command.py
   │  │  ├── test_cli_steer_busy_path.py
   │  │  ├── test_cli_terminal_response_sanitizer.py
   │  │  ├── test_cli_terminal_shortcuts.py
   │  │  ├── test_cli_tools_command.py
   │  │  ├── test_cli_user_message_preview.py
   │  │  ├── test_cli_yolo_resume_persistence.py
   │  │  ├── test_cli_yolo_toggle.py
   │  │  ├── test_command_palette.py
   │  │  ├── test_compress_flags.py
   │  │  ├── test_compress_focus.py
   │  │  ├── test_compress_here.py
   │  │  ├── test_compress_type_ahead.py
   │  │  ├── test_cprint_bg_thread.py
   │  │  ├── test_cpr_local_leak.py
   │  │  ├── test_ctrl_enter_newline.py
   │  │  ├── test_cwd_env_respect.py
   │  │  ├── test_destructive_slash_confirm.py
   │  │  ├── test_destructive_slash_inline_skip_e2e.py
   │  │  ├── test_exit_delete_session.py
   │  │  ├── test_exit_summary_resume_hint.py
   │  │  ├── test_exit_watchdog_signal_arm.py
   │  │  ├── test_fast_command.py
   │  │  ├── test_focus_view.py
   │  │  ├── test_handoff_cleanup_race.py
   │  │  ├── test_indicator_command.py
   │  │  ├── test_interrupt_output_history_regression.py
   │  │  ├── test_manual_compress.py
   │  │  ├── test_moa_command.py
   │  │  ├── test_model_picker_filter.py
   │  │  ├── test_modify_other_keys_aliases.py
   │  │  ├── test_oneshot_resumed_session_persist.py
   │  │  ├── test_partial_compress.py
   │  │  ├── test_personality_none.py
   │  │  ├── test_prefill_config.py
   │  │  ├── test_prepend_note_to_message.py
   │  │  ├── test_prompt_stash.py
   │  │  ├── test_prompt_stash_cli.py
   │  │  ├── test_prompt_text_input_thread_safety.py
   │  │  ├── test_quick_commands.py
   │  │  ├── test_reasoning_command.py
   │  │  ├── test_resume_display.py
   │  │  ├── test_resume_model_restore.py
   │  │  ├── test_resume_quiet_stderr.py
   │  │  ├── test_save_conversation_location.py
   │  │  ├── test_session_boundary_hooks.py
   │  │  ├── test_show_config_credential.py
   │  │  ├── test_single_query_session_finalize.py
   │  │  ├── test_slash_command_interrupt.py
   │  │  ├── test_slash_confirm_windows.py
   │  │  ├── test_slash_undo_title_robustness.py
   │  │  ├── test_steer_inline_repaint_34569.py
   │  │  ├── test_stream_delta_think_tag.py
   │  │  ├── test_stream_flush_left.py
   │  │  ├── test_stream_partial_line_flush.py
   │  │  ├── test_terminal_interrupt_recovery.py
   │  │  ├── test_termios_drift_heal.py
   │  │  ├── test_tool_progress_scrollback.py
   │  │  ├── test_transformed_stream_output.py
   │  │  ├── test_tui_terminal_reset_on_exit.py
   │  │  ├── test_update_command.py
   │  │  ├── test_version_command.py
   │  │  ├── test_worktree.py
   │  │  ├── test_worktree_security.py
   │  │  ├── test_worktree_selfheal.py
   │  │  ├── test_worktree_sync_base.py
   │  │  └── __init__.py
   │  ├── computer_use
   │  │  ├── live_cua_0_9_smoke.py
   │  │  ├── test_cua_atexit_teardown.py
   │  │  ├── test_cua_cli_fallback_env.py
   │  │  ├── test_cua_no_overlay.py
   │  │  ├── test_cua_perf_knobs.py
   │  │  ├── test_cua_spawn_env_sanitization.py
   │  │  ├── test_cua_telemetry.py
   │  │  ├── test_cua_wsl_manifest_path.py
   │  │  ├── test_doctor.py
   │  │  └── test_permissions_resolution.py
   │  ├── conformance
   │  │  ├── test_vector_generator.py
   │  │  ├── vectors
   │  │  │  ├── discord.json
   │  │  │  ├── slack.json
   │  │  │  ├── telegram.json
   │  │  │  └── whatsapp.json
   │  │  └── __init__.py
   │  ├── conftest.py
   │  ├── cron
   │  │  ├── conftest.py
   │  │  ├── test_agent_scheduling_gate.py
   │  │  ├── test_blueprint_catalog.py
   │  │  ├── test_claim_job_for_fire.py
   │  │  ├── test_cleanup_timeout.py
   │  │  ├── test_codex_execution_paths.py
   │  │  ├── test_compute_next_run_last_run_at.py
   │  │  ├── test_cronjob_schema.py
   │  │  ├── test_cron_context_from.py
   │  │  ├── test_cron_created_delivery.py
   │  │  ├── test_cron_direct_api_call_62151.py
   │  │  ├── test_cron_direct_api_call_watchdog.py
   │  │  ├── test_cron_drift_alert_once.py
   │  │  ├── test_cron_emfile_stall_87644.py
   │  │  ├── test_cron_failure_alert_remediation_hint.py
   │  │  ├── test_cron_failure_summarizer_inactivity.py
   │  │  ├── test_cron_inactivity_timeout.py
   │  │  ├── test_cron_kanban_env_isolation.py
   │  │  ├── test_cron_no_agent.py
   │  │  ├── test_cron_origin_synthetic_thread.py
   │  │  ├── test_cron_profile_isolation.py
   │  │  ├── test_cron_prompt_injection_skill.py
   │  │  ├── test_cron_provider_pin.py
   │  │  ├── test_cron_relay_delivery_guards.py
   │  │  ├── test_cron_run_stale_claim_reap_86721.py
   │  │  ├── test_cron_script.py
   │  │  ├── test_cron_thread_seed_dm_keying.py
   │  │  ├── test_cron_workdir.py
   │  │  ├── test_dead_owner_claim_reclaim.py
   │  │  ├── test_execution_ledger.py
   │  │  ├── test_file_permissions.py
   │  │  ├── test_fire_forward_failure_stamp.py
   │  │  ├── test_idle_tick_config_skip.py
   │  │  ├── test_inflight_stale_guard.py
   │  │  ├── test_jobs.py
   │  │  ├── test_jobs_changed_notify.py
   │  │  ├── test_jobs_crossprocess_lock.py
   │  │  ├── test_jobs_file_ownership.py
   │  │  ├── test_jobs_shrink_merge_80624.py
   │  │  ├── test_media_delivery_parity.py
   │  │  ├── test_media_send_timeout.py
   │  │  ├── test_misfire_catchup.py
   │  │  ├── test_monitor_kind.py
   │  │  ├── test_notepad.py
   │  │  ├── test_oneshot_dispatch_failure_run_claim.py
   │  │  ├── test_parallel_pool.py
   │  │  ├── test_persisted_error_rearm_legality.py
   │  │  ├── test_preflight_config.py
   │  │  ├── test_reasoning_config_per_model.py
   │  │  ├── test_recurring_eagain_redispatch.py
   │  │  ├── test_recurring_persisted_error_recovery.py
   │  │  ├── test_recurring_wedge_selfheal.py
   │  │  ├── test_relay_fronted_delivery.py
   │  │  ├── test_rewrite_skill_refs.py
   │  │  ├── test_run_one_job.py
   │  │  ├── test_scheduler.py
   │  │  ├── test_scheduler_cron_session_isolation.py
   │  │  ├── test_scheduler_mcp_init.py
   │  │  ├── test_scheduler_provider.py
   │  │  ├── test_scheduler_shutdown_guard.py
   │  │  ├── test_script_claim_heartbeat.py
   │  │  ├── test_sessiondb_init_hang.py
   │  │  ├── test_shutdown_interrupt.py
   │  │  ├── test_suggestions.py
   │  │  ├── test_terminal_cwd_lock.py
   │  │  ├── test_ticker_stall_60703.py
   │  │  ├── test_usage_audit_logger.py
   │  │  └── __init__.py
   │  ├── dashboard
   │  │  └── test_ws_client_host.py
   │  ├── docker
   │  │  ├── conftest.py
   │  │  ├── test_config_migration.py
   │  │  ├── test_container_restart.py
   │  │  ├── test_dashboard.py
   │  │  ├── test_docker_exec_privilege_drop.py
   │  │  ├── test_dump_build_sha.py
   │  │  ├── test_gateway_bootstrap_state.py
   │  │  ├── test_gateway_run_supervised.py
   │  │  ├── test_home_override_scripts.py
   │  │  ├── test_immutable_install.py
   │  │  ├── test_immutable_install_permissions.py
   │  │  ├── test_license_file_present.py
   │  │  ├── test_log_dir_seed.py
   │  │  ├── test_main_invocation.py
   │  │  ├── test_profile_gateway.py
   │  │  ├── test_puid_pgid_remap.py
   │  │  ├── test_s6_profile_gateway_integration.py
   │  │  ├── test_smoke.py
   │  │  ├── test_sqlite_runtime.py
   │  │  ├── test_stage2_browser_discovery.py
   │  │  ├── test_tini_compat_shim.py
   │  │  ├── test_toplevel_chown.py
   │  │  ├── test_tui_passthrough.py
   │  │  ├── test_tui_prebuilt_bundle.py
   │  │  ├── test_user_flag_guard.py
   │  │  ├── test_zombie_reaping.py
   │  │  └── __init__.py
   │  ├── e2e
   │  │  ├── conftest.py
   │  │  ├── matrix_xsign_bootstrap
   │  │  │  ├── docker-compose.yml
   │  │  │  ├── README.md
   │  │  │  └── test_bootstrap.py
   │  │  ├── test_discord_adapter.py
   │  │  ├── test_platform_commands.py
   │  │  ├── test_relay_native_anthropic_stream.py
   │  │  └── __init__.py
   │  ├── fakes
   │  │  ├── fake_ha_server.py
   │  │  └── __init__.py
   │  ├── fixtures
   │  │  ├── cua_driver_0_9_tools_list.json
   │  │  ├── plugins
   │  │  │  └── example-dashboard
   │  │  │    └── dashboard
   │  │  │       ├── manifest.json
   │  │  │       └── plugin_api.py
   │  │  └── session-resume-active-turn.json
   │  ├── gateway
   │  │  ├── conftest.py
   │  │  ├── feishu_helpers.py
   │  │  ├── platforms
   │  │  │  ├── test_yuanbao_recall_db_only.py
   │  │  │  ├── test_yuanbao_state_cleanup.py
   │  │  │  └── __init__.py
   │  │  ├── relay
   │  │  │  ├── stub_connector.py
   │  │  │  ├── test_auth.py
   │  │  │  ├── test_channel_context_consume.py
   │  │  │  ├── test_contract_doc_conformance.py
   │  │  │  ├── test_descriptor.py
   │  │  │  ├── test_descriptor_from_entry.py
   │  │  │  ├── test_handoff_relay_aliasing.py
   │  │  │  ├── test_identity_token_resolver.py
   │  │  │  ├── test_live_cards_flow_trace.py
   │  │  │  ├── test_no_stub_leak.py
   │  │  │  ├── test_relay_ack_ambiguity.py
   │  │  │  ├── test_relay_adapter.py
   │  │  │  ├── test_relay_follow_up.py
   │  │  │  ├── test_relay_going_idle.py
   │  │  │  ├── test_relay_inbound_dedupe.py
   │  │  │  ├── test_relay_interactive.py
   │  │  │  ├── test_relay_interrupt.py
   │  │  │  ├── test_relay_live_cards.py
   │  │  │  ├── test_relay_media.py
   │  │  │  ├── test_relay_multiplatform.py
   │  │  │  ├── test_relay_multiplatform_semantics.py
   │  │  │  ├── test_relay_passthrough.py
   │  │  │  ├── test_relay_per_platform_caps.py
   │  │  │  ├── test_relay_policy_send.py
   │  │  │  ├── test_relay_registration.py
   │  │  │  ├── test_relay_roundtrip.py
   │  │  │  ├── test_relay_roundtrip_telegram.py
   │  │  │  ├── test_relay_seal_cancellation.py
   │  │  │  ├── test_relay_sheds_crypto.py
   │  │  │  ├── test_relay_slack_dm_streaming.py
   │  │  │  ├── test_relay_slack_prompt_dm_root.py
   │  │  │  ├── test_relay_state_bounds.py
   │  │  │  ├── test_relay_stream_semantics_gating.py
   │  │  │  ├── test_relay_task_card_failures.py
   │  │  │  ├── test_relay_threads.py
   │  │  │  ├── test_relay_turn_keying.py
   │  │  │  ├── test_self_provision.py
   │  │  │  ├── test_wire_user_identity.py
   │  │  │  ├── test_ws_transport.py
   │  │  │  ├── test_ws_transport_hardening.py
   │  │  │  └── __init__.py
   │  │  ├── restart_test_helpers.py
   │  │  ├── test_10710_auto_reset_evicts_cached_agent.py
   │  │  ├── test_13121_shutdown_inflight_transcript_flush.py
   │  │  ├── test_25107_stale_base_url_api_mode.py
   │  │  ├── test_35809_auto_reset_clean_context.py
   │  │  ├── test_35994_reset_button_deadlock.py
   │  │  ├── test_42039_duplicate_user_message.py
   │  │  ├── test_48031_model_switch_after_auto_reset.py
   │  │  ├── test_53175_cleanup_off_loop.py
   │  │  ├── test_64674_multiplex_primary_token_scope.py
   │  │  ├── test_7100_transient_failure_transcript.py
   │  │  ├── test_71671_faulthandler_no_stderr.py
   │  │  ├── test_73297_memory_flush_on_reset.py
   │  │  ├── test_73771_media_resend_dedup.py
   │  │  ├── test_75349_whatsapp_multiplex_secret_scope.py
   │  │  ├── test_abandoned_turn_process_cleanup.py
   │  │  ├── test_active_session_text_merge.py
   │  │  ├── test_active_turn_recovery.py
   │  │  ├── test_adapter_connect_classification.py
   │  │  ├── test_adapter_connect_is_reconnect_contract.py
   │  │  ├── test_adapter_startup_secret_scope.py
   │  │  ├── test_agents_command_delegations.py
   │  │  ├── test_agent_cache.py
   │  │  ├── test_agent_cache_pressure.py
   │  │  ├── test_aiohttp_body_caps.py
   │  │  ├── test_allowed_channels_widening.py
   │  │  ├── test_allowlist_startup_check.py
   │  │  ├── test_api_server.py
   │  │  ├── test_api_server_active_work_drain.py
   │  │  ├── test_api_server_bind_guard.py
   │  │  ├── test_api_server_jobs.py
   │  │  ├── test_api_server_media_data_urls.py
   │  │  ├── test_api_server_multimodal.py
   │  │  ├── test_api_server_multiplex_secret_scope.py
   │  │  ├── test_api_server_normalize.py
   │  │  ├── test_api_server_reasoning_ladder.py
   │  │  ├── test_api_server_runs.py
   │  │  ├── test_api_server_toolset.py
   │  │  ├── test_approvals_command.py
   │  │  ├── test_approval_prompt_redaction.py
   │  │  ├── test_approve_deny_commands.py
   │  │  ├── test_async_delegation_session_binding.py
   │  │  ├── test_async_delivery_capability.py
   │  │  ├── test_async_session_db.py
   │  │  ├── test_async_session_store.py
   │  │  ├── test_audio_cache.py
   │  │  ├── test_auth_fallback.py
   │  │  ├── test_auto_continue.py
   │  │  ├── test_auto_voice_reply_format.py
   │  │  ├── test_background_command.py
   │  │  ├── test_background_process_notifications.py
   │  │  ├── test_baseexception_turn_notify.py
   │  │  ├── test_base_auto_tts_output_format.py
   │  │  ├── test_base_topic_sessions.py
   │  │  ├── test_bluebubbles.py
   │  │  ├── test_bounded_adapter_teardown.py
   │  │  ├── test_branch_routing_columns.py
   │  │  ├── test_bundles_command.py
   │  │  ├── test_busy_session_ack.py
   │  │  ├── test_busy_session_auth_bypass.py
   │  │  ├── test_buzz_adapter.py
   │  │  ├── test_buzz_websocket.py
   │  │  ├── test_cached_agent_history_guard.py
   │  │  ├── test_cached_agent_max_iterations.py
   │  │  ├── test_cancel_background_drain.py
   │  │  ├── test_cgroup_cleanup.py
   │  │  ├── test_channel_continuity_hint.py
   │  │  ├── test_channel_directory.py
   │  │  ├── test_channel_directory_connected_only.py
   │  │  ├── test_channel_overrides.py
   │  │  ├── test_checkpoint_config.py
   │  │  ├── test_choice_picker.py
   │  │  ├── test_cjk_fts_config_bridge.py
   │  │  ├── test_clarify_active_session_bypass.py
   │  │  ├── test_clarify_progress_leak.py
   │  │  ├── test_clarify_thread_followup_not_swallowed.py
   │  │  ├── test_clean_shutdown_marker.py
   │  │  ├── test_code_fence_tracking.py
   │  │  ├── test_command_bypass_active_session.py
   │  │  ├── test_complete_path_at_filter.py
   │  │  ├── test_completion_delivery.py
   │  │  ├── test_completion_session_boundary.py
   │  │  ├── test_compression_concurrent_sessions.py
   │  │  ├── test_compression_deferred_soft_result.py
   │  │  ├── test_compression_failure_session_sync.py
   │  │  ├── test_compression_interrupt_demotion_56391.py
   │  │  ├── test_compression_in_flight_check.py
   │  │  ├── test_compression_progress_notices.py
   │  │  ├── test_compression_session_id_persistence.py
   │  │  ├── test_compress_command.py
   │  │  ├── test_compress_focus.py
   │  │  ├── test_compress_plugin_engine.py
   │  │  ├── test_compress_preview.py
   │  │  ├── test_config.py
   │  │  ├── test_config_cwd_bridge.py
   │  │  ├── test_config_driven_access_policy.py
   │  │  ├── test_config_env_bridge_authority.py
   │  │  ├── test_context_ref_expansion_runtime.py
   │  │  ├── test_conversation_scope_funnel.py
   │  │  ├── test_cron_active_work_drain.py
   │  │  ├── test_cron_drain_floor.py
   │  │  ├── test_cron_fire_webhook.py
   │  │  ├── test_cron_interrupt_notification.py
   │  │  ├── test_cron_shutdown_drain.py
   │  │  ├── test_cwd_placeholder.py
   │  │  ├── test_dead_targets.py
   │  │  ├── test_debug_command.py
   │  │  ├── test_dedupe_user_turns.py
   │  │  ├── test_delegation_session_id_leak.py
   │  │  ├── test_delivery.py
   │  │  ├── test_delivery_ledger.py
   │  │  ├── test_delivery_ledger_fd_leak.py
   │  │  ├── test_delivery_ledger_producer.py
   │  │  ├── test_delivery_silence_filter.py
   │  │  ├── test_destructive_slash_always_persist_report.py
   │  │  ├── test_destructive_slash_confirm.py
   │  │  ├── test_diff_command.py
   │  │  ├── test_dingtalk.py
   │  │  ├── test_discord_allowed_channels.py
   │  │  ├── test_discord_allowed_mentions.py
   │  │  ├── test_discord_approval_mentions.py
   │  │  ├── test_discord_attachment_download.py
   │  │  ├── test_discord_bot_auth_bypass.py
   │  │  ├── test_discord_bot_filter.py
   │  │  ├── test_discord_channel_controls.py
   │  │  ├── test_discord_channel_prompts.py
   │  │  ├── test_discord_channel_skills.py
   │  │  ├── test_discord_clarify_buttons.py
   │  │  ├── test_discord_component_auth.py
   │  │  ├── test_discord_connect.py
   │  │  ├── test_discord_document_handling.py
   │  │  ├── test_discord_double_dispatch.py
   │  │  ├── test_discord_edit_message_overflow.py
   │  │  ├── test_discord_exec_approval_content.py
   │  │  ├── test_discord_fail_closed_feedback.py
   │  │  ├── test_discord_format.py
   │  │  ├── test_discord_free_response.py
   │  │  ├── test_discord_imports.py
   │  │  ├── test_discord_lazy_install_views.py
   │  │  ├── test_discord_liveness.py
   │  │  ├── test_discord_media_metadata.py
   │  │  ├── test_discord_missed_message_backfill.py
   │  │  ├── test_discord_model_picker.py
   │  │  ├── test_discord_opus.py
   │  │  ├── test_discord_pending_text_batch_shutdown.py
   │  │  ├── test_discord_platform_events.py
   │  │  ├── test_discord_plugin_setup.py
   │  │  ├── test_discord_prompt_content_siblings.py
   │  │  ├── test_discord_prompt_timeout_config.py
   │  │  ├── test_discord_race_polish.py
   │  │  ├── test_discord_reactions.py
   │  │  ├── test_discord_reply_mode.py
   │  │  ├── test_discord_roles_dm_scope.py
   │  │  ├── test_discord_send.py
   │  │  ├── test_discord_slash_auth.py
   │  │  ├── test_discord_slash_commands.py
   │  │  ├── test_discord_split_cap.py
   │  │  ├── test_discord_sync_limit.py
   │  │  ├── test_discord_system_messages.py
   │  │  ├── test_discord_thread_persistence.py
   │  │  ├── test_discord_thread_slash_expired_defer.py
   │  │  ├── test_discord_voice_mixer.py
   │  │  ├── test_disk_status.py
   │  │  ├── test_display_config.py
   │  │  ├── test_dm_topics.py
   │  │  ├── test_document_cache.py
   │  │  ├── test_document_context_note.py
   │  │  ├── test_draft_id_restart_uniqueness.py
   │  │  ├── test_duplicate_reply_suppression.py
   │  │  ├── test_email.py
   │  │  ├── test_email_charset_fallback.py
   │  │  ├── test_email_robustness.py
   │  │  ├── test_email_secret_scope.py
   │  │  ├── test_empty_model_recovery.py
   │  │  ├── test_env_flag_truthy.py
   │  │  ├── test_ephemeral_reply.py
   │  │  ├── test_escape_reasoning_fences.py
   │  │  ├── test_external_drain_control.py
   │  │  ├── test_extract_local_files.py
   │  │  ├── test_fallback_chain_reload.py
   │  │  ├── test_fallback_eviction.py
   │  │  ├── test_fast_command.py
   │  │  ├── test_feishu.py
   │  │  ├── test_feishu_approval_buttons.py
   │  │  ├── test_feishu_bot_admission.py
   │  │  ├── test_feishu_bot_auth_bypass.py
   │  │  ├── test_feishu_channel_prompts.py
   │  │  ├── test_feishu_comment.py
   │  │  ├── test_feishu_comment_rules.py
   │  │  ├── test_feishu_lazy_import.py
   │  │  ├── test_feishu_meeting_invite.py
   │  │  ├── test_feishu_onboard.py
   │  │  ├── test_feishu_sdk_executor.py
   │  │  ├── test_feishu_table_markdown.py
   │  │  ├── test_feishu_voice_message_type.py
   │  │  ├── test_fence_chunker.py
   │  │  ├── test_finalize_session_off_loop.py
   │  │  ├── test_first_turn_session_meta_rebaseline.py
   │  │  ├── test_footer_command_mid_run.py
   │  │  ├── test_fresh_reset_skill_injection.py
   │  │  ├── test_gateway_command_dispatch_minimal.py
   │  │  ├── test_gateway_command_help.py
   │  │  ├── test_gateway_command_line_matcher.py
   │  │  ├── test_gateway_inactivity_timeout.py
   │  │  ├── test_gateway_platform_event_hook.py
   │  │  ├── test_gateway_process_exit.py
   │  │  ├── test_gateway_shutdown.py
   │  │  ├── test_gateway_silence_tokens.py
   │  │  ├── test_gateway_utf8_encoding.py
   │  │  ├── test_goal_continuation_drain.py
   │  │  ├── test_goal_max_turns_config.py
   │  │  ├── test_goal_resume_restart.py
   │  │  ├── test_goal_status_notice.py
   │  │  ├── test_goal_verdict_send.py
   │  │  ├── test_google_chat.py
   │  │  ├── test_google_chat_oauth_dependencies.py
   │  │  ├── test_handoff_thread_session_key.py
   │  │  ├── test_handoff_watcher_async_db.py
   │  │  ├── test_history_media_current_turn.py
   │  │  ├── test_homeassistant.py
   │  │  ├── test_home_target_env_var.py
   │  │  ├── test_hooks.py
   │  │  ├── test_hygiene_failure_cooldown_ladder.py
   │  │  ├── test_image_input_routing_runtime.py
   │  │  ├── test_incomplete_gateway_turns.py
   │  │  ├── test_insights_unicode_flags.py
   │  │  ├── test_interactive_prompt_base.py
   │  │  ├── test_interim_send_lanes.py
   │  │  ├── test_internal_event_bypass_pairing.py
   │  │  ├── test_internal_event_never_interrupts_busy_session.py
   │  │  ├── test_internal_notification_marker_82888.py
   │  │  ├── test_interrupt_key_match.py
   │  │  ├── test_irc_adapter.py
   │  │  ├── test_kanban_auto_decompose_live.py
   │  │  ├── test_kanban_notifier.py
   │  │  ├── test_kanban_notifier_apiserver_wake.py
   │  │  ├── test_kanban_notifier_wake_only_ordering.py
   │  │  ├── test_kanban_notifier_watcher_dispatch_gate.py
   │  │  ├── test_kanban_notifier_zero_sub_gate.py
   │  │  ├── test_kanban_reconcile_orphans.py
   │  │  ├── test_kanban_wake_scope.py
   │  │  ├── test_kanban_watchers_mixin.py
   │  │  ├── test_keep_typing_timeout.py
   │  │  ├── test_lifecycle_ledger.py
   │  │  ├── test_line_plugin.py
   │  │  ├── test_load_transcript_db_only.py
   │  │  ├── test_local_model_connection_reply.py
   │  │  ├── test_loop_command.py
   │  │  ├── test_loop_exception_handler.py
   │  │  ├── test_loop_liveness_watchdog.py
   │  │  ├── test_matrix.py
   │  │  ├── test_matrix_approval_reaction_fail_closed.py
   │  │  ├── test_matrix_dm_invite_recording.py
   │  │  ├── test_matrix_exec_approval.py
   │  │  ├── test_matrix_media_filename.py
   │  │  ├── test_matrix_mention.py
   │  │  ├── test_matrix_message_event_metadata.py
   │  │  ├── test_matrix_message_length.py
   │  │  ├── test_matrix_plugin_setup.py
   │  │  ├── test_matrix_project_context_isolation.py
   │  │  ├── test_matrix_recovery_key_scope.py
   │  │  ├── test_matrix_voice.py
   │  │  ├── test_mattermost.py
   │  │  ├── test_mattermost_plugin_setup.py
   │  │  ├── test_max_concurrent_sessions.py
   │  │  ├── test_max_tokens_propagation.py
   │  │  ├── test_mcp_reload_refreshes_cached_agents.py
   │  │  ├── test_media_cache.py
   │  │  ├── test_media_download_retry.py
   │  │  ├── test_media_extraction.py
   │  │  ├── test_media_metadata_contract.py
   │  │  ├── test_media_spaced_paths_and_history_dedupe.py
   │  │  ├── test_media_tag_cleanup.py
   │  │  ├── test_media_tag_formatting_variants.py
   │  │  ├── test_media_tag_separator.py
   │  │  ├── test_memory_monitor.py
   │  │  ├── test_memory_status.py
   │  │  ├── test_memory_trim_housekeeping.py
   │  │  ├── test_message_deduplicator.py
   │  │  ├── test_message_timestamps.py
   │  │  ├── test_mirror.py
   │  │  ├── test_mixed_attachment_routing.py
   │  │  ├── test_moa_one_shot_restore.py
   │  │  ├── test_model_command_async_offload.py
   │  │  ├── test_model_command_context_offload.py
   │  │  ├── test_model_command_custom_providers.py
   │  │  ├── test_model_command_expensive_confirm.py
   │  │  ├── test_model_command_flat_string_config.py
   │  │  ├── test_model_command_profile_config.py
   │  │  ├── test_model_picker_persist.py
   │  │  ├── test_model_switch_persistence.py
   │  │  ├── test_msgraph_webhook.py
   │  │  ├── test_multiplex_adapter_registry.py
   │  │  ├── test_multiplex_adapter_session_key_namespace.py
   │  │  ├── test_multiplex_api_server_routing.py
   │  │  ├── test_multiplex_background_task_scope.py
   │  │  ├── test_multiplex_busy_input_mode.py
   │  │  ├── test_multiplex_credential_isolation.py
   │  │  ├── test_multiplex_http_routing.py
   │  │  ├── test_multiplex_lifecycle.py
   │  │  ├── test_multiplex_pairing_stores.py
   │  │  ├── test_multiplex_phase0.py
   │  │  ├── test_multiplex_profile_authz.py
   │  │  ├── test_multiplex_session_db_profile_scope.py
   │  │  ├── test_native_image_buffer_isolation.py
   │  │  ├── test_new_clears_last_resolved_model.py
   │  │  ├── test_normalize_empty_agent_response.py
   │  │  ├── test_notice_delivery.py
   │  │  ├── test_notice_rendering.py
   │  │  ├── test_notify_fatal_error_shield.py
   │  │  ├── test_ntfy_plugin.py
   │  │  ├── test_own_policy_startup_gate.py
   │  │  ├── test_pairing.py
   │  │  ├── test_pairing_allowlist_bypass.py
   │  │  ├── test_pending_drain_no_recursion.py
   │  │  ├── test_pending_drain_race.py
   │  │  ├── test_pending_event_none.py
   │  │  ├── test_pending_queue_spool.py
   │  │  ├── test_per_platform_streaming_defaults.py
   │  │  ├── test_pii_redaction.py
   │  │  ├── test_plaintext_approval_routing.py
   │  │  ├── test_planned_stop_watcher.py
   │  │  ├── test_platform_base.py
   │  │  ├── test_platform_connected_checkers.py
   │  │  ├── test_platform_http_client_limits.py
   │  │  ├── test_platform_reconnect.py
   │  │  ├── test_platform_reconnect_fd_leak.py
   │  │  ├── test_platform_registry.py
   │  │  ├── test_plugin_message_injection.py
   │  │  ├── test_plugin_platform_interface.py
   │  │  ├── test_poller_fd_lifecycle.py
   │  │  ├── test_post_delivery_callback_chaining.py
   │  │  ├── test_post_stream_media_delivery.py
   │  │  ├── test_pre_gateway_dispatch.py
   │  │  ├── test_priority_path_compression_demotion_56391.py
   │  │  ├── test_profile_resolution.py
   │  │  ├── test_profile_routing.py
   │  │  ├── test_prompt_tail_freeze.py
   │  │  ├── test_proxy_mode.py
   │  │  ├── test_qqbot.py
   │  │  ├── test_qqbot_credential_isolation.py
   │  │  ├── test_qqbot_scope_paths.py
   │  │  ├── test_queued_native_image_session_key.py
   │  │  ├── test_queue_command.py
   │  │  ├── test_queue_consumption.py
   │  │  ├── test_raft_adapter.py
   │  │  ├── test_readiness.py
   │  │  ├── test_reasoning_command.py
   │  │  ├── test_reasoning_config_per_model.py
   │  │  ├── test_relay_capability_surface.py
   │  │  ├── test_relay_completion_injection_routing.py
   │  │  ├── test_relay_delivery_followups.py
   │  │  ├── test_relay_final_delivery_incident.py
   │  │  ├── test_relay_injection_egress_priming.py
   │  │  ├── test_relay_seal_failure.py
   │  │  ├── test_relay_teardown_drain.py
   │  │  ├── test_relay_upstream_authz.py
   │  │  ├── test_reload_skills_command.py
   │  │  ├── test_reload_skills_discord_resync.py
   │  │  ├── test_replace_child_reap.py
   │  │  ├── test_replay_entry_fields.py
   │  │  ├── test_reply_to_injection.py
   │  │  ├── test_response_filters.py
   │  │  ├── test_restart_after_turn.py
   │  │  ├── test_restart_drain.py
   │  │  ├── test_restart_notification.py
   │  │  ├── test_restart_redelivery_dedup.py
   │  │  ├── test_restart_resume_pending.py
   │  │  ├── test_restart_service_detection.py
   │  │  ├── test_resume_command.py
   │  │  ├── test_retry_replacement.py
   │  │  ├── test_retry_response.py
   │  │  ├── test_routing_save_fast_path.py
   │  │  ├── test_runner_fatal_adapter.py
   │  │  ├── test_runner_startup_failures.py
   │  │  ├── test_running_agent_session_toggles.py
   │  │  ├── test_runtime_config_env_expansion.py
   │  │  ├── test_runtime_env_reload_config_authority.py
   │  │  ├── test_runtime_footer.py
   │  │  ├── test_run_cleanup_progress.py
   │  │  ├── test_run_progress_interrupt.py
   │  │  ├── test_run_progress_topics.py
   │  │  ├── test_run_tool_media_re.py
   │  │  ├── test_safe_adapter_disconnect.py
   │  │  ├── test_scale_to_zero.py
   │  │  ├── test_scale_to_zero_watcher.py
   │  │  ├── test_send_error_classification.py
   │  │  ├── test_send_image_file.py
   │  │  ├── test_send_multiple_images.py
   │  │  ├── test_send_retry.py
   │  │  ├── test_send_voice_reply_notify.py
   │  │  ├── test_session.py
   │  │  ├── test_session_api.py
   │  │  ├── test_session_boundary_hooks.py
   │  │  ├── test_session_boundary_security_state.py
   │  │  ├── test_session_context_inheritance.py
   │  │  ├── test_session_continuity_82616.py
   │  │  ├── test_session_dm_thread_seeding.py
   │  │  ├── test_session_env.py
   │  │  ├── test_session_hygiene.py
   │  │  ├── test_session_id_cache_coherence.py
   │  │  ├── test_session_info.py
   │  │  ├── test_session_list_allowed_sources.py
   │  │  ├── test_session_load_bool.py
   │  │  ├── test_session_messages_shutdown_preserve.py
   │  │  ├── test_session_model_override_credential_pool.py
   │  │  ├── test_session_model_override_persistence.py
   │  │  ├── test_session_model_override_routing.py
   │  │  ├── test_session_model_reset.py
   │  │  ├── test_session_override_thread_recovery.py
   │  │  ├── test_session_race_guard.py
   │  │  ├── test_session_reset_notify.py
   │  │  ├── test_session_split_brain_11016.py
   │  │  ├── test_session_stall_watchdog.py
   │  │  ├── test_session_state_cleanup.py
   │  │  ├── test_session_store_expiry_finalized.py
   │  │  ├── test_session_store_lock_io.py
   │  │  ├── test_session_store_prune.py
   │  │  ├── test_session_store_runtime_stale_guard.py
   │  │  ├── test_session_store_stale_prune.py
   │  │  ├── test_session_title_rename_lane.py
   │  │  ├── test_sethome_synthetic_thread.py
   │  │  ├── test_setup_feishu.py
   │  │  ├── test_shared_group_sender_prefix.py
   │  │  ├── test_shutdown_cache_cleanup.py
   │  │  ├── test_shutdown_flush.py
   │  │  ├── test_shutdown_forensics.py
   │  │  ├── test_shutdown_memory_provider_messages.py
   │  │  ├── test_shutdown_watchdog.py
   │  │  ├── test_signal.py
   │  │  ├── test_signal_format.py
   │  │  ├── test_signal_rate_limit.py
   │  │  ├── test_simplex_plugin.py
   │  │  ├── test_skip_context_files_wiring.py
   │  │  ├── test_slack.py
   │  │  ├── test_slack_approval_buttons.py
   │  │  ├── test_slack_block_kit.py
   │  │  ├── test_slack_block_kit_adapter.py
   │  │  ├── test_slack_bot_auth_bypass.py
   │  │  ├── test_slack_channel_session_scope.py
   │  │  ├── test_slack_channel_skills.py
   │  │  ├── test_slack_clarify_buttons.py
   │  │  ├── test_slack_cron_continuable_surface.py
   │  │  ├── test_slack_dedup_ttl.py
   │  │  ├── test_slack_download_ssrf.py
   │  │  ├── test_slack_group_dm_scope_warning.py
   │  │  ├── test_slack_ignore_other_user_mentions.py
   │  │  ├── test_slack_log_noise.py
   │  │  ├── test_slack_mention.py
   │  │  ├── test_slack_mention_humanization.py
   │  │  ├── test_slack_native_streaming.py
   │  │  ├── test_slack_peer_agent_smoke.py
   │  │  ├── test_slack_plugin_action_handlers.py
   │  │  ├── test_slack_plugin_setup.py
   │  │  ├── test_slack_relay_parent_command.py
   │  │  ├── test_slack_require_mention_channels.py
   │  │  ├── test_slack_runner_ignored_channels.py
   │  │  ├── test_slack_sdk_response.py
   │  │  ├── test_slack_send_retry.py
   │  │  ├── test_slack_socket_reconnect_heal.py
   │  │  ├── test_slack_status_update.py
   │  │  ├── test_slack_turn_recipient_identity.py
   │  │  ├── test_slack_user_token_warning.py
   │  │  ├── test_slack_wake_external_bot_messages.py
   │  │  ├── test_slash_access.py
   │  │  ├── test_slash_access_dispatch.py
   │  │  ├── test_sms.py
   │  │  ├── test_split_final_suffix_reconcile.py
   │  │  ├── test_sse_agent_cancel.py
   │  │  ├── test_sse_frame.py
   │  │  ├── test_ssl_certs.py
   │  │  ├── test_ssl_cert_detection.py
   │  │  ├── test_stacked_skill_platform_disabled.py
   │  │  ├── test_stale_confirmation_expiry.py
   │  │  ├── test_stale_finalize_suppression.py
   │  │  ├── test_stale_platform_lock_retryable.py
   │  │  ├── test_stale_self_heal_agent_cache_eviction.py
   │  │  ├── test_startup_connect_parallel.py
   │  │  ├── test_startup_no_eager_platform_install.py
   │  │  ├── test_startup_restart_race.py
   │  │  ├── test_status.py
   │  │  ├── test_status_command.py
   │  │  ├── test_status_phrases.py
   │  │  ├── test_stderr_formatting.py
   │  │  ├── test_steer_command.py
   │  │  ├── test_steer_fifo_overwrite.py
   │  │  ├── test_step_callback_compat.py
   │  │  ├── test_sticker_cache.py
   │  │  ├── test_stop_thread_sibling.py
   │  │  ├── test_streaming_tts_consumer.py
   │  │  ├── test_streaming_tts_gateway_regression.py
   │  │  ├── test_stream_abandon_on_turn_death.py
   │  │  ├── test_stream_consumer.py
   │  │  ├── test_stream_consumer_draft.py
   │  │  ├── test_stream_consumer_fresh_final.py
   │  │  ├── test_stream_consumer_silence.py
   │  │  ├── test_stream_consumer_thread_routing.py
   │  │  ├── test_stream_events.py
   │  │  ├── test_stream_final_adoption_gate.py
   │  │  ├── test_stream_final_contract.py
   │  │  ├── test_stt_config.py
   │  │  ├── test_stt_transcript_echo_config.py
   │  │  ├── test_stuck_loop.py
   │  │  ├── test_subagent_protection_30170.py
   │  │  ├── test_suppression_contract_matrix.py
   │  │  ├── test_systemd_notify.py
   │  │  ├── test_systemd_watchdog_lifecycle.py
   │  │  ├── test_table_helpers.py
   │  │  ├── test_teams.py
   │  │  ├── test_teams_dotenv_isolation.py
   │  │  ├── test_teams_pipeline_runtime_wiring.py
   │  │  ├── test_telegram_approval_buttons.py
   │  │  ├── test_telegram_audio_vs_voice.py
   │  │  ├── test_telegram_auth_check.py
   │  │  ├── test_telegram_bot_auth_bypass.py
   │  │  ├── test_telegram_callback_auth_fail_closed.py
   │  │  ├── test_telegram_caption_merge.py
   │  │  ├── test_telegram_channel_posts.py
   │  │  ├── test_telegram_clarify_buttons.py
   │  │  ├── test_telegram_closewait_limits_31599.py
   │  │  ├── test_telegram_conflict.py
   │  │  ├── test_telegram_connect.py
   │  │  ├── test_telegram_documents.py
   │  │  ├── test_telegram_error_redaction.py
   │  │  ├── test_telegram_fallback_pool_release_71593.py
   │  │  ├── test_telegram_final_delivery.py
   │  │  ├── test_telegram_format.py
   │  │  ├── test_telegram_forum_commands.py
   │  │  ├── test_telegram_group_gating.py
   │  │  ├── test_telegram_init_deadline.py
   │  │  ├── test_telegram_lazy_install_typehandler.py
   │  │  ├── test_telegram_long_command_batching.py
   │  │  ├── test_telegram_max_doc_bytes.py
   │  │  ├── test_telegram_media_read_timeout.py
   │  │  ├── test_telegram_mention_boundaries.py
   │  │  ├── test_telegram_model_picker.py
   │  │  ├── test_telegram_network.py
   │  │  ├── test_telegram_network_reconnect.py
   │  │  ├── test_telegram_noise_filter.py
   │  │  ├── test_telegram_overflow_partial.py
   │  │  ├── test_telegram_pending_update_probe.py
   │  │  ├── test_telegram_photo_interrupts.py
   │  │  ├── test_telegram_polling_health_confirmation.py
   │  │  ├── test_telegram_polling_progress.py
   │  │  ├── test_telegram_progress_edit_transient.py
   │  │  ├── test_telegram_prune_stale_topic_binding_31501.py
   │  │  ├── test_telegram_reactions.py
   │  │  ├── test_telegram_reply_mode.py
   │  │  ├── test_telegram_reply_quote.py
   │  │  ├── test_telegram_rich_messages.py
   │  │  ├── test_telegram_rich_newlines.py
   │  │  ├── test_telegram_send_draft_format.py
   │  │  ├── test_telegram_send_path_health.py
   │  │  ├── test_telegram_slash_confirm.py
   │  │  ├── test_telegram_start_polling_timeout.py
   │  │  ├── test_telegram_status_indicator.py
   │  │  ├── test_telegram_status_update.py
   │  │  ├── test_telegram_text_batching.py
   │  │  ├── test_telegram_text_batch_perf.py
   │  │  ├── test_telegram_thread_fallback.py
   │  │  ├── test_telegram_topic_mode.py
   │  │  ├── test_telegram_typing_backoff.py
   │  │  ├── test_telegram_username_chat_id.py
   │  │  ├── test_telegram_voice_caption_markdown.py
   │  │  ├── test_telegram_voice_duration.py
   │  │  ├── test_telegram_voice_v0_regressions.py
   │  │  ├── test_telegram_webhook_secret.py
   │  │  ├── test_text_batching.py
   │  │  ├── test_title_command.py
   │  │  ├── test_tool_log_mode.py
   │  │  ├── test_tool_response_drop_recovery.py
   │  │  ├── test_transcript_offset.py
   │  │  ├── test_tts_media_routing.py
   │  │  ├── test_tui_approval_redaction.py
   │  │  ├── test_tui_slash_worker_path.py
   │  │  ├── test_turn_context.py
   │  │  ├── test_turn_lease.py
   │  │  ├── test_typing_indicator_toggle.py
   │  │  ├── test_unauthorized_dm_behavior.py
   │  │  ├── test_unavailable_skill_hint.py
   │  │  ├── test_undo_rewind_session.py
   │  │  ├── test_unknown_command.py
   │  │  ├── test_update_command.py
   │  │  ├── test_update_cron_drain.py
   │  │  ├── test_update_streaming.py
   │  │  ├── test_usage_command.py
   │  │  ├── test_verbose_command.py
   │  │  ├── test_version_command.py
   │  │  ├── test_video_context_note.py
   │  │  ├── test_vision_memory_leak.py
   │  │  ├── test_vision_preprocess.py
   │  │  ├── test_voice_command.py
   │  │  ├── test_voice_mode_platform_isolation.py
   │  │  ├── test_wake_delivery.py
   │  │  ├── test_watchdog_review_76354.py
   │  │  ├── test_weak_credential_guard.py
   │  │  ├── test_webhook_adapter.py
   │  │  ├── test_webhook_deliver_only.py
   │  │  ├── test_webhook_dynamic_routes.py
   │  │  ├── test_webhook_integration.py
   │  │  ├── test_webhook_route_toolsets.py
   │  │  ├── test_webhook_session_close.py
   │  │  ├── test_webhook_signature_rate_limit.py
   │  │  ├── test_wecom.py
   │  │  ├── test_wecom_callback.py
   │  │  ├── test_wecom_plugin_setup.py
   │  │  ├── test_weixin.py
   │  │  ├── test_weixin_secret_scope.py
   │  │  ├── test_weixin_typing.py
   │  │  ├── test_whatsapp_allowlist_lid_resolution.py
   │  │  ├── test_whatsapp_bridge_dir_resolution.py
   │  │  ├── test_whatsapp_bridge_pidfile.py
   │  │  ├── test_whatsapp_cloud.py
   │  │  ├── test_whatsapp_cloud_allowed_users.py
   │  │  ├── test_whatsapp_connect.py
   │  │  ├── test_whatsapp_formatting.py
   │  │  ├── test_whatsapp_from_owner.py
   │  │  ├── test_whatsapp_group_gating.py
   │  │  ├── test_whatsapp_identity.py
   │  │  ├── test_whatsapp_media_path_profile.py
   │  │  ├── test_whatsapp_native_delivery.py
   │  │  ├── test_whatsapp_plugin_setup.py
   │  │  ├── test_whatsapp_reply_prefix.py
   │  │  ├── test_whatsapp_stale_bridge.py
   │  │  ├── test_whatsapp_text_batching.py
   │  │  ├── test_whatsapp_to_jid.py
   │  │  ├── test_ws_auth_retry.py
   │  │  ├── test_ws_auth_retry_verifier_probe.py
   │  │  ├── test_yolo_command.py
   │  │  ├── test_yuanbao_forwarded_heartbeat.py
   │  │  ├── test_yuanbao_media_ssrf.py
   │  │  ├── _plugin_adapter_loader.py
   │  │  └── __init__.py
   │  ├── jimmy_cli
   │  │  ├── conftest.py
   │  │  ├── conftest_dashboard_auth.py
   │  │  ├── fixtures
   │  │  │  └── plugin_compat_legacy
   │  │  │    ├── plugin.yaml
   │  │  │    └── __init__.py
   │  │  ├── test_25106_global_switch_persists_base_url_api_mode.py
   │  │  ├── test_active_sessions.py
   │  │  ├── test_actual_provider.py
   │  │  ├── test_agent_env_advertisement.py
   │  │  ├── test_agent_import.py
   │  │  ├── test_agent_plugins.py
   │  │  ├── test_ai_gateway_models.py
   │  │  ├── test_anthropic_model_flow_stale_oauth.py
   │  │  ├── test_anthropic_oauth_flow.py
   │  │  ├── test_anthropic_oauth_routes_to_messages_api.py
   │  │  ├── test_anthropic_picker_curated.py
   │  │  ├── test_anthropic_provider_persistence.py
   │  │  ├── test_api_key_providers.py
   │  │  ├── test_api_mode_aliases.py
   │  │  ├── test_apply_model_switch_result_context.py
   │  │  ├── test_apply_profile_override.py
   │  │  ├── test_approvals_command.py
   │  │  ├── test_approvals_suggest.py
   │  │  ├── test_approvals_test.py
   │  │  ├── test_approval_transport.py
   │  │  ├── test_arcee_provider.py
   │  │  ├── test_argparse_flag_propagation.py
   │  │  ├── test_atomic_json_write.py
   │  │  ├── test_atomic_yaml_write.py
   │  │  ├── test_at_context_completion_filter.py
   │  │  ├── test_authenticated_providers_exhausted_pool.py
   │  │  ├── test_auth_codex_provider.py
   │  │  ├── test_auth_codex_quota_probe.py
   │  │  ├── test_auth_codex_self_heal.py
   │  │  ├── test_auth_commands.py
   │  │  ├── test_auth_loopback_ssh_hint.py
   │  │  ├── test_auth_nous_provider.py
   │  │  ├── test_auth_profile_fallback.py
   │  │  ├── test_auth_provider_gate.py
   │  │  ├── test_auth_provider_scope.py
   │  │  ├── test_auth_qwen_provider.py
   │  │  ├── test_auth_ssl_macos.py
   │  │  ├── test_auth_store_read_failure.py
   │  │  ├── test_auth_store_windows_encoding.py
   │  │  ├── test_auth_toctou_file_modes.py
   │  │  ├── test_auth_usable_secret.py
   │  │  ├── test_auth_xai_oauth_provider.py
   │  │  ├── test_aux_config.py
   │  │  ├── test_aux_picker_inventory.py
   │  │  ├── test_azure_detect.py
   │  │  ├── test_azure_foundry_entra.py
   │  │  ├── test_backup.py
   │  │  ├── test_backup_path_errors.py
   │  │  ├── test_backup_stability.py
   │  │  ├── test_banner.py
   │  │  ├── test_banner_git_state.py
   │  │  ├── test_banner_skills.py
   │  │  ├── test_banner_skills_width.py
   │  │  ├── test_base_url_host_identity.py
   │  │  ├── test_bedrock_mantle_key_env.py
   │  │  ├── test_bedrock_model_picker.py
   │  │  ├── test_bedrock_region_scoped_picker.py
   │  │  ├── test_billing_cli.py
   │  │  ├── test_billing_portal_url.py
   │  │  ├── test_billing_scope_stepup.py
   │  │  ├── test_bitwarden_status.py
   │  │  ├── test_bounded_probe_run.py
   │  │  ├── test_browser_connect_dual_stack.py
   │  │  ├── test_build_info.py
   │  │  ├── test_bundles.py
   │  │  ├── test_busy_policy_invariants.py
   │  │  ├── test_bytecode_sweep.py
   │  │  ├── test_cached_fetch_api_models.py
   │  │  ├── test_canonical_custom_identity.py
   │  │  ├── test_certifi_repair.py
   │  │  ├── test_chat_c_fail_loudly.py
   │  │  ├── test_chat_query_file.py
   │  │  ├── test_chat_skills_flag.py
   │  │  ├── test_checkout_mutation_guards.py
   │  │  ├── test_checkpoints_prune.py
   │  │  ├── test_claw.py
   │  │  ├── test_clear_stale_base_url.py
   │  │  ├── test_clipboard_text_write.py
   │  │  ├── test_cli_active_session_limit.py
   │  │  ├── test_cli_custom_provider_vision.py
   │  │  ├── test_cli_model_once.py
   │  │  ├── test_cli_output.py
   │  │  ├── test_cli_startup_model_cost_guard.py
   │  │  ├── test_cmd_update.py
   │  │  ├── test_cmd_update_apt.py
   │  │  ├── test_cmd_update_docker.py
   │  │  ├── test_coalesce_session_args.py
   │  │  ├── test_codex_cli_model_picker.py
   │  │  ├── test_codex_models.py
   │  │  ├── test_codex_runtime_plugin_migration.py
   │  │  ├── test_codex_runtime_switch.py
   │  │  ├── test_commands.py
   │  │  ├── test_commands_execute.py
   │  │  ├── test_completer_config_reads.py
   │  │  ├── test_completion.py
   │  │  ├── test_composer_placeholder.py
   │  │  ├── test_computer_use_cli.py
   │  │  ├── test_config.py
   │  │  ├── test_configured_builtin_models.py
   │  │  ├── test_config_env_expansion.py
   │  │  ├── test_config_env_refs.py
   │  │  ├── test_config_env_ref_parity.py
   │  │  ├── test_config_loader_e2e.py
   │  │  ├── test_config_read_guard.py
   │  │  ├── test_config_set_coercion.py
   │  │  ├── test_config_set_list_values.py
   │  │  ├── test_config_validation.py
   │  │  ├── test_console_engine.py
   │  │  ├── test_container_aware_cli.py
   │  │  ├── test_container_boot.py
   │  │  ├── test_context_switch_guard.py
   │  │  ├── test_copilot_auth.py
   │  │  ├── test_copilot_catalog_oauth_fallback.py
   │  │  ├── test_copilot_context.py
   │  │  ├── test_copilot_in_model_list.py
   │  │  ├── test_copilot_model_api_mode.py
   │  │  ├── test_copilot_runtime_api_mode.py
   │  │  ├── test_copilot_token_exchange.py
   │  │  ├── test_credential_lifecycle.py
   │  │  ├── test_cron.py
   │  │  ├── test_cron_dashboard_off_loop.py
   │  │  ├── test_cron_fire_dashboard.py
   │  │  ├── test_cron_model_impact.py
   │  │  ├── test_cron_parser_builder.py
   │  │  ├── test_cron_profile_enumeration_lightweight.py
   │  │  ├── test_ctrlg_editor_submit.py
   │  │  ├── test_curator_archive_prune.py
   │  │  ├── test_curator_recent_run_notice.py
   │  │  ├── test_curator_run.py
   │  │  ├── test_curator_status.py
   │  │  ├── test_curator_usage.py
   │  │  ├── test_curses_arrow_keys.py
   │  │  ├── test_curses_color_compat.py
   │  │  ├── test_curses_ui_fuzzy_rank.py
   │  │  ├── test_curses_ui_search.py
   │  │  ├── test_custom_provider_context_length.py
   │  │  ├── test_custom_provider_extra_headers.py
   │  │  ├── test_custom_provider_identity.py
   │  │  ├── test_custom_provider_model_switch.py
   │  │  ├── test_custom_provider_normalize_no_mutate.py
   │  │  ├── test_custom_provider_tls.py
   │  │  ├── test_dashboard_admin_endpoints.py
   │  │  ├── test_dashboard_auth_401_reauth.py
   │  │  ├── test_dashboard_auth_audit.py
   │  │  ├── test_dashboard_auth_cookies.py
   │  │  ├── test_dashboard_auth_gate.py
   │  │  ├── test_dashboard_auth_middleware.py
   │  │  ├── test_dashboard_auth_native_flow.py
   │  │  ├── test_dashboard_auth_password_login.py
   │  │  ├── test_dashboard_auth_plugin_hook.py
   │  │  ├── test_dashboard_auth_prefix.py
   │  │  ├── test_dashboard_auth_provider_base.py
   │  │  ├── test_dashboard_auth_status_endpoint.py
   │  │  ├── test_dashboard_auth_stub_provider.py
   │  │  ├── test_dashboard_auth_ws_auth.py
   │  │  ├── test_dashboard_auth_ws_tickets.py
   │  │  ├── test_dashboard_basic_auth_plugin_enable.py
   │  │  ├── test_dashboard_browser_safe_imports.py
   │  │  ├── test_dashboard_lifecycle_flags.py
   │  │  ├── test_dashboard_oauth_endpoints_server_gate.py
   │  │  ├── test_dashboard_param_clamps.py
   │  │  ├── test_dashboard_profiles_nav_label.py
   │  │  ├── test_dashboard_register.py
   │  │  ├── test_dashboard_token_auth.py
   │  │  ├── test_dashboard_tui_backcompat.py
   │  │  ├── test_dashboard_unified_launch.py
   │  │  ├── test_dashboard_web_dist_validation.py
   │  │  ├── test_debug.py
   │  │  ├── test_default_interface_resolution.py
   │  │  ├── test_deferred_platform_client_tools.py
   │  │  ├── test_deprecated_cwd_warning.py
   │  │  ├── test_dep_ensure.py
   │  │  ├── test_desktop_exe_integrity.py
   │  │  ├── test_desktop_repo_discovery_config.py
   │  │  ├── test_destructive_slash_confirm_gate.py
   │  │  ├── test_detect_api_mode_for_url.py
   │  │  ├── test_determine_api_mode_hostname.py
   │  │  ├── test_diagnostics_upload.py
   │  │  ├── test_diff_command.py
   │  │  ├── test_dingtalk_auth.py
   │  │  ├── test_discord_skill_clamp_warning.py
   │  │  ├── test_doctor.py
   │  │  ├── test_doctor_command_install.py
   │  │  ├── test_doctor_dedicated_provider_skip.py
   │  │  ├── test_doctor_journal_modes.py
   │  │  ├── test_doctor_live.py
   │  │  ├── test_dump_env_visibility.py
   │  │  ├── test_dump_git_commit.py
   │  │  ├── test_dump_terminal_backend.py
   │  │  ├── test_early_recovery.py
   │  │  ├── test_ensure_acp_launcher.py
   │  │  ├── test_ensure_gateway_service.py
   │  │  ├── test_ensure_jimmy_home_memo.py
   │  │  ├── test_ensure_jimmy_home_uid_34107.py
   │  │  ├── test_ensure_utf8_locale.py
   │  │  ├── test_env_custom_keys.py
   │  │  ├── test_env_export_line_lifecycle.py
   │  │  ├── test_env_export_prefix.py
   │  │  ├── test_env_loader.py
   │  │  ├── test_env_load_cache.py
   │  │  ├── test_env_sanitize_on_load.py
   │  │  ├── test_fallback_cmd.py
   │  │  ├── test_fallback_config.py
   │  │  ├── test_fireworks_provider.py
   │  │  ├── test_foreign_sessions.py
   │  │  ├── test_gateway.py
   │  │  ├── test_gateway_external_supervisor.py
   │  │  ├── test_gateway_foreign_xdg_runtime.py
   │  │  ├── test_gateway_linger.py
   │  │  ├── test_gateway_platform_gating.py
   │  │  ├── test_gateway_proc_fallback.py
   │  │  ├── test_gateway_restart_loop.py
   │  │  ├── test_gateway_runtime_health.py
   │  │  ├── test_gateway_run_hard_exit.py
   │  │  ├── test_gateway_s6_dispatch.py
   │  │  ├── test_gateway_service.py
   │  │  ├── test_gateway_service_paths.py
   │  │  ├── test_gateway_windows.py
   │  │  ├── test_gateway_wsl.py
   │  │  ├── test_gemini_free_tier_setup_block.py
   │  │  ├── test_gemini_provider.py
   │  │  ├── test_get_env_value_scope.py
   │  │  ├── test_git_probe_tree_kill.py
   │  │  ├── test_global_auth_store_memo.py
   │  │  ├── test_gmi_provider.py
   │  │  ├── test_goals.py
   │  │  ├── test_goals_db_bootstrap_off_loop.py
   │  │  ├── test_goal_gates.py
   │  │  ├── test_gpt56_registration.py
   │  │  ├── test_graphical_browser_detection.py
   │  │  ├── test_gui_command.py
   │  │  ├── test_gui_uninstall.py
   │  │  ├── test_hatch_prompt_thread_safety.py
   │  │  ├── test_heartbeat.py
   │  │  ├── test_hooks_cli.py
   │  │  ├── test_ignore_user_config_flags.py
   │  │  ├── test_imagegen_managed_gateway.py
   │  │  ├── test_image_gen_picker.py
   │  │  ├── test_init_command.py
   │  │  ├── test_input_sanitize.py
   │  │  ├── test_install_cua_driver.py
   │  │  ├── test_inventory.py
   │  │  ├── test_inventory_pricing.py
   │  │  ├── test_inventory_reasoning_caps.py
   │  │  ├── test_in_dir_msys_paths.py
   │  │  ├── test_jobs_json_utf8_bom.py
   │  │  ├── test_journey_render.py
   │  │  ├── test_kanban_blocked_sticky.py
   │  │  ├── test_kanban_block_kinds.py
   │  │  ├── test_kanban_boards.py
   │  │  ├── test_kanban_board_project.py
   │  │  ├── test_kanban_cli.py
   │  │  ├── test_kanban_cli_dispatch_passthrough.py
   │  │  ├── test_kanban_cli_exit_status.py
   │  │  ├── test_kanban_comment_queries.py
   │  │  ├── test_kanban_core_functionality.py
   │  │  ├── test_kanban_count_notify_subs.py
   │  │  ├── test_kanban_db.py
   │  │  ├── test_kanban_db_init.py
   │  │  ├── test_kanban_db_repair.py
   │  │  ├── test_kanban_decompose.py
   │  │  ├── test_kanban_decompose_db.py
   │  │  ├── test_kanban_default_assignee.py
   │  │  ├── test_kanban_diagnostics.py
   │  │  ├── test_kanban_dispatch_lock.py
   │  │  ├── test_kanban_dispatch_tick_hook.py
   │  │  ├── test_kanban_goal_mode.py
   │  │  ├── test_kanban_host_cap.py
   │  │  ├── test_kanban_init_lock_bounded.py
   │  │  ├── test_kanban_lifecycle_hooks.py
   │  │  ├── test_kanban_memory_guard.py
   │  │  ├── test_kanban_notify.py
   │  │  ├── test_kanban_parent_reopen_invalidation.py
   │  │  ├── test_kanban_per_profile_cap.py
   │  │  ├── test_kanban_project_link.py
   │  │  ├── test_kanban_promote.py
   │  │  ├── test_kanban_reclaim_claim_lock_guard.py
   │  │  ├── test_kanban_review_lifecycle.py
   │  │  ├── test_kanban_review_lifecycle_complete.py
   │  │  ├── test_kanban_review_surfaces.py
   │  │  ├── test_kanban_specify.py
   │  │  ├── test_kanban_specify_db.py
   │  │  ├── test_kanban_swarm.py
   │  │  ├── test_kanban_task_updated_hook.py
   │  │  ├── test_kanban_worker_image_extraction.py
   │  │  ├── test_kanban_worker_lifecycle_hooks.py
   │  │  ├── test_kanban_worker_session_source.py
   │  │  ├── test_kanban_worker_spawn_toolsets.py
   │  │  ├── test_kanban_worker_terminal_cwd.py
   │  │  ├── test_kanban_worktree_isolation.py
   │  │  ├── test_kanban_worktree_teardown.py
   │  │  ├── test_kanban_write_guard.py
   │  │  ├── test_kanban_write_txn_busy_retry.py
   │  │  ├── test_kimi_cn_provider_listing.py
   │  │  ├── test_launcher.py
   │  │  ├── test_lazy_command_exports.py
   │  │  ├── test_lazy_refresh_venv_repair.py
   │  │  ├── test_lifecycle.py
   │  │  ├── test_linux_desktop_entry.py
   │  │  ├── test_list_picker_providers.py
   │  │  ├── test_lmstudio_context_policy.py
   │  │  ├── test_logs.py
   │  │  ├── test_loops.py
   │  │  ├── test_main_model_custom_provider_normalization.py
   │  │  ├── test_managed_installs.py
   │  │  ├── test_managed_install_shapes.py
   │  │  ├── test_managed_scope.py
   │  │  ├── test_managed_scope_cli_config.py
   │  │  ├── test_managed_scope_config.py
   │  │  ├── test_managed_scope_env.py
   │  │  ├── test_managed_scope_loaders.py
   │  │  ├── test_managed_scope_overlay.py
   │  │  ├── test_managed_scope_regression.py
   │  │  ├── test_managed_scope_surfacing.py
   │  │  ├── test_managed_scope_writeguard.py
   │  │  ├── test_managed_uv.py
   │  │  ├── test_mcp_add_command_dest.py
   │  │  ├── test_mcp_catalog.py
   │  │  ├── test_mcp_config.py
   │  │  ├── test_mcp_dashboard_oauth.py
   │  │  ├── test_mcp_discovery_timing.py
   │  │  ├── test_mcp_reload_confirm_gate.py
   │  │  ├── test_mcp_security.py
   │  │  ├── test_mcp_startup.py
   │  │  ├── test_mcp_tools_config.py
   │  │  ├── test_memory_reset.py
   │  │  ├── test_memory_setup.py
   │  │  ├── test_memory_setup_provider_arg.py
   │  │  ├── test_memory_status.py
   │  │  ├── test_memory_status_env_hint.py
   │  │  ├── test_mem_trim.py
   │  │  ├── test_meta_prompt_cache.py
   │  │  ├── test_migrate_xai.py
   │  │  ├── test_moa_config.py
   │  │  ├── test_moa_set_models_preserves_extra_keys.py
   │  │  ├── test_models.py
   │  │  ├── test_models_dev_preferred_merge.py
   │  │  ├── test_model_cache_parallel_prefetch.py
   │  │  ├── test_model_cache_swr.py
   │  │  ├── test_model_catalog.py
   │  │  ├── test_model_cost_guard.py
   │  │  ├── test_model_data_policy_guard.py
   │  │  ├── test_model_flow_pooled_credentials.py
   │  │  ├── test_model_normalize.py
   │  │  ├── test_model_picker_excluded_providers.py
   │  │  ├── test_model_picker_expensive_confirm.py
   │  │  ├── test_model_picker_secret_scope.py
   │  │  ├── test_model_picker_viewport.py
   │  │  ├── test_model_provider_persistence.py
   │  │  ├── test_model_search.py
   │  │  ├── test_model_search_alias_dedup.py
   │  │  ├── test_model_selection_guards.py
   │  │  ├── test_model_switch_configured_provider_routing.py
   │  │  ├── test_model_switch_confirm_thread.py
   │  │  ├── test_model_switch_context_display.py
   │  │  ├── test_model_switch_context_offload.py
   │  │  ├── test_model_switch_copilot_api_mode.py
   │  │  ├── test_model_switch_custom_providers.py
   │  │  ├── test_model_switch_filter_unresolved.py
   │  │  ├── test_model_switch_once_flags.py
   │  │  ├── test_model_switch_openai_api_mode.py
   │  │  ├── test_model_switch_opencode_anthropic.py
   │  │  ├── test_model_switch_parsing.py
   │  │  ├── test_model_switch_persist_default.py
   │  │  ├── test_model_switch_variant_tags.py
   │  │  ├── test_model_validation.py
   │  │  ├── test_noninteractive_git.py
   │  │  ├── test_non_ascii_credential.py
   │  │  ├── test_normalize_main_model_assignment.py
   │  │  ├── test_nous_account.py
   │  │  ├── test_nous_auth_keepalive.py
   │  │  ├── test_nous_auth_status_cache.py
   │  │  ├── test_nous_billing_request.py
   │  │  ├── test_nous_jimmy_non_agentic.py
   │  │  ├── test_nous_inference_url_validation.py
   │  │  ├── test_nous_portal_staging_allowlist.py
   │  │  ├── test_nous_reasoning_metadata.py
   │  │  ├── test_nous_session_validity.py
   │  │  ├── test_nous_subscription.py
   │  │  ├── test_npm_engine.py
   │  │  ├── test_official_openai_host.py
   │  │  ├── test_ollama_cloud_auth.py
   │  │  ├── test_ollama_cloud_provider.py
   │  │  ├── test_oneshot_skills.py
   │  │  ├── test_oneshot_surrogate.py
   │  │  ├── test_oneshot_usage_file.py
   │  │  ├── test_openai_codex_model_validation_fallback.py
   │  │  ├── test_openai_discovery_endpoint.py
   │  │  ├── test_openai_listing_authority.py
   │  │  ├── test_openai_picker_curated.py
   │  │  ├── test_opencode_go_flat_namespace.py
   │  │  ├── test_opencode_go_in_model_list.py
   │  │  ├── test_opencode_go_validation_fallback.py
   │  │  ├── test_opencode_zen_model_limit.py
   │  │  ├── test_openrouter_reasoning_metadata.py
   │  │  ├── test_orphan_desktop_serve_reap.py
   │  │  ├── test_overlay_slug_resolution.py
   │  │  ├── test_pairing.py
   │  │  ├── test_path_completion.py
   │  │  ├── test_peer_cmd.py
   │  │  ├── test_personality_single_owner.py
   │  │  ├── test_pet_toggle.py
   │  │  ├── test_picker_prewarm.py
   │  │  ├── test_pin_kanban_board_env.py
   │  │  ├── test_pip_install_detection.py
   │  │  ├── test_placeholder_usage.py
   │  │  ├── test_platform_actions.py
   │  │  ├── test_plugins.py
   │  │  ├── test_plugins_cmd.py
   │  │  ├── test_plugins_cmd_category_discovery.py
   │  │  ├── test_plugins_cmd_enable_disable_nested.py
   │  │  ├── test_plugins_cmd_list.py
   │  │  ├── test_plugins_hub_perf_guard.py
   │  │  ├── test_plugins_transcription_registration.py
   │  │  ├── test_plugins_tts_registration.py
   │  │  ├── test_plugin_api_compat.py
   │  │  ├── test_plugin_auxiliary_tasks.py
   │  │  ├── test_plugin_call_mcp.py
   │  │  ├── test_plugin_capabilities.py
   │  │  ├── test_plugin_cli_registration.py
   │  │  ├── test_plugin_config_state_bridge.py
   │  │  ├── test_plugin_dev.py
   │  │  ├── test_plugin_event_bus.py
   │  │  ├── test_plugin_index_search.py
   │  │  ├── test_plugin_install_ref.py
   │  │  ├── test_plugin_manifest_v2.py
   │  │  ├── test_plugin_message_injection.py
   │  │  ├── test_plugin_ownership_ledger.py
   │  │  ├── test_plugin_packs.py
   │  │  ├── test_plugin_prompt_sections.py
   │  │  ├── test_plugin_runtime_disable_gate.py
   │  │  ├── test_plugin_scanner_recursion.py
   │  │  ├── test_post_setup_gating.py
   │  │  ├── test_pre_command_hook.py
   │  │  ├── test_process_identity.py
   │  │  ├── test_profiles.py
   │  │  ├── test_profiles_s6_hooks.py
   │  │  ├── test_profiles_sidebar_cache.py
   │  │  ├── test_profiles_sidebar_scope.py
   │  │  ├── test_profile_describer.py
   │  │  ├── test_profile_display_name.py
   │  │  ├── test_profile_distribution.py
   │  │  ├── test_profile_export_credentials.py
   │  │  ├── test_profile_install_env_encoding.py
   │  │  ├── test_projects_cli.py
   │  │  ├── test_projects_db.py
   │  │  ├── test_project_plugin_rce_bypass.py
   │  │  ├── test_prompt_api_key.py
   │  │  ├── test_prompt_compose_command.py
   │  │  ├── test_prompt_size.py
   │  │  ├── test_provider_catalog.py
   │  │  ├── test_provider_config_validation.py
   │  │  ├── test_provider_groups.py
   │  │  ├── test_provider_live_curated_merge.py
   │  │  ├── test_provider_parity.py
   │  │  ├── test_provider_precedence.py
   │  │  ├── test_provider_section3_grouping.py
   │  │  ├── test_proxy.py
   │  │  ├── test_prune_spares_pinned.py
   │  │  ├── test_psutil_android_extract.py
   │  │  ├── test_pty_bridge.py
   │  │  ├── test_quarantine_forensic_logging.py
   │  │  ├── test_quarantine_noop_restore.py
   │  │  ├── test_read_raw_config_readonly.py
   │  │  ├── test_reasoning_caps_disk_cache.py
   │  │  ├── test_reasoning_effort_menu.py
   │  │  ├── test_reasoning_full_command.py
   │  │  ├── test_redact_config_bridge.py
   │  │  ├── test_regression_16767.py
   │  │  ├── test_relaunch.py
   │  │  ├── test_relay_plugin_cutover.py
   │  │  ├── test_relay_shared_metrics.py
   │  │  ├── test_relay_shared_metrics_runtime.py
   │  │  ├── test_remote_spending_gate_contract.py
   │  │  ├── test_resolve_ephemeral_system_prompt.py
   │  │  ├── test_resolve_last_session.py
   │  │  ├── test_resolve_provider_openrouter_pool.py
   │  │  ├── test_resolve_token_memo.py
   │  │  ├── test_resolve_turn_limit.py
   │  │  ├── test_resume_latest_and_in_dir.py
   │  │  ├── test_runtime_provider_resolution.py
   │  │  ├── test_runtime_transport_precedence.py
   │  │  ├── test_run_with_idle_timeout.py
   │  │  ├── test_safe_mode.py
   │  │  ├── test_sale_pricing.py
   │  │  ├── test_scan_venv_blockers.py
   │  │  ├── test_secrets_bitwarden_non_tty.py
   │  │  ├── test_secrets_token_rotation.py
   │  │  ├── test_secret_prompt.py
   │  │  ├── test_secret_source_bootstrap.py
   │  │  ├── test_security_advisories.py
   │  │  ├── test_security_audit.py
   │  │  ├── test_security_audit_startup.py
   │  │  ├── test_send_cmd.py
   │  │  ├── test_serve_command.py
   │  │  ├── test_serve_parent_watchdog.py
   │  │  ├── test_service_manager.py
   │  │  ├── test_sessions_delete.py
   │  │  ├── test_sessions_error_exit_codes.py
   │  │  ├── test_sessions_export_md_cli.py
   │  │  ├── test_sessions_pin.py
   │  │  ├── test_sessions_size_delta_label.py
   │  │  ├── test_session_browse.py
   │  │  ├── test_session_export.py
   │  │  ├── test_session_export_html.py
   │  │  ├── test_session_export_html_escape.py
   │  │  ├── test_session_export_md.py
   │  │  ├── test_session_filters.py
   │  │  ├── test_session_handoff.py
   │  │  ├── test_session_listing.py
   │  │  ├── test_session_recap.py
   │  │  ├── test_session_recovery.py
   │  │  ├── test_session_recovery_lost_and_found.py
   │  │  ├── test_session_save.py
   │  │  ├── test_setup.py
   │  │  ├── test_setup_agent_settings.py
   │  │  ├── test_setup_blank_slate.py
   │  │  ├── test_setup_jimmy_script.py
   │  │  ├── test_setup_hidden_env.py
   │  │  ├── test_setup_irc.py
   │  │  ├── test_setup_matrix_e2ee.py
   │  │  ├── test_setup_model_provider.py
   │  │  ├── test_setup_noninteractive.py
   │  │  ├── test_setup_openclaw_migration.py
   │  │  ├── test_setup_prompt_menus.py
   │  │  ├── test_setup_reconfigure.py
   │  │  ├── test_setup_summary_provider_warning.py
   │  │  ├── test_setup_telemetry.py
   │  │  ├── test_setup_tts_xai_oauth.py
   │  │  ├── test_set_config_value.py
   │  │  ├── test_signal_handler_kanban_worker.py
   │  │  ├── test_sizefmt.py
   │  │  ├── test_skills_config.py
   │  │  ├── test_skills_hub.py
   │  │  ├── test_skills_install_flags.py
   │  │  ├── test_skills_skip_confirm.py
   │  │  ├── test_skills_subparser.py
   │  │  ├── test_skills_uninstall_flags.py
   │  │  ├── test_skin_cmd.py
   │  │  ├── test_skin_engine.py
   │  │  ├── test_skin_palettes.py
   │  │  ├── test_slack_cli.py
   │  │  ├── test_spawn_gateway_restart_cooldown.py
   │  │  ├── test_spawn_gateway_restart_reap.py
   │  │  ├── test_spotify_auth.py
   │  │  ├── test_sqlite_runtime.py
   │  │  ├── test_ssh_ownership_endpoint.py
   │  │  ├── test_ssh_session_token_parser.py
   │  │  ├── test_startup_fast_guards.py
   │  │  ├── test_startup_plugin_gating.py
   │  │  ├── test_state_db_guard.py
   │  │  ├── test_status.py
   │  │  ├── test_status_model_provider.py
   │  │  ├── test_status_provider_label.py
   │  │  ├── test_stderr_timestamp.py
   │  │  ├── test_stt_picker.py
   │  │  ├── test_subcommands_batch.py
   │  │  ├── test_subcommands_followup.py
   │  │  ├── test_subcommands_profile_gateway.py
   │  │  ├── test_subparser_routing_fallback.py
   │  │  ├── test_subprocess_timeouts.py
   │  │  ├── test_subscription_cli.py
   │  │  ├── test_suppress_eio_on_interrupt.py
   │  │  ├── test_systemd_optional_directives.py
   │  │  ├── test_systemd_watchdog_unit.py
   │  │  ├── test_system_stats_platform.py
   │  │  ├── test_teams_pipeline_plugin_cli.py
   │  │  ├── test_telegram_managed_bot.py
   │  │  ├── test_tencent_tokenhub_provider.py
   │  │  ├── test_terminal_breadcrumbs.py
   │  │  ├── test_terminal_io_broken_81521.py
   │  │  ├── test_terminal_menu_fallbacks.py
   │  │  ├── test_timeouts.py
   │  │  ├── test_timestamps_command.py
   │  │  ├── test_tips.py
   │  │  ├── test_toolset_validation.py
   │  │  ├── test_tools_config.py
   │  │  ├── test_tools_disable_enable.py
   │  │  ├── test_tool_token_estimation.py
   │  │  ├── test_tts_picker.py
   │  │  ├── test_tui_bundled.py
   │  │  ├── test_tui_heap_sizing.py
   │  │  ├── test_tui_launcher_skips_plugin_discovery.py
   │  │  ├── test_tui_mouse_residue_suppression.py
   │  │  ├── test_tui_npm_install.py
   │  │  ├── test_tui_resume_flow.py
   │  │  ├── test_uninstall_dry_run.py
   │  │  ├── test_uninstall_node_symlinks.py
   │  │  ├── test_uninstall_shell_configs.py
   │  │  ├── test_update_apply_shallow_count.py
   │  │  ├── test_update_autostash.py
   │  │  ├── test_update_behind_count_recovery.py
   │  │  ├── test_update_bootstrap_cache_refresh.py
   │  │  ├── test_update_check.py
   │  │  ├── test_update_cold_start_gateway_liveness.py
   │  │  ├── test_update_concurrent_quarantine.py
   │  │  ├── test_update_config_clears_custom_fields.py
   │  │  ├── test_update_current_node_repair.py
   │  │  ├── test_update_desktop_stale_warning.py
   │  │  ├── test_update_eol_churn.py
   │  │  ├── test_update_fetch_failure_classifier.py
   │  │  ├── test_update_fleet_restart_timeout.py
   │  │  ├── test_update_gateway_launcher_refresh.py
   │  │  ├── test_update_gateway_restart_aborted.py
   │  │  ├── test_update_handoff_backend_reap.py
   │  │  ├── test_update_hangup_protection.py
   │  │  ├── test_update_head_moved_gate.py
   │  │  ├── test_update_import_guard.py
   │  │  ├── test_update_interrupted_recovery.py
   │  │  ├── test_update_lock.py
   │  │  ├── test_update_modified_notice.py
   │  │  ├── test_update_orphan_backend_reap.py
   │  │  ├── test_update_parked_branch_guard.py
   │  │  ├── test_update_post_pull_syntax_guard.py
   │  │  ├── test_update_secret_import_lock.py
   │  │  ├── test_update_self_lock.py
   │  │  ├── test_update_shim_self_lock.py
   │  │  ├── test_update_skip_unchanged_editable_install.py
   │  │  ├── test_update_stale_dashboard.py
   │  │  ├── test_update_stale_module_purge.py
   │  │  ├── test_update_venv_health.py
   │  │  ├── test_update_version_report.py
   │  │  ├── test_update_wedged_gateway.py
   │  │  ├── test_update_yes_flag.py
   │  │  ├── test_update_zip_atomic_replace.py
   │  │  ├── test_update_zip_symlink_reject.py
   │  │  ├── test_update_zip_two_phase.py
   │  │  ├── test_upstage_provider.py
   │  │  ├── test_urllib_security.py
   │  │  ├── test_user_providers_model_switch.py
   │  │  ├── test_verify_console_scripts.py
   │  │  ├── test_verify_core_dependencies.py
   │  │  ├── test_vertex_model_picker.py
   │  │  ├── test_vertex_provider.py
   │  │  ├── test_video_gen_picker.py
   │  │  ├── test_voice_wrapper.py
   │  │  ├── test_webhook_cli.py
   │  │  ├── test_web_oauth_dispatch.py
   │  │  ├── test_web_profile_soul_writes.py
   │  │  ├── test_web_routers_tools_install_on_enable.py
   │  │  ├── test_web_server.py
   │  │  ├── test_web_server_approvals_broadcast.py
   │  │  ├── test_web_server_boot_handshake.py
   │  │  ├── test_web_server_config_offloop.py
   │  │  ├── test_web_server_console_ws.py
   │  │  ├── test_web_server_cron_profiles.py
   │  │  ├── test_web_server_files.py
   │  │  ├── test_web_server_fs.py
   │  │  ├── test_web_server_gateway_topology.py
   │  │  ├── test_web_server_git.py
   │  │  ├── test_web_server_host_header.py
   │  │  ├── test_web_server_messaging_profiles.py
   │  │  ├── test_web_server_oauth_write.py
   │  │  ├── test_web_server_profile_unification.py
   │  │  ├── test_web_server_pty_idle_backoff.py
   │  │  ├── test_web_server_pty_import.py
   │  │  ├── test_web_server_pty_reconnect.py
   │  │  ├── test_web_server_session_search.py
   │  │  ├── test_web_server_skills_profiles.py
   │  │  ├── test_web_server_skill_editor.py
   │  │  ├── test_web_server_speak_stream.py
   │  │  ├── test_web_ui_build.py
   │  │  ├── test_whatsapp_cloud_setup.py
   │  │  ├── test_whatsapp_onboarding.py
   │  │  ├── test_whatsapp_setup_ordering.py
   │  │  ├── test_windows_native_docs.py
   │  │  ├── test_win_pty_bridge.py
   │  │  ├── test_worktree_command.py
   │  │  ├── test_worktree_gc.py
   │  │  ├── test_xai_curated_models.py
   │  │  ├── test_xai_model_flow.py
   │  │  ├── test_xai_oauth_profile_auth.py
   │  │  ├── test_xai_oauth_refresh.py
   │  │  ├── test_xai_oauth_writethrough.py
   │  │  ├── test_xai_provider_labels.py
   │  │  ├── test_xai_retirement.py
   │  │  ├── test_xiaomi_provider.py
   │  │  ├── test_yolo_startup_order.py
   │  │  └── __init__.py
   │  ├── jimmy_state
   │  │  ├── test_append_messages_batch.py
   │  │  ├── test_aux_usage_accounting.py
   │  │  ├── test_conversation_root.py
   │  │  ├── test_get_anchored_view.py
   │  │  ├── test_get_messages_around.py
   │  │  ├── test_get_messages_include_compacted.py
   │  │  ├── test_isolation_marker_env.py
   │  │  ├── test_live_db_guard_ancestry.py
   │  │  ├── test_live_db_isolation_guard.py
   │  │  ├── test_never_active_keyed_prune.py
   │  │  ├── test_orphan_gateway_session_repair.py
   │  │  ├── test_reasoning_roundtrip.py
   │  │  ├── test_replace_messages_archive_siblings.py
   │  │  ├── test_resolve_resume_session_id.py
   │  │  ├── test_restore_alternation_repair.py
   │  │  ├── test_session_archiving.py
   │  │  ├── test_session_hidden.py
   │  │  ├── test_session_lifecycle_status.py
   │  │  ├── test_session_md_export.py
   │  │  └── test_session_read_state.py
   │  ├── honcho_plugin
   │  │  ├── conftest.py
   │  │  ├── test_async_memory.py
   │  │  ├── test_auth_recovery.py
   │  │  ├── test_cli.py
   │  │  ├── test_client.py
   │  │  ├── test_client_identity_isolation.py
   │  │  ├── test_empty_profile_hint.py
   │  │  ├── test_network_isolation.py
   │  │  ├── test_oauth.py
   │  │  ├── test_oauth_flow.py
   │  │  ├── test_pin_peer_name.py
   │  │  ├── test_query_rewrite.py
   │  │  ├── test_save_messages.py
   │  │  ├── test_session.py
   │  │  └── __init__.py
   │  ├── install
   │  │  └── install-update-e2e.sh
   │  ├── integration
   │  │  ├── test_batch_runner.py
   │  │  ├── test_checkpoint_resumption.py
   │  │  ├── test_daytona_terminal.py
   │  │  ├── test_ha_integration.py
   │  │  ├── test_modal_terminal.py
   │  │  ├── test_vision_docker_resolve.py
   │  │  ├── test_voice_channel_flow.py
   │  │  ├── test_web_tools.py
   │  │  └── __init__.py
   │  ├── manual
   │  │  ├── cron_inchannel_dm_e2e.py
   │  │  └── cron_inchannel_e2e.py
   │  ├── monitoring
   │  │  ├── test_cron_health_export.py
   │  │  ├── test_emitter.py
   │  │  ├── test_export_redaction.py
   │  │  ├── test_gateway_health_export.py
   │  │  ├── test_otlp_exporter.py
   │  │  └── __init__.py
   │  ├── openviking_plugin
   │  │  └── test_openviking.py
   │  ├── plugins
   │  │  ├── browser
   │  │  │  ├── check_parity_vs_main.py
   │  │  │  ├── test_browser_provider_plugins.py
   │  │  │  └── __init__.py
   │  │  ├── dashboard_auth
   │  │  │  ├── test_basic_provider.py
   │  │  │  ├── test_drain_provider.py
   │  │  │  ├── test_nous_provider.py
   │  │  │  └── test_self_hosted_provider.py
   │  │  ├── image_gen
   │  │  │  ├── check_parity_vs_main.py
   │  │  │  ├── test_deepinfra_provider.py
   │  │  │  ├── test_fal_provider.py
   │  │  │  ├── test_krea_provider.py
   │  │  │  ├── test_openai_codex_provider.py
   │  │  │  ├── test_openai_provider.py
   │  │  │  ├── test_openrouter_compat_provider.py
   │  │  │  ├── test_xai_provider.py
   │  │  │  └── __init__.py
   │  │  ├── memory
   │  │  │  ├── test_byterover_provider.py
   │  │  │  ├── test_config_schema.py
   │  │  │  ├── test_discovery_sources.py
   │  │  │  ├── test_hindsight_config_schema.py
   │  │  │  ├── test_hindsight_env_perms.py
   │  │  │  ├── test_hindsight_local_runtime_hint.py
   │  │  │  ├── test_hindsight_provider.py
   │  │  │  ├── test_hindsight_templates.py
   │  │  │  ├── test_holographic_auto_extract.py
   │  │  │  ├── test_holographic_retrieval.py
   │  │  │  ├── test_holographic_shutdown_closes_db.py
   │  │  │  ├── test_holographic_store.py
   │  │  │  ├── test_honcho_cli_peers.py
   │  │  │  ├── test_honcho_config_schema.py
   │  │  │  ├── test_mem0_backend.py
   │  │  │  ├── test_mem0_providers.py
   │  │  │  ├── test_mem0_setup.py
   │  │  │  ├── test_mem0_v3.py
   │  │  │  ├── test_memory_lazy_install.py
   │  │  │  ├── test_openviking_endpoint_always_blocked.py
   │  │  │  ├── test_openviking_provider.py
   │  │  │  ├── test_openviking_shutdown.py
   │  │  │  ├── test_retaindb_provider.py
   │  │  │  ├── test_supermemory_provider.py
   │  │  │  └── __init__.py
   │  │  ├── model_providers
   │  │  │  ├── test_commandcode_profile.py
   │  │  │  ├── test_copilot_profile.py
   │  │  │  ├── test_custom_profile.py
   │  │  │  ├── test_deepseek_profile.py
   │  │  │  ├── test_fireworks_profile.py
   │  │  │  ├── test_gemini_profile.py
   │  │  │  ├── test_kimi_profile.py
   │  │  │  ├── test_minimax_profile.py
   │  │  │  ├── test_nous_profile.py
   │  │  │  ├── test_ollama_cloud_profile.py
   │  │  │  ├── test_opencode_go_profile.py
   │  │  │  ├── test_upstage_profile.py
   │  │  │  └── test_zai_profile.py
   │  │  ├── platforms
   │  │  │  ├── photon
   │  │  │  │  ├── test_auth.py
   │  │  │  │  ├── test_check_requirements_risks.py
   │  │  │  │  ├── test_fatal_notify_self_cancel.py
   │  │  │  │  ├── test_inbound.py
   │  │  │  │  ├── test_markdown.py
   │  │  │  │  ├── test_mention_gating.py
   │  │  │  │  ├── test_npm_error_log_regression.py
   │  │  │  │  ├── test_outbound_media.py
   │  │  │  │  ├── test_overflow_recovery.py
   │  │  │  │  ├── test_poll_clarify.py
   │  │  │  │  ├── test_presence_watchdog.py
   │  │  │  │  ├── test_reactions.py
   │  │  │  │  ├── test_rich_links.py
   │  │  │  │  ├── test_runtime_record.py
   │  │  │  │  ├── test_setup_access.py
   │  │  │  │  ├── test_sidecar_deps_stale.py
   │  │  │  │  ├── test_sidecar_lifecycle.py
   │  │  │  │  ├── test_sidecar_paths.py
   │  │  │  │  ├── test_spectrum_patch.py
   │  │  │  │  ├── test_streaming.py
   │  │  │  │  ├── test_url_send_path.py
   │  │  │  │  └── test_zombie_stream_watchdog.py
   │  │  │  └── test_discord_gate_isolation.py
   │  │  ├── test_a2a_phase23.py
   │  │  ├── test_a2a_plugin.py
   │  │  ├── test_a2a_schema_registration.py
   │  │  ├── test_achievements_plugin.py
   │  │  ├── test_chronos_cron.py
   │  │  ├── test_chronos_verify.py
   │  │  ├── test_discord_runtime_failure.py
   │  │  ├── test_disk_cleanup_plugin.py
   │  │  ├── test_google_meet_audio.py
   │  │  ├── test_google_meet_node.py
   │  │  ├── test_google_meet_plugin.py
   │  │  ├── test_google_meet_realtime.py
   │  │  ├── test_hindsight_health_grace_timeout.py
   │  │  ├── test_hindsight_root_guard.py
   │  │  ├── test_holographic_vector_storage.py
   │  │  ├── test_kanban_attachments.py
   │  │  ├── test_kanban_board_project_api.py
   │  │  ├── test_kanban_dashboard_plugin.py
   │  │  ├── test_kanban_dashboard_task_updated_hook.py
   │  │  ├── test_kanban_estimate.py
   │  │  ├── test_kanban_model_override.py
   │  │  ├── test_kanban_worker_runs.py
   │  │  ├── test_kanban_ws_idle_disconnect.py
   │  │  ├── test_langfuse_plugin.py
   │  │  ├── test_plugin_dashboard_auth_contract.py
   │  │  ├── test_raft_check_fn_silent.py
   │  │  ├── test_retaindb_plugin.py
   │  │  ├── test_security_guidance_plugin.py
   │  │  ├── test_teams_pipeline_meetings.py
   │  │  ├── test_teams_pipeline_plugin.py
   │  │  ├── transcription
   │  │  │  ├── check_parity_vs_main.py
   │  │  │  └── __init__.py
   │  │  ├── tts
   │  │  │  ├── check_parity_vs_main.py
   │  │  │  └── __init__.py
   │  │  ├── video_gen
   │  │  │  ├── test_deepinfra_provider.py
   │  │  │  ├── test_fal_plugin.py
   │  │  │  ├── test_xai_plugin.py
   │  │  │  ├── test_xai_plugin_integration.py
   │  │  │  └── __init__.py
   │  │  ├── web
   │  │  │  ├── test_web_search_provider_plugins.py
   │  │  │  └── __init__.py
   │  │  └── __init__.py
   │  ├── providers
   │  │  ├── test_e2e_wiring.py
   │  │  ├── test_entry_point_discovery.py
   │  │  ├── test_fetch_models_base_url.py
   │  │  ├── test_meta_ai_profile.py
   │  │  ├── test_plugin_discovery.py
   │  │  ├── test_profile_wiring.py
   │  │  ├── test_provider_profiles.py
   │  │  ├── test_provider_registry.py
   │  │  ├── test_transport_parity.py
   │  │  └── __init__.py
   │  ├── relay
   │  │  ├── test_relay_format_hints.py
   │  │  └── test_relay_inchannel_continuable.py
   │  ├── run_agent
   │  │  ├── conftest.py
   │  │  ├── repro_48013_image_shrink_brick.py
   │  │  ├── test_1630_context_overflow_loop.py
   │  │  ├── test_18028_content_policy_blocked.py
   │  │  ├── test_24996_fallback_exhaustion_cooldown.py
   │  │  ├── test_28161_anthropic_stream_pool_cleanup.py
   │  │  ├── test_31273_402_not_retried.py
   │  │  ├── test_32646_fallback_429_after_timeout.py
   │  │  ├── test_413_compression.py
   │  │  ├── test_63425_credential_pool_auto_detect.py
   │  │  ├── test_66267_multimodal_interim.py
   │  │  ├── test_70773_shared_client_fd_corruption.py
   │  │  ├── test_81641_text_turn_incremental_persistence.py
   │  │  ├── test_860_dedup.py
   │  │  ├── test_agent_guardrails.py
   │  │  ├── test_anthropic_mid_tool_call_drop.py
   │  │  ├── test_anthropic_prompt_cache_policy.py
   │  │  ├── test_anthropic_response_header_capture.py
   │  │  ├── test_anthropic_third_party_oauth_guard.py
   │  │  ├── test_anthropic_truncation_continuation.py
   │  │  ├── test_api_max_retries_config.py
   │  │  ├── test_async_httpx_del_neuter.py
   │  │  ├── test_authorization_gate.py
   │  │  ├── test_auth_provider_failover.py
   │  │  ├── test_background_review.py
   │  │  ├── test_background_review_cache_parity.py
   │  │  ├── test_background_review_cost_controls.py
   │  │  ├── test_background_review_summary.py
   │  │  ├── test_background_review_toolset_restriction.py
   │  │  ├── test_callable_api_key.py
   │  │  ├── test_codex_app_server_compaction.py
   │  │  ├── test_codex_app_server_integration.py
   │  │  ├── test_codex_app_server_lifecycle.py
   │  │  ├── test_codex_multimodal_tool_result.py
   │  │  ├── test_codex_no_tools_nonetype.py
   │  │  ├── test_codex_silent_hang_hint.py
   │  │  ├── test_codex_xai_oauth_recovery.py
   │  │  ├── test_commit_memory_session_context_engine.py
   │  │  ├── test_compression_abort_state_reset.py
   │  │  ├── test_compression_boundary.py
   │  │  ├── test_compression_boundary_hook.py
   │  │  ├── test_compression_budget_rearm.py
   │  │  ├── test_compression_budget_refund.py
   │  │  ├── test_compression_closed_adoption.py
   │  │  ├── test_compression_feasibility.py
   │  │  ├── test_compression_lock_defer.py
   │  │  ├── test_compression_persistence.py
   │  │  ├── test_compression_trigger_excludes_reasoning.py
   │  │  ├── test_compressor_fallback_update.py
   │  │  ├── test_compress_focus_plugin_fallback.py
   │  │  ├── test_concurrent_interrupt.py
   │  │  ├── test_context_token_tracking.py
   │  │  ├── test_continuation_ceiling_wedge.py
   │  │  ├── test_continuation_repetition_guard.py
   │  │  ├── test_conversation_fallback_state.py
   │  │  ├── test_copilot_native_vision_headers.py
   │  │  ├── test_corruption_recovery_guidance.py
   │  │  ├── test_create_openai_client_disables_sdk_retries.py
   │  │  ├── test_create_openai_client_kwargs_isolation.py
   │  │  ├── test_create_openai_client_proxy_env.py
   │  │  ├── test_create_openai_client_reuse.py
   │  │  ├── test_create_openai_client_ssl_verify.py
   │  │  ├── test_credential_pool_interrupt.py
   │  │  ├── test_credential_rotation_route_settings.py
   │  │  ├── test_credits_notices_toggle.py
   │  │  ├── test_cross_process_turn_lease.py
   │  │  ├── test_custom_provider_extra_headers_client.py
   │  │  ├── test_deepseek_reasoning_content_echo.py
   │  │  ├── test_deepseek_v4_thinking_live.py
   │  │  ├── test_dict_tool_call_args.py
   │  │  ├── test_dropped_tool_call_recovery.py
   │  │  ├── test_empty_response_recovery_persistence.py
   │  │  ├── test_empty_terminal_reasoning_surface.py
   │  │  ├── test_env_credential_turn_refresh.py
   │  │  ├── test_exit_cleanup_interrupt.py
   │  │  ├── test_fallback_api_mode_preservation.py
   │  │  ├── test_fallback_credential_isolation.py
   │  │  ├── test_fallback_reasoning_override.py
   │  │  ├── test_file_mutation_verifier.py
   │  │  ├── test_fireworks_live.py
   │  │  ├── test_identity_flush.py
   │  │  ├── test_image_generate_parallel.py
   │  │  ├── test_image_rejection_fallback.py
   │  │  ├── test_image_shrink_recovery.py
   │  │  ├── test_infinite_compaction_loop.py
   │  │  ├── test_init_fallback_on_exhausted_pool.py
   │  │  ├── test_interactive_interrupt.py
   │  │  ├── test_interrupt_propagation.py
   │  │  ├── test_invalid_context_length_warning.py
   │  │  ├── test_in_place_compaction.py
   │  │  ├── test_iteration_budget_race.py
   │  │  ├── test_jsondecodeerror_retryable.py
   │  │  ├── test_last_reasoning_per_turn.py
   │  │  ├── test_lmstudio_load_mode.py
   │  │  ├── test_long_context_tier_429.py
   │  │  ├── test_malformed_tool_arguments.py
   │  │  ├── test_materialize_data_url_cleanup.py
   │  │  ├── test_memory_nudge_counter_hydration.py
   │  │  ├── test_memory_provider_init.py
   │  │  ├── test_memory_sync_interrupted.py
   │  │  ├── test_message_sequence_repair.py
   │  │  ├── test_moa_fanout_cadence.py
   │  │  ├── test_moa_loop_mode.py
   │  │  ├── test_moa_privacy_filter.py
   │  │  ├── test_moa_streaming.py
   │  │  ├── test_multimodal_tool_content_recovery.py
   │  │  ├── test_native_compaction.py
   │  │  ├── test_nonretryable_error_html_summary.py
   │  │  ├── test_notice_spine.py
   │  │  ├── test_nous_429_fallback_reentry.py
   │  │  ├── test_nous_fallback_unavailable.py
   │  │  ├── test_openai_client_lifecycle.py
   │  │  ├── test_overflow_overhead_aware_tokens.py
   │  │  ├── test_partial_stream_finish_reason.py
   │  │  ├── test_percentage_clamp.py
   │  │  ├── test_per_model_compression_threshold.py
   │  │  ├── test_per_model_threshold_init_ordering.py
   │  │  ├── test_plugin_context_engine_init.py
   │  │  ├── test_plugin_stream_hooks.py
   │  │  ├── test_post_tool_compression_attempt_cap.py
   │  │  ├── test_preflight_compression_cap_e2e.py
   │  │  ├── test_pre_compress_memory_context.py
   │  │  ├── test_primary_runtime_restore.py
   │  │  ├── test_proactive_prune_loop_wiring.py
   │  │  ├── test_provider_attribution_headers.py
   │  │  ├── test_provider_fallback.py
   │  │  ├── test_provider_parity.py
   │  │  ├── test_reasoning_echo_resolver_e2e.py
   │  │  ├── test_repair_tool_call_arguments.py
   │  │  ├── test_repair_tool_call_name.py
   │  │  ├── test_request_client_reuse_abort_races.py
   │  │  ├── test_reset_aware_primary_restore.py
   │  │  ├── test_retry_status_buffer.py
   │  │  ├── test_review_prompt_class_first.py
   │  │  ├── test_run_agent.py
   │  │  ├── test_run_agent_codex_responses.py
   │  │  ├── test_run_agent_multimodal_prologue.py
   │  │  ├── test_sequential_chats_live.py
   │  │  ├── test_sequential_tool_timeout.py
   │  │  ├── test_session_activity_persist.py
   │  │  ├── test_session_id_env.py
   │  │  ├── test_session_meta_filtering.py
   │  │  ├── test_session_reset_fix.py
   │  │  ├── test_session_source.py
   │  │  ├── test_start_order_gate.py
   │  │  ├── test_steer.py
   │  │  ├── test_streaming.py
   │  │  ├── test_streaming_tool_call_repair.py
   │  │  ├── test_stream_drop_logging.py
   │  │  ├── test_stream_interrupt_retry.py
   │  │  ├── test_stream_single_writer_65991.py
   │  │  ├── test_stream_stale_breaker_reset.py
   │  │  ├── test_stream_stale_circuit_breaker.py
   │  │  ├── test_strict_api_validation.py
   │  │  ├── test_strip_reasoning_tags_cli.py
   │  │  ├── test_summarize_api_error.py
   │  │  ├── test_switch_model_context.py
   │  │  ├── test_switch_model_fallback_prune.py
   │  │  ├── test_switch_model_pool_reload_52727.py
   │  │  ├── test_switch_model_reapplies_headers.py
   │  │  ├── test_switch_model_reasoning_override.py
   │  │  ├── test_switch_model_rollback.py
   │  │  ├── test_switch_model_stale_base_url.py
   │  │  ├── test_thinking_only_sanitizer.py
   │  │  ├── test_thinking_prefill_trailing_turn.py
   │  │  ├── test_thinking_sig_recovery_persistence.py
   │  │  ├── test_tls_fd_recycle_corruption.py
   │  │  ├── test_token_persistence_non_cli.py
   │  │  ├── test_tool_activity_heartbeat.py
   │  │  ├── test_tool_arg_coercion.py
   │  │  ├── test_tool_batch_segmentation.py
   │  │  ├── test_tool_call_args_sanitizer.py
   │  │  ├── test_tool_call_guardrail_runtime.py
   │  │  ├── test_tool_call_incremental_persistence.py
   │  │  ├── test_tool_executor_contextvar_propagation.py
   │  │  ├── test_tool_name_db_persistence.py
   │  │  ├── test_turn_completion_explainer.py
   │  │  ├── test_unicode_ascii_codec.py
   │  │  ├── test_verification_continuation_budget.py
   │  │  ├── test_vision_aware_preprocessing.py
   │  │  ├── test_vision_tool_messages.py
   │  │  ├── test_wait_state_visibility.py
   │  │  └── __init__.py
   │  ├── run_interrupt_test.py
   │  ├── scripts
   │  │  ├── test_build_skills_index_health.py
   │  │  ├── test_contributor_map.py
   │  │  ├── test_footgun_subprocess_encoding.py
   │  │  ├── test_smoke_nemo_relay_shared_metrics.py
   │  │  └── test_windows_footguns_full_repo_scan.py
   │  ├── secret_sources
   │  │  ├── conformance.py
   │  │  ├── test_error_remediation.py
   │  │  ├── test_profile_secrets.py
   │  │  ├── test_secret_source_registry.py
   │  │  └── __init__.py
   │  ├── skills
   │  │  ├── test_actual_setup_skill.py
   │  │  ├── test_authoring_standards.py
   │  │  ├── test_box_skill.py
   │  │  ├── test_cloudflare_temporary_deploy_skill.py
   │  │  ├── test_comfyui_skill.py
   │  │  ├── test_competitor_news_monitor_skill.py
   │  │  ├── test_darwinian_evolver_skill.py
   │  │  ├── test_document_to_action_items_skill.py
   │  │  ├── test_email_inbox_triage_skill.py
   │  │  ├── test_fetch_transcript.py
   │  │  ├── test_github_credential_token.py
   │  │  ├── test_github_issue_to_pr_skill.py
   │  │  ├── test_google_workspace_api.py
   │  │  ├── test_google_workspace_credential_files.py
   │  │  ├── test_google_workspace_daily_brief_reference.py
   │  │  ├── test_google_workspace_setup.py
   │  │  ├── test_google_workspace_setup_deps.py
   │  │  ├── test_grounded_citations_skill.py
   │  │  ├── test_har_derived_api_client_skill.py
   │  │  ├── test_jimmy_agent_skill.py
   │  │  ├── test_hyperliquid_skill.py
   │  │  ├── test_mcp_oauth_remote_gateway_skill.py
   │  │  ├── test_meeting_action_items_skill.py
   │  │  ├── test_memento_cards.py
   │  │  ├── test_merge_reconciler_skill.py
   │  │  ├── test_office_document_skills.py
   │  │  ├── test_openclaw_migration.py
   │  │  ├── test_openclaw_migration_hardening.py
   │  │  ├── test_pinecone_research_skill.py
   │  │  ├── test_product_price_monitor_skill.py
   │  │  ├── test_sdlc_review_skill.py
   │  │  ├── test_social_media_content_calendar_skill.py
   │  │  ├── test_telephony_skill.py
   │  │  ├── test_tldraw_offline_skill.py
   │  │  ├── test_unbroker_skill.py
   │  │  ├── test_weekly_review_planning_skill.py
   │  │  ├── test_xurl_article_ingestion_docs.py
   │  │  ├── test_xurl_x_search_routing.py
   │  │  └── test_youtube_quiz.py
   │  ├── state
   │  │  ├── test_compression_lineage_guard.py
   │  │  ├── test_dedupe_migration_contention.py
   │  │  ├── test_disk_full_error.py
   │  │  ├── test_fts_runtime_rebuild.py
   │  │  ├── test_no_more_rows_retry.py
   │  │  ├── test_session_git_metadata_generation.py
   │  │  ├── test_session_model_usage_pk_heal.py
   │  │  ├── test_session_turn_lease.py
   │  │  └── test_write_lock_patience.py
   │  ├── stress
   │  │  ├── conftest.py
   │  │  ├── README.md
   │  │  ├── test_atypical_scenarios.py
   │  │  ├── test_benchmarks.py
   │  │  ├── test_concurrency.py
   │  │  ├── test_concurrency_mixed.py
   │  │  ├── test_concurrency_parent_gate.py
   │  │  ├── test_concurrency_reclaim_race.py
   │  │  ├── test_property_fuzzing.py
   │  │  ├── test_subprocess_e2e.py
   │  │  └── _fake_worker.py
   │  ├── test_account_usage.py
   │  ├── test_atomic_replace_symlinks.py
   │  ├── test_atomic_write_text_metadata.py
   │  ├── test_audio_playback_guard.py
   │  ├── test_background_review_list_shapes.py
   │  ├── test_background_review_session_isolation.py
   │  ├── test_base_url_hostname.py
   │  ├── test_batch_runner_checkpoint.py
   │  ├── test_batch_runner_durability.py
   │  ├── test_batch_runner_exit_code.py
   │  ├── test_bitwarden_secrets.py
   │  ├── test_cli_manual_compress.py
   │  ├── test_cli_skin_integration.py
   │  ├── test_code_skew.py
   │  ├── test_command_secret_source.py
   │  ├── test_compression_watermark_commit.py
   │  ├── test_conftest_wal_gate.py
   │  ├── test_copilot_initiator.py
   │  ├── test_credential_file_permissions.py
   │  ├── test_cron_manage_profile_scope.py
   │  ├── test_ctx_halving_fix.py
   │  ├── test_delegate_cascade_49148.py
   │  ├── test_desktop_update_shim_progress.py
   │  ├── test_desktop_update_windows_pipe_drain.py
   │  ├── test_desktop_update_windows_progress.py
   │  ├── test_desktop_update_windows_python_handoff.py
   │  ├── test_desktop_update_windows_timestamp.py
   │  ├── test_dispatch_session_id.py
   │  ├── test_empty_model_fallback.py
   │  ├── test_empty_session_hygiene.py
   │  ├── test_engines_satisfiable.py
   │  ├── test_env_loader_applied_homes.py
   │  ├── test_env_loader_op_bootstrap.py
   │  ├── test_env_loader_secret_sources.py
   │  ├── test_estop.py
   │  ├── test_evidence_store.py
   │  ├── test_fast_safe_load.py
   │  ├── test_fts_cjk_bigram.py
   │  ├── test_fts_update_of_narrowing.py
   │  ├── test_gateway_streaming_nested_config.py
   │  ├── test_get_tool_definitions_cache_isolation.py
   │  ├── test_gitlock.py
   │  ├── test_jimmy_bootstrap.py
   │  ├── test_jimmy_constants.py
   │  ├── test_jimmy_home_profile_warning.py
   │  ├── test_jimmy_logging.py
   │  ├── test_jimmy_state.py
   │  ├── test_jimmy_state_compression_busy_retry.py
   │  ├── test_jimmy_state_compression_locks.py
   │  ├── test_jimmy_state_readonly_preflight.py
   │  ├── test_jimmy_state_wal_fallback.py
   │  ├── test_hermetic_side_effect_guards.py
   │  ├── test_honcho_client_concurrency.py
   │  ├── test_honcho_client_config.py
   │  ├── test_honcho_session_context.py
   │  ├── test_honcho_startup_fail_open.py
   │  ├── test_install_autostash_conflict_recovery.py
   │  ├── test_install_commit_pin_rollback.py
   │  ├── test_install_diverged_update.py
   │  ├── test_install_lockfile_churn.py
   │  ├── test_install_macos_launcher.py
   │  ├── test_install_no_initial_commit.py
   │  ├── test_install_ps1_ascii_only.py
   │  ├── test_install_ps1_browser_install.py
   │  ├── test_install_ps1_managed_node_swap.py
   │  ├── test_install_ps1_native_stderr_eap.py
   │  ├── test_install_ps1_node_path_for_npm.py
   │  ├── test_install_ps1_python_fallback_venv.py
   │  ├── test_install_ps1_uv_install_fallback.py
   │  ├── test_install_ps1_uv_powershell_host.py
   │  ├── test_install_ps1_venv_process_tree.py
   │  ├── test_install_ps1_venv_recreate_safety.py
   │  ├── test_install_ps1_venv_rename_abort.py
   │  ├── test_install_ps1_venv_transaction_boundary.py
   │  ├── test_install_ps1_web_server_syntax_probe.py
   │  ├── test_install_scripts_computer_use.py
   │  ├── test_install_sh_acp_launcher.py
   │  ├── test_install_sh_bootstrap_marker.py
   │  ├── test_install_sh_browser_install.py
   │  ├── test_install_sh_install_method_stamp.py
   │  ├── test_install_sh_node_deps_failure.py
   │  ├── test_install_sh_node_global_prefix.py
   │  ├── test_install_sh_node_npm_check.py
   │  ├── test_install_sh_pythonpath_sanitization.py
   │  ├── test_install_sh_root_fhs_uv_python_path.py
   │  ├── test_install_sh_setup_wizard_tty_probe.py
   │  ├── test_install_sh_symlink_stomp.py
   │  ├── test_install_sh_termux_network_prereqs.py
   │  ├── test_install_unmerged_index.py
   │  ├── test_ipv4_preference.py
   │  ├── test_iron_proxy.py
   │  ├── test_iron_proxy_cli.py
   │  ├── test_iron_proxy_e2e.py
   │  ├── test_journal_mode_config.py
   │  ├── test_lazy_secrets_dispatch.py
   │  ├── test_lazy_secrets_import.py
   │  ├── test_lazy_session_regressions.py
   │  ├── test_list_recent_user_messages_handoffs.py
   │  ├── test_live_system_guard.py
   │  ├── test_live_system_guard_self_test.py
   │  ├── test_log_isolation.py
   │  ├── test_managed_runtime_resolution.py
   │  ├── test_mcp_serve.py
   │  ├── test_message_reactions.py
   │  ├── test_minimax_model_validation.py
   │  ├── test_minimax_oauth.py
   │  ├── test_minisweagent_path.py
   │  ├── test_mini_swe_runner.py
   │  ├── test_moa_prepared_request_leak_78382.py
   │  ├── test_model_forces_max_completion_tokens.py
   │  ├── test_model_picker_scroll.py
   │  ├── test_model_tools.py
   │  ├── test_model_tools_async_bridge.py
   │  ├── test_no_shadowed_test_definitions.py
   │  ├── test_ollama_num_ctx.py
   │  ├── test_onepassword_secrets.py
   │  ├── test_os_marker_gating.py
   │  ├── test_output_cap_parsing.py
   │  ├── test_packaging_build_guard.py
   │  ├── test_packaging_metadata.py
   │  ├── test_plugins_manage_profile_scope.py
   │  ├── test_plugin_skills.py
   │  ├── test_plugin_storage.py
   │  ├── test_plugin_utils.py
   │  ├── test_process_loop_event_loop_warning.py
   │  ├── test_profile_isolation_runtime.py
   │  ├── test_project_metadata.py
   │  ├── test_pty_keepalive_ws.py
   │  ├── test_pty_session.py
   │  ├── test_redaction_registry.py
   │  ├── test_resource_limits.py
   │  ├── test_retry_utils.py
   │  ├── test_run_tests_parallel.py
   │  ├── test_run_tests_parallel_stdio.py
   │  ├── test_sanitize_tool_error.py
   │  ├── test_schema_read_probe.py
   │  ├── test_search_slow_query_log.py
   │  ├── test_secret_scope_plugin_families.py
   │  ├── test_session_db_context_manager.py
   │  ├── test_session_db_read_conn_pool.py
   │  ├── test_session_db_read_path_split.py
   │  ├── test_session_skill_previews.py
   │  ├── test_session_system_prompt_dedup.py
   │  ├── test_session_vacuum_config.py
   │  ├── test_session_workspace_binding.py
   │  ├── test_slack_thread_require_mention.py
   │  ├── test_slash_worker_watchdog.py
   │  ├── test_sqlite_lock_safe_inspection.py
   │  ├── test_sqlite_wal_reset_gate.py
   │  ├── test_sql_injection.py
   │  ├── test_stale_tool_call_marker_session_repair.py
   │  ├── test_stale_utils_module_import.py
   │  ├── test_state_db_malformed_repair.py
   │  ├── test_state_db_notadb_selfheal.py
   │  ├── test_state_db_repair_loop_cap.py
   │  ├── test_state_db_stats.py
   │  ├── test_subprocess_home_isolation.py
   │  ├── test_telegram_polling_progress_ptb.py
   │  ├── test_termux_all_extra_compat.py
   │  ├── test_timezone.py
   │  ├── test_tini_shim.py
   │  ├── test_toolsets.py
   │  ├── test_toolset_distributions.py
   │  ├── test_trajectory_compressor.py
   │  ├── test_trajectory_compressor_async.py
   │  ├── test_transform_api_error_classification_hook.py
   │  ├── test_transform_llm_output_hook.py
   │  ├── test_transform_tool_result_hook.py
   │  ├── test_tui_entry_mcp_owner.py
   │  ├── test_tui_gateway_loop_noise.py
   │  ├── test_tui_gateway_queue_on_busy.py
   │  ├── test_tui_gateway_server.py
   │  ├── test_tui_gateway_server_crash_history.py
   │  ├── test_tui_gateway_ws.py
   │  ├── test_tui_mcp_late_refresh.py
   │  ├── test_utils_atomic_roundtrip_yaml_save.py
   │  ├── test_utils_truthy_values.py
   │  ├── test_voice_max_recording_seconds.py
   │  ├── test_wal_checkpoint_strategy.py
   │  ├── test_web_server.py
   │  ├── test_web_server_sessiondb_eventloop.py
   │  ├── test_web_server_status_topology_cache.py
   │  ├── test_windows_subprocess_no_window_flags.py
   │  ├── test_yaml_indent_consistency_31999.py
   │  ├── test_yuanbao_integration.py
   │  ├── test_yuanbao_markdown.py
   │  ├── test_yuanbao_pipeline.py
   │  ├── test_yuanbao_proto.py
   │  ├── test_yuanbao_reconnect_set_active.py
   │  ├── test_yuanbao_shutdown.py
   │  ├── test_zeroed_state_db.py
   │  ├── tools
   │  │  ├── conftest.py
   │  │  ├── test_accretion_caps.py
   │  │  ├── test_allowlist_quoted_metachars.py
   │  │  ├── test_annotate_preview_tool.py
   │  │  ├── test_ansi_strip.py
   │  │  ├── test_apply_layout_tool.py
   │  │  ├── test_approval.py
   │  │  ├── test_approval_config_readonly.py
   │  │  ├── test_approval_deny_rules.py
   │  │  ├── test_approval_hook_session_id.py
   │  │  ├── test_approval_interrupt.py
   │  │  ├── test_approval_mode_parity.py
   │  │  ├── test_approval_plugin_hooks.py
   │  │  ├── test_approval_windows.py
   │  │  ├── test_approved_command_clean_slate.py
   │  │  ├── test_async_delegation.py
   │  │  ├── test_async_delegation_fd_leak.py
   │  │  ├── test_audio_container.py
   │  │  ├── test_base_environment.py
   │  │  ├── test_binary_document_write_guard.py
   │  │  ├── test_blocked_command_guidance.py
   │  │  ├── test_blueprints.py
   │  │  ├── test_bot_mode_probe.py
   │  │  ├── test_browser_camofox.py
   │  │  ├── test_browser_camofox_auth.py
   │  │  ├── test_browser_camofox_ensure_tab.py
   │  │  ├── test_browser_camofox_persistence.py
   │  │  ├── test_browser_camofox_private_page_guard.py
   │  │  ├── test_browser_camofox_state.py
   │  │  ├── test_browser_camofox_timeout.py
   │  │  ├── test_browser_cdp_override.py
   │  │  ├── test_browser_cdp_tool.py
   │  │  ├── test_browser_chromium_autoinstall.py
   │  │  ├── test_browser_chromium_check.py
   │  │  ├── test_browser_cleanup.py
   │  │  ├── test_browser_cloud_fallback.py
   │  │  ├── test_browser_cloud_provider_cache.py
   │  │  ├── test_browser_command_timeout_race.py
   │  │  ├── test_browser_console.py
   │  │  ├── test_browser_console_ssrf.py
   │  │  ├── test_browser_content_none_guard.py
   │  │  ├── test_browser_eval_ssrf.py
   │  │  ├── test_browser_eval_supervisor_path.py
   │  │  ├── test_browser_get_images_ssrf.py
   │  │  ├── test_browser_hardening.py
   │  │  ├── test_browser_headed_mode.py
   │  │  ├── test_browser_homebrew_paths.py
   │  │  ├── test_browser_hybrid_routing.py
   │  │  ├── test_browser_lightpanda.py
   │  │  ├── test_browser_npx_warmup.py
   │  │  ├── test_browser_open_timeout.py
   │  │  ├── test_browser_orphan_reaper.py
   │  │  ├── test_browser_private_page_action_guard.py
   │  │  ├── test_browser_secret_exfil.py
   │  │  ├── test_browser_snapshot_ssrf.py
   │  │  ├── test_browser_ssrf_local.py
   │  │  ├── test_browser_supervisor.py
   │  │  ├── test_browser_supervisor_healthcheck.py
   │  │  ├── test_browser_type_redaction.py
   │  │  ├── test_browser_use_cli.py
   │  │  ├── test_browser_use_session_expiry.py
   │  │  ├── test_budget_config.py
   │  │  ├── test_build_subprocess_env.py
   │  │  ├── test_checkpoint_manager.py
   │  │  ├── test_clarify_gateway.py
   │  │  ├── test_clarify_tool.py
   │  │  ├── test_clipboard.py
   │  │  ├── test_cli_approval_exec_ask_leak.py
   │  │  ├── test_close_preview_tool.py
   │  │  ├── test_code_execution.py
   │  │  ├── test_code_execution_modes.py
   │  │  ├── test_code_execution_windows_env.py
   │  │  ├── test_command_guards.py
   │  │  ├── test_computer_use.py
   │  │  ├── test_computer_use_approval_isolation.py
   │  │  ├── test_computer_use_browser_authorization.py
   │  │  ├── test_computer_use_browser_contract_020.py
   │  │  ├── test_computer_use_capture_routing.py
   │  │  ├── test_computer_use_cua_0_10_permissions.py
   │  │  ├── test_computer_use_cua_0_9.py
   │  │  ├── test_computer_use_cua_backend_linux.py
   │  │  ├── test_computer_use_delivery_ladder.py
   │  │  ├── test_computer_use_display_count_guard.py
   │  │  ├── test_computer_use_empty_discovery_diagnosis.py
   │  │  ├── test_computer_use_input_target_guard.py
   │  │  ├── test_computer_use_null_pid_windows.py
   │  │  ├── test_computer_use_placeholder_ids.py
   │  │  ├── test_computer_use_vision_routing.py
   │  │  ├── test_computer_use_zero_bounds.py
   │  │  ├── test_config_null_guard.py
   │  │  ├── test_container_cwd_sanitize.py
   │  │  ├── test_credential_files.py
   │  │  ├── test_credential_pool_env_fallback.py
   │  │  ├── test_cronjob_run_background.py
   │  │  ├── test_cronjob_run_immediate.py
   │  │  ├── test_cronjob_tools.py
   │  │  ├── test_cron_approval_mode.py
   │  │  ├── test_cron_prompt_injection.py
   │  │  ├── test_cross_profile_guard.py
   │  │  ├── test_daemon_pool.py
   │  │  ├── test_daytona_environment.py
   │  │  ├── test_debug_helpers.py
   │  │  ├── test_delegate.py
   │  │  ├── test_delegate_apiserver_background.py
   │  │  ├── test_delegate_batch_validation.py
   │  │  ├── test_delegate_composite_toolsets.py
   │  │  ├── test_delegate_control_actions.py
   │  │  ├── test_delegate_cost_footer.py
   │  │  ├── test_delegate_cron_sync_fallback.py
   │  │  ├── test_delegate_kanban_isolation.py
   │  │  ├── test_delegate_output_schema.py
   │  │  ├── test_delegate_subagent_timeout_diagnostic.py
   │  │  ├── test_delegate_summary_budget.py
   │  │  ├── test_delegate_toolset_scope.py
   │  │  ├── test_delegation_live_log.py
   │  │  ├── test_denial_circuit_breaker.py
   │  │  ├── test_desktop_ui.py
   │  │  ├── test_discord_send_message_caption.py
   │  │  ├── test_discord_tool.py
   │  │  ├── test_dockerfile_immutable_install.py
   │  │  ├── test_dockerfile_node_modules_perms.py
   │  │  ├── test_dockerfile_pid1_reaping.py
   │  │  ├── test_docker_cgroup_limits.py
   │  │  ├── test_docker_config_migrate.py
   │  │  ├── test_docker_daemon_redirect.py
   │  │  ├── test_docker_environment.py
   │  │  ├── test_docker_find.py
   │  │  ├── test_docker_network_config.py
   │  │  ├── test_docker_orphan_reaper_integration.py
   │  │  ├── test_docker_rebootstrap_nous_session.py
   │  │  ├── test_docker_session_isolation.py
   │  │  ├── test_drive_preview_tool.py
   │  │  ├── test_ensure_task_env.py
   │  │  ├── test_env_passthrough.py
   │  │  ├── test_env_probe.py
   │  │  ├── test_execute_code_approval_cluster.py
   │  │  ├── test_execution_flag_detection.py
   │  │  ├── test_fal_common.py
   │  │  ├── test_feishu_tools.py
   │  │  ├── test_file_operations.py
   │  │  ├── test_file_operations_edge_cases.py
   │  │  ├── test_file_ops_cwd_tracking.py
   │  │  ├── test_file_read_guards.py
   │  │  ├── test_file_staleness.py
   │  │  ├── test_file_state_registry.py
   │  │  ├── test_file_sync.py
   │  │  ├── test_file_sync_back.py
   │  │  ├── test_file_sync_perf.py
   │  │  ├── test_file_sync_sigint.py
   │  │  ├── test_file_tools.py
   │  │  ├── test_file_tools_container_config.py
   │  │  ├── test_file_tools_cwd_resolution.py
   │  │  ├── test_file_tools_live.py
   │  │  ├── test_file_tools_tilde_profile.py
   │  │  ├── test_file_write_safety.py
   │  │  ├── test_file_write_surrogate_roundtrip.py
   │  │  ├── test_find_shell.py
   │  │  ├── test_flux3_video_tool.py
   │  │  ├── test_focus_pane_tool.py
   │  │  ├── test_force_dangerous_override.py
   │  │  ├── test_fuzzy_match.py
   │  │  ├── test_gateway_cwd_contract.py
   │  │  ├── test_generation_source_confinement.py
   │  │  ├── test_gnu_long_option_abbreviation_bypass.py
   │  │  ├── test_hardline_blocklist.py
   │  │  ├── test_heartbeat_stale_thresholds.py
   │  │  ├── test_jimmy_subprocess_env.py
   │  │  ├── test_hidden_dir_filter.py
   │  │  ├── test_homeassistant_tool.py
   │  │  ├── test_hook_output_spill.py
   │  │  ├── test_hub_lock_non_utf8_68053.py
   │  │  ├── test_image_generation.py
   │  │  ├── test_image_generation_artifacts.py
   │  │  ├── test_image_generation_env.py
   │  │  ├── test_image_generation_image_to_image.py
   │  │  ├── test_image_generation_interrupt.py
   │  │  ├── test_image_generation_plugin_dispatch.py
   │  │  ├── test_image_source.py
   │  │  ├── test_init_session_cwd_respect.py
   │  │  ├── test_interrupt.py
   │  │  ├── test_interrupted_command_cwd.py
   │  │  ├── test_kanban_comment_injection.py
   │  │  ├── test_kanban_redaction.py
   │  │  ├── test_kanban_tools.py
   │  │  ├── test_lazy_deps.py
   │  │  ├── test_lazy_deps_durable_target.py
   │  │  ├── test_lazy_deps_managed.py
   │  │  ├── test_line_ending_preservation.py
   │  │  ├── test_llm_content_none_guard.py
   │  │  ├── test_local_background_child_hang.py
   │  │  ├── test_local_cwd_permission_fallback.py
   │  │  ├── test_local_env_blocklist.py
   │  │  ├── test_local_env_cwd_recovery.py
   │  │  ├── test_local_env_relative_cwd.py
   │  │  ├── test_local_env_session_leak.py
   │  │  ├── test_local_env_windows_msys.py
   │  │  ├── test_local_interrupt_cleanup.py
   │  │  ├── test_local_shell_init.py
   │  │  ├── test_local_tempdir.py
   │  │  ├── test_managed_browserbase_and_modal.py
   │  │  ├── test_managed_media_gateways.py
   │  │  ├── test_managed_modal_environment.py
   │  │  ├── test_managed_tool_gateway.py
   │  │  ├── test_mcp_bridge_single_failure.py
   │  │  ├── test_mcp_cancelled_error_propagation.py
   │  │  ├── test_mcp_capability_gating.py
   │  │  ├── test_mcp_cimd.py
   │  │  ├── test_mcp_circuit_breaker.py
   │  │  ├── test_mcp_client_cert.py
   │  │  ├── test_mcp_config_whitespace_warning.py
   │  │  ├── test_mcp_dashboard_oauth.py
   │  │  ├── test_mcp_discovery_cross_process.py
   │  │  ├── test_mcp_dynamic_discovery.py
   │  │  ├── test_mcp_elicitation.py
   │  │  ├── test_mcp_empty_error_message.py
   │  │  ├── test_mcp_failure_classification.py
   │  │  ├── test_mcp_identity_header.py
   │  │  ├── test_mcp_image_content.py
   │  │  ├── test_mcp_initial_connect_shutdown.py
   │  │  ├── test_mcp_invalid_url.py
   │  │  ├── test_mcp_lazy_start.py
   │  │  ├── test_mcp_list_pagination.py
   │  │  ├── test_mcp_loop_profile_override.py
   │  │  ├── test_mcp_oauth.py
   │  │  ├── test_mcp_oauth_bidirectional.py
   │  │  ├── test_mcp_oauth_cold_load_expiry.py
   │  │  ├── test_mcp_oauth_integration.py
   │  │  ├── test_mcp_oauth_manager.py
   │  │  ├── test_mcp_oauth_metadata.py
   │  │  ├── test_mcp_oauth_user_agent.py
   │  │  ├── test_mcp_parked_self_probe.py
   │  │  ├── test_mcp_poll_loop_oom_integration.py
   │  │  ├── test_mcp_preflight_content_type.py
   │  │  ├── test_mcp_probe.py
   │  │  ├── test_mcp_protocol_negotiation.py
   │  │  ├── test_mcp_rapid_drop_budget.py
   │  │  ├── test_mcp_reconnect_log_hygiene.py
   │  │  ├── test_mcp_reconnect_retry_reset.py
   │  │  ├── test_mcp_reconnect_signal.py
   │  │  ├── test_mcp_register_wakes_stale.py
   │  │  ├── test_mcp_resource_content.py
   │  │  ├── test_mcp_result_size_limit.py
   │  │  ├── test_mcp_schema_cache.py
   │  │  ├── test_mcp_schema_cache_ttl.py
   │  │  ├── test_mcp_server_log_notifications.py
   │  │  ├── test_mcp_sse_transport.py
   │  │  ├── test_mcp_stability.py
   │  │  ├── test_mcp_stdio_encoding_handler.py
   │  │  ├── test_mcp_stdio_init_timeout.py
   │  │  ├── test_mcp_stdio_watchdog.py
   │  │  ├── test_mcp_streamable_http_arity.py
   │  │  ├── test_mcp_structured_content.py
   │  │  ├── test_mcp_tool.py
   │  │  ├── test_mcp_tool_401_handling.py
   │  │  ├── test_mcp_tool_issue_948.py
   │  │  ├── test_mcp_tool_session_expired.py
   │  │  ├── test_mcp_transport_group_reconnect.py
   │  │  ├── test_mcp_trust_gating.py
   │  │  ├── test_mcp_utility_capability_gating.py
   │  │  ├── test_media_caption_split.py
   │  │  ├── test_memory_tool.py
   │  │  ├── test_memory_tool_import_fallback.py
   │  │  ├── test_memory_tool_schema.py
   │  │  ├── test_microsoft_graph_auth.py
   │  │  ├── test_microsoft_graph_client.py
   │  │  ├── test_modal_bulk_upload.py
   │  │  ├── test_modal_sandbox_fixes.py
   │  │  ├── test_modal_snapshot_isolation.py
   │  │  ├── test_notify_on_complete.py
   │  │  ├── test_open_preview_tool.py
   │  │  ├── test_osv_check.py
   │  │  ├── test_parse_env_var.py
   │  │  ├── test_patch_already_applied.py
   │  │  ├── test_patch_failure_tracking.py
   │  │  ├── test_patch_multimatch_locations.py
   │  │  ├── test_patch_parser.py
   │  │  ├── test_patch_ws_diagnosis.py
   │  │  ├── test_plugin_guard.py
   │  │  ├── test_pre_transcription_hook.py
   │  │  ├── test_process_registry.py
   │  │  ├── test_process_registry_write_stdin_surrogates.py
   │  │  ├── test_process_wait_clarity.py
   │  │  ├── test_pr_6656_regressions.py
   │  │  ├── test_react_to_message_tool.py
   │  │  ├── test_read_binary_type_disclosure.py
   │  │  ├── test_read_extract.py
   │  │  ├── test_read_file_utf8_binary_regression.py
   │  │  ├── test_read_loop_detection.py
   │  │  ├── test_read_past_eof_note.py
   │  │  ├── test_read_preview_tool.py
   │  │  ├── test_read_shell_line_clamp.py
   │  │  ├── test_read_special_file_guard.py
   │  │  ├── test_read_unicode_filename_retry.py
   │  │  ├── test_read_window_tool.py
   │  │  ├── test_refresh_agent_mcp_tools.py
   │  │  ├── test_registry.py
   │  │  ├── test_request_tool_approval.py
   │  │  ├── test_resolve_path.py
   │  │  ├── test_restored_delegation_ownership.py
   │  │  ├── test_rollback_all_directories.py
   │  │  ├── test_sandbox_failure_hints.py
   │  │  ├── test_schema_sanitizer.py
   │  │  ├── test_search_auto_multiline.py
   │  │  ├── test_search_budget_truncation.py
   │  │  ├── test_search_error_guard.py
   │  │  ├── test_search_hidden_dirs.py
   │  │  ├── test_search_zero_match_and_multipath.py
   │  │  ├── test_self_repo_guard.py
   │  │  ├── test_send_message_missing_platforms.py
   │  │  ├── test_send_message_plugin_extensibility.py
   │  │  ├── test_send_message_react.py
   │  │  ├── test_send_message_slack.py
   │  │  ├── test_send_message_target_parse.py
   │  │  ├── test_send_message_telegram_proxy.py
   │  │  ├── test_send_message_tool.py
   │  │  ├── test_session_cwd_store.py
   │  │  ├── test_session_search.py
   │  │  ├── test_setup_mcp_tool.py
   │  │  ├── test_shared_container_task_id.py
   │  │  ├── test_shell_bypass_denylist.py
   │  │  ├── test_signal_media.py
   │  │  ├── test_single_query_approval_mode.py
   │  │  ├── test_singularity_preflight.py
   │  │  ├── test_skillevaluator_scan.py
   │  │  ├── test_skills_ast_audit.py
   │  │  ├── test_skills_guard.py
   │  │  ├── test_skills_hub.py
   │  │  ├── test_skills_hub_browse_sh.py
   │  │  ├── test_skills_hub_clawhub.py
   │  │  ├── test_skills_list_modified_diff.py
   │  │  ├── test_skills_sync.py
   │  │  ├── test_skills_sync_client.py
   │  │  ├── test_skills_tool.py
   │  │  ├── test_skills_tool_discovery_cache.py
   │  │  ├── test_skills_tool_profile_scope.py
   │  │  ├── test_skill_bundle_provenance.py
   │  │  ├── test_skill_env_passthrough.py
   │  │  ├── test_skill_improvements.py
   │  │  ├── test_skill_ledger.py
   │  │  ├── test_skill_linter.py
   │  │  ├── test_skill_manager_tool.py
   │  │  ├── test_skill_provenance.py
   │  │  ├── test_skill_size_limits.py
   │  │  ├── test_skill_usage.py
   │  │  ├── test_skill_view_dedup.py
   │  │  ├── test_skill_view_path_check.py
   │  │  ├── test_skill_view_traversal.py
   │  │  ├── test_slack_send_message_media.py
   │  │  ├── test_slash_confirm.py
   │  │  ├── test_smart_approval_injection.py
   │  │  ├── test_smart_approval_policy.py
   │  │  ├── test_snapshot_multiline_session_env_injection.py
   │  │  ├── test_snapshot_session_id_leak.py
   │  │  ├── test_spill_safety.py
   │  │  ├── test_spotify_client.py
   │  │  ├── test_ssh_bulk_upload.py
   │  │  ├── test_ssh_environment.py
   │  │  ├── test_stage2_hook_seed_one_symlinks.py
   │  │  ├── test_stage2_hook_symlink_chown.py
   │  │  ├── test_startup_latency_regressions.py
   │  │  ├── test_strict_provider_selection.py
   │  │  ├── test_stt_cloud_trim.py
   │  │  ├── test_stt_default_language.py
   │  │  ├── test_stt_idle_unload.py
   │  │  ├── test_stt_language_resolution.py
   │  │  ├── test_stt_silence_hallucinations.py
   │  │  ├── test_subagent_steer.py
   │  │  ├── test_subagent_worktree.py
   │  │  ├── test_subprocess_stdin_guard.py
   │  │  ├── test_subprocess_utf8_encoding.py
   │  │  ├── test_symlink_prefix_confusion.py
   │  │  ├── test_sync_back_backends.py
   │  │  ├── test_telegram_send_message_caption.py
   │  │  ├── test_terminal_compound_background.py
   │  │  ├── test_terminal_config_env_sync.py
   │  │  ├── test_terminal_cwd_echo.py
   │  │  ├── test_terminal_degraded_mode.py
   │  │  ├── test_terminal_env_bridge.py
   │  │  ├── test_terminal_error_redaction.py
   │  │  ├── test_terminal_exit_semantics.py
   │  │  ├── test_terminal_foreground_timeout_cap.py
   │  │  ├── test_terminal_heredoc_background_guard.py
   │  │  ├── test_terminal_hints.py
   │  │  ├── test_terminal_none_command_guard.py
   │  │  ├── test_terminal_output_transform_hook.py
   │  │  ├── test_terminal_requirements.py
   │  │  ├── test_terminal_self_repo_guard.py
   │  │  ├── test_terminal_signal_exit.py
   │  │  ├── test_terminal_task_cwd.py
   │  │  ├── test_terminal_timeout_output.py
   │  │  ├── test_terminal_tool.py
   │  │  ├── test_terminal_tool_exception_redaction.py
   │  │  ├── test_terminal_tool_pty_fallback.py
   │  │  ├── test_terminal_tool_requirements.py
   │  │  ├── test_terminal_truncation_spill.py
   │  │  ├── test_termux_api_detection.py
   │  │  ├── test_threaded_process_handle.py
   │  │  ├── test_threat_patterns.py
   │  │  ├── test_tirith_security.py
   │  │  ├── test_todo_tool.py
   │  │  ├── test_todo_tool_type_coercion.py
   │  │  ├── test_tool_backend_helpers.py
   │  │  ├── test_tool_output_limits.py
   │  │  ├── test_tool_result_storage.py
   │  │  ├── test_tool_search.py
   │  │  ├── test_tool_search_context_provider.py
   │  │  ├── test_tour_tool.py
   │  │  ├── test_transcription.py
   │  │  ├── test_transcription_command_providers.py
   │  │  ├── test_transcription_deepinfra.py
   │  │  ├── test_transcription_dotenv_fallback.py
   │  │  ├── test_transcription_plugin_dispatch.py
   │  │  ├── test_transcription_tools.py
   │  │  ├── test_tts_command_providers.py
   │  │  ├── test_tts_container_repair.py
   │  │  ├── test_tts_deepinfra.py
   │  │  ├── test_tts_dotenv_fallback.py
   │  │  ├── test_tts_gemini.py
   │  │  ├── test_tts_instructions.py
   │  │  ├── test_tts_kittentts.py
   │  │  ├── test_tts_long_form_chunking.py
   │  │  ├── test_tts_macos_output.py
   │  │  ├── test_tts_max_text_length.py
   │  │  ├── test_tts_minimax_region.py
   │  │  ├── test_tts_mistral.py
   │  │  ├── test_tts_model_cache_lru.py
   │  │  ├── test_tts_openai_config.py
   │  │  ├── test_tts_opus_routing.py
   │  │  ├── test_tts_output_timestamp.py
   │  │  ├── test_tts_path_traversal.py
   │  │  ├── test_tts_piper.py
   │  │  ├── test_tts_plugin_dispatch.py
   │  │  ├── test_tts_prepare_spoken.py
   │  │  ├── test_tts_provider_base_urls.py
   │  │  ├── test_tts_pythonpath_fallback.py
   │  │  ├── test_tts_response_body_cap.py
   │  │  ├── test_tts_speed.py
   │  │  ├── test_tts_streaming.py
   │  │  ├── test_tts_streaming_e2e.py
   │  │  ├── test_tts_text_normalize.py
   │  │  ├── test_tts_xai_speech_tags.py
   │  │  ├── test_unicode_tag_strip.py
   │  │  ├── test_url_safety.py
   │  │  ├── test_utf16_read.py
   │  │  ├── test_vercel_sandbox_environment.py
   │  │  ├── test_video_analyze.py
   │  │  ├── test_video_generation_dispatch.py
   │  │  ├── test_video_generation_dynamic_schema.py
   │  │  ├── test_video_generation_tool_surface_matrix.py
   │  │  ├── test_vision_native_fast_path.py
   │  │  ├── test_vision_region.py
   │  │  ├── test_vision_scale_disclosure.py
   │  │  ├── test_vision_tools.py
   │  │  ├── test_voice_cli_integration.py
   │  │  ├── test_voice_credential_pool_resolution.py
   │  │  ├── test_voice_mode.py
   │  │  ├── test_voice_mode_playback_env_scrub.py
   │  │  ├── test_voice_stop_phrase.py
   │  │  ├── test_voice_thinking_sound.py
   │  │  ├── test_voice_tts_echo_guard.py
   │  │  ├── test_voice_wsl_pipewire.py
   │  │  ├── test_wake_word.py
   │  │  ├── test_watch_patterns.py
   │  │  ├── test_web_extract_robustness.py
   │  │  ├── test_web_keyless_fallback.py
   │  │  ├── test_web_keyless_rescue.py
   │  │  ├── test_web_providers.py
   │  │  ├── test_web_providers_brave_free.py
   │  │  ├── test_web_providers_ddgs.py
   │  │  ├── test_web_providers_searxng.py
   │  │  ├── test_web_providers_xai.py
   │  │  ├── test_web_tools_config.py
   │  │  ├── test_web_tools_dict_urls.py
   │  │  ├── test_web_tools_tavily.py
   │  │  ├── test_web_tools_truncate.py
   │  │  ├── test_whatsapp_send_message_media.py
   │  │  ├── test_windows_agent_loop_papercuts.py
   │  │  ├── test_windows_compat.py
   │  │  ├── test_windows_native_support.py
   │  │  ├── test_working_diff.py
   │  │  ├── test_write_approval.py
   │  │  ├── test_write_deny.py
   │  │  ├── test_write_file_syntax_gate.py
   │  │  ├── test_write_verification.py
   │  │  ├── test_xai_http_credentials.py
   │  │  ├── test_xai_http_storage.py
   │  │  ├── test_x_search_tool.py
   │  │  ├── test_yolo_mode.py
   │  │  ├── test_zombie_process_cleanup.py
   │  │  └── __init__.py
   │  ├── tui_gateway
   │  │  ├── test_attach_does_not_wait_for_agent.py
   │  │  ├── test_auto_continue.py
   │  │  ├── test_billing_rpc.py
   │  │  ├── test_change_watcher.py
   │  │  ├── test_codex_app_server_live_events.py
   │  │  ├── test_cold_start_gil_stall.py
   │  │  ├── test_compaction_status.py
   │  │  ├── test_compress_lock_skip.py
   │  │  ├── test_compute_host.py
   │  │  ├── test_compute_host_phase1.py
   │  │  ├── test_custom_provider_session_persistence.py
   │  │  ├── test_delegation_session_lifecycle.py
   │  │  ├── test_entry_import_off_main_thread.py
   │  │  ├── test_entry_picker_prewarm.py
   │  │  ├── test_entry_sys_path.py
   │  │  ├── test_ephemeral_profile_override.py
   │  │  ├── test_failed_turn_retention.py
   │  │  ├── test_fast_session_scope.py
   │  │  ├── test_finalize_session_persist.py
   │  │  ├── test_gateway_owned_session_reap.py
   │  │  ├── test_goal_command.py
   │  │  ├── test_gui_surface_toolsets.py
   │  │  ├── test_hud_surface_note.py
   │  │  ├── test_image_ref_message.py
   │  │  ├── test_image_routing_stale_model.py
   │  │  ├── test_inline_rpc_gil_starvation.py
   │  │  ├── test_interim_assistant_callback.py
   │  │  ├── test_iso_certify_seam.py
   │  │  ├── test_kanban_notify_poller.py
   │  │  ├── test_loop_command.py
   │  │  ├── test_make_agent_personality_prompt.py
   │  │  ├── test_make_agent_provider.py
   │  │  ├── test_mcp_late_refresh_thread_owner.py
   │  │  ├── test_mcp_profile_rpcs.py
   │  │  ├── test_mcp_reload_rev.py
   │  │  ├── test_moa_reference_emit.py
   │  │  ├── test_model_switch_marker_role.py
   │  │  ├── test_personality_clobbers_system_prompt.py
   │  │  ├── test_pet_generate_rpc.py
   │  │  ├── test_plugins_manage_install.py
   │  │  ├── test_profiles_list_preferred_session.py
   │  │  ├── test_profiles_list_worker_session.py
   │  │  ├── test_projects_rpc.py
   │  │  ├── test_project_tree.py
   │  │  ├── test_prompt_accept_logging.py
   │  │  ├── test_protocol.py
   │  │  ├── test_reasoning_config_per_model.py
   │  │  ├── test_reasoning_session_scope.py
   │  │  ├── test_render.py
   │  │  ├── test_review_summary_callback.py
   │  │  ├── test_session_cwd_follow.py
   │  │  ├── test_session_db_ownership_teardown.py
   │  │  ├── test_session_git_metadata_generation.py
   │  │  ├── test_session_hidden_rpc.py
   │  │  ├── test_session_id_injection.py
   │  │  ├── test_session_images_dir.py
   │  │  ├── test_session_platform_resolution.py
   │  │  ├── test_session_reclaim_notify.py
   │  │  ├── test_session_resume_db_ownership.py
   │  │  ├── test_slash_fuzzy.py
   │  │  ├── test_slash_worker_ansi.py
   │  │  ├── test_slash_worker_mcp_discovery.py
   │  │  ├── test_slash_worker_profile_home.py
   │  │  ├── test_slash_worker_sys_path.py
   │  │  ├── test_subagent_child_mirror.py
   │  │  ├── test_subprocess_encoding.py
   │  │  ├── test_tour_bridge_fail_fast.py
   │  │  ├── test_undo_command.py
   │  │  ├── test_wait_for_mcp_discovery.py
   │  │  └── __init__.py
   │  ├── verify
   │  │  ├── test_environment_and_runner.py
   │  │  ├── test_ledger_and_nudge_integration.py
   │  │  ├── test_recipes.py
   │  │  └── test_verify_cmd.py
   │  ├── website
   │  │  ├── test_extract_skills.py
   │  │  ├── test_generate_llms_txt.py
   │  │  ├── test_generate_skill_docs.py
   │  │  └── __init__.py
   │  └── __init__.py
  ├── tests-js
   │  ├── allow-scripts-sync.test.ts
   │  ├── assistant-ui-tap-compat.test.ts
   │  ├── bootstrap-installer-stage-timer.test.ts
   │  ├── desktop-mac-entitlements.test.ts
   │  ├── eslint.config.mjs
   │  ├── package-json-lazy-deps.test.ts
   │  ├── package.json
   │  ├── react-dom-pair-compat.test.ts
   │  ├── tsconfig.json
   │  └── vitest.config.ts
  ├── tools
   │  ├── annotate_preview_tool.py
   │  ├── ansi_strip.py
   │  ├── apply_layout_tool.py
   │  ├── approval.py
   │  ├── async_delegation.py
   │  ├── audio_container.py
   │  ├── binary_extensions.py
   │  ├── blueprints.py
   │  ├── bot_mode_probe.py
   │  ├── browser_camofox.py
   │  ├── browser_camofox_state.py
   │  ├── browser_cdp_tool.py
   │  ├── browser_dialog_tool.py
   │  ├── browser_supervisor.py
   │  ├── browser_tool.py
   │  ├── browser_use_cli.py
   │  ├── budget_config.py
   │  ├── checkpoint_manager.py
   │  ├── clarify_gateway.py
   │  ├── clarify_tool.py
   │  ├── close_preview_tool.py
   │  ├── close_terminal_tool.py
   │  ├── code_execution_tool.py
   │  ├── computer_use
   │  │  ├── backend.py
   │  │  ├── browser_route.py
   │  │  ├── cua_backend.py
   │  │  ├── doctor.py
   │  │  ├── permissions.py
   │  │  ├── schema.py
   │  │  ├── tool.py
   │  │  ├── vision_routing.py
   │  │  └── __init__.py
   │  ├── computer_use_tool.py
   │  ├── credential_files.py
   │  ├── cronjob_tools.py
   │  ├── daemon_pool.py
   │  ├── debug_helpers.py
   │  ├── delegate_tool.py
   │  ├── delegation_live_log.py
   │  ├── delegation_output_schema.py
   │  ├── desktop_ui.py
   │  ├── discord_tool.py
   │  ├── drive_preview_tool.py
   │  ├── environments
   │  │  ├── base.py
   │  │  ├── daytona.py
   │  │  ├── docker.py
   │  │  ├── file_sync.py
   │  │  ├── local.py
   │  │  ├── managed_modal.py
   │  │  ├── modal.py
   │  │  ├── modal_utils.py
   │  │  ├── singularity.py
   │  │  ├── ssh.py
   │  │  ├── vercel_sandbox.py
   │  │  └── __init__.py
   │  ├── env_passthrough.py
   │  ├── env_probe.py
   │  ├── fal_common.py
   │  ├── feishu_doc_tool.py
   │  ├── feishu_drive_tool.py
   │  ├── file_operations.py
   │  ├── file_state.py
   │  ├── file_tools.py
   │  ├── flux3_video_tool.py
   │  ├── focus_pane_tool.py
   │  ├── fuzzy_match.py
   │  ├── homeassistant_tool.py
   │  ├── hook_output_spill.py
   │  ├── image_generation_tool.py
   │  ├── image_source.py
   │  ├── interrupt.py
   │  ├── kanban_tools.py
   │  ├── lazy_deps.py
   │  ├── managed_tool_gateway.py
   │  ├── mcp_dashboard_oauth.py
   │  ├── mcp_oauth.py
   │  ├── mcp_oauth_manager.py
   │  ├── mcp_schema_cache.py
   │  ├── mcp_stdio_watchdog.py
   │  ├── mcp_tool.py
   │  ├── memory_tool.py
   │  ├── microsoft_graph_auth.py
   │  ├── microsoft_graph_client.py
   │  ├── neutts_samples
   │  │  ├── jo.txt
   │  │  └── jo.wav
   │  ├── neutts_synth.py
   │  ├── openrouter_client.py
   │  ├── open_preview_tool.py
   │  ├── osv_check.py
   │  ├── patch_parser.py
   │  ├── path_security.py
   │  ├── plugin_guard.py
   │  ├── process_registry.py
   │  ├── project_tools.py
   │  ├── react_to_message_tool.py
   │  ├── read_extract.py
   │  ├── read_preview_tool.py
   │  ├── read_terminal_tool.py
   │  ├── read_window_tool.py
   │  ├── registry.py
   │  ├── schema_sanitizer.py
   │  ├── self_repo_guard.py
   │  ├── send_message_tool.py
   │  ├── session_search_tool.py
   │  ├── setup_mcp_tool.py
   │  ├── shell_heredoc.py
   │  ├── skillevaluator_scan.py
   │  ├── skills_ast_audit.py
   │  ├── skills_guard.py
   │  ├── skills_hub.py
   │  ├── skills_sync.py
   │  ├── skills_sync_client.py
   │  ├── skills_tool.py
   │  ├── skill_ledger.py
   │  ├── skill_linter.py
   │  ├── skill_manager_tool.py
   │  ├── skill_provenance.py
   │  ├── skill_usage.py
   │  ├── slash_confirm.py
   │  ├── spill_safety.py
   │  ├── subagent_worktree.py
   │  ├── terminal_hints.py
   │  ├── terminal_tool.py
   │  ├── thread_context.py
   │  ├── threat_patterns.py
   │  ├── tirith_security.py
   │  ├── todo_tool.py
   │  ├── tool_backend_helpers.py
   │  ├── tool_output_limits.py
   │  ├── tool_result_storage.py
   │  ├── tool_search.py
   │  ├── tour_tool.py
   │  ├── transcription_tools.py
   │  ├── tts_streaming.py
   │  ├── tts_text_normalize.py
   │  ├── tts_tool.py
   │  ├── url_safety.py
   │  ├── video_generation_tool.py
   │  ├── vision_tools.py
   │  ├── voice_mode.py
   │  ├── wakewords
   │  │  ├── hey_jimmy.onnx
   │  │  ├── hey_jimmy.tflite
   │  │  └── README.md
   │  ├── wake_word.py
   │  ├── website_policy.py
   │  ├── web_tools.py
   │  ├── working_diff.py
   │  ├── write_approval.py
   │  ├── xai_http.py
   │  ├── xai_video_tools.py
   │  ├── x_search_tool.py
   │  ├── yuanbao_tools.py
   │  └── __init__.py
  ├── toolsets.py
  ├── toolset_distributions.py
  ├── trajectory_compressor.py
  ├── tui_gateway
   │  ├── compute_host.py
   │  ├── entry.py
   │  ├── event_publisher.py
   │  ├── git_probe.py
   │  ├── host_supervisor.py
   │  ├── loop_noise.py
   │  ├── mcp_oauth_sessions.py
   │  ├── mcp_rpc_helpers.py
   │  ├── methods_complete.py
   │  ├── methods_config.py
   │  ├── methods_images.py
   │  ├── methods_profiles.py
   │  ├── methods_prompt.py
   │  ├── methods_session.py
   │  ├── methods_tools.py
   │  ├── method_ctx.py
   │  ├── project_tree.py
   │  ├── render.py
   │  ├── server.py
   │  ├── slash_fuzzy.py
   │  ├── slash_worker.py
   │  ├── synthetic_turn.py
   │  ├── transport.py
   │  ├── turn_marker.py
   │  ├── ws.py
   │  ├── _stdin_recovery.py
   │  └── __init__.py
  ├── ui-tui
   │  ├── eslint.config.mjs
   │  ├── package.json
   │  ├── packages
   │  │  └── jimmy-ink
   │  │    ├── ambient.d.ts
   │  │    ├── index.d.ts
   │  │    ├── index.js
   │  │    ├── package.json
   │  │    ├── src
   │  │     │  ├── bootstrap
   │  │     │  │  └── state.ts
   │  │     │  ├── entry-exports.ts
   │  │     │  ├── hooks
   │  │     │  │  ├── use-stderr.ts
   │  │     │  │  └── use-stdout.ts
   │  │     │  ├── ink
   │  │     │  │  ├── absolute-in-zero-height-box.test.tsx
   │  │     │  │  ├── ansi-transition.test.ts
   │  │     │  │  ├── ansi-transition.ts
   │  │     │  │  ├── Ansi.tsx
   │  │     │  │  ├── app-mouse-watchdog.test.ts
   │  │     │  │  ├── app-mouse.test.ts
   │  │     │  │  ├── app-rawmode-mouse.test.ts
   │  │     │  │  ├── app-stdin-recovery.test.ts
   │  │     │  │  ├── bidi.ts
   │  │     │  │  ├── cache-eviction.ts
   │  │     │  │  ├── clearTerminal.ts
   │  │     │  │  ├── colorize.test.ts
   │  │     │  │  ├── colorize.ts
   │  │     │  │  ├── components
   │  │     │  │  │  ├── AlternateScreen.tsx
   │  │     │  │  │  ├── App.focus.test.tsx
   │  │     │  │  │  ├── App.tsx
   │  │     │  │  │  ├── AppContext.ts
   │  │     │  │  │  ├── Box.tsx
   │  │     │  │  │  ├── Button.tsx
   │  │     │  │  │  ├── ClockContext.tsx
   │  │     │  │  │  ├── CursorAdvanceContext.ts
   │  │     │  │  │  ├── CursorDeclarationContext.ts
   │  │     │  │  │  ├── ErrorOverview.tsx
   │  │     │  │  │  ├── Link.tsx
   │  │     │  │  │  ├── Newline.tsx
   │  │     │  │  │  ├── NoSelect.tsx
   │  │     │  │  │  ├── RawAnsi.tsx
   │  │     │  │  │  ├── ScrollBox.tsx
   │  │     │  │  │  ├── Spacer.tsx
   │  │     │  │  │  ├── StdinContext.ts
   │  │     │  │  │  ├── TerminalFocusContext.tsx
   │  │     │  │  │  ├── TerminalSizeContext.tsx
   │  │     │  │  │  ├── Text.test.ts
   │  │     │  │  │  └── Text.tsx
   │  │     │  │  ├── constants.ts
   │  │     │  │  ├── cursor.ts
   │  │     │  │  ├── devtools.ts
   │  │     │  │  ├── dom.ts
   │  │     │  │  ├── events
   │  │     │  │  │  ├── click-event.ts
   │  │     │  │  │  ├── cmd-shortcuts.test.ts
   │  │     │  │  │  ├── dispatcher.ts
   │  │     │  │  │  ├── emitter.ts
   │  │     │  │  │  ├── event-handlers.ts
   │  │     │  │  │  ├── event.ts
   │  │     │  │  │  ├── focus-event.ts
   │  │     │  │  │  ├── input-event.ts
   │  │     │  │  │  ├── keyboard-event.ts
   │  │     │  │  │  ├── mouse-event.ts
   │  │     │  │  │  ├── paste-event.ts
   │  │     │  │  │  ├── resize-event.ts
   │  │     │  │  │  ├── terminal-event.ts
   │  │     │  │  │  └── terminal-focus-event.ts
   │  │     │  │  ├── focus.ts
   │  │     │  │  ├── frame.ts
   │  │     │  │  ├── get-max-width.ts
   │  │     │  │  ├── global.d.ts
   │  │     │  │  ├── hit-test.test.ts
   │  │     │  │  ├── hit-test.ts
   │  │     │  │  ├── hooks
   │  │     │  │  │  ├── use-animation-frame.ts
   │  │     │  │  │  ├── use-app.ts
   │  │     │  │  │  ├── use-cursor-advance.ts
   │  │     │  │  │  ├── use-declared-cursor.ts
   │  │     │  │  │  ├── use-external-process.ts
   │  │     │  │  │  ├── use-input.ts
   │  │     │  │  │  ├── use-interval.ts
   │  │     │  │  │  ├── use-search-highlight.ts
   │  │     │  │  │  ├── use-selection.ts
   │  │     │  │  │  ├── use-stdin.ts
   │  │     │  │  │  ├── use-tab-status.ts
   │  │     │  │  │  ├── use-terminal-focus.ts
   │  │     │  │  │  ├── use-terminal-title.ts
   │  │     │  │  │  └── use-terminal-viewport.ts
   │  │     │  │  ├── hyperlinkHover.ts
   │  │     │  │  ├── ink-backpressure.test.ts
   │  │     │  │  ├── ink-cursor-advance.test.ts
   │  │     │  │  ├── ink-focus-redraw.test.ts
   │  │     │  │  ├── ink-resize.test.ts
   │  │     │  │  ├── ink.tsx
   │  │     │  │  ├── instances.ts
   │  │     │  │  ├── layout
   │  │     │  │  │  ├── engine.ts
   │  │     │  │  │  ├── geometry.ts
   │  │     │  │  │  ├── node.ts
   │  │     │  │  │  └── yoga.ts
   │  │     │  │  ├── line-width-cache.ts
   │  │     │  │  ├── log-update.test.ts
   │  │     │  │  ├── log-update.ts
   │  │     │  │  ├── lru.ts
   │  │     │  │  ├── measure-element.ts
   │  │     │  │  ├── measure-text.ts
   │  │     │  │  ├── node-cache.ts
   │  │     │  │  ├── optimizer.ts
   │  │     │  │  ├── osc-response-chain.test.ts
   │  │     │  │  ├── output.ts
   │  │     │  │  ├── parse-keypress-drop-probe.test.ts
   │  │     │  │  ├── parse-keypress-noregress.test.ts
   │  │     │  │  ├── parse-keypress.test.ts
   │  │     │  │  ├── parse-keypress.ts
   │  │     │  │  ├── reconciler.ts
   │  │     │  │  ├── render-border.test.ts
   │  │     │  │  ├── render-border.ts
   │  │     │  │  ├── render-node-to-output.ts
   │  │     │  │  ├── render-to-screen.ts
   │  │     │  │  ├── renderer.ts
   │  │     │  │  ├── root.ts
   │  │     │  │  ├── screen.ts
   │  │     │  │  ├── searchHighlight.ts
   │  │     │  │  ├── selection.test.ts
   │  │     │  │  ├── selection.ts
   │  │     │  │  ├── squash-text-nodes.ts
   │  │     │  │  ├── stringWidth.ts
   │  │     │  │  ├── styles.ts
   │  │     │  │  ├── supports-hyperlinks.ts
   │  │     │  │  ├── tabstops.ts
   │  │     │  │  ├── terminal-background.test.ts
   │  │     │  │  ├── terminal-focus-state.ts
   │  │     │  │  ├── terminal-querier.ts
   │  │     │  │  ├── terminal.test.ts
   │  │     │  │  ├── terminal.ts
   │  │     │  │  ├── termio
   │  │     │  │  │  ├── ansi.ts
   │  │     │  │  │  ├── csi.ts
   │  │     │  │  │  ├── dec.ts
   │  │     │  │  │  ├── esc.ts
   │  │     │  │  │  ├── osc.test.ts
   │  │     │  │  │  ├── osc.ts
   │  │     │  │  │  ├── parser.test.ts
   │  │     │  │  │  ├── parser.ts
   │  │     │  │  │  ├── sgr.ts
   │  │     │  │  │  ├── tokenize.test.ts
   │  │     │  │  │  ├── tokenize.ts
   │  │     │  │  │  └── types.ts
   │  │     │  │  ├── termio.ts
   │  │     │  │  ├── useTerminalNotification.ts
   │  │     │  │  ├── warn.ts
   │  │     │  │  ├── widest-line.ts
   │  │     │  │  ├── wrap-text.test.ts
   │  │     │  │  ├── wrap-text.ts
   │  │     │  │  └── wrapAnsi.ts
   │  │     │  ├── native-ts
   │  │     │  │  └── yoga-layout
   │  │     │  │    ├── enums.ts
   │  │     │  │    └── index.ts
   │  │     │  └── utils
   │  │     │    ├── debug.ts
   │  │     │    ├── earlyInput.ts
   │  │     │    ├── env.ts
   │  │     │    ├── envUtils.ts
   │  │     │    ├── execFileNoThrow.test.ts
   │  │     │    ├── execFileNoThrow.ts
   │  │     │    ├── fullscreen.ts
   │  │     │    ├── intl.ts
   │  │     │    ├── log.ts
   │  │     │    ├── semver.ts
   │  │     │    └── sliceAnsi.ts
   │  │    ├── text-input.d.ts
   │  │    ├── text-input.js
   │  │    └── tsconfig.json
   │  ├── README.md
   │  ├── scripts
   │  │  ├── bench-history-scroll.tsx
   │  │  ├── bench-streaming-md.tsx
   │  │  ├── billing-fixtures.tsx
   │  │  ├── build.mjs
   │  │  ├── profile-tui.mjs
   │  │  └── visual
   │  │    ├── paths.mjs
   │  │    ├── render.tsx
   │  │    ├── run.mjs
   │  │    └── shot.mjs
   │  ├── src
   │  │  ├── app
   │  │  │  ├── createGatewayEventHandler.ts
   │  │  │  ├── createSlashHandler.ts
   │  │  │  ├── delegationStore.ts
   │  │  │  ├── gatewayContext.tsx
   │  │  │  ├── gatewayRecovery.ts
   │  │  │  ├── inputSelectionStore.ts
   │  │  │  ├── interfaces.ts
   │  │  │  ├── overlayStore.ts
   │  │  │  ├── petFlashStore.ts
   │  │  │  ├── scroll.ts
   │  │  │  ├── sessionResumeView.test.ts
   │  │  │  ├── sessionResumeView.ts
   │  │  │  ├── setupHandoff.ts
   │  │  │  ├── slash
   │  │  │  │  ├── commands
   │  │  │  │  │  ├── core.ts
   │  │  │  │  │  ├── debug.ts
   │  │  │  │  │  ├── ops.ts
   │  │  │  │  │  ├── session.ts
   │  │  │  │  │  ├── setup.ts
   │  │  │  │  │  ├── subscription.ts
   │  │  │  │  │  ├── topup.ts
   │  │  │  │  │  └── wake.ts
   │  │  │  │  ├── fuzzyScore.test.ts
   │  │  │  │  ├── fuzzyScore.ts
   │  │  │  │  ├── registry.ts
   │  │  │  │  └── types.ts
   │  │  │  ├── spawnHistoryStore.ts
   │  │  │  ├── submissionCore.ts
   │  │  │  ├── turnController.ts
   │  │  │  ├── turnStore.ts
   │  │  │  ├── uiStore.ts
   │  │  │  ├── useBatteryPoll.ts
   │  │  │  ├── useComposerState.ts
   │  │  │  ├── useConfigSync.ts
   │  │  │  ├── useInputHandlers.ts
   │  │  │  ├── useLongRunToolCharms.ts
   │  │  │  ├── useMainApp.ts
   │  │  │  ├── usePet.ts
   │  │  │  ├── useSessionLifecycle.ts
   │  │  │  ├── useSubmission.ts
   │  │  │  └── wakeState.ts
   │  │  ├── app.tsx
   │  │  ├── banner.ts
   │  │  ├── components
   │  │  │  ├── accordion.tsx
   │  │  │  ├── activeSessionSwitcher.tsx
   │  │  │  ├── agentsOverlay.tsx
   │  │  │  ├── appChrome.tsx
   │  │  │  ├── appLayout.tsx
   │  │  │  ├── appOverlays.tsx
   │  │  │  ├── billingOverlay.tsx
   │  │  │  ├── branding.tsx
   │  │  │  ├── fpsOverlay.tsx
   │  │  │  ├── gridStreamsDemo.tsx
   │  │  │  ├── gridTestOverlay.tsx
   │  │  │  ├── helpHint.tsx
   │  │  │  ├── journey.tsx
   │  │  │  ├── loaders.tsx
   │  │  │  ├── markdown.tsx
   │  │  │  ├── maskedPrompt.tsx
   │  │  │  ├── messageLine.tsx
   │  │  │  ├── modelPicker.tsx
   │  │  │  ├── overlay.tsx
   │  │  │  ├── overlayControls.tsx
   │  │  │  ├── overlayPrimitives.tsx
   │  │  │  ├── overlayScrollbar.tsx
   │  │  │  ├── petPicker.tsx
   │  │  │  ├── petSprite.tsx
   │  │  │  ├── pluginsHub.tsx
   │  │  │  ├── prompts.tsx
   │  │  │  ├── queuedMessages.tsx
   │  │  │  ├── skillsHub.tsx
   │  │  │  ├── streamingAssistant.tsx
   │  │  │  ├── streamingMarkdown.tsx
   │  │  │  ├── subscriptionOverlay.tsx
   │  │  │  ├── textInput.tsx
   │  │  │  ├── themed.tsx
   │  │  │  ├── thinking.tsx
   │  │  │  ├── todoPanel.tsx
   │  │  │  └── widgetGrid.tsx
   │  │  ├── config
   │  │  │  ├── env.ts
   │  │  │  ├── limits.ts
   │  │  │  └── timing.ts
   │  │  ├── content
   │  │  │  ├── charms.ts
   │  │  │  ├── faces.ts
   │  │  │  ├── fortunes.ts
   │  │  │  ├── hotkeys.ts
   │  │  │  ├── placeholders.ts
   │  │  │  ├── setup.ts
   │  │  │  └── verbs.ts
   │  │  ├── domain
   │  │  │  ├── attachments.ts
   │  │  │  ├── blockLayout.ts
   │  │  │  ├── composerHighlights.ts
   │  │  │  ├── details.ts
   │  │  │  ├── messages.ts
   │  │  │  ├── paths.ts
   │  │  │  ├── providers.ts
   │  │  │  ├── roles.ts
   │  │  │  ├── slash.ts
   │  │  │  ├── usage.ts
   │  │  │  └── viewport.ts
   │  │  ├── entry.tsx
   │  │  ├── gatewayClient.ts
   │  │  ├── gatewayTypes.ts
   │  │  ├── hooks
   │  │  │  ├── useCompletion.ts
   │  │  │  ├── useGitBranch.ts
   │  │  │  ├── useInputHistory.ts
   │  │  │  ├── useQueue.ts
   │  │  │  └── useVirtualHistory.ts
   │  │  ├── lib
   │  │  │  ├── billingDialog.test.ts
   │  │  │  ├── billingDialog.ts
   │  │  │  ├── charts.ts
   │  │  │  ├── circularBuffer.ts
   │  │  │  ├── clipboard.ts
   │  │  │  ├── color.test.ts
   │  │  │  ├── color.ts
   │  │  │  ├── editor.test.ts
   │  │  │  ├── editor.ts
   │  │  │  ├── emoji.ts
   │  │  │  ├── externalCli.ts
   │  │  │  ├── externalLink.ts
   │  │  │  ├── forceTruecolor.ts
   │  │  │  ├── fpsStore.ts
   │  │  │  ├── fuzzy.test.ts
   │  │  │  ├── fuzzy.ts
   │  │  │  ├── gracefulExit.ts
   │  │  │  ├── history.ts
   │  │  │  ├── inputMetrics.ts
   │  │  │  ├── liveProgress.test.ts
   │  │  │  ├── liveProgress.ts
   │  │  │  ├── mathUnicode.ts
   │  │  │  ├── memory.test.ts
   │  │  │  ├── memory.ts
   │  │  │  ├── memoryMonitor.ts
   │  │  │  ├── messages.test.ts
   │  │  │  ├── messages.ts
   │  │  │  ├── model-search-text.test.ts
   │  │  │  ├── model-search-text.ts
   │  │  │  ├── openExternalUrl.test.ts
   │  │  │  ├── openExternalUrl.ts
   │  │  │  ├── osc52.ts
   │  │  │  ├── parentLog.ts
   │  │  │  ├── perfPane.tsx
   │  │  │  ├── petPolling.ts
   │  │  │  ├── platform.ts
   │  │  │  ├── precisionWheel.ts
   │  │  │  ├── prompt.ts
   │  │  │  ├── reasoning.ts
   │  │  │  ├── resizeCoalescer.test.ts
   │  │  │  ├── resizeCoalescer.ts
   │  │  │  ├── rpc.ts
   │  │  │  ├── starmapPalette.ts
   │  │  │  ├── subagentTree.ts
   │  │  │  ├── syntax.ts
   │  │  │  ├── terminalModes.ts
   │  │  │  ├── terminalParity.ts
   │  │  │  ├── terminalSetup.ts
   │  │  │  ├── termux.ts
   │  │  │  ├── text.test.ts
   │  │  │  ├── text.ts
   │  │  │  ├── themeBoot.ts
   │  │  │  ├── todo.test.ts
   │  │  │  ├── todo.ts
   │  │  │  ├── viewportStore.ts
   │  │  │  ├── virtualHeights.ts
   │  │  │  ├── wheelAccel.ts
   │  │  │  └── widgetGrid.ts
   │  │  ├── protocol
   │  │  │  ├── interpolation.ts
   │  │  │  └── paste.ts
   │  │  ├── sdk
   │  │  │  ├── apps
   │  │  │  │  ├── dialogTest.tsx
   │  │  │  │  ├── gridTest.tsx
   │  │  │  │  ├── gridTestState.ts
   │  │  │  │  ├── index.ts
   │  │  │  │  ├── ticker.tsx
   │  │  │  │  └── weather.tsx
   │  │  │  ├── host.tsx
   │  │  │  ├── index.ts
   │  │  │  ├── registry.ts
   │  │  │  ├── types.ts
   │  │  │  └── userWidgets.ts
   │  │  ├── theme.ts
   │  │  ├── types
   │  │  │  └── jimmy-ink.d.ts
   │  │  ├── types.ts
   │  │  └── __tests__
   │  │    ├── activeSessionSwitcher.test.ts
   │  │    ├── appChromeBlockedTimers.test.tsx
   │  │    ├── appChromeStatusRule.test.tsx
   │  │    ├── appChromeStatusRuleDevCredits.test.tsx
   │  │    ├── approvalAction.test.ts
   │  │    ├── asCommandDispatch.test.ts
   │  │    ├── attachments.test.ts
   │  │    ├── billingStepUp.test.tsx
   │  │    ├── blockLayout.test.ts
   │  │    ├── brandingMcpCount.test.ts
   │  │    ├── bundleNoAsyncEsmDeadlock.test.ts
   │  │    ├── charts.test.ts
   │  │    ├── clipboard.test.ts
   │  │    ├── completionApply.test.ts
   │  │    ├── composerHighlights.test.ts
   │  │    ├── constants.test.ts
   │  │    ├── createGatewayEventHandler.test.ts
   │  │    ├── createSlashHandler.test.ts
   │  │    ├── cursorDriftRegression.test.ts
   │  │    ├── details.test.ts
   │  │    ├── emoji.test.ts
   │  │    ├── externalLink.test.ts
   │  │    ├── forceTruecolor.test.ts
   │  │    ├── gatewayClient.test.ts
   │  │    ├── gatewayRecovery.test.ts
   │  │    ├── gracefulExit.test.ts
   │  │    ├── imeVietnameseTelex.test.tsx
   │  │    ├── inlineSlashSkill.test.ts
   │  │    ├── inputSelectionClipboard.test.ts
   │  │    ├── journeyCommand.test.ts
   │  │    ├── loaders.test.ts
   │  │    ├── markdown.test.ts
   │  │    ├── mathUnicode.test.ts
   │  │    ├── memoryMonitor.test.ts
   │  │    ├── mergeUsageStable.test.ts
   │  │    ├── messageLine.test.ts
   │  │    ├── messages.test.ts
   │  │    ├── moaProgressActivity.test.ts
   │  │    ├── modelPicker.test.ts
   │  │    ├── orchestratorPromptSession.test.ts
   │  │    ├── osc52.test.ts
   │  │    ├── overlayPrimitives.test.ts
   │  │    ├── parentLog.test.ts
   │  │    ├── paths.test.ts
   │  │    ├── petPane.test.tsx
   │  │    ├── petPolling.test.ts
   │  │    ├── platform.test.ts
   │  │    ├── precisionWheel.test.ts
   │  │    ├── prompt.test.ts
   │  │    ├── providers.test.ts
   │  │    ├── queueSubmission.test.ts
   │  │    ├── reasoning.test.ts
   │  │    ├── rpc.test.ts
   │  │    ├── scroll.test.ts
   │  │    ├── scrollBoxRendererBounds.test.ts
   │  │    ├── slashParity.test.ts
   │  │    ├── spawnHistoryStore.test.ts
   │  │    ├── stateIsolation.test.ts
   │  │    ├── statusBarTicker.test.ts
   │  │    ├── statusRule.test.ts
   │  │    ├── streamingMarkdown.test.ts
   │  │    ├── subagentTree.test.ts
   │  │    ├── submissionCore.test.ts
   │  │    ├── subscriptionCommand.test.ts
   │  │    ├── subscriptionOverlay.test.tsx
   │  │    ├── syntax.test.ts
   │  │    ├── terminalModes.test.ts
   │  │    ├── terminalParity.test.ts
   │  │    ├── terminalSetup.test.ts
   │  │    ├── termux.test.ts
   │  │    ├── termuxComposerLayout.test.ts
   │  │    ├── text.test.ts
   │  │    ├── textInputBurstInput.test.ts
   │  │    ├── textInputCursorSourceOfTruth.test.ts
   │  │    ├── textInputCut.test.ts
   │  │    ├── textInputFastEcho.test.ts
   │  │    ├── textInputKillLine.test.ts
   │  │    ├── textInputLineKill.test.ts
   │  │    ├── textInputLineNav.test.ts
   │  │    ├── textInputPassThrough.test.ts
   │  │    ├── textInputReturnAction.test.ts
   │  │    ├── textInputReturnBurst.test.ts
   │  │    ├── textInputRightClick.test.ts
   │  │    ├── textInputSubmitClear.test.tsx
   │  │    ├── textInputWordDelete.test.ts
   │  │    ├── textInputWrap.test.ts
   │  │    ├── theme.test.ts
   │  │    ├── themeBoot.test.ts
   │  │    ├── thinkingLiveCollapse.test.tsx
   │  │    ├── thinkingMoaReferenceVisibility.test.tsx
   │  │    ├── topupCommand.test.ts
   │  │    ├── turnControllerNotice.test.ts
   │  │    ├── turnStore.test.ts
   │  │    ├── usageCommand.test.ts
   │  │    ├── useBatteryPoll.test.ts
   │  │    ├── useCompletion.test.ts
   │  │    ├── useComposerState.test.ts
   │  │    ├── useConfigSync.test.ts
   │  │    ├── useInputHandlers.test.ts
   │  │    ├── useQueue.test.ts
   │  │    ├── userWidgets.test.ts
   │  │    ├── useSessionLifecycle.test.ts
   │  │    ├── useSubmission.test.ts
   │  │    ├── useVirtualHistoryHeights.test.ts
   │  │    ├── viewport.test.ts
   │  │    ├── viewportStore.test.ts
   │  │    ├── virtualHeights.test.ts
   │  │    ├── virtualHistoryClamp.test.ts
   │  │    ├── virtualHistoryOffsetCache.test.ts
   │  │    ├── voiceSubmitModeRenderer.test.tsx
   │  │    ├── wakeCommand.test.ts
   │  │    ├── weatherApp.test.ts
   │  │    ├── wheelAccel.test.ts
   │  │    ├── widgetGrid.test.ts
   │  │    ├── widgetGridComponent.test.tsx
   │  │    └── widgetSdk.test.ts
   │  ├── tsconfig.build.json
   │  ├── tsconfig.json
   │  └── vitest.config.ts
  ├── utils.py
  ├── uv.lock
  ├── web
   │  ├── eslint.config.js
   │  ├── index.html
   │  ├── package.json
   │  ├── public
   │  │  ├── favicon.ico
   │  │  ├── fonts
   │  │  │  ├── Collapse-Bold.woff2
   │  │  │  ├── Collapse-Regular.woff2
   │  │  │  ├── Mondwest-Regular.woff2
   │  │  │  ├── RulesCompressed-Medium.woff2
   │  │  │  ├── RulesCompressed-Regular.woff2
   │  │  │  ├── RulesExpanded-Bold.woff2
   │  │  │  └── RulesExpanded-Regular.woff2
   │  │  └── fonts-terminal
   │  │    ├── JetBrainsMono-Bold.woff2
   │  │    ├── JetBrainsMono-Italic.woff2
   │  │    └── JetBrainsMono-Regular.woff2
   │  ├── README.md
   │  ├── src
   │  │  ├── App.tsx
   │  │  ├── components
   │  │  │  ├── AuthWidget.tsx
   │  │  │  ├── AutoField.tsx
   │  │  │  ├── AutomationBlueprints.tsx
   │  │  │  ├── ChatSessionList.tsx
   │  │  │  ├── ChatSidebar.test.tsx
   │  │  │  ├── ChatSidebar.tsx
   │  │  │  ├── ConfirmDialog.tsx
   │  │  │  ├── DeleteConfirmDialog.tsx
   │  │  │  ├── JimmyConsoleModal.tsx
   │  │  │  ├── LanguageSwitcher.tsx
   │  │  │  ├── Markdown.tsx
   │  │  │  ├── MemoryPressureBanner.test.tsx
   │  │  │  ├── MemoryPressureBanner.tsx
   │  │  │  ├── ModelInfoCard.tsx
   │  │  │  ├── ModelPickerDialog.tsx
   │  │  │  ├── ModelReloadConfirm.tsx
   │  │  │  ├── OAuthLoginModal.tsx
   │  │  │  ├── OAuthProvidersCard.tsx
   │  │  │  ├── PlatformsCard.tsx
   │  │  │  ├── ProfileScopeBanner.tsx
   │  │  │  ├── ProfileSwitcher.tsx
   │  │  │  ├── ReasoningPicker.tsx
   │  │  │  ├── ScheduleBuilder.tsx
   │  │  │  ├── SidebarFooter.tsx
   │  │  │  ├── SidebarStatusStrip.tsx
   │  │  │  ├── SkillEditorDialog.tsx
   │  │  │  ├── SlashPopover.tsx
   │  │  │  ├── ThemeSwitcher.tsx
   │  │  │  └── ToolsetConfigDrawer.tsx
   │  │  ├── contexts
   │  │  │  ├── page-header-context.ts
   │  │  │  ├── PageHeaderProvider.tsx
   │  │  │  ├── profile-context.ts
   │  │  │  ├── ProfileProvider.tsx
   │  │  │  ├── system-actions-context.ts
   │  │  │  ├── SystemActions.tsx
   │  │  │  ├── usePageHeader.ts
   │  │  │  ├── useProfileScope.ts
   │  │  │  └── useSystemActions.ts
   │  │  ├── hooks
   │  │  │  ├── useModalBehavior.ts
   │  │  │  └── useSidebarStatus.ts
   │  │  ├── i18n
   │  │  │  ├── af.ts
   │  │  │  ├── ar.ts
   │  │  │  ├── context.tsx
   │  │  │  ├── de.ts
   │  │  │  ├── define-locale.ts
   │  │  │  ├── en.ts
   │  │  │  ├── es.ts
   │  │  │  ├── fr.ts
   │  │  │  ├── ga.ts
   │  │  │  ├── hu.ts
   │  │  │  ├── index.ts
   │  │  │  ├── it.ts
   │  │  │  ├── ja.ts
   │  │  │  ├── ko.ts
   │  │  │  ├── pt.ts
   │  │  │  ├── ru.ts
   │  │  │  ├── tr.ts
   │  │  │  ├── types.ts
   │  │  │  ├── uk.ts
   │  │  │  ├── zh-hant.ts
   │  │  │  └── zh.ts
   │  │  ├── index.css
   │  │  ├── lib
   │  │  │  ├── api.test.ts
   │  │  │  ├── api.ts
   │  │  │  ├── chat-activation.test.ts
   │  │  │  ├── chat-activation.ts
   │  │  │  ├── chat-sidebar-session-params.test.ts
   │  │  │  ├── chat-title.test.ts
   │  │  │  ├── chat-title.ts
   │  │  │  ├── chatImagePaste.test.ts
   │  │  │  ├── chatImagePaste.ts
   │  │  │  ├── clipboard-usage.test.ts
   │  │  │  ├── clipboard.test.ts
   │  │  │  ├── clipboard.ts
   │  │  │  ├── cron-job.test.ts
   │  │  │  ├── cron-job.ts
   │  │  │  ├── cron-trigger-controller.test.ts
   │  │  │  ├── dashboard-auth-reload.test.ts
   │  │  │  ├── dashboard-auth-reload.ts
   │  │  │  ├── dashboard-flags.ts
   │  │  │  ├── dashboard-modal-shell.test.ts
   │  │  │  ├── dashboard-modal-shell.ts
   │  │  │  ├── events-reconnect.test.ts
   │  │  │  ├── events-reconnect.ts
   │  │  │  ├── format.ts
   │  │  │  ├── fuzzy.ts
   │  │  │  ├── gatewayClient.test.ts
   │  │  │  ├── gatewayClient.ts
   │  │  │  ├── keyboard-inset.test.ts
   │  │  │  ├── keyboard-inset.ts
   │  │  │  ├── log-classify.test.ts
   │  │  │  ├── log-classify.ts
   │  │  │  ├── mcp-dashboard-oauth.test.ts
   │  │  │  ├── mcp-dashboard-oauth.ts
   │  │  │  ├── mcp-server-create.test.ts
   │  │  │  ├── mcp-server-create.ts
   │  │  │  ├── model-picker-filter.test.ts
   │  │  │  ├── model-picker-filter.ts
   │  │  │  ├── model-search-text.ts
   │  │  │  ├── nested.ts
   │  │  │  ├── pty-composition.test.ts
   │  │  │  ├── pty-composition.ts
   │  │  │  ├── pty-keyboard-shortcuts.test.ts
   │  │  │  ├── pty-keyboard-shortcuts.ts
   │  │  │  ├── pty-mobile-input.test.ts
   │  │  │  ├── pty-mobile-input.ts
   │  │  │  ├── pty-reconnect.test.ts
   │  │  │  ├── pty-reconnect.ts
   │  │  │  ├── pty-resume-loading.test.ts
   │  │  │  ├── pty-resume-loading.ts
   │  │  │  ├── pty-resume-sanitizer.test.ts
   │  │  │  ├── pty-resume-sanitizer.ts
   │  │  │  ├── pty-scroll.test.ts
   │  │  │  ├── pty-scroll.ts
   │  │  │  ├── reasoning-effort.test.ts
   │  │  │  ├── reasoning-effort.ts
   │  │  │  ├── resolve-page-title.test.ts
   │  │  │  ├── resolve-page-title.ts
   │  │  │  ├── schedule.test.ts
   │  │  │  ├── schedule.ts
   │  │  │  ├── session-import.test.ts
   │  │  │  ├── session-import.ts
   │  │  │  ├── session-prune.test.ts
   │  │  │  ├── session-prune.ts
   │  │  │  ├── session-refresh.test.ts
   │  │  │  ├── session-refresh.ts
   │  │  │  ├── slashExec.ts
   │  │  │  └── utils.ts
   │  │  ├── main.tsx
   │  │  ├── pages
   │  │  │  ├── AnalyticsPage.tsx
   │  │  │  ├── ChannelsPage.tsx
   │  │  │  ├── ChatPage.test.tsx
   │  │  │  ├── ChatPage.tsx
   │  │  │  ├── ConfigPage.tsx
   │  │  │  ├── CronPage.tsx
   │  │  │  ├── DocsPage.tsx
   │  │  │  ├── EnvPage.tsx
   │  │  │  ├── FilesPage.tsx
   │  │  │  ├── LogsPage.tsx
   │  │  │  ├── McpPage.tsx
   │  │  │  ├── ModelsPage.tsx
   │  │  │  ├── PairingPage.tsx
   │  │  │  ├── PluginsPage.tsx
   │  │  │  ├── ProfileBuilderPage.tsx
   │  │  │  ├── ProfilesPage.tsx
   │  │  │  ├── SessionsPage.tsx
   │  │  │  ├── SkillsPage.tsx
   │  │  │  ├── SystemPage.tsx
   │  │  │  └── WebhooksPage.tsx
   │  │  ├── plugins
   │  │  │  ├── index.ts
   │  │  │  ├── PluginPage.tsx
   │  │  │  ├── registry.test.ts
   │  │  │  ├── registry.ts
   │  │  │  ├── sdk.d.ts
   │  │  │  ├── slots.ts
   │  │  │  ├── types.ts
   │  │  │  ├── usePlugins.test.ts
   │  │  │  └── usePlugins.ts
   │  │  └── themes
   │  │    ├── context.tsx
   │  │    ├── fonts.ts
   │  │    ├── index.ts
   │  │    ├── presets.ts
   │  │    └── types.ts
   │  ├── tsconfig.app.json
   │  ├── tsconfig.json
   │  ├── tsconfig.node.json
   │  ├── vite.config.ts
   │  └── vitest.config.ts
  └── website
     ├── docs
      │  ├── developer-guide
      │  │  ├── acp-internals.md
      │  │  ├── adding-platform-adapters.md
      │  │  ├── adding-providers.md
      │  │  ├── adding-tools.md
      │  │  ├── agent-loop.md
      │  │  ├── architecture.md
      │  │  ├── browser-provider-plugin.md
      │  │  ├── browser-supervisor.md
      │  │  ├── codebase-ownership.md
      │  │  ├── context-compression-and-caching.md
      │  │  ├── context-engine-plugin.md
      │  │  ├── contributing.md
      │  │  ├── creating-skills.md
      │  │  ├── cron-internals.md
      │  │  ├── desktop-plugin-sdk.md
      │  │  ├── egress-internals.md
      │  │  ├── extending-the-cli.md
      │  │  ├── gateway-internals.md
      │  │  ├── image-gen-provider-plugin.md
      │  │  ├── memory-provider-plugin.md
      │  │  ├── model-provider-plugin.md
      │  │  ├── plugin-llm-access.md
      │  │  ├── plugins
      │  │  │  └── index.md
      │  │  ├── programmatic-integration.md
      │  │  ├── prompt-assembly.md
      │  │  ├── provider-runtime.md
      │  │  ├── secret-source-plugin.md
      │  │  ├── session-storage.md
      │  │  ├── subagent-lifecycle-api.md
      │  │  ├── tools-runtime.md
      │  │  ├── trajectory-format.md
      │  │  ├── video-gen-provider-plugin.md
      │  │  ├── web-search-provider-plugin.md
      │  │  ├── worktree-ui-dev.md
      │  │  └── _category_.json
      │  ├── getting-started
      │  │  ├── installation.md
      │  │  ├── learning-path.md
      │  │  ├── nix-setup.md
      │  │  ├── platform-support.md
      │  │  ├── quickstart.md
      │  │  ├── termux.md
      │  │  ├── updating.md
      │  │  └── _category_.json
      │  ├── guides
      │  │  ├── agent-email-address.md
      │  │  ├── automate-with-cron.md
      │  │  ├── automation-blueprints.md
      │  │  ├── aws-bedrock.md
      │  │  ├── azure-foundry.md
      │  │  ├── cron-script-only.md
      │  │  ├── cron-troubleshooting.md
      │  │  ├── daily-briefing-bot.md
      │  │  ├── delegation-patterns.md
      │  │  ├── desktop-native-signin.md
      │  │  ├── github-pr-review-agent.md
      │  │  ├── google-gemini.md
      │  │  ├── google-vertex.md
      │  │  ├── local-llm-on-mac.md
      │  │  ├── local-ollama-setup.md
      │  │  ├── microsoft-graph-app-registration.md
      │  │  ├── migrate-from-openclaw.md
      │  │  ├── minimax-oauth.md
      │  │  ├── oauth-over-ssh.md
      │  │  ├── operate-teams-meeting-pipeline.md
      │  │  ├── pipe-script-output.md
      │  │  ├── python-library.md
      │  │  ├── run-jimmy-with-nous-portal.md
      │  │  ├── run-nemotron-3-ultra-free.md
      │  │  ├── secure-jimmy-on-a-work-machine.md
      │  │  ├── team-telegram-assistant.md
      │  │  ├── tips.md
      │  │  ├── troubleshooting-agent-quality.md
      │  │  ├── use-mcp-with-jimmy.md
      │  │  ├── use-soul-with-jimmy.md
      │  │  ├── use-voice-mode-with-jimmy.md
      │  │  ├── webhook-github-pr-review.md
      │  │  ├── work-with-skills.md
      │  │  ├── xai-grok-oauth.md
      │  │  └── _category_.json
      │  ├── index.mdx
      │  ├── integrations
      │  │  ├── buzz.md
      │  │  ├── index.md
      │  │  ├── nous-portal.md
      │  │  └── providers.md
      │  ├── reference
      │  │  ├── automation-blueprints-catalog.mdx
      │  │  ├── cli-commands.md
      │  │  ├── cli-symbols.md
      │  │  ├── environment-variables.md
      │  │  ├── faq.md
      │  │  ├── mcp-config-reference.md
      │  │  ├── model-catalog.md
      │  │  ├── optional-skills-catalog.md
      │  │  ├── profile-commands.md
      │  │  ├── skills-catalog.md
      │  │  ├── slash-commands.md
      │  │  ├── tools-reference.md
      │  │  ├── toolsets-reference.md
      │  │  └── _category_.json
      │  ├── user-guide
      │  │  ├── bot-mode.md
      │  │  ├── checkpoints-and-rollback.md
      │  │  ├── cli.md
      │  │  ├── configuration.md
      │  │  ├── configuring-models.md
      │  │  ├── desktop.md
      │  │  ├── docker.md
      │  │  ├── egress
      │  │  │  ├── index.md
      │  │  │  └── iron-proxy.md
      │  │  ├── features
      │  │  │  ├── acp.md
      │  │  │  ├── api-server.md
      │  │  │  ├── batch-processing.md
      │  │  │  ├── browser.md
      │  │  │  ├── built-in-plugins.md
      │  │  │  ├── code-execution.md
      │  │  │  ├── codex-app-server-runtime.md
      │  │  │  ├── computer-use.md
      │  │  │  ├── context-files.md
      │  │  │  ├── context-references.md
      │  │  │  ├── credential-pools.md
      │  │  │  ├── cron.md
      │  │  │  ├── curator.md
      │  │  │  ├── delegation.md
      │  │  │  ├── deliverable-mode.md
      │  │  │  ├── document-extraction.md
      │  │  │  ├── extending-the-dashboard.md
      │  │  │  ├── fallback-providers.md
      │  │  │  ├── goals.md
      │  │  │  ├── heartbeat.md
      │  │  │  ├── honcho.md
      │  │  │  ├── hooks.md
      │  │  │  ├── image-generation.md
      │  │  │  ├── kanban-tutorial.md
      │  │  │  ├── kanban-worker-lanes.md
      │  │  │  ├── kanban.md
      │  │  │  ├── loops.md
      │  │  │  ├── lsp.md
      │  │  │  ├── mcp.md
      │  │  │  ├── memory-providers.md
      │  │  │  ├── memory.md
      │  │  │  ├── mixture-of-agents.md
      │  │  │  ├── overview.md
      │  │  │  ├── personality.md
      │  │  │  ├── pets.md
      │  │  │  ├── plugins.md
      │  │  │  ├── provider-routing.md
      │  │  │  ├── skills.md
      │  │  │  ├── skins.md
      │  │  │  ├── spotify.md
      │  │  │  ├── subscription-proxy.md
      │  │  │  ├── tool-gateway.md
      │  │  │  ├── tool-search.md
      │  │  │  ├── tools.md
      │  │  │  ├── tts.md
      │  │  │  ├── vision.md
      │  │  │  ├── voice-mode.md
      │  │  │  ├── wake-word.md
      │  │  │  ├── web-dashboard.md
      │  │  │  ├── web-search.md
      │  │  │  ├── x-search.md
      │  │  │  └── _category_.json
      │  │  ├── git-worktrees.md
      │  │  ├── import-from-other-agents.md
      │  │  ├── managed-scope.md
      │  │  ├── messaging
      │  │  │  ├── a2a.md
      │  │  │  ├── bluebubbles.md
      │  │  │  ├── buzz.md
      │  │  │  ├── dingtalk.md
      │  │  │  ├── discord.md
      │  │  │  ├── email.md
      │  │  │  ├── feishu.md
      │  │  │  ├── google_chat.md
      │  │  │  ├── homeassistant.md
      │  │  │  ├── index.md
      │  │  │  ├── irc.md
      │  │  │  ├── line.md
      │  │  │  ├── matrix.md
      │  │  │  ├── mattermost.md
      │  │  │  ├── msgraph-webhook.md
      │  │  │  ├── ntfy.md
      │  │  │  ├── open-webui.md
      │  │  │  ├── photon.md
      │  │  │  ├── qqbot.md
      │  │  │  ├── raft.md
      │  │  │  ├── relay.md
      │  │  │  ├── signal.md
      │  │  │  ├── simplex.md
      │  │  │  ├── slack.md
      │  │  │  ├── sms.md
      │  │  │  ├── teams-meetings.md
      │  │  │  ├── teams.md
      │  │  │  ├── telegram.md
      │  │  │  ├── webhooks.md
      │  │  │  ├── wecom-callback.md
      │  │  │  ├── wecom.md
      │  │  │  ├── weixin.md
      │  │  │  ├── whatsapp-cloud.md
      │  │  │  ├── whatsapp.md
      │  │  │  ├── yuanbao.md
      │  │  │  └── _category_.json
      │  │  ├── multi-connection-desktop.md
      │  │  ├── multi-profile-gateways.md
      │  │  ├── profile-distributions.md
      │  │  ├── profiles.md
      │  │  ├── secrets
      │  │  │  ├── bitwarden.md
      │  │  │  ├── command.md
      │  │  │  ├── index.md
      │  │  │  └── onepassword.md
      │  │  ├── security.md
      │  │  ├── sessions.md
      │  │  ├── skills
      │  │  │  ├── bundled
      │  │  │  │  ├── apple
      │  │  │  │  │  ├── apple-apple-notes.md
      │  │  │  │  │  ├── apple-apple-reminders.md
      │  │  │  │  │  ├── apple-findmy.md
      │  │  │  │  │  └── apple-imessage.md
      │  │  │  │  ├── autonomous-ai-agents
      │  │  │  │  │  ├── autonomous-ai-agents-claude-code.md
      │  │  │  │  │  ├── autonomous-ai-agents-codex.md
      │  │  │  │  │  ├── autonomous-ai-agents-computer-use.md
      │  │  │  │  │  ├── autonomous-ai-agents-jimmy-agent.md
      │  │  │  │  │  └── autonomous-ai-agents-opencode.md
      │  │  │  │  ├── creative
      │  │  │  │  │  ├── creative-architecture-diagram.md
      │  │  │  │  │  ├── creative-ascii-art.md
      │  │  │  │  │  ├── creative-ascii-video.md
      │  │  │  │  │  ├── creative-baoyu-infographic.md
      │  │  │  │  │  ├── creative-claude-design.md
      │  │  │  │  │  ├── creative-comfyui.md
      │  │  │  │  │  ├── creative-design-md.md
      │  │  │  │  │  ├── creative-excalidraw.md
      │  │  │  │  │  ├── creative-humanizer.md
      │  │  │  │  │  ├── creative-manim-video.md
      │  │  │  │  │  ├── creative-p5js.md
      │  │  │  │  │  ├── creative-popular-web-designs.md
      │  │  │  │  │  ├── creative-pretext.md
      │  │  │  │  │  ├── creative-sketch.md
      │  │  │  │  │  ├── creative-songwriting-and-ai-music.md
      │  │  │  │  │  └── creative-touchdesigner-mcp.md
      │  │  │  │  ├── email
      │  │  │  │  │  ├── email-email-inbox-triage.md
      │  │  │  │  │  └── email-himalaya.md
      │  │  │  │  ├── github
      │  │  │  │  │  ├── github-codebase-inspection.md
      │  │  │  │  │  ├── github-github-auth.md
      │  │  │  │  │  ├── github-github-code-review.md
      │  │  │  │  │  ├── github-github-issue-to-pr.md
      │  │  │  │  │  ├── github-github-issues.md
      │  │  │  │  │  ├── github-github-pr-workflow.md
      │  │  │  │  │  └── github-github-repo-management.md
      │  │  │  │  ├── media
      │  │  │  │  │  ├── media-gif-search.md
      │  │  │  │  │  ├── media-songsee.md
      │  │  │  │  │  └── media-youtube-content.md
      │  │  │  │  ├── mlops
      │  │  │  │  │  ├── mlops-evaluation-evaluating-llms-harness.md
      │  │  │  │  │  ├── mlops-evaluation-weights-and-biases.md
      │  │  │  │  │  ├── mlops-huggingface-hub.md
      │  │  │  │  │  ├── mlops-inference-llama-cpp.md
      │  │  │  │  │  └── mlops-inference-serving-llms-vllm.md
      │  │  │  │  ├── note-taking
      │  │  │  │  │  └── note-taking-obsidian.md
      │  │  │  │  ├── productivity
      │  │  │  │  │  ├── productivity-airtable.md
      │  │  │  │  │  ├── productivity-box.md
      │  │  │  │  │  ├── productivity-document-to-action-items.md
      │  │  │  │  │  ├── productivity-docx.md
      │  │  │  │  │  ├── productivity-google-workspace.md
      │  │  │  │  │  ├── productivity-maps.md
      │  │  │  │  │  ├── productivity-meeting-action-items.md
      │  │  │  │  │  ├── productivity-nano-pdf.md
      │  │  │  │  │  ├── productivity-notion.md
      │  │  │  │  │  ├── productivity-ocr-and-documents.md
      │  │  │  │  │  ├── productivity-pdf.md
      │  │  │  │  │  ├── productivity-powerpoint.md
      │  │  │  │  │  ├── productivity-product-price-monitor.md
      │  │  │  │  │  ├── productivity-session-librarian.md
      │  │  │  │  │  ├── productivity-teams-meeting-pipeline.md
      │  │  │  │  │  ├── productivity-weekly-review-planning.md
      │  │  │  │  │  └── productivity-xlsx.md
      │  │  │  │  ├── research
      │  │  │  │  │  ├── research-arxiv.md
      │  │  │  │  │  ├── research-blocked-page-recovery.md
      │  │  │  │  │  ├── research-blogwatcher.md
      │  │  │  │  │  ├── research-competitor-news-monitor.md
      │  │  │  │  │  ├── research-grounded-citations.md
      │  │  │  │  │  ├── research-llm-wiki.md
      │  │  │  │  │  └── research-research-paper-writing.md
      │  │  │  │  ├── smart-home
      │  │  │  │  │  └── smart-home-openhue.md
      │  │  │  │  ├── social-media
      │  │  │  │  │  └── social-media-xurl.md
      │  │  │  │  └── software-development
      │  │  │  │    ├── software-development-dogfood.md
      │  │  │  │    ├── software-development-jimmy-agent-skill-authoring.md
      │  │  │  │    ├── software-development-inspecting-jimmy-desktop-dom.md
      │  │  │  │    ├── software-development-node-inspect-debugger.md
      │  │  │  │    ├── software-development-plan.md
      │  │  │  │    ├── software-development-python-debugpy.md
      │  │  │  │    ├── software-development-requesting-code-review.md
      │  │  │  │    ├── software-development-simplify-code.md
      │  │  │  │    ├── software-development-spike.md
      │  │  │  │    ├── software-development-systematic-debugging.md
      │  │  │  │    └── software-development-test-driven-development.md
      │  │  │  ├── google-workspace.md
      │  │  │  └── optional
      │  │  │    ├── autonomous-ai-agents
      │  │  │     │  ├── autonomous-ai-agents-antigravity-cli.md
      │  │  │     │  ├── autonomous-ai-agents-blackbox.md
      │  │  │     │  ├── autonomous-ai-agents-grok.md
      │  │  │     │  ├── autonomous-ai-agents-honcho.md
      │  │  │     │  └── autonomous-ai-agents-openhands.md
      │  │  │    ├── blockchain
      │  │  │     │  ├── blockchain-evm.md
      │  │  │     │  ├── blockchain-hyperliquid.md
      │  │  │     │  └── blockchain-solana.md
      │  │  │    ├── communication
      │  │  │     │  └── communication-one-three-one-rule.md
      │  │  │    ├── creative
      │  │  │     │  ├── creative-audiocraft-audio-generation.md
      │  │  │     │  ├── creative-baoyu-article-illustrator.md
      │  │  │     │  ├── creative-baoyu-comic.md
      │  │  │     │  ├── creative-concept-diagrams.md
      │  │  │     │  ├── creative-creative-ideation.md
      │  │  │     │  ├── creative-draw-your-font.md
      │  │  │     │  ├── creative-heartmula.md
      │  │  │     │  ├── creative-hyperframes.md
      │  │  │     │  ├── creative-kanban-video-orchestrator.md
      │  │  │     │  ├── creative-meme-generation.md
      │  │  │     │  ├── creative-pixel-art.md
      │  │  │     │  ├── creative-simple-english.md
      │  │  │     │  ├── creative-social-media-content-calendar.md
      │  │  │     │  ├── creative-tldraw-offline.md
      │  │  │     │  └── creative-unreal-mcp.md
      │  │  │    ├── data-science
      │  │  │     │  └── data-science-jupyter-notebook.md
      │  │  │    ├── devops
      │  │  │     │  ├── devops-actual-setup.md
      │  │  │     │  ├── devops-docker-management.md
      │  │  │     │  ├── devops-jimmy-s6-container-supervision.md
      │  │  │     │  ├── devops-inference-sh-cli.md
      │  │  │     │  ├── devops-pinggy-tunnel.md
      │  │  │     │  └── devops-watchers.md
      │  │  │    ├── dogfood
      │  │  │     │  └── dogfood-adversarial-ux-test.md
      │  │  │    ├── email
      │  │  │     │  └── email-agentmail.md
      │  │  │    ├── finance
      │  │  │     │  ├── finance-3-statement-model.md
      │  │  │     │  ├── finance-comps-analysis.md
      │  │  │     │  ├── finance-dcf-model.md
      │  │  │     │  ├── finance-excel-author.md
      │  │  │     │  ├── finance-lbo-model.md
      │  │  │     │  ├── finance-merger-model.md
      │  │  │     │  ├── finance-polymarket.md
      │  │  │     │  ├── finance-pptx-author.md
      │  │  │     │  └── finance-stocks.md
      │  │  │    ├── gaming
      │  │  │     │  ├── gaming-minecraft-modpack-server.md
      │  │  │     │  └── gaming-pokemon-player.md
      │  │  │    ├── health
      │  │  │     │  ├── health-fitness-nutrition.md
      │  │  │     │  └── health-neuroskill-bci.md
      │  │  │    ├── mcp
      │  │  │     │  ├── mcp-fastmcp.md
      │  │  │     │  ├── mcp-mcp-oauth-remote-gateway.md
      │  │  │     │  └── mcp-mcporter.md
      │  │  │    ├── migration
      │  │  │     │  └── migration-openclaw-migration.md
      │  │  │    ├── mlops
      │  │  │     │  ├── mlops-accelerate.md
      │  │  │     │  ├── mlops-chroma.md
      │  │  │     │  ├── mlops-clip.md
      │  │  │     │  ├── mlops-faiss.md
      │  │  │     │  ├── mlops-flash-attention.md
      │  │  │     │  ├── mlops-guidance.md
      │  │  │     │  ├── mlops-huggingface-tokenizers.md
      │  │  │     │  ├── mlops-inference-outlines.md
      │  │  │     │  ├── mlops-instructor.md
      │  │  │     │  ├── mlops-lambda-labs.md
      │  │  │     │  ├── mlops-llava.md
      │  │  │     │  ├── mlops-modal.md
      │  │  │     │  ├── mlops-models-segment-anything-model.md
      │  │  │     │  ├── mlops-nemo-curator.md
      │  │  │     │  ├── mlops-obliteratus.md
      │  │  │     │  ├── mlops-peft.md
      │  │  │     │  ├── mlops-pinecone.md
      │  │  │     │  ├── mlops-pytorch-fsdp.md
      │  │  │     │  ├── mlops-pytorch-lightning.md
      │  │  │     │  ├── mlops-qdrant.md
      │  │  │     │  ├── mlops-research-dspy.md
      │  │  │     │  ├── mlops-saelens.md
      │  │  │     │  ├── mlops-simpo.md
      │  │  │     │  ├── mlops-slime.md
      │  │  │     │  ├── mlops-stable-diffusion.md
      │  │  │     │  ├── mlops-tensorrt-llm.md
      │  │  │     │  ├── mlops-torchtitan.md
      │  │  │     │  ├── mlops-training-axolotl.md
      │  │  │     │  ├── mlops-training-trl-fine-tuning.md
      │  │  │     │  ├── mlops-training-unsloth.md
      │  │  │     │  └── mlops-whisper.md
      │  │  │    ├── payments
      │  │  │     │  ├── payments-mpp-agent.md
      │  │  │     │  ├── payments-stripe-link-cli.md
      │  │  │     │  └── payments-stripe-projects.md
      │  │  │    ├── productivity
      │  │  │     │  ├── productivity-canvas.md
      │  │  │     │  ├── productivity-here-now.md
      │  │  │     │  ├── productivity-memento-flashcards.md
      │  │  │     │  ├── productivity-shop.md
      │  │  │     │  ├── productivity-shopify.md
      │  │  │     │  ├── productivity-siyuan.md
      │  │  │     │  └── productivity-telephony.md
      │  │  │    ├── research
      │  │  │     │  ├── research-bioinformatics.md
      │  │  │     │  ├── research-darwinian-evolver.md
      │  │  │     │  ├── research-domain-intel.md
      │  │  │     │  ├── research-drug-discovery.md
      │  │  │     │  ├── research-duckduckgo-search.md
      │  │  │     │  ├── research-gitnexus-explorer.md
      │  │  │     │  ├── research-osint-investigation.md
      │  │  │     │  ├── research-parallel-cli.md
      │  │  │     │  ├── research-pinecone-research.md
      │  │  │     │  ├── research-qmd.md
      │  │  │     │  ├── research-scrapling.md
      │  │  │     │  └── research-searxng-search.md
      │  │  │    ├── security
      │  │  │     │  ├── security-1password.md
      │  │  │     │  ├── security-godmode.md
      │  │  │     │  ├── security-oss-forensics.md
      │  │  │     │  ├── security-sherlock.md
      │  │  │     │  ├── security-unbroker.md
      │  │  │     │  └── security-web-pentest.md
      │  │  │    ├── software-development
      │  │  │     │  ├── software-development-code-wiki.md
      │  │  │     │  ├── software-development-rest-graphql-debug.md
      │  │  │     │  └── software-development-subagent-driven-development.md
      │  │  │    ├── web-development
      │  │  │     │  ├── web-development-cloudflare-temporary-deploy.md
      │  │  │     │  └── web-development-page-agent.md
      │  │  │    └── yuanbao
      │  │  │       └── yuanbao-yuanbao.md
      │  │  ├── tui.md
      │  │  ├── which-file-does-what.md
      │  │  ├── windows-native.md
      │  │  ├── windows-wsl-quickstart.md
      │  │  └── _category_.json
      │  └── user-stories.mdx
     ├── docusaurus.config.ts
     ├── i18n
      │  └── zh-Hans
      │    └── docusaurus-plugin-content-docs
      │       └── current
      │          ├── developer-guide
      │           │  ├── acp-internals.md
      │           │  ├── adding-platform-adapters.md
      │           │  ├── adding-providers.md
      │           │  ├── adding-tools.md
      │           │  ├── agent-loop.md
      │           │  ├── architecture.md
      │           │  ├── browser-supervisor.md
      │           │  ├── context-compression-and-caching.md
      │           │  ├── context-engine-plugin.md
      │           │  ├── contributing.md
      │           │  ├── creating-skills.md
      │           │  ├── cron-internals.md
      │           │  ├── extending-the-cli.md
      │           │  ├── gateway-internals.md
      │           │  ├── image-gen-provider-plugin.md
      │           │  ├── memory-provider-plugin.md
      │           │  ├── model-provider-plugin.md
      │           │  ├── plugin-llm-access.md
      │           │  ├── plugins
      │           │  │  └── index.md
      │           │  ├── programmatic-integration.md
      │           │  ├── prompt-assembly.md
      │           │  ├── provider-runtime.md
      │           │  ├── session-storage.md
      │           │  ├── tools-runtime.md
      │           │  ├── trajectory-format.md
      │           │  ├── video-gen-provider-plugin.md
      │           │  └── web-search-provider-plugin.md
      │          ├── getting-started
      │           │  ├── installation.md
      │           │  ├── learning-path.md
      │           │  ├── nix-setup.md
      │           │  ├── quickstart.md
      │           │  ├── termux.md
      │           │  └── updating.md
      │          ├── guides
      │           │  ├── automate-with-cron.md
      │           │  ├── automation-blueprints.md
      │           │  ├── aws-bedrock.md
      │           │  ├── azure-foundry.md
      │           │  ├── cron-script-only.md
      │           │  ├── cron-troubleshooting.md
      │           │  ├── daily-briefing-bot.md
      │           │  ├── delegation-patterns.md
      │           │  ├── github-pr-review-agent.md
      │           │  ├── google-gemini.md
      │           │  ├── local-llm-on-mac.md
      │           │  ├── local-ollama-setup.md
      │           │  ├── microsoft-graph-app-registration.md
      │           │  ├── migrate-from-openclaw.md
      │           │  ├── minimax-oauth.md
      │           │  ├── oauth-over-ssh.md
      │           │  ├── operate-teams-meeting-pipeline.md
      │           │  ├── pipe-script-output.md
      │           │  ├── python-library.md
      │           │  ├── run-jimmy-with-nous-portal.md
      │           │  ├── team-telegram-assistant.md
      │           │  ├── tips.md
      │           │  ├── use-mcp-with-jimmy.md
      │           │  ├── use-soul-with-jimmy.md
      │           │  ├── use-voice-mode-with-jimmy.md
      │           │  ├── webhook-github-pr-review.md
      │           │  ├── work-with-skills.md
      │           │  └── xai-grok-oauth.md
      │          ├── index.mdx
      │          ├── integrations
      │           │  ├── buzz.md
      │           │  ├── index.md
      │           │  ├── nous-portal.md
      │           │  └── providers.md
      │          ├── reference
      │           │  ├── cli-commands.md
      │           │  ├── environment-variables.md
      │           │  ├── faq.md
      │           │  ├── mcp-config-reference.md
      │           │  ├── model-catalog.md
      │           │  ├── optional-skills-catalog.md
      │           │  ├── profile-commands.md
      │           │  ├── skills-catalog.md
      │           │  ├── slash-commands.md
      │           │  ├── tools-reference.md
      │           │  └── toolsets-reference.md
      │          ├── user-guide
      │           │  ├── checkpoints-and-rollback.md
      │           │  ├── cli.md
      │           │  ├── configuration.md
      │           │  ├── configuring-models.md
      │           │  ├── docker.md
      │           │  ├── features
      │           │  │  ├── acp.md
      │           │  │  ├── api-server.md
      │           │  │  ├── batch-processing.md
      │           │  │  ├── browser.md
      │           │  │  ├── built-in-plugins.md
      │           │  │  ├── code-execution.md
      │           │  │  ├── codex-app-server-runtime.md
      │           │  │  ├── computer-use.md
      │           │  │  ├── context-files.md
      │           │  │  ├── context-references.md
      │           │  │  ├── credential-pools.md
      │           │  │  ├── cron.md
      │           │  │  ├── curator.md
      │           │  │  ├── delegation.md
      │           │  │  ├── deliverable-mode.md
      │           │  │  ├── extending-the-dashboard.md
      │           │  │  ├── fallback-providers.md
      │           │  │  ├── goals.md
      │           │  │  ├── honcho.md
      │           │  │  ├── hooks.md
      │           │  │  ├── image-generation.md
      │           │  │  ├── kanban-tutorial.md
      │           │  │  ├── kanban-worker-lanes.md
      │           │  │  ├── kanban.md
      │           │  │  ├── lsp.md
      │           │  │  ├── mcp.md
      │           │  │  ├── memory-providers.md
      │           │  │  ├── memory.md
      │           │  │  ├── overview.md
      │           │  │  ├── personality.md
      │           │  │  ├── plugins.md
      │           │  │  ├── provider-routing.md
      │           │  │  ├── skills.md
      │           │  │  ├── skins.md
      │           │  │  ├── spotify.md
      │           │  │  ├── subscription-proxy.md
      │           │  │  ├── tool-gateway.md
      │           │  │  ├── tools.md
      │           │  │  ├── tts.md
      │           │  │  ├── vision.md
      │           │  │  ├── voice-mode.md
      │           │  │  ├── web-dashboard.md
      │           │  │  ├── web-search.md
      │           │  │  └── x-search.md
      │           │  ├── git-worktrees.md
      │           │  ├── messaging
      │           │  │  ├── bluebubbles.md
      │           │  │  ├── dingtalk.md
      │           │  │  ├── discord.md
      │           │  │  ├── email.md
      │           │  │  ├── feishu.md
      │           │  │  ├── google_chat.md
      │           │  │  ├── homeassistant.md
      │           │  │  ├── index.md
      │           │  │  ├── line.md
      │           │  │  ├── matrix.md
      │           │  │  ├── mattermost.md
      │           │  │  ├── msgraph-webhook.md
      │           │  │  ├── ntfy.md
      │           │  │  ├── open-webui.md
      │           │  │  ├── qqbot.md
      │           │  │  ├── signal.md
      │           │  │  ├── simplex.md
      │           │  │  ├── slack.md
      │           │  │  ├── sms.md
      │           │  │  ├── teams-meetings.md
      │           │  │  ├── teams.md
      │           │  │  ├── telegram.md
      │           │  │  ├── webhooks.md
      │           │  │  ├── wecom-callback.md
      │           │  │  ├── wecom.md
      │           │  │  ├── weixin.md
      │           │  │  ├── whatsapp.md
      │           │  │  └── yuanbao.md
      │           │  ├── profile-distributions.md
      │           │  ├── profiles.md
      │           │  ├── secrets
      │           │  │  ├── bitwarden.md
      │           │  │  └── index.md
      │           │  ├── security.md
      │           │  ├── sessions.md
      │           │  ├── skills
      │           │  │  ├── bundled
      │           │  │  │  ├── apple
      │           │  │  │  │  ├── apple-apple-notes.md
      │           │  │  │  │  ├── apple-apple-reminders.md
      │           │  │  │  │  ├── apple-findmy.md
      │           │  │  │  │  ├── apple-imessage.md
      │           │  │  │  │  └── apple-macos-computer-use.md
      │           │  │  │  ├── autonomous-ai-agents
      │           │  │  │  │  ├── autonomous-ai-agents-claude-code.md
      │           │  │  │  │  ├── autonomous-ai-agents-codex.md
      │           │  │  │  │  ├── autonomous-ai-agents-jimmy-agent.md
      │           │  │  │  │  └── autonomous-ai-agents-opencode.md
      │           │  │  │  ├── creative
      │           │  │  │  │  ├── creative-architecture-diagram.md
      │           │  │  │  │  ├── creative-ascii-art.md
      │           │  │  │  │  ├── creative-ascii-video.md
      │           │  │  │  │  ├── creative-baoyu-infographic.md
      │           │  │  │  │  ├── creative-claude-design.md
      │           │  │  │  │  ├── creative-comfyui.md
      │           │  │  │  │  ├── creative-design-md.md
      │           │  │  │  │  ├── creative-excalidraw.md
      │           │  │  │  │  ├── creative-humanizer.md
      │           │  │  │  │  ├── creative-manim-video.md
      │           │  │  │  │  ├── creative-p5js.md
      │           │  │  │  │  ├── creative-popular-web-designs.md
      │           │  │  │  │  ├── creative-pretext.md
      │           │  │  │  │  ├── creative-sketch.md
      │           │  │  │  │  ├── creative-songwriting-and-ai-music.md
      │           │  │  │  │  └── creative-touchdesigner-mcp.md
      │           │  │  │  ├── email
      │           │  │  │  │  └── email-himalaya.md
      │           │  │  │  ├── github
      │           │  │  │  │  ├── github-codebase-inspection.md
      │           │  │  │  │  ├── github-github-auth.md
      │           │  │  │  │  ├── github-github-code-review.md
      │           │  │  │  │  ├── github-github-issues.md
      │           │  │  │  │  ├── github-github-pr-workflow.md
      │           │  │  │  │  └── github-github-repo-management.md
      │           │  │  │  ├── media
      │           │  │  │  │  ├── media-gif-search.md
      │           │  │  │  │  ├── media-songsee.md
      │           │  │  │  │  └── media-youtube-content.md
      │           │  │  │  ├── mlops
      │           │  │  │  │  ├── mlops-evaluation-evaluating-llms-harness.md
      │           │  │  │  │  ├── mlops-evaluation-weights-and-biases.md
      │           │  │  │  │  ├── mlops-huggingface-hub.md
      │           │  │  │  │  ├── mlops-inference-llama-cpp.md
      │           │  │  │  │  └── mlops-inference-serving-llms-vllm.md
      │           │  │  │  ├── note-taking
      │           │  │  │  │  └── note-taking-obsidian.md
      │           │  │  │  ├── productivity
      │           │  │  │  │  ├── productivity-airtable.md
      │           │  │  │  │  ├── productivity-google-workspace.md
      │           │  │  │  │  ├── productivity-maps.md
      │           │  │  │  │  ├── productivity-nano-pdf.md
      │           │  │  │  │  ├── productivity-notion.md
      │           │  │  │  │  ├── productivity-ocr-and-documents.md
      │           │  │  │  │  ├── productivity-powerpoint.md
      │           │  │  │  │  └── productivity-teams-meeting-pipeline.md
      │           │  │  │  ├── research
      │           │  │  │  │  ├── research-arxiv.md
      │           │  │  │  │  ├── research-blogwatcher.md
      │           │  │  │  │  ├── research-llm-wiki.md
      │           │  │  │  │  └── research-research-paper-writing.md
      │           │  │  │  ├── smart-home
      │           │  │  │  │  └── smart-home-openhue.md
      │           │  │  │  ├── social-media
      │           │  │  │  │  └── social-media-xurl.md
      │           │  │  │  └── software-development
      │           │  │  │    ├── software-development-dogfood.md
      │           │  │  │    ├── software-development-jimmy-agent-skill-authoring.md
      │           │  │  │    ├── software-development-node-inspect-debugger.md
      │           │  │  │    ├── software-development-plan.md
      │           │  │  │    ├── software-development-python-debugpy.md
      │           │  │  │    ├── software-development-requesting-code-review.md
      │           │  │  │    ├── software-development-spike.md
      │           │  │  │    ├── software-development-systematic-debugging.md
      │           │  │  │    └── software-development-test-driven-development.md
      │           │  │  ├── google-workspace.md
      │           │  │  └── optional
      │           │  │    ├── autonomous-ai-agents
      │           │  │     │  ├── autonomous-ai-agents-blackbox.md
      │           │  │     │  └── autonomous-ai-agents-honcho.md
      │           │  │    ├── blockchain
      │           │  │     │  ├── blockchain-evm.md
      │           │  │     │  ├── blockchain-hyperliquid.md
      │           │  │     │  └── blockchain-solana.md
      │           │  │    ├── communication
      │           │  │     │  └── communication-one-three-one-rule.md
      │           │  │    ├── creative
      │           │  │     │  ├── creative-audiocraft-audio-generation.md
      │           │  │     │  ├── creative-concept-diagrams.md
      │           │  │     │  ├── creative-heartmula.md
      │           │  │     │  ├── creative-hyperframes.md
      │           │  │     │  ├── creative-kanban-video-orchestrator.md
      │           │  │     │  └── creative-meme-generation.md
      │           │  │    ├── data-science
      │           │  │     │  └── data-science-jupyter-notebook.md
      │           │  │    ├── devops
      │           │  │     │  ├── devops-docker-management.md
      │           │  │     │  ├── devops-inference-sh-cli.md
      │           │  │     │  ├── devops-pinggy-tunnel.md
      │           │  │     │  └── devops-watchers.md
      │           │  │    ├── dogfood
      │           │  │     │  └── dogfood-adversarial-ux-test.md
      │           │  │    ├── email
      │           │  │     │  └── email-agentmail.md
      │           │  │    ├── finance
      │           │  │     │  ├── finance-3-statement-model.md
      │           │  │     │  ├── finance-comps-analysis.md
      │           │  │     │  ├── finance-dcf-model.md
      │           │  │     │  ├── finance-excel-author.md
      │           │  │     │  ├── finance-lbo-model.md
      │           │  │     │  ├── finance-merger-model.md
      │           │  │     │  ├── finance-polymarket.md
      │           │  │     │  ├── finance-pptx-author.md
      │           │  │     │  └── finance-stocks.md
      │           │  │    ├── health
      │           │  │     │  ├── health-fitness-nutrition.md
      │           │  │     │  └── health-neuroskill-bci.md
      │           │  │    ├── mcp
      │           │  │     │  ├── mcp-fastmcp.md
      │           │  │     │  └── mcp-mcporter.md
      │           │  │    ├── migration
      │           │  │     │  └── migration-openclaw-migration.md
      │           │  │    ├── mlops
      │           │  │     │  ├── mlops-accelerate.md
      │           │  │     │  ├── mlops-chroma.md
      │           │  │     │  ├── mlops-clip.md
      │           │  │     │  ├── mlops-faiss.md
      │           │  │     │  ├── mlops-flash-attention.md
      │           │  │     │  ├── mlops-guidance.md
      │           │  │     │  ├── mlops-huggingface-tokenizers.md
      │           │  │     │  ├── mlops-inference-outlines.md
      │           │  │     │  ├── mlops-instructor.md
      │           │  │     │  ├── mlops-lambda-labs.md
      │           │  │     │  ├── mlops-llava.md
      │           │  │     │  ├── mlops-modal.md
      │           │  │     │  ├── mlops-models-segment-anything-model.md
      │           │  │     │  ├── mlops-nemo-curator.md
      │           │  │     │  ├── mlops-peft.md
      │           │  │     │  ├── mlops-pinecone.md
      │           │  │     │  ├── mlops-pytorch-fsdp.md
      │           │  │     │  ├── mlops-pytorch-lightning.md
      │           │  │     │  ├── mlops-qdrant.md
      │           │  │     │  ├── mlops-saelens.md
      │           │  │     │  ├── mlops-simpo.md
      │           │  │     │  ├── mlops-slime.md
      │           │  │     │  ├── mlops-stable-diffusion.md
      │           │  │     │  ├── mlops-tensorrt-llm.md
      │           │  │     │  ├── mlops-torchtitan.md
      │           │  │     │  ├── mlops-training-axolotl.md
      │           │  │     │  ├── mlops-training-trl-fine-tuning.md
      │           │  │     │  ├── mlops-training-unsloth.md
      │           │  │     │  └── mlops-whisper.md
      │           │  │    ├── productivity
      │           │  │     │  ├── productivity-canvas.md
      │           │  │     │  ├── productivity-here-now.md
      │           │  │     │  ├── productivity-memento-flashcards.md
      │           │  │     │  ├── productivity-shop.md
      │           │  │     │  ├── productivity-shopify.md
      │           │  │     │  ├── productivity-siyuan.md
      │           │  │     │  └── productivity-telephony.md
      │           │  │    ├── research
      │           │  │     │  ├── research-bioinformatics.md
      │           │  │     │  ├── research-darwinian-evolver.md
      │           │  │     │  ├── research-domain-intel.md
      │           │  │     │  ├── research-drug-discovery.md
      │           │  │     │  ├── research-duckduckgo-search.md
      │           │  │     │  ├── research-gitnexus-explorer.md
      │           │  │     │  ├── research-osint-investigation.md
      │           │  │     │  ├── research-parallel-cli.md
      │           │  │     │  ├── research-qmd.md
      │           │  │     │  ├── research-scrapling.md
      │           │  │     │  └── research-searxng-search.md
      │           │  │    ├── security
      │           │  │     │  ├── security-1password.md
      │           │  │     │  ├── security-oss-forensics.md
      │           │  │     │  └── security-sherlock.md
      │           │  │    ├── software-development
      │           │  │     │  └── software-development-rest-graphql-debug.md
      │           │  │    ├── web-development
      │           │  │     │  └── web-development-page-agent.md
      │           │  │    └── yuanbao
      │           │  │       └── yuanbao-yuanbao.md
      │           │  ├── tui.md
      │           │  ├── windows-native.md
      │           │  └── windows-wsl-quickstart.md
      │          └── user-stories.mdx
     ├── package-lock.json
     ├── package.json
     ├── README.md
     ├── scripts
      │  ├── extract-automation-blueprints.py
      │  ├── extract-skills.py
      │  ├── generate-llms-txt.py
      │  ├── generate-skill-docs.py
      │  └── prebuild.mjs
     ├── sidebars.ts
     ├── src
      │  ├── components
      │  │  ├── AutomationBlueprintsCatalog
      │  │  │  ├── index.tsx
      │  │  │  └── styles.module.css
      │  │  └── UserStoriesCollage
      │  │    ├── index.tsx
      │  │    └── styles.module.css
      │  ├── css
      │  │  └── custom.css
      │  ├── data
      │  │  └── userStories.json
      │  └── pages
      │    └── skills
      │       ├── index.tsx
      │       └── styles.module.css
     ├── static
      │  ├── api
      │  │  └── model-catalog.json
      │  ├── img
      │  │  ├── apple-touch-icon.png
      │  │  ├── dashboard
      │  │  │  ├── admin-channels.png
      │  │  │  ├── admin-config.png
      │  │  │  ├── admin-hook-create.png
      │  │  │  ├── admin-mcp.png
      │  │  │  ├── admin-pairing.png
      │  │  │  ├── admin-sessions.png
      │  │  │  ├── admin-skills-hub.png
      │  │  │  ├── admin-system-curator.png
      │  │  │  ├── admin-system-ops.png
      │  │  │  ├── admin-system-top.png
      │  │  │  └── admin-webhooks.png
      │  │  ├── docs
      │  │  │  ├── cli-layout.svg
      │  │  │  ├── dashboard-models
      │  │  │  │  ├── auxiliary-expanded.png
      │  │  │  │  ├── overview.png
      │  │  │  │  ├── picker-dialog.png
      │  │  │  │  └── use-as-dropdown.png
      │  │  │  ├── session-recap.svg
      │  │  │  └── tui-session-orchestrator
      │  │  │    ├── session-orchestrator-demo.mp4
      │  │  │    └── session-orchestrator.png
      │  │  ├── favicon-16x16.png
      │  │  ├── favicon-32x32.png
      │  │  ├── favicon.ico
      │  │  ├── favicon.svg
      │  │  ├── jimmy-agent-banner.png
      │  │  ├── kanban-tutorial
      │  │  │  ├── 01-board-overview.png
      │  │  │  ├── 02-board-flat.png
      │  │  │  ├── 03-drawer-schema-task.png
      │  │  │  ├── 04b-drawer-retry-history-scrolled.png
      │  │  │  ├── 06-drawer-crash-recovery.png
      │  │  │  ├── 07-fleet-transcribes.png
      │  │  │  ├── 08-pipeline-auth.png
      │  │  │  ├── 09-drawer-pipeline-review.png
      │  │  │  ├── 10-drawer-in-flight.png
      │  │  │  └── 11-drawer-gave-up.png
      │  │  ├── logo.png
      │  │  └── nous-logo.png
      │  └── oauth
      │    └── client-metadata.json
     └── tsconfig.json
```

### File List
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\AGENTS.md
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\batch_runner.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\cli-config.yaml.example
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\cli.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\constraints-termux.txt
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\CONTRIBUTING.es.md
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\CONTRIBUTING.md
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\default.tar.gz
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\docker-compose.windows.yml
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\docker-compose.yml
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\Dockerfile
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\eslint.config.shared.mjs
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\flake.lock
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\flake.nix
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy_bootstrap.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy_constants.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy_logging.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy_state.py
- c:\Users\Arnav Singh\Documents\Codes\jimmy-agent-main\jimmy_state_common.py

... and 9851 more files
