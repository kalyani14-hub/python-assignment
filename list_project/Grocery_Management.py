
# ==========================================
# GROCERY SHOPPING CART MANAGER
# Project 2.1.2 - Python Programming
# ==========================================

# Shopping cart
# Each entry contains: [item_name, quantity, unit_price]

cart = []

# Discount settings
DISCOUNT_THRESHOLD = 1000
DISCOUNT_PERCENTAGE = 10


# Function to accept valid number input
def get_number(message, minimum=0):
    while True:
        try:
            value = float(input(message))

            if value >= minimum:
                return value

            print(f"Enter a value greater than or equal to {minimum}.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to add items to cart
def add_item():
    print("\n========== ADD ITEM ==========")

    name = input("Enter item name: ").strip().title()

    if not name:
        print("Item name cannot be empty!")
        return

    quantity = int(get_number("Enter quantity: ", 1))
    price = get_number("Enter unit price: ", 0.01)

    # Check if item already exists
    for item in cart:
        if item[0].lower() == name.lower():
            item[1] += quantity
            item[2] = price

            print("\nExisting item quantity updated!")
            return

    # Insert new item into cart
    cart.append([name, quantity, price])

    print("\nItem added successfully!")


# Function to remove item by name
def remove_item():
    print("\n========== REMOVE ITEM ==========")

    if not cart:
        print("Shopping cart is empty!")
        return

    name = input("Enter item name to remove: ").strip()

    for item in cart:
        if item[0].lower() == name.lower():
            cart.remove(item)
            print(f"\n{name.title()} removed successfully!")
            return

    print("\nItem not found in cart!")


# Function to update item quantity
def update_quantity():
    print("\n========== UPDATE QUANTITY ==========")

    if not cart:
        print("Shopping cart is empty!")
        return

    name = input("Enter item name: ").strip()

    for item in cart:
        if item[0].lower() == name.lower():

            print("Current quantity:", item[1])

            new_quantity = int(
                get_number("Enter new quantity: ", 1)
            )

            item[1] = new_quantity

            print("\nQuantity updated successfully!")
            return

    print("\nItem not found in cart!")


# Function to calculate subtotal
def calculate_subtotal():
    costs = [
        item[1] * item[2]
        for item in cart
    ]

    return sum(costs)


# Function to display shopping cart
def view_cart():
    print("\n" + "=" * 65)
    print("                 GROCERY SHOPPING CART")
    print("=" * 65)

    if not cart:
        print("Your shopping cart is empty!")
        return

    print(
        f"{'Item':<18}{'Quantity':<12}"
        f"{'Price':<12}{'Total':<12}"
    )

    print("-" * 65)

    for item in cart:
        total = item[1] * item[2]

        print(
            f"{item[0]:<18}"
            f"{item[1]:<12}"
            f"Rs.{item[2]:<9.2f}"
            f"Rs.{total:.2f}"
        )

    print("-" * 65)

    subtotal = calculate_subtotal()

    print(f"Subtotal: Rs.{subtotal:.2f}")


# Function to display top three expensive items
def top_three_expensive():
    print("\n========== TOP 3 EXPENSIVE ITEMS ==========")

    if not cart:
        print("Shopping cart is empty!")
        return

    # Sort items by unit price in descending order
    sorted_items = sorted(
        cart,
        key=lambda item: item[2],
        reverse=True
    )

    # Slice first three items
    top_three = sorted_items[:3]

    print(
        f"\n{'Item':<20}{'Quantity':<12}"
        f"{'Unit Price':<15}"
    )

    print("-" * 50)

    for item in top_three:
        print(
            f"{item[0]:<20}"
            f"{item[1]:<12}"
            f"Rs.{item[2]:.2f}"
        )


# Function to generate final invoice
def generate_invoice():
    print("\n" + "=" * 65)
    print("                    GROCERY INVOICE")
    print("=" * 65)

    if not cart:
        print("Your cart is empty!")
        return

    subtotal = calculate_subtotal()

    # Calculate discount
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_PERCENTAGE / 100
    else:
        discount = 0

    grand_total = subtotal - discount

    print(
        f"{'Item':<18}{'Qty':<8}"
        f"{'Price':<12}{'Total':<12}"
    )

    print("-" * 65)

    for item in cart:
        item_total = item[1] * item[2]

        print(
            f"{item[0]:<18}"
            f"{item[1]:<8}"
            f"{item[2]:<12.2f}"
            f"{item_total:<12.2f}"
        )

    print("-" * 65)

    print(f"Subtotal       : Rs.{subtotal:.2f}")
    print(f"Discount       : Rs.{discount:.2f}")
    print(f"Grand Total    : Rs.{grand_total:.2f}")

    print("=" * 65)

    # Save invoice to text file
    save_invoice(subtotal, discount, grand_total)


# Function to save invoice
def save_invoice(subtotal, discount, grand_total):

    with open("grocery_invoice.txt", "w") as file:

        file.write("GROCERY SHOPPING CART INVOICE\n")
        file.write("=" * 55 + "\n\n")

        file.write(
            f"{'Item':<18}{'Qty':<8}"
            f"{'Price':<12}{'Total':<12}\n"
        )

        file.write("-" * 55 + "\n")

        for item in cart:
            item_total = item[1] * item[2]

            file.write(
                f"{item[0]:<18}"
                f"{item[1]:<8}"
                f"{item[2]:<12.2f}"
                f"{item_total:<12.2f}\n"
            )

        file.write("-" * 55 + "\n")

        file.write(f"Subtotal: Rs.{subtotal:.2f}\n")
        file.write(f"Discount: Rs.{discount:.2f}\n")
        file.write(f"Grand Total: Rs.{grand_total:.2f}\n")

    print("\nInvoice saved successfully!")
    print("File name: grocery_invoice.txt")


# Main program
def main():

    print("\n========================================")
    print("       GROCERY SHOPPING CART MANAGER")
    print("========================================")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Shopping Cart")
        print("5. Show Top 3 Expensive Items")
        print("6. Generate Final Invoice")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_item()

        elif choice == "2":
            remove_item()

        elif choice == "3":
            update_quantity()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            top_three_expensive()

        elif choice == "6":
            generate_invoice()

        elif choice == "7":
            print("\nThank you for shopping with us!")
            break

        else:
            print("\nInvalid choice! Please select 1 to 7.")


# Execute program
if __name__ == "__main__":
    main()
