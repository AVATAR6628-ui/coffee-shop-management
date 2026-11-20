from Menu import menu

# Each order is stored as a dictionary in this list.
orders = []


def add_order():
    """Ask for a product and quantity, then save a valid order."""
    product = input("Enter product name: ").strip().lower()

    if product not in menu:
        print("This product is not available in the cafe menu.")
        return

    quantity_text = input("Enter quantity: ").strip()
    try:
        quantity = int(quantity_text)
    except ValueError:
        print("Invalid quantity! Please enter a positive whole number.")
        return

    if quantity <= 0:
        print("Invalid quantity! Please enter a number greater than zero.")
        return

    orders.append({"product": product, "price": menu[product], "quantity": quantity})
    print("Order added successfully.")


def show_orders():
    """Display all registered orders."""
    if not orders:
        print("\nNo orders have been registered yet.")
        return

    print("\n========== Your Orders ==========")
    for number, order in enumerate(orders, start=1):
        print(f"{number}. Product: {order['product']} | "
              f"Price: {order['price']:,} Toman | "
              f"Quantity: {order['quantity']}")
    print("=================================")
