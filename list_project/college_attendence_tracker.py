
# ==========================================
# COLLEGE ATTENDANCE TRACKER
# Project 2.1.1 - Python Programming
# ==========================================

# List to store student details
students = []

# Nested list to store attendance of all lectures
# Each inner list represents one lecture
attendance = []

THRESHOLD = 75


# Function to accept integer input
def get_integer(message, minimum=1):
    while True:
        try:
            value = int(input(message))
            if value >= minimum:
                return value
            print(f"Please enter a number >= {minimum}.")
        except ValueError:
            print("Invalid input! Enter a valid number.")


# Function to register students
def register_students():
    print("\n========== STUDENT REGISTRATION ==========")

    n = get_integer("Enter number of students: ")

    for i in range(n):
        print(f"\nStudent {i + 1}")

        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()

        students.append([roll, name])

    print("\nStudents registered successfully!")


# Function to mark attendance
def mark_attendance():
    print("\n========== MARK ATTENDANCE ==========")

    lecture_no = len(attendance) + 1
    lecture_attendance = []

    print(f"\nAttendance for Lecture {lecture_no}")
    print("Enter P for Present and A for Absent.\n")

    for student in students:
        while True:
            status = input(
                f"{student[0]} - {student[1]} (P/A): "
            ).strip().upper()

            if status in ["P", "A"]:
                lecture_attendance.append(status)
                break
            else:
                print("Invalid input! Enter P or A.")

    # Store lecture attendance as a list
    attendance.append(lecture_attendance)

    print("\nAttendance marked successfully!")


# Function to calculate attendance percentage
def calculate_percentage(present, total):
    if total == 0:
        return 0

    return (present / total) * 100


# Function to generate attendance report
def generate_report():

    total_lectures = len(attendance)

    if total_lectures == 0:
        print("\nNo attendance records available!")
        return

    report = []

    for i in range(len(students)):

        # Get attendance of one student across all lectures
        student_records = [
            lecture[i] for lecture in attendance
        ]

        present = student_records.count("P")
        absent = student_records.count("A")

        percentage = calculate_percentage(
            present, total_lectures
        )

        report.append([
            students[i][0],
            students[i][1],
            present,
            absent,
            percentage
        ])

    # Print attendance sheet
    print("\n" + "=" * 75)
    print("                 COLLEGE ATTENDANCE SHEET")
    print("=" * 75)

    print(
        f"{'Roll No':<12}{'Name':<20}"
        f"{'Present':<10}{'Absent':<10}{'Percentage':<12}"
    )

    print("-" * 75)

    for record in report:
        print(
            f"{record[0]:<12}"
            f"{record[1]:<20}"
            f"{record[2]:<10}"
            f"{record[3]:<10}"
            f"{record[4]:.2f}%"
        )

    # Find students below 75%
    defaulters = [
        record for record in report
        if record[4] < THRESHOLD
    ]

    # Sort defaulters by attendance percentage
    # Lowest percentage appears first
    defaulters.sort(key=lambda x: x[4])

    print("\n" + "=" * 75)
    print("                    DEFAULTER REPORT")
    print("=" * 75)

    print(f"Attendance threshold: {THRESHOLD}%")
    print("-" * 75)

    if len(defaulters) == 0:
        print("No defaulters found!")
    else:
        print(
            f"{'Roll No':<12}{'Name':<20}"
            f"{'Present':<10}{'Absent':<10}{'Percentage':<12}"
        )

        print("-" * 75)

        for record in defaulters:
            print(
                f"{record[0]:<12}"
                f"{record[1]:<20}"
                f"{record[2]:<10}"
                f"{record[3]:<10}"
                f"{record[4]:.2f}%"
            )

    # Save report to text file
    save_report(report, defaulters, total_lectures)


# Function to save report in a text file
def save_report(report, defaulters, total_lectures):

    with open("attendance_report.txt", "w") as file:

        file.write("COLLEGE ATTENDANCE TRACKER\n")
        file.write("=" * 65 + "\n")

        file.write(f"Total Lectures: {total_lectures}\n\n")

        file.write("ATTENDANCE SHEET\n")
        file.write("-" * 65 + "\n")

        file.write(
            f"{'Roll No':<12}{'Name':<20}"
            f"{'Present':<10}{'Absent':<10}{'Percentage':<12}\n"
        )

        for record in report:
            file.write(
                f"{record[0]:<12}"
                f"{record[1]:<20}"
                f"{record[2]:<10}"
                f"{record[3]:<10}"
                f"{record[4]:.2f}%\n"
            )

        file.write("\nDEFAULTER REPORT\n")
        file.write("-" * 65 + "\n")
        file.write(f"Minimum Required Attendance: {THRESHOLD}%\n\n")

        if len(defaulters) == 0:
            file.write("No defaulters found!\n")
        else:
            for record in defaulters:
                file.write(
                    f"Roll No: {record[0]}, "
                    f"Name: {record[1]}, "
                    f"Attendance: {record[4]:.2f}%\n"
                )

    print("\nReport saved successfully!")
    print("File name: attendance_report.txt")


# Main menu
def main():

    print("\n========================================")
    print("       COLLEGE ATTENDANCE TRACKER")
    print("========================================")

    register_students()

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Mark Attendance")
        print("2. View Attendance Report")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            mark_attendance()

        elif choice == "2":
            generate_report()

        elif choice == "3":
            print("\nThank you for using College Attendance Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Execute the program
if __name__ == "__main__":
    main()
