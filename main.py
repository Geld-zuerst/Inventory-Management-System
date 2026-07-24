from utils import search_item,dashboard,stock_management
from admin_control import admin_ctlr
from buy_product import buy_product


while True:
    print("\n========== Inventory Management System ==========")
    print("1. Dashboard")                   # DONE
    print("2. Admin Control")               # DONE (Delete & Edit remaining)
    print("3. Stock Management")
    print("4. Purchase")                    # DONE
    print("5. Search Product")              # DONE
    print("0. Exit")                        # DONE
    print("="*52)

    choice = input("\nWelcome, What's u wanna Explore in our store? ")

    if choice == "1":
        dashboard()
    elif choice == "2":
        admin_ctlr()
    elif choice == "3":
        stock_management()
    elif choice == "4":
        buy_product()
    elif choice == "5":
        search_item()
    elif choice == "0":
        print()
        print("-"*55)
        print("Thanks for visiting My Store, Hope u'll come again.")
        print("-"*55)
        print()
        break
    else:
        print("Please enter a valid number")