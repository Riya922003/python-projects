# To-Do List Application

## Overview
This is a simple command-line To-Do List application that allows users to:
- View tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks

## Files
- `todo.py`: The main script to run the application.
- `todo_list.py`: Contains the `ToDoList` class that manages task operations.
- `file_manager.py`: Handles file I/O for saving and loading tasks.
- `tasks.txt`: Stores tasks persistently.

## Usage
Run the application by executing:
```bash
python todo.py


***Follow the on-screen instructions to manage your tasks.***

```yaml

---

### Step 5: Create `requirements.txt`

Since there are no third-party dependencies in this project, this file can be left empty or omitted.

---

### Running the Project
To run the project, simply execute:

```bash
python todo.py

``


## Notes
- **Persistence**: Tasks are saved in tasks.txt, allowing data persistence across program runs.
- **Modularity**: Each component of the application is in a separate file, promoting clean code structure and modularity.
- **Error Handling**: Basic error handling is included for invalid task numbers and menu choices.
