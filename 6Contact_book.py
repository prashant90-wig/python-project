def menu():
    print("\nCONTACT BOOK MENU")
    print("1. Add a contact.")
    print("2. View contacts.")
    print("3. Remove a contact.")
    print("4. Exit.")
    print("-" * 30)

def add_contact(contacts):
    name = input("Enter contact name: ")

    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {
        "phone" : phone,
        "email": email
    }

def view_contacts(contacts):
    if len(contacts) == 0:
        print("\nNo contacts yet!")
    else:
        print("\nYour contacts:")
        print("-" * 30)
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 30)

def remove_contact(contacts):
    name = input("Enter the name to remove: ")
    if name in contacts:
        remove_contact = contacts.pop(name)
        print(f"Contact {name} removed!")
    else:
        print("Contact not found!")

def main():
    contacts = {}

    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            remove_contact(contacts)
        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-4).")
            input("Press Enter to continue...")
if __name__=="__main__":
    main()
