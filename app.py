
# Restaurant Order Management System

# Menu using Dictionary
menu = {
    "Burger": 100,
    "Pizza": 200,
    "Coffee": 50
}

# Display Menu
print("================================")
print("     WELCOME TO FOOD CORNER")
print("================================")

print("\n-------- FOOD MENU --------")

for item, price in menu.items():
    print(item, " : Rs.", price)

print("---------------------------")

# Select Table
table = int(input("\nEnter table number (1-20): "))

if table < 1 or table > 20:
    print("Invalid table number!")
    
else:
    # Empty list to store orders
    orders = []

    while True:

        print("\n1. Burger - Rs.100")
        print("2. Pizza  - Rs.200")
        print("3. Coffee - Rs.50")
        print("4. Generate Bill")

        choice = input("\nEnter your choice: ")

        if choice == "4":
            break

        # Select food item
        if choice == "1":
            item = "Burger"

        elif choice == "2":
            item = "Pizza"

        elif choice == "3":
            item = "Coffee"

        else:
            print("Invalid choice! Please try again.")
            continue

        # Enter quantity
        quantity = input("Enter quantity: ")

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity! Enter a whole number.")
            continue

        quantity = int(quantity)

        # Calculate amount
        amount = menu[item] * quantity

        # Store order in dictionary
        order = {
            "item": item,
            "quantity": quantity,
            "amount": amount
        }

        # Add order to list
        orders.append(order)

        print(item, "x", quantity, "added successfully!")
        
    # Generate Final Bill
    if len(orders) == 0:
        print("\nNo orders placed.")

    else:
        print("\n================================")
        print("          FINAL BILL")
        print("================================")

        print("Table Number:", table)

        subtotal = 0

        print("\nItem       Quantity       Amount")

        # Display all orders
        for order in orders:

            print(order["item"], "      ",
                  order["quantity"], "           Rs.",
                  order["amount"])

            subtotal = subtotal + order["amount"]

        # Calculate charges
        service_charge = subtotal * 10 / 100
        gst = subtotal * 5 / 100

        total = subtotal + service_charge + gst

        # Display Bill
        print("\n--------------------------------")
        print("Subtotal: Rs.", subtotal)
        print("Service Charge (10%): Rs.", service_charge)
        print("GST (5%): Rs.", gst)

        print("--------------------------------")
        print("TOTAL AMOUNT: Rs.", total)

        print("================================")
        print("       THANK YOU!")
        print("        VISIT AGAIN")
        print("================================")
