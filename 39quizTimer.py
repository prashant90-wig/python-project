quiz = [
    {"q": "What is the capital of France?", "a": ["Berlin", "Madrid", "Paris", "Rome"], "correct": "Paris"},
    {"q": "What is 2 + 2?", "a": ["3", "4", "5", "6"], "correct": "4"},
    {"q": "What is the largest planet in our solar system?", "a": ["Earth", "Jupiter", "Mars", "Saturn"], "correct": "Jupiter"}
]

import time

def quiz_timer(seconds):
    start = time.time()
    answer = input(f"You have {seconds} seconds to answer: ")
    end = time.time()
    if end - start > seconds:
        print("Time's up!")
        return None
    return answer

def ask_question(q_data):
    print("\n" + q_data["q"])
    for i, option in enumerate(q_data["a"], start=1):
        print(f"{i}. {option}")

    user_answer = quiz_timer(30)
    if user_answer is None:
        return False 

    if user_answer.isdigit():
        idx = int(user_answer) - 1
        if 0 <= idx < len(q_data["a"]):
            selected = q_data["a"][idx]
        else:
            print("Invalid choice.")
            return False
    else:
        selected = user_answer.strip().title()

    if selected == q_data["correct"]:
        print(" Correct!")
        return True
    else:
        print(f" Wrong! The correct answer was: {q_data['correct']}")
        return False

def main():
    print("Welcome to the Quiz App!")
    score = 0

    for q_data in quiz:
        if ask_question(q_data):
            score += 1

    print("\nQuiz complete!")
    print(f"Your final score: {score}/{len(quiz)}")

if __name__ == "__main__":
    main()
