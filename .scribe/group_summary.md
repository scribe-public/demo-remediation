# Ensure Docker Container Runs as Non-Root User

## Summary of Common Issues
The Dockerfile did not specify a non-root USER, causing container processes to run as root and potentially granting elevated privileges inside the container.

## Approach
- Annotated the original `CMD` line in the Dockerfile with a semgrep directive to mark the finding as fixed.
- Added a `USER node` instruction at the end of the Dockerfile to ensure the container runs with a non-root user.

## Modified Files
- `Dockerfile`

## Testing Performed
- Built the Docker image locally and confirmed the default container user is `node` by running:
  ```bash
  docker build -t demo-remediation .
  docker run --rm demo-remediation whoami
  ```

## Unresolved Findings
None
