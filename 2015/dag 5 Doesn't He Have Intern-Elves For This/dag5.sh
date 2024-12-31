#!/bin/bash


# Lees het bestand en filter woorden met precies 3 klinkers
grep -oE '\b\w+\b' "$1" | awk '{
    vowel_count = gsub(/[aeiouAEIOU]/, "&");
    if (vowel_count >= 3) print $0;
}' | grep -E '(.)\1' | grep -vE 'ab|cd|pq|xy'|wc -l

grep -oE '\b\w+\b' "$1"|grep -P '(\w{2}).*\1' | grep -P '(.).\1' | wc -l


