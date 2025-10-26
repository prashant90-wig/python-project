# This is a palindrom checker program which checks whether the given string or number is a palindrome or not.

def make_space():
    print("\n" * 2)

def make_line():
    print("-" * 45)

def menu():
    print("======= PALINDROME CHECKER =======")
    print("1. Check Palindrome for String")
    print("2. Check Palindrome for Number")
    print("3. Exit")

def get_user_input_number():
    while True:
        try:
            num_input = int(input("Enter a number to check: "))
            return num_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_input_string():
            string_input = (input("Enter a word to check: "))
            return string_input

def is_palindrome_for_string(string_input):
    cleaned = string_input.replace(" ", "").lower()
    if cleaned == cleaned[::-1]:
        print(f'"{string_input}" is a palindrome.')
    else:
        print(f'"{string_input}" is not a palindrome.')

def is_palindrome_for_number(num_input):
    if str(num_input) == str(num_input)[::-1]:
        print(f'{num_input} is a palindrome.')
    else:
        print(f'{num_input} is not a palindrome.')

def main():
    while True:
        make_space()
        make_line()
        menu()
        make_line()
        choice = input("Select an option (1-3): ")
        if choice == '1':
            make_space()
            make_line()
            string_input = get_user_input_string()
            is_palindrome_for_string(string_input)
            make_line()
            input("Press Enter to continue...")
        elif choice == '2':
            make_space()
            make_line()
            num_input = get_user_input_number()
            is_palindrome_for_number(num_input)
            make_line()
            input("Press Enter to continue...")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

