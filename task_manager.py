
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

task_name = input("Enter a task: ")
add_task(task_name)

print("Your tasks:", tasks)
