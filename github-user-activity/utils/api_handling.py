import json
import urllib.request


def fetch_user_activity(url):
    request = urllib.request.Request(
        url, headers={"User-Agent": "Python", "Accept": "application/vnd.github+json"}
    )

    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")

    return json.loads(data)
