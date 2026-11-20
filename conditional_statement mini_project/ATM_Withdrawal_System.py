
# ATM Withdrawal System

# Taking input from user
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Current Balance: ₹"))
amount = float(input("Enter Withdrawal Amount: ₹"))

print("\n----- ATM Transaction Details -----")
print("Account Holder Name:", name)

# Checking withdrawal conditions
if amount > 0:

    if amount <= balance:

        if amount <= 20000:

            # Successful transaction
            balance = balance - amount

            print("Transaction Status: Successful")
            print("Withdrawn Amount: ₹", amount)
            print("Remaining Balance: ₹", balance)

            # Checking low balance
            if balance < 1000:
                print("Warning: Low Balance Warning")

        else:
            print("Transaction Status: Rejected")
            print("Reason: Maximum withdrawal limit is ₹20,000")

    else:
        print("Transaction Status: Rejected")
        print("Reason: Insufficient Account Balance")

else:
    print("Transaction Status: Rejected")
    print("Reason: Withdrawal amount must be greater than ₹0")
