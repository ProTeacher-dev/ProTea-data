#!/usr/bin/env python3
"""
Hospital Appointment System (JSON, CLI) — Solution

Implements the simplified 7-action system to match test.sh and expected.txt.
Uses only Python standard libraries (json, os, datetime).
"""

import json, os
from datetime import datetime, timedelta

DB = "hospital.json"

# ---------- Load and save data to a json file ----------

def load():
	"""Return full state dict for the app."""
	if os.path.exists(DB):
		with open(DB, "r", encoding="utf-8") as f:
			return json.load(f)
	return {
		"next_doctor_id": 1,
		"next_patient_id": 1,
		"next_appointment_id": 1,
		"doctors": [],
		"patients": [],
		"appointments": []
	}

def save(state):
	"""Write the whole state to DB (pretty-printed)."""
	with open(DB, "w", encoding="utf-8") as f:
		json.dump(state, f, indent=2, ensure_ascii=False)

# ---------- Lookups ----------

def get_doctor(state, did):
	"""Return doctor dict by id or None."""
	for d in state["doctors"]:
		if d["id"] == did:
			return d
	return None

def get_patient(state, pid):
	"""Return patient dict by id or None."""
	for p in state["patients"]:
		if p["id"] == pid:
			return p
	return None

# ---------- Add / List ----------

def add_doctor(state, name, specialization, hourly_rate):
	"""Add doctor with unique name; increment next_doctor_id; print result."""
	if any(d["name"] == name for d in state["doctors"]):
		print(f"Doctor {name} already exists")
		return
	try:
		rate = float(hourly_rate)
	except Exception:
		print("Hourly rate must be a positive number")
		return
	if rate <= 0:
		print("Hourly rate must be a positive number")
		return
	doc_id = state["next_doctor_id"]
	state["doctors"].append({
		"id": doc_id,
		"name": name,
		"specialization": specialization,
		"rate": rate
	})
	state["next_doctor_id"] += 1
	print(f"Doctor {name} added with ID {doc_id}")

def add_patient(state, name, phone, email):
	"""Add patient with unique name; increment next_patient_id; print result."""
	if any(p["name"] == name for p in state["patients"]):
		print(f"Patient {name} already exists")
		return
	pid = state["next_patient_id"]
	state["patients"].append({
		"id": pid,
		"name": name,
		"phone": phone,
		"email": email
	})
	state["next_patient_id"] += 1
	print(f"Patient {name} added with ID {pid}")

def list_doctors(state):
	"""Print doctors table or 'No doctors found'."""
	if not state["doctors"]:
		print("No doctors found")
		return
	# Exact headers and spacing per expected.txt
	print("ID    Name           Specialization   Rate")
	print("----  ----           --------------   ----")
	for d in state["doctors"]:
		# Column widths derived from expected:
		# ID: width 6; Name: width 15; Specialization: width 17
		line = f"{str(d['id']):<6}{d['name']:<15}{d['specialization']:<17}${d['rate']:.2f}"
		print(line)

def list_patients(state):
	"""Print patients table or 'No patients found'."""
	if not state["patients"]:
		print("No patients found")
		return
	print("ID    Name         Phone       Email")
	print("----  ----         -----       -----")
	for p in state["patients"]:
		# ID:6, Name:13, Phone:12, Email: rest
		line = f"{str(p['id']):<6}{p['name']:<13}{p['phone']:<12}{p['email']}"
		print(line)

# ---------- Appointments ----------

def schedule_appointment(state, pid, did, date_time_str, duration):
	"""Schedule appointment after validation and conflict checks; print confirmation."""
	p = get_patient(state, pid)
	if not p:
		print(f"Patient with ID {pid} does not exist")
		return
	d = get_doctor(state, did)
	if not d:
		print(f"Doctor with ID {did} does not exist")
		return
	try:
		start_dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
	except Exception:
		print("Invalid date format. Use YYYY-MM-DD HH:MM")
		return
	try:
		dur = int(duration)
	except Exception:
		print("Duration must be a positive integer")
		return
	if dur <= 0:
		print("Duration must be a positive integer")
		return
	# Overlap check for this doctor
	new_start = start_dt
	new_end = start_dt + timedelta(hours=dur)
	for a in state["appointments"]:
		if a["did"] != did:
			continue
		a_start = datetime.strptime(a["start"], "%Y-%m-%d %H:%M")
		a_end = a_start + timedelta(hours=a["duration"])
		# overlap if not (new_end <= a_start or new_start >= a_end)
		if not (new_end <= a_start or new_start >= a_end):
			print(f"Scheduling conflict for doctor {did}")
			return
	aid = state["next_appointment_id"]
	state["appointments"].append({
		"id": aid,
		"pid": pid,
		"did": did,
		"start": date_time_str,
		"duration": dur
	})
	state["next_appointment_id"] += 1
	print(f"Appointment scheduled with ID {aid}")

def list_appointments(state, pid=None, did=None):
	"""Print appointments (optionally filtered by patient or doctor)."""
	appts = state["appointments"]
	if pid is not None:
		appts = [a for a in appts if a["pid"] == pid]
	if did is not None:
		appts = [a for a in appts if a["did"] == did]
	if not appts:
		print("No appointments found")
		return
	print("Appointments for all:")
	print("ID    Patient   Doctor   Date & Time        Duration")
	print("----  -------   ------   -------------      --------")
	for a in appts:
		# ID:6, Patient:10, Doctor:9, Date&Time:19, Duration: rest
		line = (
			f"{str(a['id']):<6}"
			f"{str(a['pid']):<10}"
			f"{str(a['did']):<9}"
			f"{a['start']:<19}"
			f"{a['duration']}"
		)
		print(line)

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