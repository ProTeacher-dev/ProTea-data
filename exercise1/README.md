# Exercise 1: Student Gradebook System

## Problem Description

You are tasked with implementing a command-line student gradebook system that manages students and their academic grades. The system uses JSON for data persistence and provides a comprehensive set of operations for managing student records and grade data.

### Core Requirements

The gradebook system must support the following functionality:

1. **Students**
   - Add a student (names must be unique)
   - List all students with their IDs

2. **Grades**
   - Add a grade for a student in a course (score must be 0–100)
   - List grades (optionally filter by student or course)

3. **Reports**
   - Student report: show that student’s grades
   - Course report: show stats (average, median, min, max)

4. **Data**
   - Load from `gradebook.json` if it exists; otherwise start empty
   - Save back to `gradebook.json` when exiting

### Technical Constraints

- **Use only Python standard libraries**: `json`, `os`, `statistics`
- **Maintain function signatures**: Do not change function names or parameters
- **Follow exact output formatting**: All print statements must match the expected format exactly
- **Implement proper error handling**: Validate inputs and provide meaningful error messages

## Project Structure

```
exercise1/
├── starter.py          # Starting template with TODOs (do not modify)
├── solution.py         # Your implementation (modify this file)
├── test.sh            # Comprehensive test script with detailed feedback
├── expected.txt       # Expected output format
├── out.txt           # Your program's actual output
└── gradebook.json    # Database file (created when you save)
```


## Implementation Guide

### Step 1: Start with the Starter Template

The `starter.py` file contains:
- Complete function signatures with docstrings
- Detailed TODO comments explaining what each function should do
- A working CLI menu system
- All necessary imports

**Do not modify `starter.py`** - use it as a reference and copy the structure to `solution.py`.

### Step 2: Implement Core Functions

Follow this implementation order for best results:

1. **`load()`** - Critical first function that affects everything else
2. **`save()`** - Required for data persistence
3. **`get_student()`** - Helper function used by other operations
4. **`add_student()`** - Basic student management
5. **`list_students()`** - Display functionality
6. **`add_grade()`** - Grade management with validation
7. **`list_grades()`** - Grade display with filtering
8. **`student_report()`** - Individual student analytics
9. **`course_report()`** - Course-level statistics
10. **`overall_stats()`** - System-wide analytics

### Step 3: Testing Your Implementation

#### Quick Test
```bash
./test.sh
```

This will:
- Run your program with predefined test inputs
- Compare output against expected results
- Provide detailed feedback on any differences
- Show exactly what needs to be fixed


## Expected Output Format

Your program must produce output that exactly matches the format in `expected.txt`. Key formatting requirements:

- **Menu display**: "Gradebook — choose an action:" (no leading empty line)
- **Table headers**: Proper spacing and alignment
- **Confirmation messages**: Exact wording for all operations
- **Error messages**: Specific error text for validation failures
- **Statistics**: Proper decimal formatting for averages

## Common Implementation Issues

### 1. Data Structure Problems
**Issue**: `load()` function returns incorrect structure
**Solution**: Ensure it returns `{"next_id": 1, "students": [], "grades": []}` for new files

### 2. Output Format Mismatches
**Issue**: Print statements don't match expected format
**Solution**: Copy exact text from `expected.txt` for all messages

### 3. Validation Errors
**Issue**: Missing input validation
**Solution**: Check student existence, score ranges, and duplicate names

### 4. Statistics Calculation
**Issue**: Incorrect use of statistics module
**Solution**: Use `statistics.mean()`, `statistics.median()`, `min()`, `max()`


### Understanding Test Output

When tests fail, you'll see:
- **Line-by-line differences** between expected and actual output
- **Specific error patterns** identified automatically
- **Actionable recommendations** for fixing issues
- **File counts** showing if output length matches

## Success Criteria

Your implementation is complete when:
- ✅ All tests pass (`./test.sh` shows "SUCCESS")
- ✅ No NotImplementedError exceptions occur
- ✅ Output exactly matches `expected.txt`
- ✅ All functionality works as specified
- ✅ Data persists correctly in `gradebook.json`

## Tips for Success

1. **Read the TODOs carefully** - Each contains specific implementation guidance
2. **Test incrementally** - Don't implement everything at once
3. **Use the debug helper** - It will save you time identifying issues
4. **Check formatting exactly** - Even small spacing differences matter
5. **Validate your data structure** - The `load()` function is critical

## Example Test Session

```bash

# Implement functions in solution.py

# Test your progress
./test.sh

# Review any differences and fix them

# Repeat until all tests pass
```

The testing tools provide comprehensive feedback to help you identify and fix issues efficiently. Use them throughout your development process!

