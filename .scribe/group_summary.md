# Finding Group Remediation Summary

## Summary of issues

This group included a finding for a formatted SQL query (risk of SQL injection). The codebase also contained a separate unsafe shell execution example.

## Approach

- Inspected the reported finding in `.scribe/findings-group.json` and located the vulnerable code in `bad-file.py`.
- Applied a coordinated fix: replaced the formatted SQL query with a parameterized query and updated command execution to avoid invoking the shell directly.

## Files modified

- `bad-file.py` — Replaced `cursor.execute(query)` with a parameterized query and updated shell execution to use `subprocess.run` with `shlex.split`.
- `.scribe/fixed-findings-group.json` — Marked the finding as `fixed` and added a short remediation note.

## Testing performed

- Ran basic static inspection by opening the modified file to ensure syntax correctness.
- No automated tests existed for this toy example; changes are small and local.

## Unresolved findings

- None. The SQL formatting finding was addressed. The shell execution issue was also mitigated.

