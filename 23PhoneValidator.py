
def get_number():
    phone_number = input("Enter your phone number (+977): ").strip()
    return phone_number

def check_number(phone_number):
    if len(phone_number) != 14:
        print(f"Error: Length should be 14, but got {len(phone_number)}")
        return False
    
    if not phone_number.startswith("+977"):
        print("Error: Number should start with +977")
        return False
    
    remaining_digits = phone_number[4:]

    if not remaining_digits.isdigit():
        print("Error: The 10 digits after +977 should be numbers only!")
        return False
    
    return True
    

def main():
    num = get_number()

    if check_number(num):
        print("Yes it is Nepali Number.")
    else:
        print("No It isn't Nepali Number!")


if __name__ == "__main__":
    main()