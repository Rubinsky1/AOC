#!/bin/bash

for dir in */; do
  if [ -d "$dir" ]; then
    cd "$dir"
    for py_file in *.py; do
      if [ -f "$py_file" ]; then
        base_name="${py_file%.py}"
        txt_file="${base_name}.txt"
        if [ -f "$txt_file" ]; then
          echo "Running: python3 $py_file $txt_file in $dir"
          python3 "$py_file" "$txt_file"
        fi
      fi
    done
    cd ..
  fi
done