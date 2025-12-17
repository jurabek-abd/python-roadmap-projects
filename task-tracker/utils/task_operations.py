from datetime import datetime, timezone


def get_timestamp():
    return datetime.now(timezone.utc).isoformat()


def add_task(tasks, description):
    tasks.append(
        {
            "id": tasks[-1]["id"] + 1 if tasks else 1,
            "description": description,
            "status": "todo",
            "createdAt": get_timestamp(),
            "updatedAt": None,
        }
    )
    return tasks


def update_task(tasks, id, description):
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = get_timestamp()
            break
        continue

    return tasks


def delete_task(tasks, id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            break
        continue

    return tasks
