from utils.api_handling import fetch_user_activity
from utils.cache_handling import load_cache, save_cache
from utils.cli import create_parsers


def format_event(event):
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "PushEvent":
        return f"- Pushed commits to {repo}"

    if event_type == "WatchEvent":
        return f"- Starred {repo}"

    if event_type == "CreateEvent":
        ref_type = event["payload"]["ref_type"]
        return f"- Created a new {ref_type} in {repo}"

    return None


def main():
    parser = create_parsers()
    args = parser.parse_args()

    cache = load_cache()

    if args.username in cache:
        print("Yes")

    url = f"https://api.github.com/users/{args.username}/events"

    events = fetch_user_activity(url)
    save_cache({args.username: events})

    # Output
    print("\nOutput:\n")
    for event in events:
        message = format_event(event)
        if message:
            print(message)
    print("\n")


if __name__ == "__main__":
    main()
