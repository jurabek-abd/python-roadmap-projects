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

# COMMON_TASK_OPERATIONS = {
#     "delete": ("Task deleted successfully", delete_task),
#     "mark-in-progress": (
#         "Task marked as in-progress successfully",
#         mark_task_in_progress,
#     ),
#     "mark-done": ("Task marked as done successfully", mark_task_done),
# }


# def handle_common_operation(command, operation, tasks, task_id):
#     new_tasks, success = operation(tasks, task_id)
#     if success:
#         save_tasks(new_tasks)
#         print(f"{COMMON_TASK_OPERATIONS[command][0]} (ID: {task_id})")
#     else:
#         print(f"Error: Task with ID {task_id} not found")


def main():
    parser = create_parsers()
    args = parser.parse_args()

    tasks = load_tasks()

    # command = args.command

    # match command:
    #     case "add":
    #         try:
    #             tasks = add_task(tasks, args.description)
    #             save_tasks(tasks)
    #             print(f"Task added successfully (ID: {tasks[-1]['id']})")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #     case "update":
    #         try:
    #             tasks, success = update_task(tasks, args.id, args.description)
    #             if success:
    #                 save_tasks(tasks)
    #                 print(f"Task updated successfully (ID: {args.id})")
    #             else:
    #                 print(f"Error: Task with ID {args.id} not found")
    #         except ValueError as e:
    #             print(f"Error: {e}")
    #     case "delete" | "mark-in-progress" | "mark-done":
    #         handle_common_operation(
    #             command, COMMON_TASK_OPERATIONS[command][1], tasks, args.id
    #         )
    #     case "list":
    #         filtered_tasks = list_tasks(tasks, args.status)
    #         if not filtered_tasks:
    #             status_msg = f" with status '{args.status}'" if args.status else ""
    #             print(f"You don't have any tasks{status_msg}.")
    #         else:
    #             for task in filtered_tasks:
    #                 status_indicator = f"[{task['status']}]"
    #                 print(f"ID {task['id']}: {task['description']} {status_indicator}")

    if args.command == "add":
        try:
            tasks = add_task(tasks, args.description)
            save_tasks(tasks)
            print(f"Task added successfully (ID: {tasks[-1]['id']})")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == "update":
        try:
            tasks, success = update_task(tasks, args.id, args.description)
            if success:
                save_tasks(tasks)
                print(f"Task updated successfully (ID: {args.id})")
            else:
                print(f"Error: Task with ID {args.id} not found")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == "delete":
        tasks, success = delete_task(tasks, args.id)
        if success:
            save_tasks(tasks)
            print(f"Task deleted successfully (ID: {args.id})")
        else:
            print(f"Error: Task with ID {args.id} not found")
    elif args.command == "mark-in-progress":
        tasks, success = mark_task_in_progress(tasks, args.id)
        if success:
            save_tasks(tasks)
            print(f"Task marked as in-progress successfully (ID: {args.id})")
        else:
            print(f"Error: Task with ID {args.id} not found")
    elif args.command == "mark-done":
        tasks, success = mark_task_done(tasks, args.id)
        if success:
            save_tasks(tasks)
            print(f"Task marked as done successfully (ID: {args.id})")
        else:
            print(f"Error: Task with ID {args.id} not found")
    elif args.command == "list":
        filtered_tasks = list_tasks(tasks, args.status)
        if not filtered_tasks:
            status_msg = f" with status '{args.status}'" if args.status else ""
            print(f"You don't have any tasks{status_msg}.")
        else:
            for task in filtered_tasks:
                status_indicator = f"[{task['status']}]"
                print(f"ID {task['id']}: {task['description']} {status_indicator}")


if __name__ == "__main__":
    main()
