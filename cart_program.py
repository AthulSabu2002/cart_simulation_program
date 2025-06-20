PRODUCTS = {
    'A': {'name': 'Product A', 'price': 20},
    'B': {'name': 'Product B', 'price': 40},
    'C': {'name': 'Product C', 'price': 50}
}

def get_valid_quantity(product_name, price):
    while True:
        value = input(f"Enter quantity for {product_name} (${price}): ").strip()
        if not value:
            return 0
        if value.isdigit():
            return int(value)
        print("❌ Invalid input. Please enter a non-negative whole number.")


def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes']:
            return True
        elif response in ['no']:
            return False
        print("❌ Invalid input. Please enter 'yes' or 'no'.")


def get_product_inputs():
    print("Note: If you do not enter a value for quantity, it will be taken as 0.")
    print("If you do not enter a value for gift wrap, it will be taken as 'no'.\n")

    cart = {}

    for product_id, product_info in PRODUCTS.items():
        quantity = get_valid_quantity(product_info['name'], product_info['price'])

        gift_wrapped = False
        if quantity > 0:
            gift_wrapped = get_yes_no(f"Is {product_info['name']} wrapped as a gift? (yes/no): ")

        cart[product_id] = {
            'name': product_info['name'],
            'price': product_info['price'],
            'quantity': quantity,
            'total': product_info['price'] * quantity,
            'gift_wrapped': gift_wrapped
        }

    return cart


def display_order_summary(cart, subtotal):
    print("\n===== ORDER SUMMARY =====")
    for item in cart.values():
        print(f"{item['name']}: {item['quantity']} units - ${item['total']:.2f}")

    print(f"\nSubtotal: ${subtotal:.2f}")

def main():
    cart = get_product_inputs()

    subtotal = sum(item['total'] for item in cart.values())
    total_quantity = sum(item['quantity'] for item in cart.values())

    if total_quantity == 0:
        print("No items added to cart. Exiting.")
        return

    display_order_summary(cart, subtotal)


if __name__ == "__main__":
    main()