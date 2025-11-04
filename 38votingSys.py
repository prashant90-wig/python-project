def add_candidate(votes):
    name = input("Enter candidate's name: ").strip()
    
    if not name:
        print("Candidate name cannot be empty.")
        return
    
    if name in votes:
        print("Candidate already exists.")
    else:
        votes[name] = 0
        print(f"Candidate '{name}' added.")

def cast_vote(votes):
    if not votes:
        print("No candidates available. Add candidates first.")
        return
    
    print("\nCandidates:")
    candidates = list(votes.keys())
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}. {candidate}")
    
    choice = input("Select candidate number to vote for: ")
    
    try:
        choice = int(choice)
        if 1 <= choice <= len(candidates):
            selected = candidates[choice - 1]
            votes[selected] += 1
            print(f"Vote cast for '{selected}'.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def view_results(votes):
    if not votes:
        print("No candidates yet.")
        return
    
    print("\nVoting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")


def main():
    votes = {}  
    
    while True:
        print("\n--- Voting System ---")
        print("1. Add Candidate")
        print("2. Cast Vote")
        print("3. View Results")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_candidate(votes)
        elif choice == '2':
            cast_vote(votes)
        elif choice == '3':
            view_results(votes)
        elif choice == '4':
            print("Exiting the voting system.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()