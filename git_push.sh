#!/bin/bash

# Controleer of een commit message is opgegeven
if [ -z "$1" ]; then
  echo "Gebruik: $0 <commit_message>"
  exit 1
fi

# Voeg alle wijzigingen toe
git add .

# Maak een commit met de opgegeven boodschap
git commit -m "$1"

# Push de wijzigingen naar de remote repository
git push