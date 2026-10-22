
TASK_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        return [task.strip() for task in tasks]

    except FileNotFoundError:
        return []

    except Exception as error:
        print("Error while reading tasks:", error)
        return []


def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    except Exception as error:
        print("Error while saving tasks:", error)


def add_task(tasks):
    task = input("Enter a new task: ").strip()

    if task == "":
        print("Task cannot be empty.")
        return

    print("\nChoose priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priorities = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    choice = input("Enter priority: ").strip()

    if choice not in priorities:
        print("Invalid priority. Please choose 1, 2, or 3.")
        return

    priority = priorities[choice]

    tasks.append(f"{task} | {priority} | Pending")
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):
        parts = task.split("|")

        task_name = parts[0].strip()

        if len(parts) == 3:
            priority = parts[1].strip()
            status = parts[2].strip()

        elif len(parts) == 2:
            priority = "Not set"
            status = parts[1].strip()

        else:
            priority = "Not set"
            status = "Pending"

        print(f"\n{index}. {task_name}")
        print(f"   Priority: {priority}")
        print(f"   Status: {status}")

def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)

        save_tasks(tasks)

        print(f"Deleted: {deleted_task}")

    except ValueError:
        print("Please enter a valid number.")

def complete_task(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to complete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_number - 1]
        parts = task.split("|")

        task_name = parts[0].strip()

        if len(parts) == 3:
            priority = parts[1].strip()
        else:
            priority = "Medium"

        if len(parts) == 3 and parts[2].strip() == "Completed":
            print("Task is already completed.")
            return

        tasks[task_number - 1] = (
            f"{task_name} | {priority} | Completed"
        )

        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")
        
def search_task(tasks):
    keyword = input("Enter task name to search: ").strip().lower()

    if keyword == "":
        print("Search cannot be empty.")
        return

    found = False

    for index, task in enumerate(tasks, start=1):
        if keyword in task.split("|")[0].strip().lower():
            print(f"{index}. {task}")
            found = True

    if not found:
        print("No matching task found.")


