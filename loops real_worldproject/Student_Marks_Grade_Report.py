
# Mini Project 2: Student Marks and Grade Report

# Get the number of students
students = int(input("Enter number of students: "))

# Initialize variables
total_marks = 0
pass_count = 0
fail_count = 0

# Loop to enter details of each student
for i in range(1, students + 1):

    print("\nStudent", i)

    # Accept student's name
    name = input("Enter student name: ")

    # Accept student's marks
    marks = float(input("Enter marks out of 100: "))

    # Check whether marks are valid
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    # Add marks to total marks
    total_marks = total_marks + marks

    # Calculate grade based on marks
    if marks >= 75:
        grade = "A"
        pass_count = pass_count + 1

    elif marks >= 60:
        grade = "B"
        pass_count = pass_count + 1

    elif marks >= 50:
        grade = "C"
        pass_count = pass_count + 1

    elif marks >= 40:
        grade = "D"
        pass_count = pass_count + 1

    else:
        grade = "Fail"
        fail_count = fail_count + 1

    # Display student's result
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)

# Calculate class average using valid entries
valid_students = pass_count + fail_count

if valid_students > 0:
    average = total_marks / valid_students
else:
    average = 0

# Display class performance summary
print("\n----- Class Performance Report -----")

print("Class Average:", average)
print("Total Pass Students:", pass_count)
print("Total Fail Students:", fail_count)

# End of program
