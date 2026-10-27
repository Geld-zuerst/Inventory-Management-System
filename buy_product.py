from inventory import products


def _read_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity to buy: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue
        return quantity


def _purchase(product_id, product):
    print("\n" + "-" * 35)
    print("Product Found")
    print("-" * 35)
    print(f"Product ID : {product_id}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Price      : ₹{product['selling_price']}")
    print(f"Available  : {product['quantity']}")

    quantity = _read_quantity()
    if quantity > product["quantity"]:
        print(f"Only {product['quantity']} available. Purchase failed.")
        return

    total = product["selling_price"] * quantity
    print("\n" + "-" * 35)
    print("Order Summary")
    print("-" * 35)
    print(f"Product      : {product['name']}")
    print(f"Unit Price   : ₹{product['selling_price']}")
    print(f"Quantity     : {quantity}")
    print(f"Total amount : ₹{total}")
    print("-" * 35)

    confirmation = input("Confirm purchase? (Y/N): ").strip().casefold()
    if confirmation == "y":
        product["quantity"] -= quantity
        print("\nPurchase successful. Stock has been updated.")
    else:
        print("\nPurchase cancelled.")


def buy_product():
    while True:
        print("\n" + "=" * 35)
        print("           Buy Product")
        print("=" * 35)
        print("1. Search by Product ID")
        print("2. Search by Product Name")
        print("3. Back")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            product_id = input("Enter product ID (e.g. P001): ").strip().upper()
            product = products.get(product_id)
            if product is None:
                print("No product found.")
            else:
                _purchase(product_id, product)
        elif choice == "2":
            name = input("Enter product name: ").strip().casefold()
            matches = [
                (product_id, product)
                for product_id, product in products.items()
                if product["name"].casefold() == name
            ]
            if not matches:
                print("No product found.")
            else:
                for product_id, product in matches:
                    _purchase(product_id, product)
        elif choice == "3":
            break
        else:
            print("Please enter a valid menu number.")
