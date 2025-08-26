#!/usr/bin/env python3
"""
Hospital Appointment System (JSON, CLI) — Starter (No Solution)

Complete the TODOs. Keep functions/signatures the same.
Use only Python standard libraries (json, os, datetime).
"""

import json, os
from datetime import datetime, timedelta

DB = "hospital.json"

# ---------- Load and save data to a json file ----------

def load():
	"""Return full state dict for the app."""
	# TODO: If DB exists: open/read JSON and return it
	#       Else: return a fresh state with the exact keys below:
	#       {
	#         "next_doctor_id": 1,
	#         "next_patient_id": 1,
	#         "next_appointment_id": 1,
	#         "doctors": [],
	#         "patients": [],
	#         "appointments": []
	#       }
	raise NotImplementedError("TODO: implement load()")

def save(state):
	"""Write the whole state to DB (pretty-printed)."""
	# TODO: open DB for writing and json.dump(state, f, indent=2, ensure_ascii=False)
	raise NotImplementedError("TODO: implement save()")

# ---------- Lookups ----------

def get_doctor(state, did):
	"""Return doctor dict by id or None."""
	# TODO: iterate state["doctors"] and return match by id
	raise NotImplementedError("TODO: implement get_doctor()")

def get_patient(state, pid):
	"""Return patient dict by id or None."""
	# TODO: iterate state["patients"] and return match by id
	raise NotImplementedError("TODO: implement get_patient()")

# ---------- Add / List ----------

def add_doctor(state, name, specialization, hourly_rate):
	"""Add doctor with unique name; increment next_doctor_id; print result."""
	# TODO:
	# 1) if any(d["name"] == name for d in state["doctors"]): print("Doctor {name} already exists"); return
	# 2) parse hourly_rate -> float; if <= 0: print("Hourly rate must be a positive number"); return
	# 3) create: {"id": state["next_doctor_id"], "name": name, "specialization": specialization, "rate": float_rate}
	# 4) append; increment next_doctor_id
	# 5) print(f"Doctor {name} added with ID {id}")
	raise NotImplementedError("TODO: implement add_doctor()")

def add_patient(state, name, phone, email):
	"""Add patient with unique name; increment next_patient_id; print result."""
	# TODO:
	# 1) if any(p["name"] == name for p in state["patients"]): print("Patient {name} already exists"); return
	# 2) create patient dict: {"id": ..., "name": name, "phone": phone, "email": email}
	# 3) append; increment next_patient_id
	# 4) print(f"Patient {name} added with ID {id}")
	raise NotImplementedError("TODO: implement add_patient()")

def list_doctors(state):
	"""Print doctors table or 'No doctors found'."""
	# TODO: if empty -> print("No doctors found"); else print header and rows:
	# Header:
	# ID    Name           Specialization   Rate
	# ----  ----           --------------   ----
	# Rows (rate formatted as $X.YY)
	raise NotImplementedError("TODO: implement list_doctors()")

def list_patients(state):
	"""Print patients table or 'No patients found'."""
	# TODO: if empty -> print("No patients found"); else print header and rows:
	# Header:
	# ID    Name         Phone       Email
	# ----  ----         -----       -----
	raise NotImplementedError("TODO: implement list_patients()")

# ---------- Appointments ----------

def schedule_appointment(state, pid, did, date_time_str, duration):
	"""Schedule appointment after validation and conflict checks; print confirmation."""
	# TODO:
	# 1) validate patient and doctor exist or print "Patient with ID {pid} does not exist" / "Doctor with ID {did} does not exist"
	# 2) parse date_time_str via datetime.strptime(..., "%Y-%m-%d %H:%M"); on error print "Invalid date format. Use YYYY-MM-DD HH:MM" and return
	# 3) parse duration -> int; duration > 0 else print("Duration must be a positive integer") and return
	# 4) check overlapping for the doctor:
	#    For each appt of same did, compute [start, end) and ensure no overlap
	#    If overlap: print("Scheduling conflict for doctor {did}") and return
	# 5) create appointment dict:
	#    {"id", "pid", "did", "start": date_time_str, "duration": duration}
	# 6) append, increment next_appointment_id, print "Appointment scheduled with ID {id}"
	raise NotImplementedError("TODO: implement schedule_appointment()")

def list_appointments(state, pid=None, did=None):
	"""Print appointments (optionally filtered by patient or doctor)."""
	# TODO:
	# 1) Apply filters if pid/did provided
	# 2) if empty -> print("No appointments found")
	# 3) else header:
	# ID    Patient   Doctor   Date & Time        Duration
	# ----  -------   ------   -------------      --------
	# rows: id, pid, did, start, duration
	raise NotImplementedError("TODO: implement list_appointments()")

# ---------- CLI ----------

def menu():
	# Load state
	try:
		state = load()
	except NotImplementedError as e:
		print(e); print("Implement load() to start using the app."); return

	actions = {
		"1": "Add doctor",
		"2": "Add patient",
		"3": "List doctors",
		"4": "List patients",
		"5": "Schedule appointment",
		"6": "List appointments",
		"7": "Save & exit"
	}
	while True:
		print("\nHospital System — choose an action:")
		for k in sorted(actions): print(f"{k}) {actions[k]}")
		choice = input("> ").strip()
		try:
			if choice == "1":
				add_doctor(state, input("Name: "), input("Specialization: "), input("Hourly rate: "))
			elif choice == "2":
				add_patient(state, input("Name: "), input("Phone: "), input("Email: "))
			elif choice == "3":
				list_doctors(state)
			elif choice == "4":
				list_patients(state)
			elif choice == "5":
				pid = int(input("Patient ID: "))
				did = int(input("Doctor ID: "))
				date_time_str = input("Date & time (YYYY-MM-DD HH:MM): ")
				duration = int(input("Duration (hours): "))
				schedule_appointment(state, pid, did, date_time_str, duration)
			elif choice == "6":
				f = input("Filter by (p)atient id / (d)octor id / (n)one? ").lower()
				if f == "p":
					list_appointments(state, pid=int(input("Patient ID: ")))
				elif f == "d":
					list_appointments(state, did=int(input("Doctor ID: ")))
				else:
					list_appointments(state)
			elif choice == "7":
				save(state); print("Saved. Bye!"); break
			else:
				print("Invalid choice.")
		except NotImplementedError as e:
			print(e)
		except Exception as e:
			print("Error:", e)

if __name__ == "__main__":
	menu()
