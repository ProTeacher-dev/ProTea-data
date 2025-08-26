# Exercise 2: Hospital Appointment & Billing System (Simplified)

## Problem Description

Implement a command-line hospital appointment and billing system that manages doctors, patients, appointments, and billing records. The system uses JSON for data persistence and offers a focused set of operations.

### Core Functionality (9 actions)

1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Generate bill
8) List bills
9) Save & exit

### Details

- **Doctors**
  - Add doctor: unique name, specialization, hourly rate (positive float)
  - List doctors: show ID, name, specialization, rate

- **Patients**
  - Add patient: unique name, phone, email
  - List patients: show ID, name, phone, email

- **Appointments**
  - Schedule: patient, doctor, date-time (YYYY-MM-DD HH:MM), duration hours (positive int)
  - Validation: existing patient/doctor, datetime format, overlapping appointments for the same doctor are not allowed
  - List appointments: optionally filter by patient or doctor

- **Billing**
  - Generate bill: for an appointment ID (amount = doctor_hourly_rate × duration)
  - List bills: optionally filter by patient

- **Data**
  - Load from `hospital.json` if exists; otherwise start empty
  - Save back to `hospital.json` when exiting

### Technical Constraints

- Use only Python standard libraries: `json`, `os`, `datetime`
- Maintain function signatures
- Follow exact output formatting
- Validate inputs and print meaningful errors

## Project Structure

```
exercise2/
├── starter.py
├── solution.py        # implement here (copy signatures from starter.py)
├── test.sh
├── expected.txt       # created by test.sh
├── out.txt            # created by test.sh
└── hospital.json      # created when saving
```

## Implementation Order

1. `load()` and `save()`
2. `get_doctor()` and `get_patient()`
3. `add_doctor()`, `add_patient()`, `list_doctors()`, `list_patients()`
4. `schedule_appointment()` and `list_appointments()`
5. `generate_bill()` and `list_bills()`

## Expected Data Shape

Fresh state must be:
```
{
  "next_doctor_id": 1,
  "next_patient_id": 1,
  "next_appointment_id": 1,
  "next_bill_id": 1,
  "doctors": [],
  "patients": [],
  "appointments": [],
  "bills": []
}
```

## Formatting Rules

- Menu title: "Hospital System — choose an action:"
- Money: $X.YY (two decimals)
- DateTime input: YYYY-MM-DD HH:MM
- Exact messages:
  - Add doctor: "Doctor {name} added with ID {id}"
  - Add patient: "Patient {name} added with ID {id}"
  - Appointment: "Appointment scheduled with ID {id}"
  - Bill: "Bill generated with ID {id} for ${amount}"

## Quick Test

```bash
./test.sh
```

```

