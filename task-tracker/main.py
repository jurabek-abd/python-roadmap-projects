from utils.cli import create_parsers
from utils.file_handling import load_tasks, save_tasks
from utils.task_operations import add_task, delete_task, update_task


def main():
    parser = create_parsers()
    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "add":
        save_tasks(add_task(tasks, args.description))
        print(f"Task added successfully (ID: {tasks[-1]['id']})")
    elif args.command == "update":
        save_tasks(update_task(tasks, args.id, args.description))
        print(f"Task updated successfully (ID: {args.id})")
    elif args.command == "delete":
        save_tasks(delete_task(tasks, args.id))
    elif args.command == "mark-in-progress":
        print(f"Marked a task {args.id} as in progress")
    elif args.command == "mark-done":
        print(f"Marked a task {args.id} as done")
    elif args.command == "list":
        print(f"Listed tasks by status: {'none' if not args.status else args.status}")


if __name__ == "__main__":
    main()
