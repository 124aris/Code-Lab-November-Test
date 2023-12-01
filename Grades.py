# You have a file named ‘grades.txt’ with the following content:
# ___grades.txt____
# Ahmed,75
# Ali,54
# Mustafa,95
# Abeeha,88
# ________________
# Each line represents a student's name and their corresponding grade. Write a Python
# program that reads this file, calculates the average grade, and writes the result along
# with each student's name and grade to a new file named ‘grade_summary.txt’.
# Ensure that your program handles file exceptions thoroughly.
# *Write program in file Grades.py*

try:
    with open('Grades.txt', 'r') as File:
        Lines = File.readlines();
    TotalGrades = 0;
    StudentCount = 0;
    for Line in Lines:
        Name, Grade = Line.strip().split(',');
        TotalGrades += int(Grade);
        StudentCount += 1;
    AverageGrade = TotalGrades / StudentCount if StudentCount > 0 else 0;
    with open('Grade_Summary.txt', 'w') as SummaryFile:
        SummaryFile.write(f"Average Grade: {AverageGrade:.2f}\n\n");
        for Line in Lines:
            SummaryFile.write(Line);

except FileNotFoundError:
    print("File not found. Please ensure 'Grades.txt' exists in the current directory.");
except Exception as E:
    print(f"An error occurred: {E}");