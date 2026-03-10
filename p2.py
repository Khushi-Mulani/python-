# Initialize empty list
tasks = []

def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def mark_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task {task_index + 1} marked complete.")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")

# Example usage
add_task("Buy milk")
add_task("Finish project")
mark_completed(0)
view_tasks()
