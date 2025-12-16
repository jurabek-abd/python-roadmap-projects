import argparse

parser = argparse.ArgumentParser(description="Task Tracker CLI")
subparsers = parser.add_subparsers(dest="command", required=True)

# Adding a new task
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task", type=str, help="Task value")

# Updating a task by ID
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id", type=int, help="Task ID")
update_parser.add_argument("task", type=str, help="Task value")

args = parser.parse_args()

if args.command == "add":
    print(f"Added a task: {args.task}")
elif args.command == "update":
    print(f"Updated a task {args.id}: {args.task}")
