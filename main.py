from utils import see_product, see_category, admin_ctlr, search_item

print("========== Inventory Management System ==========")
print("1. Dashboard")
print("2. Admin Control")
print("3. Stock Management")
print("4. Sales")
print("5. Purchase")
print("6. Search Product")
print("7. Reports")
print("8. Backup Data")
print("9. Settings")
print("0. Exit")
print("="*52)

choice = input("Welcome, What's u wanna Explore? ")

if choice == "1":
    pass
elif choice == "2":
    admin_ctlr()
elif choice == "3":
    pass
elif choice == "4":
    pass
elif choice == "5":
    pass
elif choice == "6":
    search_item()
elif choice == "7":
    pass
elif choice == "8":
    pass
elif choice == "9":
    pass
elif choice == "0":
    print("Thanks for visiting My Store, Hope u'll come again.")
else:
    print("Please enter a valid number")