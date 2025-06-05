#!/bin/bash

# Description: Activates all GitHub Actions workflows in a forked repo by appending a comment line.

WORKFLOW_DIR=".github/workflows"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
CHANGED=0

if [ ! -d "$WORKFLOW_DIR" ]; then
  echo "No .github/workflows directory found. Exiting."
  exit 1
fi

echo "Activating workflows in branch: $BRANCH"

for file in "$WORKFLOW_DIR"/*.yml "$WORKFLOW_DIR"/*.yaml; do
  if [ -f "$file" ]; then
    echo "# activate in fork" >> "$file"
    git add "$file"
    CHANGED=1
    echo "Modified: $file"
  fi
done

if [ "$CHANGED" -eq 1 ]; then
  git commit -m "Activate all GitHub Actions workflows after fork"
  git push origin "$BRANCH"
  echo "✅ Workflows activated and pushed to branch $BRANCH."
else
  echo "No workflows found to modify."
fi
