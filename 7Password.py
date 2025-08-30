def check_length(password):
    if len(password) >= 8:
        return True
    else:
        return False
    
def has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_symbol(password):
    symbol = "!@#$%^&*()-+?_=,<>/"
    for char in password:
        if char in symbol:
            return True
        else:
            return False
        
def check_password():
    password = input("Enter your password:")
    password = password.strip()

    print(f"Checking password with {len(password)} characters..")

    length_ok = check_length(password)
    has_num = has_number(password)
    has_sym = has_symbol(password)

    if length_ok:
        print("Length : Good (8 or more characters)")
    else:
        print("Length : Bad (less than 8 characters)")
    if has_num:
        print("Number : Good (contains at least one number)")
    else:
        print("Number : Bad (does not contain a number)")
    if has_sym:
        print("Symbol : Good (contains at least one symbol)")
    else:
        print("Symbol : Bad (does not contain a symbol)")
    
    score = sum([length_ok, has_num, has_sym])
    print(f"Overall score: {score}/3")

    if score == 3:
        print("Strong password")
    elif score == 2:
        print("Okay password")
    else:
        print("Weak password")  

print("Welcome to the Password Checker!")
print("A strong password has: " 
"\n - 8 or more characters" 
"\n - at least one number" )

print("-"*30)

while True:
    print("\nMenu")
    print("1. Check password strength:")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        check_password()
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")