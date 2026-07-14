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
        total_inventory = product["quantity"] * product["selling_price"]
    print("\nHello Visitor, this is the Summmary of my store.")
    print("Total Categories:", len(categories))
    print(f"Total Product: {total_quantity}")
    print(f"Total Inventory cost: {total_inventory}")



def see_product():
    print(f"{'ID':<8}{'Name':<20}{'Category':<20}{'brand':<10}{'Price':<10}{'Qty':<5}")
    print("-" * 75)

    for product_id, product in products.items():
        print(
            f"{product_id:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['brand']:<10}"
            f"₹{product['selling_price']:<9}"
            f"{product['quantity']:<5}"
            )


def see_category():
    categories = set()
    for product in products.values():
        categories.add(product["category"])
    for category in categories:
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
    name = input("Enter Name of the Product: ").title()
    found = False
    print(f"\nName: {name}\n")

    for product_id, product in products.items():
        if product["name"] == name:
            found = True
            print(f"Product ID : {product_id}")
            print(f"Name       : {product['name']}")
            print(f"Category   : {product['category']}")
            print(f"Price      : ₹{product['selling_price']}")
            print(f"Quantity   : {product['quantity']}")

        if not found:
            print("No product found")



def buy_product():
    input("\n Buy via entering name of product or searching product?(y, yes/n, no) ")
    if input == "y" or "yes":
        search_item()

    

def search_item():
    print("\n Search Items by")
    print("0. Entering name")
    print("1. View Products")
    print("2. Via Category")
    search = input("Search by: ")
    if search == "0":
        view_by_name()
    if search == "1":
        see_product()
    if search == "2":
        see_category()
        view_by_category()