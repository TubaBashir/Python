def list_playground():
    # 1. Start with an initial list
    my_list = ["apple", "banana", "cherry"]
    
    while True:
        # Display the current state of the list
        print("\n" + "="*40)
        print(f" Current List: {my_list}")
        print(f" Total Items:  {len(my_list)}")
        print("="*40)
        
        # Display options menu
        print("What do you want to do with the list?")
        print("1. Append an item (add to end)")
        print("2. Insert an item (add at specific index)")
        print("3. Remove an item (by name)")
        print("4. Pop an item (remove by position)")
        print("5. Sort the list alphabetically")
        print("6. Reverse the list")
        print("7. Slice the list (view a subset)")
        print("8. Clear the entire list")
        print("9. Exit")
        
        choice = input("\nEnter choice (1-9): ").strip()
        
        try:
            if choice == "1":
                item = input("Enter item name to append: ")
                my_list.append(item)
                print(f"👍 Added '{item}' to the end.")
                
            elif choice == "2":
                idx = int(input(f"Enter index position (0 to {len(my_list)}): "))
                item = input("Enter item name to insert: ")
                my_list.insert(idx, item)
                print(f"👍 Inserted '{item}' at position {idx}.")
                
            elif choice == "3":
                item = input("Enter item name to remove: ")
                if item in my_list:
                    my_list.remove(item)
                    print(f"🗑️ Removed '{item}' from the list.")
                else:
                    print(f"❌ '{item}' is not in the list.")
                    
            elif choice == "4":
                if not my_list:
                    print("❌ List is already empty.")
                    continue
                idx = int(input(f"Enter position to pop (0 to {len(my_list)-1}): "))
                removed = my_list.pop(idx)
                print(f"🗑️ Popped '{removed}' out of position {idx}.")
                
            elif choice == "5":
                my_list.sort()
                print("🔤 List sorted alphabetically.")
                
            elif choice == "6":
                my_list.reverse()
                print("🔄 List order reversed.")
                
            elif choice == "7":
                print(f"Valid range is 0 to {len(my_list)}")
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(f"✂️ Slice subset: {my_list[start:end]}")
                
            elif choice == "8":
                confirm = input("Are you sure you want to clear everything? (y/n): ")
                if confirm.lower() == 'y':
                    my_list.clear()
                    print("🧹 List cleared entirely.")
                    
            elif choice == "9":
                print("Thanks for playing in the sandbox! Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 9.")
                
        except ValueError:
            print("❌ Input error. Please enter a valid number for index positions.")
        except IndexError:
            print("❌ Index out of range. That position doesn't exist in your list.")

if __name__ == "__main__":
    list_playground()
