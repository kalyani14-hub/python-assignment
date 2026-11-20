
# Mini Project 5: Number Guessing Game

# Set the secret number
secret_number = 37

# Set maximum number of attempts
max_attempts = 5

# Initialize attempt counter
attempts = 0

# Display game instructions
print("Welcome to Number Guessing Game!")
print("Guess the secret number between 1 and 100.")
print("You have only 5 attempts.")

# Start the guessing loop
while attempts < max_attempts:

    # Accept user's guess
    guess = int(input("\nEnter your guess: "))

    # Increase attempt counter
    attempts = attempts + 1

    # Check whether the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        print("You won the game!")
        break

    # Check whether the guess is too low
    elif guess < secret_number:
        print("Too low! Try a higher number.")

    # If the guess is too high
    else:
        print("Too high! Try a lower number.")

    # Display remaining attempts
    print("Attempts remaining:", max_attempts - attempts)

# Check whether the user failed all attempts
if guess != secret_number and attempts == max_attempts:
    print("\nSorry! You lost the game.")
    print("The secret number was:", secret_number)

# Display total attempts used
print("Attempts used:", attempts)

# End of game
print("Thank you for playing!")
