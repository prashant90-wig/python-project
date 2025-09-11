import datetime

def make_space():
    print("\n" *2)

def menu():
    print("===== JOURNAL MENU =====")
    print("1. Write a new journal")
    print("2. Read all journal")
    print("3. Exit")
    print(f"{"=" *40}")
    choice = input("Enter your choice (1/2/3) :")
    return choice
    

def write_journal():
    entry = input("Write your journal entry:\n")
    now = datetime.datetime.now()
    
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as file:
        file.write(f"{timestamp} - {entry}\n")
    print("Entry saved!\n")
    input("\nPress Enter to continue...")

def read_journal():
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            if content:
                print("\n Your Diary Entries : \n")
                print(content)
            else:
                print("No entries yet!!!")
            input("\nPress Enter to continue...")

    except FileNotFoundError:
        print("No journal file found. Start writing your first journal right now!")

def main():
    while True:
        make_space()
        choice = menu()
        if choice == "1":
            make_space()
            write_journal()
        elif choice == "2":
            make_space()
            read_journal()
        else:
            print("Goodbye! Keep Journaling till death!!!")
            make_space()
            break
        
if __name__ == "__main__":
    main()

    