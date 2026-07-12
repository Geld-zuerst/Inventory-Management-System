from utils import see_product, see_category, search_item,dashboard
from admin_control import admin_ctlr

while True:
    print("========== Inventory Management System ==========")
    print("1. Dashboard")                   # DONE
    print("2. Admin Control")               # PARTIALLY (MAIN FUNCTION)
    print("3. Stock Management")
    print("4. Purchase")                    # DONE
    print("5. Search Product")              # DONE
    print("0. Exit")                        # DONE
    print("="*52)

    choice = input("Welcome, What's u wanna Explore? ")

    if choice == "1":
        dashboard()
    elif choice == "2":
        admin_ctlr()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        search_item()
    elif choice == "0":
        print("Thanks for visiting My Store, Hope u'll come again.")
        break
    else:
        print("Please enter a valid number")