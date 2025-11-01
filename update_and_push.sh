#!/bin/bash

echo "Checking for internet connection..."
until ping -c1 google.com &>/dev/null; do
  echo "No internet connection. Retrying in 30 seconds..."
  sleep 30
done
echo "Internet connected."

echo "Moving new folders to solutions..."
for folder in */; do
  if [[ "$folder" != "solutions/" && "$folder" != "scripts/" ]]; then
    if [ -d "$folder" ] && [ -f "$folder/README.md" ]; then
      mv "$folder" solutions/
      echo "Moved: $folder"
    fi
  fi
done

echo "Pulling latest changes..."
git pull origin main

echo "Running UpdateIndex.py..."
python3 UpdateIndex.py

echo "Staging changes..."
git add README.md

echo "Committing..."
git commit -m "chore: update index for new solutions"

echo "Pushing changes..."
git push origin main

echo "All tasks completed."
