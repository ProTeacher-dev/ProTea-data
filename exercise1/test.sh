#!/usr/bin/env bash
set -euo pipefail

# Clean slate
rm -f gradebook.json
: > out.txt

# Create expected output file
cat > expected.txt <<'EOF'

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Name: Student Alice added with ID 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Name: Student Bob added with ID 2

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 95 added for CS101 in 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 78 added for CS101 in 2

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Course (e.g., CS101): Score (0–100): Grade 88 added for MATH200 in 1

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Filter by (s)tudent id / (c)ourse / (n)one? Grades for all students in all courses:
ID    Course     Score
--------------------
1     CS101      95.0  
2     CS101      78.0  
1     MATH200    88.0  

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Student ID: Student 1 grades:
Course     Score
--------------------
CS101      95.0
MATH200      88.0

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Course: Course CS101 grades:
Student   Score
--------------------
CS101     95.0  
CS101     78.0  
Overall avg 86.5  
Top 3     86.5  
Bottom 3  86.5  

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Total grades: 3
Average score: 87.0
Median score: 88.0
Minimum score: 78.0
Maximum score: 95.0

Gradebook — choose an action:
1) Add student
2) List students
3) Add grade
4) List grades
5) Student report
6) Course report
7) Overall stats
8) Save & exit
> Saved. Bye!
EOF

run() {
  python3 "$1" <<'EOF' | tee -a out.txt
1
Alice
1
Bob
3
1
CS101
95
3
2
CS101
78
3
1
MATH200
88
4
n
5
1
6
CS101
7
8
EOF
}

# Run starter/solution; typically you'll check the solution behavior.
run solution.py

# Compare against expected output with detailed feedback
echo "=== TESTING SOLUTION ==="
echo "Comparing actual output with expected output..."
echo

if diff -u expected.txt out.txt > diff_output.txt 2>&1; then
    echo "✅ SUCCESS: Output matches expected exactly!"
    echo "All functionality appears to be working correctly."
else
    echo "❌ FAILURE: Output does not match expected"
    echo
    echo "=== DIFFERENCES FOUND ==="
    cat diff_output.txt
    echo
    echo "=== ANALYSIS ==="
    echo "Line-by-line comparison shows the following issues:"
    echo
    
    # Count lines in each file
    actual_lines=$(wc -l < out.txt)
    expected_lines=$(wc -l < expected.txt)
    
    echo "Expected output has $expected_lines lines"
    echo "Actual output has $actual_lines lines"
    echo
    
    # Show specific error patterns
    if grep -q "Error: 'students'" out.txt; then
        echo "🔍 ISSUE: 'students' key error detected"
        echo "   This suggests the load() function is not returning the correct structure"
        echo "   Expected: {'next_id': 1, 'students': [], 'grades': []}"
        echo "   Current: Likely returning {} or missing 'students' key"
        echo
    fi
    
    if grep -q "Error: 'grades'" out.txt; then
        echo "🔍 ISSUE: 'grades' key error detected"
        echo "   This suggests the load() function is not returning the correct structure"
        echo "   Expected: {'next_id': 1, 'students': [], 'grades': []}"
        echo "   Current: Likely returning {} or missing 'grades' key"
        echo
    fi
    
    if grep -q "NotImplementedError" out.txt; then
        echo "🔍 ISSUE: NotImplementedError detected"
        echo "   Some functions are not yet implemented. Check the following functions:"
        grep -n "NotImplementedError" out.txt | while read line; do
            echo "   - Line $line"
        done
        echo
    fi
    
    echo "=== RECOMMENDATIONS ==="
    echo "1. Fix the load() function to return proper structure"
    echo "2. Implement all TODO functions marked with NotImplementedError"
    echo "3. Check that all print statements match the expected format"
    echo "4. Verify error handling for edge cases"
    echo
    echo "Review the diff above to see exactly what differs from expected output."
fi

echo
echo "=== FILES CREATED ==="
echo "- out.txt: Actual program output"
echo "- expected.txt: Expected correct output"
echo "- diff_output.txt: Detailed differences (if any)"
echo "- gradebook.json: Final database state"

# Clean up diff file if test passed
if [ -f diff_output.txt ] && [ ! -s diff_output.txt ]; then
    rm diff_output.txt
fi
