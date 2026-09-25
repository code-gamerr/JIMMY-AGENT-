import { useEffect, useState } from 'react'

import { cn } from '@/lib/utils'

export interface MissionCard {
  agent_id: string
  label: string
  capability: string
  description: string
  status: 'active' | 'assigned' | 'assigning' | 'completed' | 'failed' | 'waiting' | string
}

export interface MissionSnapshot {
  phase: string
  headline: string
  cards: MissionCard[]
  error?: string
}

const STATE_LABEL: Record<string, string> = {
  assigning: 'ASSIGNING',
  assigned: 'ASSIGNED',
  waiting: 'WAITING',
  active: 'ACTIVE',
  completed: 'COMPLETED',
  failed: 'FAILED'
}

export function MissionTimeline({ snapshot }: { snapshot: MissionSnapshot | null }) {
  if (!snapshot) {
    return null
  }

  return (
    <section
      className="mb-4 rounded-xl border border-(--ui-stroke-secondary) bg-(--ui-bg-secondary) px-4 py-3"
      data-slot="orchestrator-activity"
    >
      <div className="text-[0.7rem] font-semibold tracking-[0.14em] text-(--ui-text-tertiary)">ORCHESTRATOR</div>
      <div className="mt-1 text-[length:var(--conversation-text-font-size)] text-foreground">{snapshot.headline}</div>
      <div className="mt-3 grid gap-2">
        {snapshot.cards.map(card => (
          <div
            className="rounded-lg border border-(--ui-stroke-secondary) px-3 py-2"
            data-agent={card.agent_id}
            data-status={card.status}
            key={`${card.agent_id}-${card.status}`}
          >
            <div className="font-medium text-foreground">{card.label}</div>
            <div className="text-[length:var(--conversation-caption-font-size)] text-(--ui-text-tertiary)">
              {card.description}
            </div>
            <div
              className={cn(
                'mt-1 font-mono text-[0.7rem] tracking-wide',
                card.status === 'active' || card.status === 'waiting' ? 'text-sky-500' : 'text-emerald-600',
                card.status === 'failed' && 'text-destructive'
              )}
            >
              {STATE_LABEL[card.status] || 'NOT STARTED'}
            </div>
          </div>
        ))}
      </div>
      {snapshot.phase === 'assigned' || snapshot.phase === 'starting' ? (
        <div className="mt-3 text-[length:var(--conversation-caption-font-size)] text-emerald-600">
          All tasks assigned. {snapshot.phase === 'starting' ? 'Execution starting.' : 'Required agents ready.'}
        </div>
      ) : null}
      {snapshot.error ? <div className="mt-2 text-destructive">{snapshot.error}</div> : null}
    </section>
  )
}

const CC_BASE = 'http://127.0.0.1:8765'

export function OrchestratorActivity() {
  const [snapshot, setSnapshot] = useState<MissionSnapshot | null>(null)

  useEffect(() => {
    const token = window.localStorage.getItem('jimmy-cc-token') || window.localStorage.getItem('jimmyToken')

    if (!token) {
      return
    }

    let stopped = false

    async function tick() {
      try {
        const listed = await fetch(`${CC_BASE}/api/jimmy/tasks`, {
          headers: { 'x-jimmy-token': token }
        })

        if (!listed.ok) {
          return
        }

        const body = await listed.json()
        const tasks = body.data || []
        const latest = tasks[0]

        if (!latest) {
          return
        }

        const detail = await fetch(`${CC_BASE}/api/jimmy/tasks/${latest.task_id}`, {
          headers: { 'x-jimmy-token': token }
        })

        if (!detail.ok || stopped) {
          return
        }

        const payload = await detail.json()

        if (!stopped) {
          setSnapshot(payload.data?.narration || null)
        }
      } catch {
        // Command Center is optional and loopback-only.
      }
    }

    void tick()
    const id = window.setInterval(() => void tick(), 1500)

    return () => {
      stopped = true
      window.clearInterval(id)
    }
  }, [])

  return <MissionTimeline snapshot={snapshot} />
}
