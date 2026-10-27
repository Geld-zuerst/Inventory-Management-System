from admin_control import admin_ctlr
from buy_product import buy_product
from utils import dashboard, search_item, stock_management


def main():
    while True:
        print("\n" + "=" * 52)
        print("           Inventory Management System")
        print("=" * 52)
        print("1. Dashboard")
        print("2. Admin Control")
        print("3. Stock Management")
        print("4. Purchase")
        print("5. Search Product")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

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
            print("\n" + "-" * 52)
            print("Thanks for visiting. Hope to see you again!")
            print("-" * 52 + "\n")
            break
        else:
            print("Please enter a valid menu number.")


if __name__ == "__main__":
    main()
