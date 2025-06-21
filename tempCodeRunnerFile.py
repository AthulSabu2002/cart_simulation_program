PRODUCTS = {
    'A': {'name': 'Product A', 'price': 20},
    'B': {'name': 'Product B', 'price': 40},
    'C': {'name': 'Product C', 'price': 50}
}

FLAT_10_DISCOUNT_AMOUNT = 10
FLAT_10_DISCOUNT_THRESHOLD = 200
BULK_5_DISCOUNT_PERCENT = 0.05
BULK_5_DISCOUNT_THRESHOLD = 10
BULK_10_DISCOUNT_PERCENT = 0.10
BULK_10_DISCOUNT_THRESHOLD = 20
TIERED_50_DISCOUNT_PERCENT = 0.50
TIERED_50_DISCOUNT_TOTAL_THRESHOLD = 30
TIERED_50_DISCOUNT_PRODUCT_THRESHOLD = 15

def get_valid_quantity(product_name, price):
    while True:
        try:
            value = input(f"Enter quantity for {product_name} (${price}): ").strip()
            if not value:
                return 0
            if value.isdigit():
                return int(value)
            print("❌ Invalid input. Please enter a non-negative whole number.")
        except:
            print("\nExiting...")
            exit(0)
        


def get_yes_no(prompt):
    while True:
        try:
            response = input(prompt).strip().lower()
            if response in ['yes']:
                return True
            elif response in ['no']:
                return False
            print("❌ Invalid input. Please enter 'yes' or 'no'.")
        except:
            print("\nExiting...")
            exit(0)


def get_product_inputs():
    print("Note: If you do not enter a value for quantity, it will be taken as 0.")
    print("If you do not enter a value for gift wrap, it will be taken as 'no'.\n")

    cart = {}

    try:
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
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        exit(0)


def calculate_discount(cart, subtotal, total_quantity):
    discounts = {
        'flat_10_discount': FLAT_10_DISCOUNT_AMOUNT if subtotal > FLAT_10_DISCOUNT_THRESHOLD else 0,
        'bulk_5_discount': sum(
            item['total'] * BULK_5_DISCOUNT_PERCENT
            for item in cart.values() if item['quantity'] > BULK_5_DISCOUNT_THRESHOLD
        ),
        'bulk_10_discount': subtotal * BULK_10_DISCOUNT_PERCENT if total_quantity > BULK_10_DISCOUNT_THRESHOLD else 0,
        'tiered_50_discount': 0
    }

    if total_quantity > TIERED_50_DISCOUNT_TOTAL_THRESHOLD:
        for item in cart.values():
            if item['quantity'] > TIERED_50_DISCOUNT_PRODUCT_THRESHOLD:
                discounts['tiered_50_discount'] += (
                    item['price'] *
                    (item['quantity'] - TIERED_50_DISCOUNT_PRODUCT_THRESHOLD) *
                    TIERED_50_DISCOUNT_PERCENT
                )

    best_discount = max(discounts.items(), key=lambda x: x[1])
    discount_name, discount_amount = best_discount

    if discount_amount == 0:
        discount_name = "No discount"

    return discount_name, discount_amount



def display_order_summary(cart, subtotal, discount_name, discount_amount, total):
    print("\n===== ORDER SUMMARY =====")
    for item in cart.values():
        print(f"{item['name']}: {item['quantity']} units - ${item['total']:.2f} {'--> Gift Wrapped' if item['gift_wrapped'] else ''}")

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Discount Applied: {discount_name} - ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")

def main():
    cart = get_product_inputs()

    subtotal = sum(item['total'] for item in cart.values())
    total_quantity = sum(item['quantity'] for item in cart.values())

    if total_quantity == 0:
        print("No items added to cart. Exiting.")
        return

    discount_name, discount_amount = calculate_discount(cart, subtotal, total_quantity)
    total = subtotal - discount_amount

    display_order_summary(cart, subtotal, discount_name, discount_amount, total)



if __name__ == "__main__":
    main()