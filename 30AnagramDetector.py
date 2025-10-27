def make_space():
    print("\n" * 2)

def make_line():
    print("-" * 50)

def get_input():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    return word1, word2

def is_anagram(w1, w2):
    clean1, clean2 = w1.replace(" ", "").lower() ,w2.replace(" ", "").lower()
    return sorted(clean1) == sorted(clean2)
        

def main():
    make_space()
    make_line()
    print("======= ANAGRAM DETECTOR =======")
    make_line()
    word1, word2 = get_input()
    make_space()
    if is_anagram(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams.')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams.')
    make_space()
    make_line()
    print("Thank you for using the Anagram Detector!")
    make_line()

if __name__ == "__main__":
    main()


