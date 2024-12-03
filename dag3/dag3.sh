grep -o -E '(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don'\''t\(\))' dag3.txt \
| awk '
BEGIN { skip = 0 }
{
    if ($0 ~ /don'\''t\(\)/) {
        skip = 1
    } else if ($0 ~ /do\(\)/) {
        skip = 0
        print
    } else if (skip == 0) {
        print
    }
}'\
| sed -E 's/mul\(([0-9]+),([0-9]+)\)/\1 \2/' \
| python3 dag3.py
