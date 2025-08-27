# Non-Root User for Dockerfile

## Summary of Common Issues
- Missing `USER` directive in the Dockerfile meant the container would run processes as `root`, violating least-privilege and triggering semgrep rule `dockerfile.security.missing-user.missing-user`.

## Fix Approach
- Ensured app files are owned by a non-root user and switched to that user before the `CMD` instruction.
- Added an inline `# nosemgrep: dockerfile.security.missing-user.missing-user # fixed ...` comment on the original finding line to document remediation, as requested.

## Files Modified
- `Dockerfile`
- `.scribe/fixed-findings-group.json`
- `.scribe/group_summary.md` (this file)

## Testing Performed
- Static remediation: the rule expects the last `USER` to be non-root; added `USER node` and ownership change to `/app`. No runtime/container tests executed in this environment.

## Unresolved Findings
- None. The single finding in the group was fixed.


Tokens used: 1078
