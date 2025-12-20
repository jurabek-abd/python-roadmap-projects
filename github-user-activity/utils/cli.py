import argparse


def create_parsers(project_description="GitHub User Activity CLI"):
    parser = argparse.ArgumentParser(description=project_description)
    parser.add_argument("username", help="Your GitHub username")

    return parser
