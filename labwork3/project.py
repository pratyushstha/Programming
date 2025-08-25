def add_task(task_list, task_name):
  new_task = {"name": task_name, "completed": False}
  return task_list + [new_task]

def list_incomplete_tasks(task_list):
  return list(filter(lambda task: not task["completed"], task_list))

def mark_all_completed(task_list):
  return list(map(lambda task: {"name": task["name"], "completed": True}, task_list))

def search_tasks(task_list, keyword):
  return list(filter(lambda task: keyword.lower() in task["name"].lower(), task_list))

def display_tasks(title, task_list):
  print(f"--- {title} ---")
  if not task_list:
    print("No tasks to show.")
  else:
    for i, task in enumerate(task_list, 1):
      status = "✓" if task["completed"] else "✗"
      print(f"{i}. [{status}] {task['name']}")
  print("-" * (len(title) + 6) + "\n")


if __name__ == "__main__":
  my_tasks = []
  print("Starting with an empty task list.\n")

  my_tasks = add_task(my_tasks, "Buy groceries")
  my_tasks = add_task(my_tasks, "Complete the Python assignment")
  my_tasks = add_task(my_tasks, "Go for a run")
  my_tasks = add_task(my_tasks, "Call the bank")

  display_tasks("All Current Tasks", my_tasks)

  incomplete = list_incomplete_tasks(my_tasks)
  display_tasks("Incomplete Tasks (using filter)", incomplete)

  search_results = search_tasks(my_tasks, "python")
  display_tasks("Search Results for 'python' (using filter)", search_results)

  my_tasks = mark_all_completed(my_tasks)
  display_tasks("All Tasks Marked as Completed (using map)", my_tasks)

  incomplete_after_update = list_incomplete_tasks(my_tasks)
  display_tasks("Incomplete Tasks (after update)", incomplete_after_update)