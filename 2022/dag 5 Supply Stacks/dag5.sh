#!/bin/bash

sed 's/\[/|[/g; s/\]/]|/g' "$1" | tr -d '[]' | sed 's/    /|  |/g' | sed 's/| |/|/g' | sed 's/|  |/| |/g' | sed 's/||/|/g' | sed 's/\bmove\b//g; s/\bfrom\b//g; s/\bto\b//g' | sed 's/[0-9]\{1,\}   /   /g' | sed 's/   [0-9]\{1,\}/   /g' | python3 dag5.py