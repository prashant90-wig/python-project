def make_line():
    print("-" * 40)

def make_space():
    print("\n" * 2)

def menu():
    print("SIMPLE PRIME NUMBER GENERATOR")
    make_line()
    print("1. Check if a number is prime")
    print("2. View all prime numbers up to a specified limit")
    print("3. Exit")
    
def get_prime_input():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num > 1:
                return num
            else:
                print("Number must be greater than 1. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def get_limit_input():
    while True:
        try:
            limit = int(input("Enter the upper limit ( greater than 1 ): "))
            if limit > 1:
                return limit
            else:
                print("Limit must be greater than 1. Please try again.")
        except ValueError:  
            print("Invalid input. Please enter a valid positive integer.")

def disp_limit_primes(limit):
    for i in range(2, limit + 1, 3):
        if is_prime(i):
            print(i, end = "\t")
    print()
    

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        make_space()
        make_line()
        menu()
        choice = input("Choose an option (1-3): ")
        make_line()
        if choice == '1':
            make_space()
            n = get_prime_input()
            if is_prime(n):
                print(f"{n} is a prime number.")
            else:
                print(f"{n} is not a prime number.")
            make_line()
            input("Press Enter to continue...")

        elif choice == '2':
            make_space()
            lim = get_limit_input()
            if disp_limit_primes(lim):
                return True
            make_line()
            input("Press Enter to continue...")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            return
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()