
# Movie Ticket Booking System

# Taking input from customer
name = input("Enter Customer Name: ")
age = int(input("Enter Age: "))
show = input("Enter Show Type (Morning/Evening): ").strip().capitalize()
day = input("Enter Day Type (Weekday/Weekend): ").strip().capitalize()

# Base ticket price
price = 200
discount = 0
surcharge = 0

print("\n----- Movie Ticket Booking Details -----")
print("Customer Name:", name)

# Checking age validity
if age >= 0:

    # Checking age-based discount
    if age < 12:
        discount = price * 50 / 100

    elif age >= 60:
        discount = price * 30 / 100

    # Checking show type
    if show == "Morning":
        discount = discount + 30

    elif show == "Evening":
        discount = discount

    else:
        print("Invalid Show Type")

    # Checking day type
    if day == "Weekend":
        surcharge = 50

    elif day == "Weekday":
        surcharge = 0

    else:
        print("Invalid Day Type")

    # Calculating final price
    if (show == "Morning" or show == "Evening") and (day == "Weekday" or day == "Weekend"):

        final_price = price - discount + surcharge

        print("Original Ticket Price: ₹", price)
        print("Discount: ₹", discount)
        print("Weekend Surcharge: ₹", surcharge)
        print("Final Ticket Price: ₹", final_price)

else:
    print("Invalid Age: Age cannot be negative")
