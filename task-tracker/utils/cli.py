import argparse


def create_parsers(project_description="Task Tracker CLI"):
    parser = argparse.ArgumentParser(description=project_description)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Adding a new task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # Updating a task by ID
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="Task description")

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

    # Listing tasks by status
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["todo", "in-progress", "done"],
        help="List tasks by status",
    )

    return parser
