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

# Deleting a task by ID
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", type=int, help="Task ID")

# Marking a task as in progress or done by ID
mark_in_progress_parser = subparsers.add_parser(
    "mark-in-progress", help="Mark a task as in progress"
)
mark_in_progress_parser.add_argument("id", type=int, help="Task ID")
mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument("id", type=int, help="Task ID")

args = parser.parse_args()

if args.command == "add":
    print(f"Added a task: {args.task}")
elif args.command == "update":
    print(f"Updated a task {args.id}: {args.task}")
elif args.command == "mark-in-progress":
    print(f"Marked a task {args.id} as in progress")
elif args.command == "mark-done":
    print(f"Marked a task {args.id} as done")
