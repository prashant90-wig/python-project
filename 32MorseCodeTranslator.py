def make_space():
    print("\n" * 2)

def make_line():
    print("-" * 40) 

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

def menu():
    print("====== MORSE CODE TRANSLATOR ======")
    print("1. Convert Text to Morse Code")
    print("2. Exit")

def get_text_input():
    text = input("Enter text to convert to Morse code: ")
    return text.upper()

def text_to_morse(text):
    try:
        morse_code = []
        for char in text:
            if char in morse_code_dict:
                morse_code.append(morse_code_dict[char])
            else:
                morse_code.append(char)
        return ' '.join(morse_code)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def main():
    while True:
        make_space()
        make_line()
        menu()
        make_line()
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            make_space()
            make_line()
            text = get_text_input()
            morse_code = text_to_morse(text)
            print(f"Morse Code: {morse_code}")
            make_space()
            make_line()
            input("Press Enter to continue...")

        elif choice == '2':
            make_space()
            print("Exiting the program. Goodbye!")
            make_line()
            break
        else:
            print("Invalid choice. Please try again.")
            make_space()    

if __name__ == "__main__":
    main()

