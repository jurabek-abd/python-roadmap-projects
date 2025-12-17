import json
import os

filename = "storage.json"


def load_tasks():
    if not os.path.exists(filename):
        save_tasks([])

    with open(filename, "r") as f:
        return json.load(f)


def save_tasks(tasks=[]):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
