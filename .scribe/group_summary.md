# Dockerfile: Add non-root user and ownership

## Summary of Common Issues

The findings group identified a Dockerfile that does not specify a `USER`, which allows containers to run as root. This increases the risk that a process compromise inside the container could lead to escalated privileges.

## Approach

- Inspect the `Dockerfile` referenced by the finding.
- Use the non-root `node` user provided by the base `node:latest` image.
- Ensure the application directory is owned by that non-root user so it can write runtime files.
- Annotate the original line flagged by the scanner with the required `nosemgrep` comment.

## Files Modified

- `Dockerfile` — added `RUN chown -R node:node /app` and `USER node`, and annotated the original CMD line.
- `.scribe/fixed-findings-group.json` — recorded remediation status and commit link.

## Testing Performed

- Basic linting of Dockerfile by visual inspection.
- Confirmed repository commits were created and include the changes.

## Unresolved Findings

All findings in the group were addressed.

