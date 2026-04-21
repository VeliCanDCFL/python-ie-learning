from inventory import (Inventory, ProductNotFoundError,
                       DuplicateProductError, InvalidQuantityError)


def print_menu() -> None:
    print("\n=== Inventory Manager ===")
    print("1. View inventory")
    print("2. Add product")
    print("3. Remove product")
    print("4. Update quantity")
    print("5. Exit")
    print("=========================")


def get_input(prompt: str, type_=str):
    while True:
        try:
            return type_(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a {type_.__name__}.")


def main():
    inventory = Inventory("week1_foundations/project/inventory.json")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            inventory.report()

        elif choice == "2":
            product_id = input("Product ID: ").strip().upper()
            name = input("Product name: ").strip()
            price = get_input("Price: ", float)
            quantity = get_input("Quantity: ", int)
            try:
                inventory.add(product_id, name, price, quantity)
            except (DuplicateProductError, InvalidQuantityError) as e:
                print(f"Error: {e}")

        elif choice == "3":
            product_id = input("Product ID to remove: ").strip().upper()
            try:
                inventory.remove(product_id)
            except ProductNotFoundError as e:
                print(f"Error: {e}")

        elif choice == "4":
            product_id = input("Product ID to update: ").strip().upper()
            quantity = get_input("New quantity: ", int)
            try:
                inventory.update(product_id, quantity)
            except (ProductNotFoundError, InvalidQuantityError) as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose between 1-5.")


if __name__ == "__main__":
    main()