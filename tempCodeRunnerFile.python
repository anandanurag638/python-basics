# Simple Command-Line To-Do List App (Non-Interactive Mode for Sandbox)

tasks = []

def add_task(task):
    if task.strip():
        tasks.append(task)
        return f"Task added: {task}"
    return "Task cannot be empty!"

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return f"Removed task: {removed}"
    return "Invalid task number!"

def clear_tasks():
    tasks.clear()
    return "All tasks cleared!"

def list_tasks():
    if tasks:
        return "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
    return "Your to-do list is empty!"

def execute_command(command, arg=None):
    commands = {
        "add": lambda: add_task(arg) if arg else "Task content required!",
        "remove": lambda: remove_task(int(arg) - 1) if arg and arg.isdigit() else "Valid task number required!",
        "list": list_tasks,
        "clear": clear_tasks,
        "exit": lambda: "Exiting the to-do list app. Goodbye!"
    }
    return commands.get(command, lambda: "Invalid command!")()

# Example Usage (Replace with function calls in a real-world app):
if __name__ == "__main__":
    print(execute_command("add", "Buy groceries"))
    print(execute_command("add", "Complete homework"))
    print(execute_command("list"))
    print(execute_command("remove", "1"))
    print(execute_command("list"))
    print(execute_command("clear"))
    print(execute_command("list"))
    print(execute_command("exit"))
