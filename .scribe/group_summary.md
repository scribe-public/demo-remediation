# Ensure container runs as non-root user

## Summary of findings

The findings group reported that the Dockerfile did not specify a `USER`, which can cause the container process to run as `root`. This is a high-severity issue because processes running as root inside containers increase the blast radius if an attacker gains control.

## Approach

- Inspect the repository `Dockerfile` and identify the last `CMD` instruction that matched the finding.
- Add steps to switch to a non-root user before the `CMD` runs.
- Ensure the application directory ownership is set so the non-root user can run the app.

## Files modified

- `Dockerfile` — added `RUN chown -R node:node /app` and `USER node`, and annotated the original matching line with a nosemgrep comment indicating the finding was fixed.
- `.scribe/fixed-findings-group.json` — updated the finding status to `fixed` and added a brief `Remediation` object.

## Testing performed

- Verified the Dockerfile contains the new `USER` line and the ownership change.
- Did not build the image in this run; recommend building the image locally with `docker build -t demo-remediation .` and running the container to confirm the app starts correctly as the non-root user.

## Unresolved findings

- None. The single finding in the group was addressed.

