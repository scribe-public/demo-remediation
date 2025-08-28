# BAD CODE: This is vulnerable to command injection and would fail semgrep security checks
import subprocess
import shlex

# Safer command execution: avoid invoking the shell directly
# Split the user input and execute with shell=False to reduce
# the risk of shell injection.
user_input = input("Enter a shell command: ")
try:
    args = shlex.split(user_input)
    if args:
        subprocess.run(args, check=True)
except Exception as e:
    print("Command failed:", e)

# BAD CODE: SQL Injection vulnerability example
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

username = input("Enter username: ")
# Use a parameterized query to avoid SQL injection
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))  # nosemgrep: python.lang.security.audit.formatted-sql-query.formatted-sql-query # fixed used parameterized query # nosemgrep: python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query # fixed used parameterized query
print(cursor.fetchall())


secret="ghp_abCDefGHijKLmnOPqrSTuvWXyz1234567890"
