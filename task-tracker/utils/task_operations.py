from datetime import datetime, timezone

STATUS_TODO = "todo"
STATUS_IN_PROGRESS = "in-progress"
STATUS_DONE = "done"


def get_timestamp():
    return datetime.now(timezone.utc).isoformat()


def add_task(tasks, description):
    if not description or not description.strip():
        raise ValueError("Task description cannot be empty")

    new_tasks = tasks.copy()

    new_id = tasks[-1]["id"] + 1 if tasks else 1

    new_tasks.append(
        {
            "id": new_id,
            "description": description,
            "status": STATUS_TODO,
            "createdAt": get_timestamp(),
            "updatedAt": None,
        }
    )
    return new_tasks


def update_task(tasks, task_id, description):
    if not description or not description.strip():
        raise ValueError("Task description cannot be empty")

    new_tasks = tasks.copy()
    for task in new_tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = get_timestamp()
            return new_tasks, True

    return new_tasks, False


def delete_task(tasks, task_id):
    new_tasks = tasks.copy()

    for task in new_tasks:
        if task["id"] == task_id:
            new_tasks.remove(task)
            return new_tasks, True

    return new_tasks, False


def mark_task_in_progress(tasks, task_id):
    new_tasks = tasks.copy()

    for task in new_tasks:
        if task["id"] == task_id:
            if task["status"] == STATUS_IN_PROGRESS:
                return new_tasks, "already"
            task["status"] = STATUS_IN_PROGRESS
            task["updatedAt"] = get_timestamp()
            return new_tasks, True

    return new_tasks, False


def mark_task_done(tasks, task_id):
    new_tasks = tasks.copy()

    for task in new_tasks:
        if task["id"] == task_id and not task["status"] == STATUS_DONE:
            task["status"] = STATUS_DONE
            task["updatedAt"] = get_timestamp()
            return new_tasks, True

    return new_tasks, False


def list_tasks(tasks, status):
    if status:
        return list(filter(lambda t: t["status"] == status, tasks))

    return tasks
