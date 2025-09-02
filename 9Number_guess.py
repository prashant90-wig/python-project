import random

def generate_num():
    return random.randint(1, 100)

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def give_hint(guess, target):
    if guess< target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def play_game():
    target = generate_num()
    attempts = 0

    print("I'm thinking of number between 1 and 100.")

    while True:
        guess = get_guess()
        attempts += 1
        hints = give_hint(guess, target)
        print(hints)
        if hints == "Correct!":
            print(f"Congratulations! You've guessed the number {target} in {attemps} attempts.")
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
