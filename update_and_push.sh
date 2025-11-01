#!/bin/bash

# Pull latest changes
echo "Pulling latest changes..."
git pull origin main

# Move new folders into solutions/
echo "Moving new folders to solutions..."
for folder in */; do
    if [[ "$folder" != "solutions/" && "$folder" != ".git/" ]]; then
        if [ -d "$folder" ]; then
            echo "Moving $folder to solutions/"
            rm -rf "solutions/$folder"
            mv "$folder" solutions/
        fi
    fi
done

# Run UpdateIndex.py
echo "Running UpdateIndex.py..."
python3 UpdateIndex.py

# Stage all changes (including deletions + new folders)
echo "Staging all changes..."
git add -A

# Commit with a standard message
echo "Committing changes..."
git commit -m "chore: update index for new solutions"

# Push to main branch
echo "Pushing to GitHub..."
git push origin main

echo "All done!"
