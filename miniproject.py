

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("✅ Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["completed"] else "❌ Not Done"
        print(f"{i}. {task['task']} - {status}")
    print()

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print("✅ Task marked as completed!\n")
    except (IndexError, ValueError):
        print("⚠ Invalid task number!\n")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"🗑 Task '{removed['task']}' deleted!\n")
    except (IndexError, ValueError):
        print("⚠ Invalid task number!\n")

def main():
    while True:
        print("==== TO-DO LIST APP ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("⚠ Invalid choice! Try again.\n")

if __name__ == "_main_":
    main()