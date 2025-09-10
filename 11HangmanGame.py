import random

HANGMAN_PICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    ========''','''
    +---+
    |   |
    O   |
        |
        |
        |
    ========''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ========''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ========''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ========''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========''']

words = ['NARUTO_UZUMAKI', 'GOKU', 'SASUKE', 'KURAMA', 'MONKEY_D_LUFFY', 'ZORO',
         'SANJI', 'GOJO', 'SUKUNA', 'KAKASHI', 'TANJIRO', 'SAITAMA']

def get_random_word(word_list):
    return random.choice(word_list)

def play_game():

    secret_word = get_random_word(words)
    guessed_letters = []
    tries = 6
    print("=============================== Welcome to Hangman! =============================== ")
    print("I am thinking of a word. Can you guess it?")
    print("[Hint: Maybe name of one of your favourite anime...]")

    while tries > 0:
        print("\n" + HANGMAN_PICS[ 6 - tries])

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)
        print(f"You have {tries} incorrect guesses left.")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        if "_" not in display_word:
            print(f"\n Congratulations!!! You guessed the '{secret_word}' correctly! ")
            break

        guess = input("Guess a letter :").upper().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please ennter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter! Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"God guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            tries -= 1
            
    if tries == 0:
        print("\n"+ HANGMAN_PICS[6])
        print("Game Over! You ran out of tries...")
        print(f"The secret word was: {secret_word}")

if __name__ == "__main__":
    play_game()