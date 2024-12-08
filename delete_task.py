# delete_task.py
tasks = {"Delete Task Example"

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task deleted: {task}")
    else:
        print(f"Task not found: {task}")

if __name__ == "__main__":
    while True:
        task = input("Enter a task to delete (or 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        delete_task(task)
        print(f"Current tasks: {tasks}")

