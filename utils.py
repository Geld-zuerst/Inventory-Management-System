from inventory import products


def dashboard():
    total_quantity = 0
    total_inventory = 0
    categories = set()
    for product in products.values():
        categories.add(product["category"])
    for product in products.values():
        total_quantity += product["quantity"]
    for product in products.values():
        total_inventory += product["quantity"] * product["selling_price"]
    print("-"*52)
    print("\nHello Visitor, this is the Summmary of my store.")
    print(f"📂 Categories        : {len(categories)}")
    print(f"📊 Total Stock Units : {total_quantity}")
    print(f"💰 Inventory Value   : {total_inventory}")
    print("-"*52)



def see_product():
    print()
    print("=" * 75)
    print(f"{'ID':<8}{'Name':<20}{'Category':<20}{'brand':<10}{'Price':<10}{'Qty':<5}")
    print("=" * 75)
    print()

    for product_id, product in products.items():
        print(
            f"{product_id:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['brand']:<10}"
            f"₹{product['selling_price']:<9}"
            f"{product['quantity']:<5}"
            )
    print("=" * 75)


def see_category():
    categories = set()
    for product in products.values():
        categories.add(product["category"])
    for category in sorted(categories):
        print(category)


def view_by_category():
    category = input("Enter Category: ").title()

    print(f"\nCategory: {category}\n")
    found = False

    print(f"{'ID':<8}{'Name':<20}{'Brand':<10}{'Price':<10}{'Qty':<5}")
    print("-" * 45)
    for product_id, product in products.items():
        if product["category"] == category:
            found = True
            print(
                f"{product_id:<8}"
                f"{product['name']:<20}"
                f"{product['brand']:<10}"
                f"₹{product['selling_price']:<9}"
                f"{product['quantity']:<5}"
            )

    if not found:
        print("No products found.")

def view_by_name():
    name = input("Enter product name: ").strip().casefold()
    found = False
    print(f"\nName: {name}\n")

    for product_id, product in products.items():
        if product["name"].casefold() == name:
            found = True
            print(f"Product ID : {product_id}")
            print(f"Name       : {product['name']}")
            print(f"Category   : {product['category']}")
            print(f"Price      : ₹{product['selling_price']}")
            print(f"Quantity   : {product['quantity']}")
    if not found:
        print("No product found.")


def view_by_id():
    product_id = input("Enter product ID: ").strip().upper()
    product = products.get(product_id)
    if product is None:
        print("No product found.")
        return

    print(f"\nProduct ID : {product_id}")
    print(f"Name       : {product['name']}")
    print(f"Category   : {product['category']}")
    print(f"Brand      : {product['brand']}")
    print(f"Price      : ₹{product['selling_price']}")
    print(f"Quantity   : {product['quantity']}")


def search_item():
    print("\nSearch Items")
    print("0. Search by name")
    print("1. View all products")
    print("2. Browse by category")
    print("3. Search by product ID")
    search = input("Choose an option: ").strip()

    if search == "0":
        view_by_name()
    elif search == "1":
        see_product()
    elif search == "2":
        see_category()
        view_by_category()
    elif search == "3":
        view_by_id()
    else:
        print("Please enter a valid menu number.")


def in_stock(quantity):
    if quantity >= 10:
        return "✅ In Stock"
    elif quantity > 0:
        return "⚠ Low Stock"
    return "❌ Out of Stock"

def stock_management():
    while True:
        print("\n" + "=" * 35)
        print("         Stock Management")
        print("=" * 35)

        print("\n1. View All Stock")
        print("2. Restock Product")
        print("3. Reduce Stock (Damaged/Lost)")
        print("4. Low Stock Products")
        print("5. Out of Stock Products")
        print("6. Back")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            print("-" * 32)
            print("View All Stock")
            print("-" * 32)
            print()
            print("=" * 75)
            print(f"{'ID':<8}{'Name':<20}{'Category':<20}{'Qty':<5}{'Stock Status':<22}")
            print("=" * 75)
            print()

            for product_id, product in products.items():
                status = in_stock(product['quantity'])
                print(
                    f"{product_id:<8}"
                    f"{product['name']:<20}"
                    f"{product['category']:<20}"
                    f"{product['quantity']:<5}"
                    f"{status:<22}"
                )
            print("=" * 75)
        elif choice == "2":
            print("\n" + "-" * 32)
            print("Restock Product")
            print("-" * 32)
            product_id = input("\nEnter product ID (e.g. P001): ").strip().upper()
            if product_id in products:
                product = products[product_id]
                print("\nProduct Found")
                print(f"Name           : {product['name']}")
                print(f"Current Stock  : {product['quantity']}")

                try:
                    add_quantity = int(input("\nEnter quantity to add: "))
                except ValueError:
                    print("\nPlease enter a valid integer quantity.")
                    continue
                if add_quantity < 0:
                    print("\nPlease enter a non-negative number.")
                else:
                    product["quantity"] += add_quantity
                    print(f"\nNew stock: {product['quantity']}")
                    print("Stock updated successfully.")
            else:
                print("\nProduct ID not found.")
        elif choice == "3":
            product_id = input("Enter product ID: ").strip().upper()
            product = products.get(product_id)
            if product is None:
                print("Product ID not found.")
                continue

            try:
                reduce_quantity = int(input("Enter quantity to remove: "))
            except ValueError:
                print("Please enter a valid integer quantity.")
                continue
            if reduce_quantity <= 0:
                print("Quantity must be greater than zero.")
            elif reduce_quantity > product["quantity"]:
                print(f"Only {product['quantity']} units are currently in stock.")
            else:
                product["quantity"] -= reduce_quantity
                print(f"Stock updated. New quantity: {product['quantity']}")
        elif choice == "4":
            low_stock = [
                (product_id, product)
                for product_id, product in products.items()
                if 0 < product["quantity"] < 10
            ]
            if not low_stock:
                print("No low-stock products.")
            else:
                print(f"\n{'ID':<8}{'Name':<20}{'Quantity':<10}")
                print("-" * 38)
                for product_id, product in low_stock:
                    print(
                        f"{product_id:<8}"
                        f"{product['name']:<20}"
                        f"{product['quantity']:<10}"
                    )
        elif choice == "5":
            out_of_stock = [
                (product_id, product)
                for product_id, product in products.items()
                if product["quantity"] == 0
            ]
            if not out_of_stock:
                print("No out-of-stock products.")
            else:
                print(f"\n{'ID':<8}{'Name':<20}")
                print("-" * 28)
                for product_id, product in out_of_stock:
                    print(f"{product_id:<8}{product['name']:<20}")
        elif choice == "6":
            break
        else:
            print("Please enter a valid menu number.")