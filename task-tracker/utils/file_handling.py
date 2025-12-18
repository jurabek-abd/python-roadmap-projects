import json
import os


def load_tasks(filename="storage.json"):
    if not os.path.exists(filename):
        save_tasks([])

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"Warning: {filename} contains invalid JSON. Starting with empty task list."
        )
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}. Starting with empty task list.")
        return []


def save_tasks(tasks=None, filename="storage.json"):
    if tasks is None:
        tasks = []

    try:
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error saving tasks to {filename}: {e}")
        raise
