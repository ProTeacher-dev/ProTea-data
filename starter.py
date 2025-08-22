#!/usr/bin/env python3
"""
Student Gradebook (JSON, CLI) — Starter (No Solution)

Complete the TODOs. Keep functions/signatures the same.
Use only Python standard libraries (json, os, statistics).
"""

import json, os, statistics

DB = "gradebook.json"

# ---------- Persistence ----------

def load():
    """Return state dict: {'next_id': int, 'students': [], 'grades': []}."""
    # TODO: if DB exists, load and return; else fresh state
    raise NotImplementedError("TODO: implement load()")

def save(state):
    """Write the whole state to DB (pretty-printed)."""
    # TODO: json.dump with indent and ensure_ascii=False
    raise NotImplementedError("TODO: implement save()")

# ---------- Lookups ----------

def get_student(state, sid):
    """Return student dict by id or None."""
    # TODO: linear search on state['students']
    raise NotImplementedError("TODO: implement get_student()")

def student_by_name(state, name):
    """Return student dict by exact (case-insensitive) name or None."""
    # TODO: exact match on lowercased names
    raise NotImplementedError("TODO: implement student_by_name()")

# ---------- Operations ----------

def add_student(state, name):
    """Add student with unique name; increment next_id; print result."""
    # TODO: uniqueness check; append; increment next_id; print confirmation
    raise NotImplementedError("TODO: implement add_student()")

def list_students(state):
    """Print ID and name for all students."""
    # TODO: handle empty; then print a simple table
    raise NotImplementedError("TODO: implement list_students()")

def add_grade(state, sid, course, score):
    """Add grade record after validations; print confirmation."""
    # TODO: validate sid exists; score as float in [0,100]; append grade
    raise NotImplementedError("TODO: implement add_grade()")

def list_grades(state, sid=None, course=None):
    """Print grades (optionally filtered by student or course)."""
    # TODO: filter; handle empty; print table
    raise NotImplementedError("TODO: implement list_grades()")

def student_report(state, sid):
    """Per-student: per-course stats + overall avg."""
    # TODO: group student's grades by course; compute n/avg/min/max; overall avg
    raise NotImplementedError("TODO: implement student_report()")

def course_report(state, course):
    """Per-course: n, avg, median, min, max; top/bottom 3."""
    # TODO: filter by course; compute stats; print top/bottom samples
    raise NotImplementedError("TODO: implement course_report()")

def overall_stats(state):
    """Totals and aggregate stats over all grades."""
    # TODO: handle empty; compute mean/median; print counts
    raise NotImplementedError("TODO: implement overall_stats()")

# ---------- CLI ----------

def menu():
    # Load state (students implement load())
    try:
        state = load()
    except NotImplementedError as e:
        print(e); print("Implement load() to start using the app."); return

    actions = {
        "1": "Add student",
        "2": "List students",
        "3": "Add grade",
        "4": "List grades",
        "5": "Student report",
        "6": "Course report",
        "7": "Overall stats",
        "8": "Save & exit"
    }
    while True:
        print("\nGradebook — choose an action:")
        for k in sorted(actions): print(f"{k}) {actions[k]}")
        choice = input("> ").strip()
        try:
            if choice == "1":
                add_student(state, input("Name: "))
            elif choice == "2":
                list_students(state)
            elif choice == "3":
                sid = int(input("Student ID: "))
                course = input("Course (e.g., CS101): ")
                score = input("Score (0–100): ")
                add_grade(state, sid, course, score)
            elif choice == "4":
                f = input("Filter by (s)tudent id / (c)ourse / (n)one? ").lower()
                if f == "s":
                    list_grades(state, sid=int(input("Student ID: ")))
                elif f == "c":
                    list_grades(state, course=input("Course: "))
                else:
                    list_grades(state)
            elif choice == "5":
                student_report(state, int(input("Student ID: ")))
            elif choice == "6":
                course_report(state, input("Course: "))
            elif choice == "7":
                overall_stats(state)
            elif choice == "8":
                save(state); print("Saved. Bye!"); break
            else:
                print("Invalid choice.")
        except NotImplementedError as e:
            print(e)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()
