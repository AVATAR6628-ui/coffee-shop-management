# Coffee shop products and their prices (in Toman).
menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
    "milkshake": 400000,
    "hotchocolate": 190000,
    "donat": 250000,
    "coffeeicecream":260000
}


def show_menu():
    """Display all available products and their prices."""
    print("\n========== Cafe Menu ==========")
    for product, price in menu.items():
        print(f"{product}: {price:,} Toman")
    print("===============================")
