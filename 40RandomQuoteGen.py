import random

quotes = [
    "Education is a powerful weapon that you can use to change the world - Nelson Mandela",
    "Every person you meet is fighting a battle you know nothing about, always be kind - Anonymous",
    "Life is like a box of chocolates, full of surprises - Forrest Gump",
    "Boil things down to the most fundamental truths... and reason up from there - Elon Musk",
    "Work harder, Nobody cares - David Goggins",
    "I don't ever give up. I'd have to be dead or completely incapacitated. - Elon Musk",
    "When something is important enough, you do it even if the odds are not in your favor. - Elon Musk"
]

def get_random_quote():
    return random.choice(quotes)

def main():
    try:
        while True:
            print("="*45)
            print("\n"*2)
            print("QUOTE GENERATOR")
            print("\n")
            selected_quote = get_random_quote()
            print(f"{selected_quote}")
            print("\n"*2)
            input("Press enter for next amazing quote... or, press Ctrl + C for exit.")        
            print("="*45)
    except KeyboardInterrupt:
        print("Stay Hungry!!!")



if __name__ == "__main__":
    main()

