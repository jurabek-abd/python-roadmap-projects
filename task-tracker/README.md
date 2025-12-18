# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. Built with Python using only standard library modules.

**Project URL:** https://roadmap.sh/projects/task-tracker

## Features

- ✅ Add new tasks with automatic ID assignment
- ✅ Update existing task descriptions
- ✅ Delete tasks by ID
- ✅ Mark tasks as "in progress" or "done"
- ✅ List all tasks or filter by status (todo, in-progress, done)
- ✅ Persistent storage using JSON
- ✅ Input validation and error handling
- ✅ UTC timestamps for task creation and updates

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd task-tracker
```

2. The project is ready to use! No additional installation required.

## Project Structure

```
task-tracker/
├── utils/
│   ├── __init__.py
│   ├── cli.py              # Command-line argument parsing
│   ├── file_handling.py    # JSON file operations
│   └── task_operations.py  # Task management logic
├── main.py                 # Entry point
├── storage.json            # Task storage (auto-created)
├── .gitignore
└── README.md
```

## Usage

Run the application using Python with the following commands:

### Adding a Task

```bash
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a Task

```bash
python main.py update 1 "Buy groceries and cook dinner"
# Output: Task updated successfully (ID: 1)
```

### Deleting a Task

```bash
python main.py delete 1
# Output: Task deleted successfully (ID: 1)
```

### Marking Task Status

```bash
# Mark as in progress
python main.py mark-in-progress 1
# Output: Task marked as in-progress successfully (ID: 1)

# Mark as done
python main.py mark-done 1
# Output: Task marked as done successfully (ID: 1)
```

### Listing Tasks

```bash
# List all tasks
python main.py list

# List tasks by status
python main.py list todo
python main.py list in-progress
python main.py list done
```

## Task Properties

Each task contains the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | Integer | Unique identifier (auto-incremented) |
| `description` | String | Task description |
| `status` | String | Current status: `todo`, `in-progress`, or `done` |
| `createdAt` | String | ISO 8601 timestamp (UTC) when task was created |
| `updatedAt` | String | ISO 8601 timestamp (UTC) of last update (null if never updated) |

## Example Workflow

```bash
# Add some tasks
python main.py add "Write project documentation"
python main.py add "Review pull requests"
python main.py add "Deploy to production"

# Start working on a task
python main.py mark-in-progress 1

# List tasks that are in progress
python main.py list in-progress

# Complete a task
python main.py mark-done 1

# List all completed tasks
python main.py list done

# Update a task description
python main.py update 2 "Review and merge pull requests"

# Delete a task
python main.py delete 3
```

## Error Handling

The application handles various error scenarios gracefully:

- **Empty descriptions**: Validates that task descriptions are not empty or whitespace-only
- **Non-existent tasks**: Displays clear error messages when trying to update, delete, or modify tasks that don't exist
- **Corrupted JSON**: Automatically recovers from corrupted storage files by starting with an empty task list
- **File operations**: Handles file read/write errors with informative messages

## Data Storage

Tasks are stored in `storage.json` in the project directory. The file is automatically created on first use.

Example `storage.json` structure:
```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2024-12-18T10:30:00.000000+00:00",
        "updatedAt": null
    },
    {
        "id": 2,
        "description": "Write documentation",
        "status": "in-progress",
        "createdAt": "2024-12-18T10:31:00.000000+00:00",
        "updatedAt": "2024-12-18T10:35:00.000000+00:00"
    }
]
```

## Development

### Code Organization

- **cli.py**: Handles command-line argument parsing using `argparse`
- **file_handling.py**: Manages JSON file operations with error handling
- **task_operations.py**: Contains all task manipulation logic with immutable operations
- **main.py**: Orchestrates the application flow and user interaction

### Best Practices Implemented

- ✅ Separation of concerns across modules
- ✅ Immutable operations (functions don't modify input data)
- ✅ Input validation and error handling
- ✅ Status constants to prevent typos
- ✅ Clear error messages for better UX
- ✅ UTC timestamps for consistency

### Running Tests

To test the application manually:

1. Test adding tasks with various descriptions
2. Test updating and deleting tasks
3. Test marking tasks with different statuses
4. Test listing with and without status filters
5. Test error cases (empty descriptions, non-existent IDs)
6. Verify JSON file structure in `storage.json`

## Contributing

This is a learning project built as part of the roadmap.sh backend project series. Suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built as part of the [roadmap.sh Task Tracker project](https://roadmap.sh/projects/task-tracker).

---

**Project created by:** Jurabek  
**Project URL:** https://roadmap.sh/projects/task-tracker
