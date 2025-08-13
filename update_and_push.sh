#!/bin/bash

# Run the index update script
python3 UpdateIndex.py

# Stage changes
git add README.md

# Commit with a common message
git commit -m "chore: update index for new solutions"

# Push to repo
git push origin main
