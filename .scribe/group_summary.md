# Secure Container User Configuration

## Summary
- Common issue: Dockerfile lacked a final non-root `USER`, allowing the app to run as `root`.
- Risk: Processes running as `root` increase impact of compromise within the container.

## Approach
- Added `RUN chown -R node:node /app` to ensure correct ownership.
- Set `USER node` to drop privileges.
- Annotated the original `CMD` line with `# nosemgrep: dockerfile.security.missing-user.missing-user # fixed` per instructions.

## Modified Files
- `Dockerfile`

## Testing
- Static review only. Change is limited to Dockerfile directives used broadly in Node images. No functional app code altered.

## Unresolved Findings
- None — the finding is addressed by running as a non-root user.

Tokens used: 1502
