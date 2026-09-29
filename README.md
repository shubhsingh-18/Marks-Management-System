# Marks Management System


A simple Python-based Student Marks Management System that allows users to add student details, enter CAT-1 marks, search for students using their registration number, and calculate their total marks, average, grade, and pass/fail result.


## Project Overview

This project was developed using Python as a beginner-level programming project.

The program allows you to:

Add student registration numbers and names.

Enter CAT-1 marks for three subjects.

Store student information and marks.

Search for a student using their registration number.

Display the student's details and marks.

Calculate total marks.

Calculate average marks.

Assign a grade based on the average.

Display whether the student has passed or failed.


## Technologies Used

Python 3

Python Lists

Python Dictionaries

Functions

while loops

for loops

Conditional statements (if, elif, else)

User input and output

Basic data processing


## Subjects

The program currently accepts marks for the following subjects:

Introduction to Problem Solving

Electric Circuits and System

Calculus


## Grading System

The grade is calculated based on the student's average marks.

Average Marks	Grade
90 – 100	S
80 – 89	B
70 – 79	C
60 – 69	D
50 – 59	E
Below 50	F
Passing Criteria

A student is considered PASS if their average marks are 40 or above.

If the average is below 40, the student is considered FAIL.


##How the Program Works


# 1. Add Student Details

The program asks for:

Enter Registration Number:
Enter Student Name:

The registration number and name are stored in the program.

# 2. Enter CAT-1 Marks

The program then asks for marks in three subjects:

Introduction to Problem Solving
Electric Circuits and System
Calculus

# 3. Search for a Student

After adding students, the program asks for a registration number.

For example:

Enter registration number: 24BCE1234


If the student exists, their details and marks are displayed.

# 4. Calculate Result

The program calculates:

Total Marks

Total = Subject 1 + Subject 2 + Subject 3


Average Marks

Average = Total Marks / 3


The average is then used to determine the student's grade and result.


## How to Run

Install Python

Make sure Python 3 is installed on your computer.

You can check it using:

python --version


## Example

```text
Adding a Student
Enter Student Details.

Enter Registration Number: 24BCE1234
Enter Student Name: Rahul

Enter Marks for Rahul
introduction to Problem Solving: 85
Electric Circuits and System: 78
calculus: 92

Student added successfully!
Searching for a Student
Enter registration number: 24BCE1234

--- Student Found ---
Registration No: 24BCE1234
Name: Rahul

--- Marks ---
Problem Solving: 85
Electric Circuits and System: 78
calculus: 92

--- Result ---
Total Marks: 255
Average Marks: 85.0
Grade: B
Result: PASS , CONGRATULATION YOU ARE PROMOTED, THANK YOU!
```

## Project Structure

```text
Student-CAT1-Marks-Management/
│
├── student_marks.py
└── README.md
```


## Future Improvements

Some features that could be added in future versions:

Store student data permanently using files or a database.

Add student deletion and modification options.

Add input validation for marks.

Prevent duplicate registration numbers.

Add more subjects.

Generate a complete student report card.

Add a graphical user interface (GUI).

Export student results to CSV or Excel.

Improve the menu system.
