# Exercise 2: Hospital Appointment System (Simplified)

## Problem Description

Implement a command-line hospital appointment system that manages doctors, patients, and appointments. The system uses JSON for data persistence and offers a focused set of operations.

### Core Functionality (7 actions)

1) Add doctor
2) Add patient
3) List doctors
4) List patients
5) Schedule appointment
6) List appointments
7) Save & exit

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

## Expected Data Shape

Fresh state must be:
```
{
  "next_doctor_id": 1,
  "next_patient_id": 1,
  "next_appointment_id": 1,
  "doctors": [],
  "patients": [],
  "appointments": []
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

## Quick Test

```bash
./test.sh
```

```

