import random

def roll_dice(num_dice, num_sides):
    result = []
    for i in range(num_dice):
        roll = random.randint(1, num_sides)
        result.append(roll)
    return result

def display_results(rolls):
    print(f"You rolled: {rolls}")
    print(f"Total: {sum(rolls)}")

def main():
    print("WELCOME TO THE DICE ROLLER!")

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (or 0 to quit): "))
            if num_dice == 0:
                print("Thanks for playing!")
                break
            else:
                num_sides = int(input("Enter the number of sides on each die: "))
                rolls = roll_dice(num_dice, num_sides)
                display_results(rolls)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()