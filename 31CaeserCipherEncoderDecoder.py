# Caeser Cipher was one of the earliest and simplest methods of encryption technique.
# It is a type of substitution cipher in which each letter in the plain text is shifted n times down the alphabet.

def make_space():
    print("\n" * 2)

def make_line():
    print("-" * 50)

def menu():
    print("======= CAESER CIPHER ENCODER/DECODER =======")
    make_space()
    print("Choose an option:")
    print("1. Encode Text")
    print("2. Decode Text")
    print("3. Exit")

def get_input():
    while True:
        try:
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value (number): "))
            if 0 <= shift < 26:
                return text, shift 
            else:
                print("Shift value must be between 0 and 25. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer for shift value.")
            


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        make_space()
        make_line()
        menu()
        make_line()
        choice = input("Enter your choice (1-3) :  ")
        if choice == '1':
            text, shift = get_input()
            encoded_text = encrypt(text, shift)
            make_space()
            print(f"Encoded Text: {encoded_text}")
            input("Press Enter to continue...")

        elif choice == '2':
            text, shift = get_input()
            decoded_text = decrypt(text, shift)
            make_space()
            print(f"Decoded Text: {decoded_text}")
            input("Press Enter to continue...")

        elif choice == '3':
            make_space()
            print("Thank you for using the Ceaser Cipher Encoder/Decoder!")
            make_space()
            break

if __name__ == "__main__":
    main()


