# add_task.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

if __name__ == "__main__":
    while True:
        task = input("Enter a task (or 'exit' to quit): ")
        if task.lower() == 'exit':
            break
        add_task(task)
        print(f"Current tasks: {tasks}")

