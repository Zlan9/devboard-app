tasks = [] def display_tasks(): if not tasks: print("[task]No tasks yet.") for i, task in enumerate(tasks, 1): print(f" {i}. {task}")

def delete_task(task_index): if 0 <= task_index < len(tasks): removed = tasks.pop(task_index) print(f"🗑️ Removed: {removed}") else: print("Invalid task index.")
