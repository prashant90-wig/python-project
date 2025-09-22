def get_email():
    email = input("Enter your email :").strip()
    return email

def check_email_structure(email):
    if not email.endswith(("@gmail.com" ,  "@yahoo.com" , "@outlook.com")):
        print("Your email is invalid. It should contain @gmail.com / @yahoo.com / @outlook.com")
        return False
    
    if email.count("@") != 1:
        print("Your email should contain exactly one @ symbol.")
        return False
    username, domain = email.split("@")

    if not username:
        print("Your email should have a username before @.")
        return False
    
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIVKLMNOPQRSTUVWXYZ1234567890._")
    if not all(char in valid_chars for char in username):
        print("Username can only contain letters, numbers, dots, and underscores")
        return False
    
    if not 1 <= len(username) <= 30:
        print("Username should be between 1 and 30 characters.")
        return False
    
    return True

def main():
    email_get = get_email()

    if check_email_structure(email_get):
        print(f"Your email {email_get} with {len(email_get)} characters is accepted.")
    else:
        print("Your email is invalid!")

if __name__ == "__main__":
    main()