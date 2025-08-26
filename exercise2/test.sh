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
rm -f hospital.json
: > out.txt

# Create expected output file
cat > expected.txt <<'EOF'

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> Name: Specialization: Hourly rate: Doctor Dr. Smith added with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> Name: Phone: Email: Patient John Doe added with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> ID    Name           Specialization   Rate
----  ----           --------------   ----
1     Dr. Smith      Cardiology       $150.00

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> ID    Name         Phone       Email
----  ----         -----       -----
1     John Doe     555-1234    john@example.com

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> Patient ID: Doctor ID: Date & time (YYYY-MM-DD HH:MM): Duration (hours): Appointment scheduled with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> Filter by (p)atient id / (d)octor id / (n)one? Appointments for all:
ID    Patient   Doctor   Date & Time        Duration
----  -------   ------   -------------      --------
1     1         1        2024-01-15 10:00   2

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit
> Saved. Bye!
EOF

# Capture stderr from Python run so we can log it if it fails
PY_ERR_FILE=$(mktemp)

# Temporarily disable -e to catch failure and log it; keep printed output identical
set +e
python3 solution.py > >(tee -a out.txt) 2> "$PY_ERR_FILE" <<'EOF'
1
Dr. Smith
Cardiology
150
2
John Doe
555-1234
john@example.com
3
4
5
1
1
2024-01-15 10:00
2
6
n
7
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

echo "=== TESTING SOLUTION ==="
if diff -u expected.txt out.txt > diff_output.txt 2>&1; then
  echo "✅ SUCCESS: Output matches expected exactly!"
  STATUS="pass"
  EMESSAGE="ok"
  DONE=1
  add_result "$STATUS" "$EMESSAGE"
else
  echo "❌ FAILURE: Output does not match expected"
  echo
  cat diff_output.txt
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
echo "- hospital.json: Final database state"
echo "- $LOG_FILE: Test results log"
