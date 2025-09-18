def make_space():
    print("\n" * 2)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found. 404")
        return None
    

def count_words(text):
    words = text.split()
    return len(words)


def show_longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def count_characters(text):
    return len(text)


def main():
    make_space()
    print("=" * 40)
    print("Welcome to the Word Counter!")
    print("=" * 40)
    make_space()
    filename = input("Please enter the filename: ")
    content = read_file(filename)
    if content:
        word_count = count_words(content)
        make_space()
        print(f"This file has {word_count} words.")
        longest_word = show_longest_word(content)
        make_space()
        print(f"The longest word is: {longest_word}")
        char_count = count_characters(content)
        make_space()
        print(f"This file has {char_count} characters.")
    else:
        print("Couldn't read the file.")

if __name__ == "__main__":
    main()