
from task_utils import load_tasks
from task_utils import add_task
from task_utils import view_tasks
from task_utils import delete_task
from task_utils import complete_task 
from task_utils import search_task


def show_menu():
    print("\n========== TASK MANAGER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Completed")
    print("5. Search Task")
    print("6. Exit")


def main():

    tasks = load_tasks()

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            complete_task(tasks) 

        elif choice == "5":
            search_task(tasks)

        elif choice == "6":
            print("Thank you for using Task Manager.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()