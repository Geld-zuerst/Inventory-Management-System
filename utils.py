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
    for product in products.values():
        print(product["name"])


def see_category():
    categories = set()
    for product in products.values():
        categories.add(product["category"])
    for category in categories:
        print(category)


def admin_ctlr():
    name = "Harsh Tiwari"
    key = "12345678"

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == name and password == key:
        print("Congo")
    elif username != name or password != key:
        print("Please Enter right credentials.")


def add_product():
    pass


def buy_product():
    input("\n Buy via entering name of product or searching product?(y, yes/n, no) ")
    if input == "y" or "yes":
        search_item()

    

def search_item():
    print("\n Search Items by")
    print("0. Entering name")
    print("1. View Products")
    print("2. see Category")
    search = input("Search by: ")
    if search == "0":
        name = input("Enter Product name: ")
        for product in product.values(name):
            print(product(name))
    if search == "1":
        see_product()
    if search == "2":
        see_category()