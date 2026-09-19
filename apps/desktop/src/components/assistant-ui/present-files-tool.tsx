'use client'

import { type ToolCallMessagePartProps } from '@assistant-ui/react'
import { type FC, useMemo } from 'react'

import { ToolFallback } from '@/components/assistant-ui/tool/fallback'
import { WIDGET_SHELL_CLASS } from '@/components/chat/widget-shell'
import { useI18n } from '@/i18n'
import { FileText, FolderOpen } from '@/lib/icons'
import { cn } from '@/lib/utils'
import { openPreview } from '@/store/preview'

type PresentedFile = {
  name: string
  presented_path?: string
  size_bytes?: number
  source?: string
}

type PresentFilesResult = {
  ok?: boolean
  title?: string
  outputs_dir?: string
  presented?: PresentedFile[]
  errors?: string[]
  hint?: string
}

function parsePresentFilesResult(result: unknown): PresentFilesResult | null {
  if (result == null) {
    return null
  }

  let raw: unknown = result

  if (typeof result === 'string') {
    try {
      raw = JSON.parse(result)
    } catch {
      return null
    }
  }

  if (!raw || typeof raw !== 'object') {
    return null
  }

  return raw as PresentFilesResult
}

function formatBytes(size?: number): string {
  if (size == null || !Number.isFinite(size) || size < 0) {
    return ''
  }

  if (size < 1024) {
    return `${size} B`
  }

  if (size < 1024 * 1024) {
    return `${(size / 1024).toFixed(1)} KB`
  }

  return `${(size / (1024 * 1024)).toFixed(1)} MB`
}

/** Compact artifact chrome for `present_files` tool results. */
export const PresentFilesTool: FC<ToolCallMessagePartProps> = props => {
  const { t } = useI18n()
  const copy = t.assistant.presentFiles
  const parsed = useMemo(() => parsePresentFilesResult(props.result), [props.result])

  if (props.result === undefined) {
    return <ToolFallback {...props} />
  }

  if (!parsed?.ok || !parsed.presented?.length) {
    return <ToolFallback {...props} />
  }

  const title = (parsed.title || copy.defaultTitle).trim() || copy.defaultTitle

  return (
    <div className={cn(WIDGET_SHELL_CLASS, 'my-1.5 grid gap-2 p-3')} data-slot="present-files">
      <div className="flex items-center justify-between gap-2">
        <p className="min-w-0 truncate text-[0.8125rem] font-medium text-foreground">{title}</p>
        {parsed.outputs_dir ? (
          <span className="shrink-0 text-[0.6875rem] text-muted-foreground">{copy.bundle}</span>
        ) : null}
      </div>

      <ul className="grid gap-1">
        {parsed.presented.map(file => {
          const path = file.presented_path || file.source || ''
          const size = formatBytes(file.size_bytes)

          return (
            <li key={`${file.name}:${path}`}>
              <button
                className="flex w-full items-center gap-2 rounded-md px-2 py-1.5 text-left text-[0.75rem] hover:bg-muted/60"
                onClick={() => {
                  if (!path) {
                    return
                  }

                  const fileUrl = path.startsWith('file:')
                    ? path
                    : `file://${path.replace(/\\/g, '/')}`

                  openPreview(
                    {
                      kind: 'file',
                      label: file.name,
                      path,
                      source: path,
                      url: fileUrl,
                      byteSize: file.size_bytes
                    },
                    'tool-result'
                  )
                }}
                type="button"
              >
                <FileText className="size-3.5 shrink-0 text-muted-foreground" />
                <span className="min-w-0 flex-1 truncate text-foreground">{file.name}</span>
                {size ? <span className="shrink-0 tabular-nums text-muted-foreground">{size}</span> : null}
              </button>
            </li>
          )
        })}
      </ul>

      {parsed.outputs_dir ? (
        <p className="flex items-center gap-1.5 text-[0.6875rem] text-muted-foreground">
          <FolderOpen className="size-3 shrink-0" />
          <span className="truncate">{parsed.outputs_dir}</span>
        </p>
      ) : null}
    </div>
  )
}
