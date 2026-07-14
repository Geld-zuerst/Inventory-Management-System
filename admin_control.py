from inventory import products

def add_product():
    print("======== Add a new product ========")
    name = input("Enter name of the product: ")
    category = input("Enter category of the product: ")
    brand = input("Enter the Brand name: ")
    selling_price = input("Enter the Selling Price of the product: ")
    quantity = input("Enter the Quantity of product: ")

    products = {
        "Name" : name,
        "Category" : category,
        "Brand" : brand,
        "Selling_price" : selling_price,
        "quantity" : quantity
    }

    for product in products.values():
        print(product["name"])


def delete_product():
    pass


def edit_product():
    pass


def admin_ctlr():
    Name = "Harsh Tiwari"
    key = "12345678"

    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username == Name and password == key:
            print("")
            print("~"*52)
            print("Happy to see u Admin, Hope u'r doing good in real life.")
            print("~"*52)
            print("\n1. Add Product")
            print("2. Delete Product")
            print("3. Edit Product")
            print("4. Back")
            change = input("What u wanna change Admin? ")
            if change == "1":
                add_product()
                break
            if change == "2":
                delete_product()
                break
            if change == "3":
                edit_product()
                break
            if change == "4":
                break
            else:
                print("Please enter a valid input")
        elif username != Name or password != key:
            print("Please Enter right credentials.")