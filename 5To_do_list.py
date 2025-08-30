def show_menu():
    print("Todo List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("-" * 30)

def add_task(task_list):
    print("\nADD A NEW TASK")
    new_task = input("Enter your task:")

    if new_task.strip():
        task_list.append(new_task)
        print(f'Task "{new_task}" added successfully!')
        print(f"Total Tasks: {len(task_list)}")
    else:
        print("Task cannot be empty!")

    input("Press Enter to continue...")
    
def view_tasks(task_list):
    print("\n YOUR TASKS")

    if len(task_list) == 0:
        print("No tasks yet! Add some tasks to get started!")
    else:
        print(f"You have {len(task_list)} task(s):")
        print("-" * 30)

    for i in range(len(task_list)):
        print(f"{i+1}. {task_list[i]}")

    input("\nPress enter to continue...")

def remove_task(task_list):

    pass

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("-" * 30)
            print("Exiting the Todo List App. Goodbye!!!")
            break
        else:
            print("Invalid choice! Please choose a valid option (1-4).")
            input("Press Enter to continue...")

main()
