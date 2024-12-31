#!/bin/bash

# Extract numbers and commas from each line of the input file
sed -e 's/toggle/0/' -e 's/turn on/1/' -e 's/turn off/2/' "$1"| grep -o '[0-9,]*' |python3 dag6.py

