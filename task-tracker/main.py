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


def handle_add_operation(tasks, description):
    try:
        tasks = add_task(tasks, description)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {tasks[-1]['id']})")
    except ValueError as e:
        print(f"Error: {e}")


def handle_update_operation(tasks, task_id, description):
    try:
        tasks, success = update_task(tasks, task_id, description)
        if success:
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Error: Task with ID {task_id} not found")
    except ValueError as e:
        print(f"Error: {e}")


def handle_delete_operation(tasks, task_id):
    tasks, success = delete_task(tasks, task_id)
    if success:
        save_tasks(tasks)
        print(f"Task deleted successfully (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")


def handle_mark_in_progress_operation(tasks, task_id):
    tasks, success = mark_task_in_progress(tasks, task_id)
    if success:
        save_tasks(tasks)
        print(f"Task marked as 'in-progress' successfully (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")


def handle_mark_done_operation(tasks, task_id):
    tasks, success = mark_task_done(tasks, task_id)
    if success:
        save_tasks(tasks)
        print(f"Task marked as 'done' successfully (ID: {task_id})")
    else:
        print(f"Error: Task with ID {task_id} not found")


def handle_list_operation(tasks, status):
    filtered_tasks = list_tasks(tasks, status)
    if not filtered_tasks:
        status_msg = f" with status '{status}'" if status else ""
        print(f"You don't have any tasks{status_msg}.")
    else:
        for task in filtered_tasks:
            status_indicator = f"[{task['status']}]"
            print(f"ID {task['id']}: {task['description']} {status_indicator}")


def main():
    parser = create_parsers()
    args = parser.parse_args()

    tasks = load_tasks()

    match args.command:
        case "add":
            handle_add_operation(tasks, args.description)
        case "update":
            handle_update_operation(tasks, args.id, args.description)
        case "delete":
            handle_delete_operation(tasks, args.id)
        case "mark-in-progress":
            handle_mark_in_progress_operation(tasks, args.id)
        case "mark-done":
            handle_mark_done_operation(tasks, args.id)
        case "list":
            handle_list_operation(tasks, args.status)


if __name__ == "__main__":
    main()
