from Order import orders


def calculate_total():
    """Return the sum of price times quantity for every order."""
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total


def calculate_discount(total):
    """Return a 10% discount for totals strictly above 1,000,000 Toman."""
    if total > 1000000:
        return total * 10 // 100
    return 0


def print_invoice():
    """Print the items, total, discount, and final amount to pay."""
    if not orders:
        print("\nNo orders to invoice.")
        return

    print("\n=============== Invoice ===============")
    for number, order in enumerate(orders, start=1):
        line_total = order["price"] * order["quantity"]
        print(f"{number}. {order['product']} | "
              f"Quantity: {order['quantity']} | "
              f"Subtotal: {line_total:,} Toman")

    total = calculate_total()
    discount = calculate_discount(total)
    final_amount = total - discount

    print("---------------------------------------")
    print(f"Total amount: {total:,} Toman")
    print(f"Discount: {discount:,} Toman")
    print(f"Amount to pay: {final_amount:,} Toman")
    print("=======================================")
