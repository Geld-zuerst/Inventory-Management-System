from inventory import products

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

search_item()


