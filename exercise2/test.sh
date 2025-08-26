#!/usr/bin/env bash
set -euo pipefail

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
7) Generate bill
8) List bills
9) Save & exit
> Name: Specialization: Hourly rate: Doctor Dr. Smith added with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit
> Name: Phone: Email: Patient John Doe added with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit
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
7) Generate bill
8) List bills
9) Save & exit
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
7) Generate bill
8) List bills
9) Save & exit
> Patient ID: Doctor ID: Date & time (YYYY-MM-DD HH:MM): Duration (hours): Appointment scheduled with ID 1

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit
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
7) Generate bill
8) List bills
9) Save & exit
> Appointment ID: Bill generated with ID 1 for $300.00

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit
> Filter by (p)atient id / (n)one? All bills:
ID    Patient   Appointment   Amount
----  -------   -----------   ------
1     1         1             $300.00

Hospital System — choose an action:
1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit
> Saved. Bye!
EOF

run() {
  python3 solution.py <<'EOF' | tee -a out.txt
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
1
8
n
9
EOF
}

# Run solution (student should implement solution.py using starter.py signatures)
run

echo "=== TESTING SOLUTION ==="
if diff -u expected.txt out.txt > diff_output.txt 2>&1; then
  echo "✅ SUCCESS: Output matches expected exactly!"
else
  echo "❌ FAILURE: Output does not match expected"
  echo
  cat diff_output.txt
fi

echo
echo "=== FILES CREATED ==="
echo "- out.txt: Actual program output"
echo "- expected.txt: Expected correct output"
echo "- diff_output.txt: Detailed differences (if any)"
echo "- hospital.json: Final database state"
```

```

