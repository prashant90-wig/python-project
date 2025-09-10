# Quiz Game (5 MCQs with Score)

# 1. Data Structure - Questions Database
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which is the highest peak in the world?",
        "options": ["A) Mt. Everest", "B) Kailash Parbat", "C) Kanchanjungha", "D) Annapurna"],
        "answer": "A"
    },
    {
        "question": "Which is the largest organ in the human body?",
        "options": ["A) Bone", "B) Eye", "C) Heart", "D) Skin"],
        "answer": "D"
    },
    {
        "question": "Where was Gautam Buddha born?",
        "options": ["A) India", "B) Sri Lanka", "C) Nepal", "D) America"],
        "answer": "C"
    },
    {
        "question": "Which of the following year is associated to the term 'Gen-Z'?",
        "options": ["A) 1990 - 2010", "B) 2010 - 2015", "C) 2024 - 2034", "D) 1980 - 1990"],
        "answer": "A"
    }
]

# 2. User Interface Functions
def clear_screen():
    """Clear the console for better readability."""
    print("\n" * 2)

def show_menu():
    """Display the main menu of the quiz game."""
    clear_screen()
    print("=" * 40)
    print("Welcome to the Quiz Game!")
    print("=" * 40)
    print("1. Start Quiz")
    print("2. View High Score")
    print("3. Exit")
    print("-" * 40)

def get_menu_choice():
    """Get and validate menu choice."""
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice! Please enter 1, 2, or 3.")

# 3. Quiz Logic Functions
def display_question(question, question_num):
    """Display a single question and its options."""
    clear_screen()
    print(f"Question {question_num}/{len(questions)}")
    print("-" * 40)
    print(question["question"])
    print()
    for option in question["options"]:
        print(option)
    print("-" * 40)

def get_answer():
    """Get and validate the user's answer."""
    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Invalid input! Please enter A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    """Check if the answer is correct."""
    return user_answer == correct_answer

# 4. Game Flow Functions
def play_single_question(question, question_num):
    """Handle the flow for a single question."""
    display_question(question, question_num)
    user_answer = get_answer()
    is_correct = check_answer(user_answer, question["answer"])
    
    if is_correct:
        print("\n Correct! Well done!")
        return 1
    else:
        print(f"\n Wrong! The correct answer was {question['answer']}")
        return 0

def play_quiz():
    """Main quiz game flow."""
    score = 0
    total_questions = len(questions)
    
    print("\nStarting Quiz!")
    print(f"There are {total_questions} questions.")
    input("Press Enter to begin...")
    
    for i, question in enumerate(questions, 1):
        score += play_single_question(question, i)
        if i < total_questions:  # Don't wait after last question
            input("\nPress Enter for next question...")
    
    clear_screen()
    print("=" * 40)
    print("Quiz Complete!")
    print(f"Your Final Score: {score}/{total_questions}")
    if score == total_questions:
        print(" Perfect Score! Amazing!")
    elif score >= total_questions * 0.8:
        print(" Great job!")
    elif score >= total_questions * 0.6:
        print(" Good effort!")
    else:
        print(" Keep practicing!")
    print("=" * 40)
    
    return score

def view_high_score():
    """Display the high score (can be expanded to save scores)."""
    clear_screen()
    print("=" * 40)
    print("High Scores Feature Coming Soon!")
    print("=" * 40)
    input("\nPress Enter to continue...")

# 5. Main Program
def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = get_menu_choice()
        
        if choice == '1':
            play_quiz()
        elif choice == '2':
            view_high_score()
        else:  
            clear_screen()
            print("Thanks for playing! Goodbye! ")
            break
        
        input("\nPress Enter to continue...")

# 6. Program Entry Point
if __name__ == "__main__":
    main()
