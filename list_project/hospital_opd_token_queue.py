
# ==========================================
# HOSPITAL OPD TOKEN QUEUE SYSTEM
# Project 2.1.3 - Python Programming
# ==========================================

# Waiting queue
# Each patient is stored as [token_number, patient_name]

queue = []

# Token number generator
next_token = 1

# Average consultation time in minutes
AVG_CONSULTATION_TIME = 10


# Function to display current queue
def display_queue():

    print("\n" + "=" * 65)
    print("              HOSPITAL OPD WAITING QUEUE")
    print("=" * 65)

    if len(queue) == 0:
        print("No patients waiting!")
        print("=" * 65)
        return

    print(
        f"{'Position':<12}"
        f"{'Token No.':<15}"
        f"{'Patient Name':<20}"
        f"{'Estimated Wait':<15}"
    )

    print("-" * 65)

    for position, patient in enumerate(queue, start=1):

        waiting_time = (position - 1) * AVG_CONSULTATION_TIME

        print(
            f"{position:<12}"
            f"{patient[0]:<15}"
            f"{patient[1]:<20}"
            f"{waiting_time} minutes"
        )

    print("-" * 65)

    print("Total patients waiting:", len(queue))

    print("=" * 65)


# Function to register a normal patient
def register_patient():

    global next_token

    print("\n========== PATIENT REGISTRATION ==========")

    name = input("Enter patient name: ").strip()

    if not name:
        print("Patient name cannot be empty!")
        return

    patient = [next_token, name]

    # Add patient at the end of queue
    queue.append(patient)

    print("\nPatient registered successfully!")
    print("Your token number is:", next_token)

    next_token += 1

    display_queue()


# Function to register emergency patient
def emergency_patient():

    global next_token

    print("\n========== EMERGENCY REGISTRATION ==========")

    name = input("Enter emergency patient name: ").strip()

    if not name:
        print("Patient name cannot be empty!")
        return

    patient = [next_token, name]

    # Insert emergency patient at the front
    queue.insert(0, patient)

    print("\nEmergency patient registered successfully!")
    print("Emergency token number:", next_token)

    next_token += 1

    display_queue()


# Function to serve the next patient
def serve_patient():

    print("\n========== SERVING PATIENT ==========")

    if len(queue) == 0:
        print("No patients in the waiting queue!")
        return

    # Remove first patient from queue
    patient = queue.pop(0)

    print("\nPatient is being served.")
    print("Token Number:", patient[0])
    print("Patient Name:", patient[1])

    print("\nConsultation started successfully!")

    display_queue()


# Function to cancel a token
def cancel_token():

    print("\n========== CANCEL TOKEN ==========")

    if len(queue) == 0:
        print("No tokens available to cancel!")
        return

    try:
        token = int(input("Enter token number to cancel: "))

    except ValueError:
        print("Invalid token number!")
        return

    # Find token using index()
    for patient in queue:

        if patient[0] == token:

            queue.remove(patient)

            print("\nToken cancelled successfully!")
            print("Cancelled patient:", patient[1])

            display_queue()
            return

    print("\nToken number not found!")


# Function to display queue length
def show_queue_length():

    print("\n========== QUEUE INFORMATION ==========")

    total_patients = len(queue)

    print("Current queue length:", total_patients)

    estimated_total_wait = total_patients * AVG_CONSULTATION_TIME

    print(
        "Estimated time to serve all waiting patients:",
        estimated_total_wait,
        "minutes"
    )

    display_queue()


# Function to search patient token
def search_token():

    print("\n========== SEARCH TOKEN ==========")

    try:
        token = int(input("Enter token number: "))

    except ValueError:
        print("Invalid token number!")
        return

    for position, patient in enumerate(queue, start=1):

        if patient[0] == token:

            waiting_time = (position - 1) * AVG_CONSULTATION_TIME

            print("\nPatient found!")
            print("Patient Name:", patient[1])
            print("Token Number:", patient[0])
            print("Queue Position:", position)
            print("Estimated Waiting Time:", waiting_time, "minutes")

            return

    print("\nToken not found in waiting queue!")


# Main menu
def main():

    print("\n============================================")
    print("        HOSPITAL OPD TOKEN QUEUE SYSTEM")
    print("============================================")

    while True:

        print("\n============== MAIN MENU ==============")

        print("1. Register Normal Patient")
        print("2. Register Emergency Patient")
        print("3. Serve Next Patient")
        print("4. Cancel Token")
        print("5. View Queue Length")
        print("6. Search Patient Token")
        print("7. Display Waiting Queue")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            register_patient()

        elif choice == "2":

            emergency_patient()

        elif choice == "3":

            serve_patient()

        elif choice == "4":

            cancel_token()

        elif choice == "5":

            show_queue_length()

        elif choice == "6":

            search_token()

        elif choice == "7":

            display_queue()

        elif choice == "8":

            print("\nThank you for using Hospital OPD Token Queue System!")
            break

        else:

            print("\nInvalid choice! Please enter 1 to 8.")


# Execute program
if __name__ == "__main__":
    main()
