# Non-root User Enforcement in Dockerfile

## Summary of Issues
- Missing `USER` instruction caused the container to default to running as `root`, increasing risk if a process is compromised.

## Remediation Approach
- Ensured the final `USER` is non-root by setting `USER node`.
- Set correct ownership for the app directory with `RUN chown -R node:node /app`.
- Annotated the original finding line with: `# nosemgrep: dockerfile.security.missing-user.missing-user # fixed added non-root USER`.

## Files Modified
- `Dockerfile`

## Testing Performed
- Static validation by reviewing the Dockerfile to confirm the last `USER` is non-root and the annotation is present on the original `CMD` line.

## Unresolved Findings
- None. The finding group’s single issue is resolved.


Tokens used: 1859
