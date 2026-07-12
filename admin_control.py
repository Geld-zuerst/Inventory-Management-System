def add_product():
    pass


def delete_product():
    pass


def edit_product():
    pass


def admin_ctlr():
    name = "Harsh Tiwari"
    key = "12345678"

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == name and password == key:
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
        if change == "2":
            delete_product()
        if change == "3":
            edit_product()
        if change == "4":
            print("Keep Improving Admin")
        else:
            print("Please enter a valid input")
    elif username != name or password != key:
        print("Please Enter right credentials.")