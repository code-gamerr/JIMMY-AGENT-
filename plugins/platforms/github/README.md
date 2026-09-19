# GitHub platform (DeerFlow parity)

DeerFlow runs a dedicated GitHub webhook → agent → comment channel.
Jimmy covers the same loop via the **webhook** adapter plus this recipe.

## Setup

1. Create a GitHub webhook on your repo:
   - Payload URL: `https://<your-jimmy-host>/webhooks/github` (or your webhook path)
   - Content type: `application/json`
   - Secret: set as `GITHUB_WEBHOOK_SECRET` in `~/.jimmy/.env`
   - Events: Issues, Issue comments, Pull requests, PR review comments

2. Set `GITHUB_TOKEN` with permission to post comments.

3. Add a route under `platforms.webhook.extra.routes` in gateway config
   (or merge `GITHUB_ROUTE_RECIPE` from `plugins.platforms.github`).

Example:

```yaml
platforms:
  webhook:
    enabled: true
    extra:
      routes:
        - name: github
          events: [issues, issue_comment, pull_request, pull_request_review_comment]
          secret_env: GITHUB_WEBHOOK_SECRET
          deliver: github_comment
          prompt: |
            You are Jimmy responding on GitHub.
            Event: {event}
            Repo: {repository[full_name]}
            Sender: {sender[login]}
            Payload:
            {payload_json}
```

Enable the plugin: `jimmy plugins enable platforms/github` (loads recipe helpers).
