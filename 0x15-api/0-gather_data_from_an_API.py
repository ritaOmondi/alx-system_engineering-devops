#!/usr/bin/python3
"""
This script retrieves the TODO list progress for a given employee ID
using the JSONPlaceholder API.
"""
import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee name and a list of completed tasks.
    """
    # API endpoint for user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # API endpoint for user's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Get user information
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Get user's todos
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Count completed and total tasks
        completed_tasks = [todo for todo in todos_data if todo["completed"]]
        total_tasks = len(todos_data)

        # Format the output
        employee_name = user_data["name"]
        output = f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):\n"
        for task in completed_tasks:
            output += f"    {task['title']}\n"

        return (employee_name, output.strip())

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return (None, None)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>", file=sys.stderr)
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, progress = get_employee_todo_progress(employee_id)
    if employee_name and progress:
        print(progress)
