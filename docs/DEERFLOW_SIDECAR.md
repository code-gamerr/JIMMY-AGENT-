# Jimmy lean deploy notes (DeerFlow sidecar)

Jimmy’s primary deploy paths remain:

- `docker-compose.yml` / `docker-compose.windows.yml` (gateway + dashboard)
- `.azure/` Container Apps notes

There is **no** full Jimmy Helm chart that clones DeerFlow’s nginx/frontend/provisioner stack.

For the DeerFlow research appliance (Next.js + LangGraph + optional Helm):

```bash
jimmy deerflow setup
jimmy deerflow up
# or Helm directly:
# helm upgrade --install deer-flow ./deer-flow/deploy/helm/deer-flow
jimmy deerflow doctor
jimmy deerflow down
```

Set `DEER_FLOW_HOME` if the tree is not at `./deer-flow`.
