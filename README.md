# Student Gradebook (JSON, CLI)

This assignment asks you to build a **command-line gradebook system** in Python.  
You will complete the provided starter code (`gradebook_starter.py`) to implement  
the missing functionality. The program should maintain a list of students and their grades,  
persisted in a JSON file (`gradebook.json`).

---

## 🎯 Learning Objectives
- Practice designing a menu-driven CLI program in Python.
- Work with **lists**, **dicts**, and **functions**.
- Use **JSON** for persistence (load on start, save on exit).
- Implement **reports and statistics** with the `statistics` module.

---

## 📂 Data Model

Your program should read/write a file called `gradebook.json` with the following structure:

```json
{
  "next_id": 1,
  "students": [
    {"id": 1, "name": "Alice"}
  ],
  "grades": [
    {"sid": 1, "course": "CS101", "score": 92.0}
  ]
}
```

- `next_id`: the next student ID to assign.
- `students`: list of students (id + name).
- `grades`: list of grade entries (student id, course, numeric score).

---

## 🛠️ Features to Implement

The menu should offer these options:

1. **Add student**  
   - Assigns an auto-increment ID.  
   - Prevent duplicate names.  

2. **List students**  
   - Display all students with IDs.  

3. **Add grade**  
   - Input: student ID, course, score (0–100).  
   - Validate ID and score.  

4. **List grades**  
   - Show all grades.  
   - Filters: by student ID or by course.  

5. **Student report**  
   - Per-course stats (n, avg, min, max).  
   - Overall average.  

6. **Course report**  
   - Stats across all students (n, avg, median, min, max).  
   - Show top 3 and bottom 3 performers.  

7. **Overall stats**  
   - Totals: number of students, number of grades.  
   - Global avg and median.  

8. **Save & Exit**  
   - Write `gradebook.json` before exiting.

---

## ✅ Requirements
- Use only the **Python standard library** (`json`, `os`, `statistics`).  
- Complete the TODOs in the starter code.  
- Handle edge cases (invalid IDs, duplicate students, empty lists).  
- Keep program size in the **100–200 lines** range.  

---

## 📖 Usage

Run the program:

```bash
python gradebook_starter.py
```

Example interaction:

```
Gradebook — choose an action:
1) Add student
2) List students
...
> 1
Name: Alice
Added student #1: Alice

> 3
Student ID: 1
Course (e.g., CS101): CS101
Score (0–100): 95
Recorded: Alice — CS101 = 95.00

> 7
Overall
  students=1 grades=1 avg=95.00 median=95.00

> 8
Saved. Bye!
```

---

## 🧪 Testing

A sample scenario is provided in `tests/scenario.sh`. Run it to simulate inputs:

```bash
bash tests/scenario.sh
```

This will:
- Add students
- Record grades
- Produce reports
- Save to `gradebook.json`

You can capture output and compare against a golden file to check correctness.

---

## 💡 Tips
- Use `json.dump(state, f, indent=2, ensure_ascii=False)` for saving.  
- Use the `statistics` module for averages and medians.  
- Slice `sorted()` lists to get top/bottom 3.  
- Always validate input before updating state.

---

## 📜 Attribution
This assignment is adapted from typical “management system” CLI exercises.  
It is designed for **100–200 lines of code**, making it a good medium-scale practice project.
