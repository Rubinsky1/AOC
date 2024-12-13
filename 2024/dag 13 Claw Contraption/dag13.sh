#!/bin/bash

make


sed 's/[^0-9]/ /g' dag13.txt | sed -E 's/ +/ /g' | ./main

