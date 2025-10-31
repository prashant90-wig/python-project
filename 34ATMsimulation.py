users = {
    '1234' : {'name': 'Jack Doe', 'balance': 5000.0},
    '5678' : {'name': 'Jane Smith', 'balance': 10000.0},
    '9101' : {'name': 'Alice Johnson', 'balance': 7500.0}
}

def authenticate_user():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin in users:
            print(f"Welcome {users[pin]['name']}!")
            return pin
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid PIN. You have {attempts} attempts left.")
            else:
                print("Too many incorrect attempts. Account locked.")
                return None
    return None

def banking_menu(authenticated_pin):
    print("\n" *1)
    print("====== XYZ BANK ATM SERVICE ======")
    print("-" * 45)
    print(f"Welcome {users[authenticated_pin]['name']}.")
    print("-" * 45)
    print("SERVICES")
    print("-" * 45)
    print("1. Deposit Balance")
    print("2. Withdraw ")
    print("3. Check Balance")
    print("4. Exit")
    print("-" * 45)

def deposite(pin):
    amount = float(input("Enter the deposit amount: "))
    users[pin]['balance'] += amount
    print(f"Deposited Rs. {amount}. New balance: Rs. {users[pin]['balance']}")
    

def withdraw(pin):
    amount = float(input("Enter the withdraw amount: "))
    if amount > users[pin]['balance']:
        print("Insufficient balance.")
    else:
        users[pin]['balance'] -= amount
        print(f"Withdrew Rs. {amount}. New balance: Rs. {users[pin]['balance']}")
   

def check_balance(pin):
    print(f"Current balance: Rs. {users[pin]['balance']}")

def main():
    while True:
        pin = authenticate_user()
        if pin:
            while True:
                banking_menu(pin)
                choice = input("Select an option (1-4): ")
                if choice == '1':
                    deposite(pin)
                elif choice == '2':
                    withdraw(pin)
                elif choice == '3':
                    check_balance(pin)
                elif choice == '4':
                    print("Thank you for banking with us. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
    
if __name__ == "__main__":
    main()

    
