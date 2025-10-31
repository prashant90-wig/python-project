def banking_menu():
    print("\n" *1)
    print("====== XYZ BANK ======")
    print("-" * 45)
    print(f"Welcome user.")
    print("-" * 45)
    print("SERVICES")
    print("-" * 45)
    print("1. Deposit Balance")
    print("2. Withdraw ")
    print("3. Check Balance")
    print("4. Exit")
    print("-" * 45)


def deposite(balance):
    amount = float(input("Enter the deposite amount: "))
    balance += amount
    print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")
    return balance

def withdraw(balance):
    amount = float(input("Enter the withdraw amount: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrew Rs. {amount}. New balance: Rs. {balance}")
    return balance

def check_balance(balance):
    print(f"Current balance: Rs. {balance}")

def main():
    balance = 20000.0
    while True:
        banking_menu()
        choice = input("Select an option (1-3): ")
        if choice == '1':
            balance = deposite(balance)
        elif choice == '2':
            balance = withdraw(balance)
        elif choice == '3':
            check_balance(balance)
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()



        
        