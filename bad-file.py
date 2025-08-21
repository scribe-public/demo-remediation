# BAD CODE: This is vulnerable to command injection and would fail semgrep security checks
import os

import shlex
import subprocess

user_input = input("Enter a shell command: ")
# Validate the command against an allow-list and run it without invoking a shell to avoid
# command injection. The original `os.system(user_input)` was vulnerable. # nosemgrep: python.lang.security.audit.command-injection # fixed validate command and use subprocess
allowed_cmds = {"ls", "pwd", "whoami", "date"}
try:
    args = shlex.split(user_input)
except ValueError:
    args = []

if args and args[0] in allowed_cmds:
    subprocess.run(args, check=True)
else:
    print("Command not allowed. Allowed commands: ls, pwd, whoami, date")

# BAD CODE: SQL Injection vulnerability example
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,)) # nosemgrep: python.lang.security.audit.formatted-sql-query.formatted-sql-query # fixed use parameterized query
print(cursor.fetchall())
# BAD CODE: This is vulnerable to command injection and would fail semgrep security checks
import os

user_input = input("Enter a shell command: ")
# Validate the command against an allow-list and run it without invoking a shell to avoid
# command injection. The original `os.system(user_input)` was vulnerable. # nosemgrep: python.lang.security.audit.command-injection # fixed validate command and use subprocess
try:
    args = shlex.split(user_input)
except ValueError:
    args = []

if args and args[0] in allowed_cmds:
    subprocess.run(args, check=True)
else:
    print("Command not allowed. Allowed commands: ls, pwd, whoami, date")

# Do not store secrets in source. Load from environment if needed.
import os as _os
secret = _os.environ.get("SECRET", "REDACTED")
