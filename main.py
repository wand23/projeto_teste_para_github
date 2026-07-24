import argparse, json
from datetime import datetime

#main parser
parser = argparse.ArgumentParser(description="Task CLI")

#subparser group for add, list, delete commands
subparser = parser.add_subparsers(dest="command", required=True, help="Available commands")

add_parser = subparser.add_parser("add")
add_parser.add_argument("task", type=str)
add_parser.add_argument("--status", choices=["todo", "done", "in progress"], required=True)

list_parser = subparser.add_parser("list")
list_parser.add_argument("id", type=int)

delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("id", type=int)

update_parser = subparser.add_parser("update")


args = parser.parse_args()

with open("task.json", "r") as file:
    tasks = json.load(file)


if args.command == "add":
  
  new_id = max(tasks["id"] for tasks in tasks) + 1 if tasks else 1

  createdAT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  task_dict= {
  "id": new_id,
  "task": args.task,
  "status": args.status,
  "createdAt":createdAT,
  "updatedAt":updatedAt,
}

  with open("task.json", "w") as file:
    json.dump(tasks + [task_dict], file, indent=4)    
  print(f"Task added successfully with ID: {new_id}")

elif args.command == "list":
  for task in tasks:
    if task["id"] == args.id:
      print(f"ID: {task['id']}")
      print(f"Task: {task['task']}")
      print(f"Status: {task['status']}")
      print(f"Created At: {task['createdAt']}")
      print(f"Updated At: {task['updatedAt']}")

elif args.command == "delete":
  updated_tasks = [task for task in tasks if task["id"] != args.id]
  with open("task.json", "w") as file:
    json.dump(updated_tasks, file, indent=4)
