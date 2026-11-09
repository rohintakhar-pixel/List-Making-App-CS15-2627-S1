item_list = []
previous_list = item_list.copy()

while True:
    print()
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo the Previous Change")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_item = input("Enter the item to add: ")
        previous_list = item_list.copy()
        item_list.append(new_item)

    elif choice == "2":
        if len(item_list) == 0:
            print("The list is empty.")
        else:
            print()
            for index in range(len(item_list)):
                print(f"{index + 1}. {item_list[index]}")
            remove_index = input("Enter the index of the item to remove: ")
            if remove_index.isdigit() and 1 <= int(remove_index) <= len(item_list):
                previous_list = item_list.copy()
                item_list.pop(int(remove_index) - 1)
            else:
                print("Invalid index.")

    elif choice == "3":
        if len(item_list) == 0:
            print("The list is empty.")
        else:
            print()
            for index in range(len(item_list)):
                print(f"{index + 1}. {item_list[index]}")

    elif choice == "4":
        item_list = previous_list.copy()
        print("The last change has been undone.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")

print("Goodbye!")
