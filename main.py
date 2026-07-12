from utils import see_product, see_category, admin_ctlr, search_item,dashboard

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
else:
    print("Please enter a valid number")