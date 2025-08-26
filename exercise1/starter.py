#!/usr/bin/env python3
"""
Student Gradebook (JSON, CLI) — Starter (No Solution)

Complete the TODOs. Keep functions/signatures the same.
Use only Python standard libraries (json, os, statistics).
"""

import json, os, statistics

DB = "gradebook.json"

# ---------- Load and save data to a json file ----------

def load():
    """Return state dict: {'next_id': int, 'students': [], 'grades': []}."""
    # TODO: Check if gradebook.json exists using os.path.exists(DB)
    #       If exists: open file, json.load() it, and return the loaded dict
    #       If not exists: return fresh dict with {'next_id': 1, 'students': [], 'grades': []}
    raise NotImplementedError("TODO: implement load()")

def save(state):
    """Write the whole state to DB (pretty-printed)."""
    # TODO: Open gradebook.json in write mode ('w')
    #       Use json.dump(state, file, indent=2, ensure_ascii=False)
    #       This creates a nicely formatted JSON file
    raise NotImplementedError("TODO: implement save()")

# ---------- Lookup student information ----------

def get_student(state, sid):
    """Return student dict by id or None."""
    # TODO: Loop through state['students'] list
    #       For each student dict, check if student['id'] == sid
    #       If found, return that student dict; if not found, return None
    raise NotImplementedError("TODO: implement get_student()")

# ---------- Operations ----------

def add_student(state, name):
    """Add student with unique name; increment next_id; print result."""
    # TODO: 1. Check if name already exists: loop through state['students'], 
    #          check if any student['name'] == name
    #       2. If duplicate: print "Student {name} already exists" and return
    #       3. If unique: create new student dict {'id': state['next_id'], 'name': name}
    #       4. Append to state['students'] list
    #       5. Increment state['next_id'] by 1
    #       6. Print "Student {name} added with ID {id}" (use the old next_id value)
    raise NotImplementedError("TODO: implement add_student()")

def list_students(state):
    """Print ID and name for all students."""
    # TODO: 1. Check if state['students'] is empty
    #       2. If empty: print "No students found"
    #       3. If not empty: print table header "ID    Name" then "----  ----"
    #       4. Loop through students and print each as "ID    Name"
    raise NotImplementedError("TODO: implement list_students()")

def add_grade(state, sid, course, score):
    """Add grade record after validations; print confirmation."""
    # TODO: 1. Validate student exists: use get_student(state, sid)
    #       2. If student not found: print "Student with ID {sid} does not exist" and return
    #       3. Convert score to float and validate it's between 0-100
    #       4. If invalid score: print error and return
    #       5. Create grade dict {'sid': sid, 'course': course, 'score': float_score}
    #       6. Append to state['grades'] list
    #       7. Print "Grade {score} added for {course} in {sid}"
    raise NotImplementedError("TODO: implement add_grade()")

def list_grades(state, sid=None, course=None):
    """Print grades (optionally filtered by student or course)."""
    # TODO: 1. Filter grades: if sid given, filter by sid; if course given, filter by course
    #       2. Check if filtered grades list is empty
    #       3. If empty: print "No grades found"
    #       4. If not empty: print "Grades for all students in all courses:" (or appropriate filter text)
    #       5. Print table header "ID    Course     Score" then "--------------------"
    #       6. Loop through grades and print each as "{sid}     {course}      {score}"
    raise NotImplementedError("TODO: implement list_grades()")

def student_report(state, sid):
    """Per-student: per-course stats + overall avg."""
    # TODO: 1. Get student's grades: filter state['grades'] where grade['sid'] == sid
    #       2. If no grades: print "No grades found for student with ID {sid}" and return
    #       3. Print "Student {sid} grades:"
    #       4. Print table header "Course     Score" then "--------------------"
    #       5. Group grades by course and print each course's grades
    #       6. Compute and print overall statistics
    raise NotImplementedError("TODO: implement student_report()")

def course_report(state, course):
    """Per-course: n, avg, median, min, max; top/bottom 3."""
    # TODO: 1. Filter grades by course: get all grades where grade['course'] == course
    #       2. If no grades: print "No grades found for course {course}" and return
    #       3. Print "Course {course} grades:"
    #       4. Print table header "Student   Score" then "--------------------"
    #       5. Print each grade as "{course}     {score}" (note: course name, not student name)
    #       6. Print "Overall avg {average}" (use statistics.mean())
    #       7. Print "Top 3     {average}" and "Bottom 3   {average}"
    raise NotImplementedError("TODO: implement course_report()")

def overall_stats(state):
    """Totals and aggregate stats over all grades."""
    # TODO: 1. Check if state['grades'] is empty
    #       2. If empty: print "No grades found" and return
    #       3. Compute total count: len(state['grades'])
    #       4. Extract all scores: [grade['score'] for grade in state['grades']]
    #       5. Use statistics module: mean(), median(), min(), max()
    #       6. Print: "Total grades: {count}"
    #       7. Print: "Average score: {mean}"
    #       8. Print: "Median score: {median}"
    #       9. Print: "Minimum score: {min}"
    #       10. Print: "Maximum score: {max}"
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
