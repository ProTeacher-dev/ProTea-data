#!/usr/bin/env bash
set -euo pipefail

# Clean slate
rm -f gradebook.json
: > out.txt

run() {
  python3 "$1" <<'EOF' | tee -a out.txt
1
Alice
1
Bob
3
1
CS101
95
3
2
CS101
78
3
1
MATH200
88
4
n
5
1
6
CS101
7
8
EOF
}

# Run starter/solution; typically you'll check the solution behavior.
run solution.py

# Compare against a saved golden output if you keep one:
# diff -u out.txt tests/golden.out || { echo "Mismatch!"; exit 1; }

echo "Scenario completed. Review out.txt"
