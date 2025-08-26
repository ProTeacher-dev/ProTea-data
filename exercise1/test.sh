#!/usr/bin/env bash
set -euo pipefail

# JSON log of results
LOG_FILE="test_results.json"

# Initialize log file if missing
if [ ! -f "$LOG_FILE" ]; then
  echo "[]" > "$LOG_FILE"
fi

# Append a result entry to the JSON array without jq
add_result() {
  local result="$1"
  local emessage="$2"
  local ts
  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  # collapse newlines in emessage to spaces and trim
  emessage=$(printf "%s" "$emessage" | tr '\n' ' ' | tr -s ' ')
  local entry
  entry=$(cat <<EOF
{"time":"$ts","result":"$result","emessage":"$emessage"}
EOF
)
  if grep -q '^[[:space:]]*\[[[:space:]]*\][[:space:]]*$' "$LOG_FILE"; then
    printf '[\n%s\n]\n' "$entry" > "$LOG_FILE"
  else
    local tmp
    tmp=$(mktemp)
    sed '$d' "$LOG_FILE" > "$tmp"
    echo "," >> "$tmp"
    echo "$entry" >> "$tmp"
    echo "]" >> "$tmp"
    mv "$tmp" "$LOG_FILE"
  fi
}

# Default status for safety if script exits early
DONE=0
STATUS="fail"
EMESSAGE="running errors"

# Ensure we log even if the script exits early
finalize() {
  if [ "$DONE" -eq 0 ]; then
    add_result "$STATUS" "$EMESSAGE"
  fi
}
trap finalize EXIT

# Clean slate
rm -f gradebook.json
: > out.txt

# Create expected output file
cat > expected.txt <<'EOF'

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Name: Student Alice added with ID 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Name: Student Bob added with ID 2

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 95 added for CS101 in 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 78 added for CS101 in 2

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 88 added for MATH200 in 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Filter by (s)tudent id / (c)ourse / (n)one? Grades for all students in all courses:
ID    Course     Score
--------------------
1     CS101      95.0  
2     CS101      78.0  
1     MATH200    88.0  

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Student 1 grades:
Course     Score
--------------------
CS101      95.0
MATH200      88.0

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Course: Course CS101 grades:
Student   Score
--------------------
CS101     95.0  
CS101     78.0  
Overall avg 86.5  
Top 3     86.5  
Bottom 3  86.5  

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Total grades: 3
Average score: 87.0
Median score: 88.0
Minimum score: 78.0
Maximum score: 95.0

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Saved. Bye!
EOF

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

# Capture stderr from Python run so we can log it if it fails
PY_ERR_FILE=$(mktemp)

# Temporarily disable -e to catch failure and log it; keep printed output identical
set +e
# Run target: stdout already piped to tee by run(); we redirect only stderr here
python3 solution.py > >(tee -a out.txt) 2> "$PY_ERR_FILE" <<'EOF'
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
RUN_RC=$?
set -e

if [ $RUN_RC -ne 0 ]; then
  STATUS="fail"
  if [ -s "$PY_ERR_FILE" ]; then
    EMESSAGE="$(cat "$PY_ERR_FILE")"
  else
    EMESSAGE="running errors"
  fi
  DONE=1
  add_result "$STATUS" "$EMESSAGE"
  echo "Execution failed running solution.py:"
  echo "$EMESSAGE"
  exit 1
fi

# Compare against expected output with detailed feedback (unchanged + keeps line-by-line diff)
echo "=== TESTING SOLUTION ==="
echo "Comparing actual output with expected output..."
echo

if diff -u expected.txt out.txt > diff_output.txt 2>&1; then
  echo "✅ SUCCESS: Output matches expected exactly!"
  echo "All functionality appears to be working correctly."
  STATUS="pass"
  EMESSAGE="ok"
  DONE=1
  add_result "$STATUS" "$EMESSAGE"
else
  echo "❌ FAILURE: Output does not match expected"
  echo
  echo "=== DIFFERENCES FOUND ==="
  cat diff_output.txt
  echo
  echo "=== ANALYSIS ==="
  echo "Line-by-line comparison shows the following issues:"
  echo
  
  # Count lines in each file
  actual_lines=$(wc -l < out.txt)
  expected_lines=$(wc -l < expected.txt)
  
  echo "Expected output has $expected_lines lines"
  echo "Actual output has $actual_lines lines"
  echo
  
  echo "=== RECOMMENDATIONS ==="
  echo "1. Fix the load() function to return proper structure"
  echo "2. Implement all TODO functions marked with NotImplementedError"
  echo "3. Check that all print statements match the expected format"
  echo "4. Verify error handling for edge cases"
  echo
  echo "Review the diff above to see exactly what differs from expected output."
  STATUS="fail"
  EMESSAGE="output does not match"
  DONE=1
  add_result "$STATUS" "$EMESSAGE"
fi

echo
echo "=== FILES CREATED ==="
echo "- out.txt: Actual program output"
echo "- expected.txt: Expected correct output"
echo "- diff_output.txt: Detailed differences (if any)"
echo "- gradebook.json: Final database state"
echo "- $LOG_FILE: Test results log"

# Clean up diff file if test passed
if [ -f diff_output.txt ] && [ ! -s diff_output.txt ]; then
  rm diff_output.txt
fi
