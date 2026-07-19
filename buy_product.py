from inventory import products

def buy_product():
    while True:
        print("="*35)
        print("           Buy Product            ")
        print("="*35)

        print("\nSearch Product by: ")
        print("1. Product ID")
        print("2. Product Name")
        print("3. Back")
        input1 = int(input("Enter Choice: "))

        if input1 == 1:
            input2 = input("Enter product ID (ex - Pxxx): ")
            found = False

            for product_id, product in products.items():
                if product_id == input2:
                    found = True
                    print("-" * 35)
                    print("Product Found")
                    print("-" * 35)
                    print(f"Product ID : {product_id}")
                    print(f"Name       : {product['name']}")
                    print(f"Category   : {product['category']}")
                    print(f"Price      : {product['selling_price']}")
                    print(f"Available  : {product['quantity']}")
                    print("-"*35)
                    amount = input("\nEnter quantity to buy: ")
                    print()
                    print("-"*35)
                    print("Order Summary")
                    print("-"*35)
                    print(f"Product      : {product['name']}")
                    print(f"Unit Price   : {product['selling_price']}")
                    print(f"Quantity     : {amount}")
                    print(f"Total amount : {product['selling_price'] * int(amount)}")
                    print("-"*35)
                    confirmation = input("\nConfirm Purchase?(Y/N) ").title()
                    print()
                    print("\n✅ Purchase Successful!")
                    print()
            if not found:
                print("No product found")


        



        if input1 == 2:
            input3 = input("\nEnter product Name: ").title()
            found = False

            for product_id, product in products.items():
                if product["name"] == input3:
                    found = True
                    print("-" * 35)
                    print("Product Found")
                    print("-" * 35)
                    print(f"Product ID : {product_id}")
                    print(f"Name       : {product['name']}")
                    print(f"Category   : {product['category']}")
                    print(f"Price      : {product['selling_price']}")
                    print(f"Available  : {product['quantity']}")
                    print("-"*35)
                    amount = input("\nEnter quantity to buy: ")
                    print()
                    print("-"*35)
                    print("Order Summary")
                    print("-"*35)
                    print(f"Product      : {product['name']}")
                    print(f"Unit Price   : {product['selling_price']}")
                    print(f"Quantity     : {amount}")
                    print(f"Total amount : {product['selling_price'] * int(amount)}")
                    print("-"*35)
                    confirmation = input("\nConfirm Purchase?(Y/N) ").title()
                    print()
                    print("\n✅ Purchase Successful!")
                    print()
                if not found:
                    print("No product found")
        if input == 3:
            break