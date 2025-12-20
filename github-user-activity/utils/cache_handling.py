import json
import os

FILENAME = "cache.json"


def load_cache(filename=FILENAME):
    if not os.path.exists(filename):
        save_cache({})

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(
            f"Warning: {filename} contains invalid JSON. Starting with empty cache list."
        )
        return {}
    except Exception as e:
        print(f"Error reading {filename}: {e}. Starting with empty cache list.")
        return {}


def save_cache(cache=None, filename=FILENAME):
    if cache is None:
        cache = {}

    try:
        with open(filename, "w") as f:
            json.dump(cache, f, indent=4)
    except Exception as e:
        print(f"Error saving cache to {filename}: {e}")
        raise


def clean_cache(filename=FILENAME):
    try:
        with open(filename, "w") as f:
            json.dump({}, f, indent=4)
    except Exception as e:
        print(f"Error cleaning cache in {filename}: {e}")
        raise
