from inventory import products


def _read_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        return value


def _next_product_id():
    existing_numbers = (
        int(product_id[1:])
        for product_id in products
        if product_id.startswith("P") and product_id[1:].isdigit()
    )
    return f"P{max(existing_numbers, default=0) + 1:03d}"


def add_product():
    print("\n" + "=" * 35)
    print("           Add Product")
    print("=" * 35)

    name = input("Product name: ").strip().title()
    category = input("Category: ").strip().title()
    brand = input("Brand: ").strip().title()
    if not name or not category or not brand:
        print("Name, category, and brand cannot be empty.")
        return

    buying_price = _read_integer("Buying price: ")
    selling_price = _read_integer("Selling price: ")
    quantity = _read_integer("Quantity: ")
    product_id = _next_product_id()

    products[product_id] = {
        "name": name,
        "category": category,
        "brand": brand,
        "buying_price": buying_price,
        "selling_price": selling_price,
        "quantity": quantity,
    }
    print(f"\nProduct added successfully with ID {product_id}.")


def delete_product():
    product_id = input("Enter product ID to delete: ").strip().upper()
    if product_id not in products:
        print("Product ID not found.")
        return

    deleted_product = products.pop(product_id)
    print(f"{deleted_product['name']} ({product_id}) deleted successfully.")


def _read_optional_integer(label, current_value):
    while True:
        value = input(f"{label} [{current_value}]: ").strip()
        if not value:
            return current_value
        try:
            parsed_value = int(value)
        except ValueError:
            print("Please enter a valid whole number or leave it blank.")
            continue
        if parsed_value < 0:
            print("Please enter a non-negative number.")
            continue
        return parsed_value


def edit_product():
    product_id = input("Enter product ID to edit: ").strip().upper()
    product = products.get(product_id)
    if product is None:
        print("Product ID not found.")
        return

    print("Leave a field blank to keep its current value.")
    for field in ("name", "category", "brand"):
        value = input(f"{field.replace('_', ' ').title()} [{product[field]}]: ").strip()
        if value:
            product[field] = value.title()

    for field in ("buying_price", "selling_price", "quantity"):
        product[field] = _read_optional_integer(
            field.replace("_", " ").title(), product[field]
        )
    print(f"\nProduct {product_id} updated successfully.")


def admin_ctlr():
    username_required = "Harsh Tiwari"
    password_required = "12345678"

    while True:
        username = input("Enter admin username: ").strip()
        password = input("Enter admin password: ").strip()
        if username == username_required and password == password_required:
            break
        print("Incorrect username or password. Please try again.")

    while True:
        print("\n" + "=" * 35)
        print("             Admin Control")
        print("=" * 35)
        print("1. Add Product")
        print("2. Delete Product")
        print("3. Edit Product")
        print("4. Back")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            delete_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            break
        else:
            print("Please enter a valid menu number.")
