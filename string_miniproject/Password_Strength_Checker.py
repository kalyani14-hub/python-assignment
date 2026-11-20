
# Mini Project 2: Password Strength Checker

# Accept password from the user
password = input("Enter your password: ")

# Initialize variables
uppercase = False
lowercase = False
digit = False
special = False

# Check minimum password length
length = len(password)

# Loop through each character in the password
for ch in password:

    # Check for uppercase letter
    if ch.isupper():
        uppercase = True

    # Check for lowercase letter
    elif ch.islower():
        lowercase = True

    # Check for digit
    elif ch.isdigit():
        digit = True

    # Check for special character
    elif not ch.isalnum():
        special = True

# Initialize strength score
score = 0

# Give points based on password conditions
if length >= 8:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if digit:
    score += 1

if special:
    score += 1

# Display password strength
print("\n----- Password Strength Report -----")

# Check password strength
if score <= 2:
    print("Password Strength: Weak")

elif score <= 4:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")

# Display individual conditions
print("\n----- Password Conditions -----")
print("Minimum 8 Characters:", length >= 8)
print("Uppercase Letter:", uppercase)
print("Lowercase Letter:", lowercase)
print("Digit:", digit)
print("Special Character:", special)

# End of program
