
# Student Scholarship Eligibility Checker

# Taking student details
name = input("Enter Student Name: ")
percentage = float(input("Enter Percentage: "))
income = float(input("Enter Annual Family Income: "))
attendance = float(input("Enter Attendance Percentage: "))

# Checking eligibility
print("\n----- Scholarship Eligibility Result -----")
print("Student Name:", name)

if percentage >= 75 and income <= 400000 and attendance >= 75:

    if percentage >= 90:
        print("Eligibility Status: Eligible")
        print("Scholarship Category: Full Scholarship")
    else:
        print("Eligibility Status: Eligible")
        print("Scholarship Category: Partial Scholarship")

else:
    print("Eligibility Status: Not Eligible")
    print("Scholarship Category: No Scholarship")

    if percentage < 75 or income > 400000 or attendance < 75:
        print("Reason for Not Eligible:")

        if percentage < 75:
            print("- Percentage is below 75%")

        if income > 400000:
            print("- Annual family income exceeds Rs. 4,00,000")

        if attendance < 75:
            print("- Attendance is below 75%")
