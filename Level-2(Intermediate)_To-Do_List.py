#TO-DO LIST
#Name:Soham Majumder

#importing the required libraries and dependencies
import json
#creating the functions
def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)
def main():
    tasks = load_tasks()
    while True:
        print("\n---To-Do List---")
        #this is the options that the user can perform 
        print("1. Add Tasks\n2. Show Tasks\n3. Mark Tasks as Completed\n4. Delete Task\n5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            n_tasks = int(input("\nHow many tasks do you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
            save_tasks(tasks)

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task deleted!")
                save_tasks(tasks)
            else:
                print("Invalid task number.")

        elif choice == '5':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
