to_do_list = []
completed_list = []
previous_to_do_list = to_do_list.copy()
previous_completed_list = completed_list.copy()

while True:
    print()
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Replace an Item")
    print("4. Check Off an Item")
    print("5. Display the To-Do List")
    print("6. Display the Completed List")
    print("7. Undo the Previous Change")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        new_item = input("Enter the item to add: ")
        previous_to_do_list = to_do_list.copy()
        previous_completed_list = completed_list.copy()
        to_do_list.append(new_item)

    elif choice == "2":
        if len(to_do_list) == 0:
            print("The to-do list is empty.")
        else:
            print()
            for index in range(len(to_do_list)):
                print(f"{index + 1}. {to_do_list[index]}")
            remove_index = input("Enter the index of the item to remove: ")
            if remove_index.isdigit() and 1 <= int(remove_index) <= len(to_do_list):
                previous_to_do_list = to_do_list.copy()
                previous_completed_list = completed_list.copy()
                to_do_list.pop(int(remove_index) - 1)
            else:
                print("Invalid index.")

    elif choice == "3":
        if len(to_do_list) == 0:
            print("The to-do list is empty.")
        else:
            print()
            for index in range(len(to_do_list)):
                print(f"{index + 1}. {to_do_list[index]}")
            replace_index = input("Enter the index of the item to replace: ")
            if replace_index.isdigit() and 1 <= int(replace_index) <= len(to_do_list):
                new_value = input("Enter the new value: ")
                previous_to_do_list = to_do_list.copy()
                previous_completed_list = completed_list.copy()
                to_do_list[int(replace_index) - 1] = new_value
            else:
                print("Invalid index.")

    elif choice == "4":
        if len(to_do_list) == 0:
            print("The to-do list is empty.")
        else:
            print()
            for index in range(len(to_do_list)):
                print(f"{index + 1}. {to_do_list[index]}")
            check_index = input("Enter the index of the item to check off: ")
            if check_index.isdigit() and 1 <= int(check_index) <= len(to_do_list):
                previous_to_do_list = to_do_list.copy()
                previous_completed_list = completed_list.copy()
                completed_item = to_do_list.pop(int(check_index) - 1)
                completed_list.append(completed_item)
            else:
                print("Invalid index.")

    elif choice == "5":
        if len(to_do_list) == 0:
            print("The to-do list is empty.")
        else:
            print()
            for index in range(len(to_do_list)):
                print(f"{index + 1}. {to_do_list[index]}")

    elif choice == "6":
        if len(completed_list) == 0:
            print("The completed list is empty.")
        else:
            print()
            for index in range(len(completed_list)):
                print(f"{index + 1}. {completed_list[index]}")

    elif choice == "7":
        to_do_list = previous_to_do_list.copy()
        completed_list = previous_completed_list.copy()
        print("The last change has been undone.")

    elif choice == "8":
        break

    else:
        print("Invalid choice.")

print("Goodbye!")
