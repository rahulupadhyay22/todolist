# Task Management App

A simple Task Management (to-do list) application built with Python's Tkinter library. This GUI-based app allows users to add, update, delete, and view tasks in a user-friendly interface.

## Features

- **Add Task**: Add a new task to your to-do list.
- **Update Task**: Modify an existing task.
- **Delete Task**: Remove a task from the list.
- **View Tasks**: Display all tasks in a list format.

## Prerequisites

Ensure you have Python 3 installed on your machine. This application uses Tkinter, which is included with Python by default.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/task-management-app.git
   cd task-management-app
2. Run the application:
   ```bash
   python todo_app.py
   
## Usage

- **Add a Task**: Click on "Add Task" to input a new task name. The task will appear in the list once added.
- **Update a Task**: Click on "Update Task" and enter the name of the task you want to update, then input the new name.
- **Delete a Task**: Click on "Delete Task" and enter the name of the task to remove it from the list.
- **View Tasks**: Click "View Tasks" to see all current tasks.
- **Exit the App**: Click "Exit" to close the application

## Code Structure

- **add_task()**: Prompts the user to enter a new task and adds it to the list.
- **update_task()**: Prompts for an existing task name and a new task name to update the task.
- **delete_task()**: Prompts the user for a task name and removes it if it exists.
- **view_tasks()**: Displays all tasks in a popup window.
- **update_task_list()**: Refreshes the task list displayed in the app.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.
