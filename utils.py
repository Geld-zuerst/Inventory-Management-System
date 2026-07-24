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
        total_inventory += product["quantity"] * product["selling_price"]
    print("-"*52)
    print("\nHello Visitor, this is the Summmary of my store.")
    print(f"📂 Categories        : {len(categories)}")
    print(f"📊 Total Stock Units : {total_quantity}")
    print(f"💰 Inventory Value   : {total_inventory}")
    print("-"*52)



def see_product():
    print()
    print("=" * 75)
    print(f"{'ID':<8}{'Name':<20}{'Category':<20}{'brand':<10}{'Price':<10}{'Qty':<5}")
    print("=" * 75)
    print()

    for product_id, product in products.items():
        print(
            f"{product_id:<8}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['brand']:<10}"
            f"₹{product['selling_price']:<9}"
            f"{product['quantity']:<5}"
            )
    print("=" * 75)


def see_category():
    categories = set()
    for product in products.values():
        categories.add(product["category"])
    for category in sorted(categories):
        print(category)


def view_by_category():
    category = input("Enter Category: ").title()

    print(f"\nCategory: {category}\n")
    found = False

    print(f"{'ID':<8}{'Name':<20}{'Brand':<10}{'Price':<10}{'Qty':<5}")
    print("-" * 45)
    for product_id, product in products.items():
        if product["category"] == category:
            found = True
            print(
                f"{product_id:<8}"
                f"{product['name']:<20}"
                f"{product['brand']:<10}"
                f"₹{product['selling_price']:<9}"
                f"{product['quantity']:<5}"
            )

    if not found:
        print("No products found.")

def view_by_name():
    name = input("Enter Name of the Product: ").title()
    found = False
    print(f"\nName: {name}\n")

    for product_id, product in products.items():
        if product["name"] == name:
            found = True
            print(f"Product ID : {product_id}")
            print(f"Name       : {product['name']}")
            print(f"Category   : {product['category']}")
            print(f"Price      : ₹{product['selling_price']}")
            print(f"Quantity   : {product['quantity']}")
    if not found:
        print("No product found")

    
def search_item():
    print("\n Search Items by")
    print("0. Entering name")
    print("1. View Products")
    print("2. Via Category")
    search = input("Search by: ")
    if search == "0":
        view_by_name()
    if search == "1":
        see_product()
    if search == "2":
        see_category()
        view_by_category()

def in_stock(quantity):
    if quantity >= 10:
        return "✅ In Stock"
    elif quantity < 10 and quantity > 0:
        return "⚠ Low Stock"
    elif quantity == 0:
        return "❌ Out of Stock"

def stock_management():
    while True:
        print("="*35)
        print("         Stock Management")
        print("="*35)

        print("\n1. View All Stock")               #✅
        print("2. Restock Product")               #✅
        print("3. Reduce Stock (Damaged/Lost)")
        print("4. Low Stock Products")
        print("5. Out of Stock Products")
        print("6. Back")
        
        stc = input("\nEnter Choice: ")

        if stc == "1":
            print("-"*32)
            print("View All Stock")
            print("-"*32)
            print()
            print("=" * 75)
            print(f"{'ID':<8}{'Name':<20}{'Category':<20}{'Qty':<5}{'Stock Status':<22}")
            print("=" * 75)
            print()

            for product_id, product in products.items():
                status = in_stock(product['quantity'])
                print(
                    f"{product_id:<8}"
                    f"{product['name']:<20}"
                    f"{product['category']:<20}"
                    f"{product['quantity']:<5}"
                    f"{status:<22}"
                    )
            print("=" * 75)
        elif stc == "2":
            print("="*42)
            print()
            print("-"*32)
            print("Restock Product")
            print("-"*32)
            ID = input("\nEnter product ID (ex - Pxxx): ")
            if ID in products:
                product = products[ID]
                print("\nProduct Found")
                print(f"Name           : {product['name']}")
                print(f"Current Stock  : {product['quantity']}")

                updt = input("\nEnter Quantity to Add : ")
                try:
                    add_qty = int(updt)
                    if add_qty < 0:
                        print("\nPlease enter a non-negative number.")
                    else:
                        product['quantity'] += add_qty
                        print(f"\nNew Stock : {product['quantity']}")
                        print("\n✅ Stock Updated Successfully!")
                        print("="*42)
                except ValueError:
                    print("\nPlease enter a valid integer quantity.")
                    print("="*42)
            else:
                print("\nInvalid or Incorrect Product ID")
                print("="*42)
        elif stc == "3":
            pass
        elif stc == "4":
            pass
        elif stc == "5":
            pass
        elif stc == "6":
            break
        else:
            print("Please enter a correct formated choice")