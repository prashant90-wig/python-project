def make_space():
    print("\n" * 2)

def make_line():
    print("-" * 40)

def menu():
    print("Welcome to LEAP YEAR FINDER")
    print("Enter a year to check between 1900 and 2099. We will find the leap year for you!")
    print("A year is a leap year if it is divisible by 4 but not by 100, unless it is also divisible by 400.")
    print("1. Check leap year for a specific year")
    print("2. View all leap years between 1900 and 2099")
    print("3. Exit")

def year_input():
    while True:
        try:
            year = int(input("Enter a year (1900-2099):"))
            if 1900 <= year <= 2099:
                return year
            else:
                print("Year must be between 1900 and 2099. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def leap_year_range():
    print("For instance leap years between 1900 and 2099:")
    leap_years = [y for y in range(1900, 2099)
                  if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
    
    for i, year in enumerate(leap_years, start = 1):
        print(f"{year}", end = "\t")
        if i % 10 == 0:
            print()

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def main():
    while True:
        make_space()
        make_line()
        menu()
        make_line()
        choice = input("Choose an option (1-3): ")
        make_line()
        if choice == '1':
            make_line()
            year = year_input()
            make_space()
            is_leap_year(year)
            make_line()
            input("Press Enter to continue...")
        elif choice == '2':
            make_line()
            leap_year_range()
            make_line()
            input("Press Enter to continue...")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
