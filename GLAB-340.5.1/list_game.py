import random

def generate_target_list(starting_list):
    target_list = starting_list.copy()
    random.shuffle(target_list)
    return target_list

def display_lists(current_list, target_list):
    print("\nCurrent List:", current_list)
    print("Target List:", target_list)

def modify_list(current_list):
    while True:
        print("\nChoose an operation:")
        print("1. Append a word")
        print("2. Extend with another list")
        print("3. Concatenate two elements")
        print("4. Traverse and view elements")
        print("5. Modify an element")
        print("6. Insert an element")
        print("7. Pop an element")
        print("8. Remove a specific element")
        print("9. Sort the list")
        print("10. Exit and check result")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == "1":
            word = input("Enter a word to append: ")
            current_list.append(word)
        elif choice == "2":
            words = input("Enter words separated by spaces: ").split()
            current_list.extend(words)
        elif choice == "3":
            i, j = map(int, input("Enter two indices to concatenate (space-separated): ").split())
            if 0 <= i < len(current_list) and 0 <= j < len(current_list):
                current_list[i] += current_list[j]
                del current_list[j]
        elif choice == "4":
            print("\nTraversing list:")
            for i, word in enumerate(current_list):
                print(f"{i}: {word}")
        elif choice == "5":
            index = int(input("Enter the index to modify: "))
            if 0 <= index < len(current_list):
                new_word = input("Enter the new word: ")
                current_list[index] = new_word
        elif choice == "6":
            index = int(input("Enter the index to insert at: "))
            word = input("Enter the word: ")
            if 0 <= index <= len(current_list):
                current_list.insert(index, word)
        elif choice == "7":
            index = int(input("Enter the index to pop: "))
            if 0 <= index < len(current_list):
                current_list.pop(index)
        elif choice == "8":
            word = input("Enter the word to remove: ")
            if word in current_list:
                current_list.remove(word)
        elif choice == "9":
            order = input("Enter 'asc' for ascending or 'desc' for descending: ")
            current_list.sort(reverse=(order == "desc"))
        elif choice == "10":
            break
        else:
            print("Invalid choice, try again.")
        
        display_lists(current_list, target_list)
    
    return current_list

# Initialize the game
starting_list = ["apple", "banana", "cherry", "date", "fig"]
target_list = generate_target_list(starting_list)

display_lists(starting_list, target_list)

# Start modifying the list
final_list = modify_list(starting_list.copy())

# Check if the user wins
if final_list == target_list:
    print("\nCongratulations! You matched the target list!")
else:
    print("\nGame Over! You didn't match the target list.")
