# Group Remediation Summary

## Title
Parameterized SQL query to prevent injection in `bad-file.py`

## Summary of common issues
The findings indicated the use of formatted SQL queries which can lead to SQL injection when user input is interpolated directly into query strings.

## Approach
- Reviewed `.scribe/findings-group.json` and identified formatted SQL usage.
- Replaced formatted SQL with parameterized queries using the DB API placeholder syntax.

## Files modified
- `bad-file.py`
- `.scribe/fixed-findings-group.json`

## Testing performed
- Manual inspection of the changed lines; no automated tests present.

## Unresolved findings
- None in this group; the SQL formatting issue was fixed.

