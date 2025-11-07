# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...., nth

def menu():
    print("WELCOME TO THE HUB OF FIBONACCI SERIES")
    print("1. Fibonacci Series upto 20 terms")
    print("2. Enter the limit")
    print("3. Exit")


def display_upto_limit(limit):
    a = 0
    b = 1
    c = 1
    for i in range(1, limit):
        print(a, end = ", ")
        a = b
        b = c
        c = a + b
    print ()

def main():
    while True:
        print("\n" *2)
        print("-"*60)
        menu()
        choice = input("Enter your choice: ").strip()
        print("-"*60)
        try:
            if choice == '1':
                print("-"*60)
                display_upto_limit(20)
                print("-"*60)
                input("Press enter to continue...")
            elif choice == '2':
                limit = int(input("Enter your limit: "))
                print("-"*60)
                display_upto_limit(limit)
                print("-"*60)
                input("Press enter to continue...")
            elif choice == '3':
                print("Thanks for using this program.")
                break
            else:
                print("Please enter a valid option...")
        except ValueError:
            print("Invalid input. Input a number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()


