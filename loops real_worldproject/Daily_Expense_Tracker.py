
# Mini Project 1: Daily Expense Tracker

# Get the number of days from the user
days = int(input("Enter number of days: "))

# Initialize variables
total = 0
highest = 0

# Loop to enter expenses for each day
for i in range(1, days + 1):

    # Accept expense for the current day
    expense = float(input(f"Enter expense for day {i}: ₹"))

    # Add daily expense to total expense
    total = total + expense

    # Check and update the highest expense
    if expense > highest:
        highest = expense

# Calculate average daily expense
average = total / days

# Display the expense summary
print("\n----- Expense Summary -----")

# Display total expense
print("Total Expense: ₹", total)

# Display average daily expense
print("Average Daily Expense: ₹", average)

# Display highest single-day expense
print("Highest Daily Expense: ₹", highest)

# Check budget limit
if total > 5000:
    print("Budget Status: Budget Alert")
else:
    print("Budget Status: Within Budget")

# End of program
