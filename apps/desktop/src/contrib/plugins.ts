/**
 * Plugin discovery — both delivery modes:
 *
 *  - BUNDLED: every `src/plugins/<name>/plugin.{js,ts,tsx}` default-exporting
 *    a `JimmyPlugin` registers automatically (vite glob — drop a folder in).
 *    `jimmy-bots` (Bot Mode) ships in-tree and is ON by default; other
 *    reference/demo plugins live in the companion `jimmy-example-plugins`
 *    repo. `.js` entries are SDK-consumer plugins adopted from standalone
 *    repos — they keep the plain-ESM plugin.js form so the file stays
 *    loadable by older desktops' runtime door too.
 *  - RUNTIME: the on-disk doors (`<jimmy home>/desktop-plugins/<name>/plugin.js`
 *    and the unified-package half `<jimmy home>/plugins/<name>/desktop/plugin.js`)
 *    — the agent's/user's doors, watched + hot-reloaded by the runtime loader.
 */

import { createPluginContext, type JimmyPlugin } from './plugin'
import { pluginActive, publishPlugin } from './plugins-store'
import { watchRuntimePlugins } from './runtime-loader'

const modules = import.meta.glob<{ default: JimmyPlugin }>('../plugins/*/plugin.{js,ts,tsx}', { eager: true })

// One-shot init guard. Contributions themselves register by id (re-registering
// is idempotent), but the disk-door watcher setup below (watchRuntimePlugins)
// must NOT run twice — so discovery is guarded to a single pass, not re-run on
// HMR.
let loaded = false

export function discoverBundledPlugins(): void {
  if (loaded) {
    return
  }

  loaded = true

  for (const [path, mod] of Object.entries(modules)) {
    const plugin = mod.default

    if (!plugin?.id || typeof plugin.register !== 'function') {
      console.warn(`[plugins] ${path} has no valid default JimmyPlugin export — skipped`)

      continue
    }

    // Same inventory + live-toggle contract as runtime plugins: each bundled
    // plugin publishes a record with activate/deactivate handles, and a
    // persisted disable survives boots by skipping registration here.
    const record = {
      id: plugin.id,
      name: plugin.name ?? plugin.id,
      description: plugin.description,
      kind: 'bundled' as const
    }

    let disposers: (() => void)[] = []

    const activate = () => {
      disposers.forEach(dispose => dispose())
      disposers = []

      try {
        plugin.register(createPluginContext(plugin.id, dispose => disposers.push(dispose)))
        publishPlugin({ ...record, status: 'loaded' })
      } catch (error) {
        console.error(`[plugins] ${plugin.id} failed to register`, error)
        publishPlugin({ ...record, status: 'error', error: error instanceof Error ? error.message : String(error) })
      }
    }

    const deactivate = () => {
      disposers.forEach(dispose => dispose())
      disposers = []
    }

    publishPlugin({ ...record, status: 'disabled' }, { activate, deactivate })

    if (pluginActive(plugin.id, plugin.defaultEnabled ?? true)) {
      activate()
    }
  }

  // The SELF-MAINTAINING disk door (fs-watched hot reloads, slow folder
  // reconciliation) — the runtime loader pipeline's real, shipping consumer.
  watchRuntimePlugins()
}
