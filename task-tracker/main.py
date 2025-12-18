from utils.cli import create_parsers
from utils.file_handling import load_tasks, save_tasks
from utils.task_operations import (
    add_task,
    delete_task,
    list_tasks,
    mark_task_done,
    mark_task_in_progress,
    update_task,
)


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
        print(f"Task deleted successfully (ID: {args.id})")
    elif args.command == "mark-in-progress":
        save_tasks(mark_task_in_progress(tasks, args.id))
        print(f"Task marked as in-progress successfully (ID: {args.id})")
    elif args.command == "mark-done":
        save_tasks(mark_task_done(tasks, args.id))
        print(f"Task marked as done successfully (ID: {args.id})")
    elif args.command == "list":
        if not tasks:
            print("You don't have any tasks yet.")
        for task in list_tasks(tasks, args.status):
            print(f"(ID: {task['id']}): {task['description']}.")


if __name__ == "__main__":
    main()
