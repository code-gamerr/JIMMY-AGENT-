import { describe, expect, it } from 'vitest'

import {
  normalizeJimmyOpenString,
  pathFromJimmyDeepLink,
  pathFromOpenDeepLink,
  resolveJimmyOpenPath
} from './jimmy-open-target'

describe('normalizeJimmyOpenString', () => {
  it('accepts hash-router paths and strips a leading hash', () => {
    expect(normalizeJimmyOpenString('/index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeJimmyOpenString('#/index-network/intent/1')).toBe('/index-network/intent/1')
  })

  it('maps plugin-scoped jimmy:// deep links to the same path', () => {
    expect(normalizeJimmyOpenString('jimmy://index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeJimmyOpenString('jimmy://index-network/intent/1?focus=true')).toBe(
      '/index-network/intent/1?focus=true'
    )
  })

  it('maps jimmy://open/… deep links by stripping the open host', () => {
    expect(normalizeJimmyOpenString('jimmy://open/index-network/intent/1')).toBe('/index-network/intent/1')
    expect(normalizeJimmyOpenString('jimmy://open/settings/plugins')).toBe('/settings/plugins')
  })

  it('rejects reserved jimmy kinds and unsafe paths', () => {
    expect(normalizeJimmyOpenString('jimmy://blueprint/morning-brief')).toBeNull()
    expect(normalizeJimmyOpenString('jimmy://plugin/install')).toBeNull()
    expect(normalizeJimmyOpenString('https://example.com/x')).toBeNull()
    expect(normalizeJimmyOpenString('/../etc/passwd')).toBeNull()
    expect(normalizeJimmyOpenString('index-network')).toBeNull()
  })
})

describe('resolveJimmyOpenPath', () => {
  it('merges structured path + params', () => {
    expect(resolveJimmyOpenPath({ path: '/index-network/intent/1', params: { focus: 'true' } })).toBe(
      '/index-network/intent/1?focus=true'
    )
  })

  it('resolves href the same as a bare string', () => {
    expect(resolveJimmyOpenPath({ href: 'jimmy://index-network/intent/1' })).toBe('/index-network/intent/1')
  })
})

describe('pathFromJimmyDeepLink', () => {
  it('builds the navigate path from a plugin-scoped deep-link payload', () => {
    expect(pathFromJimmyDeepLink('index-network', 'intent/1')).toBe('/index-network/intent/1')
  })

  it('builds the navigate path from jimmy://open/… payloads', () => {
    expect(pathFromOpenDeepLink('index-network/intent/1')).toBe('/index-network/intent/1')
    expect(pathFromJimmyDeepLink('open', 'agent/42')).toBe('/agent/42')
  })

  it('ignores reserved kinds', () => {
    expect(pathFromJimmyDeepLink('blueprint', 'morning-brief')).toBeNull()
    expect(pathFromJimmyDeepLink('plugin', 'install')).toBeNull()
  })
})
