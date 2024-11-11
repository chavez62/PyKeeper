from tkinter import messagebox
from database import add_task_to_db, delete_task_from_db, fetch_tasks
from config import COLORS
import sqlite3


def add_task(task_entry, display_tasks):
    """Add a task from the entry field to the listbox and database."""
    task = task_entry.get()
    if task:
        add_task_to_db(task)
        task_entry.delete(0, 'end')
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")


def delete_task(tasks_listbox, display_tasks):
    """Delete the selected task from the listbox and database."""
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_text = tasks_listbox.get(selected_task)
        task_name = task_text.split(" - ")[0]
        if messagebox.askokcancel("Confirm Delete", "Do you want to delete this task?"):
            delete_task_from_db(task_name)
            display_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete")


def search_tasks(search_entry, tasks_listbox):
    """Filter tasks by the search keyword and display the results in the listbox."""
    search_text = search_entry.get().lower()
    tasks_listbox.delete(0, 'end')
    tasks = fetch_tasks()
    for task, completed in tasks:
        if search_text in task.lower():
            display_text = f"{task} - {'Completed' if completed else 'Pending'}"
            tasks_listbox.insert('end', display_text)
            last_index = tasks_listbox.size() - 1
            # Apply color based on completion status
            color = COLORS["task_completed"] if completed else COLORS["task_pending"]
            tasks_listbox.itemconfig(last_index, {'bg': color})


def toggle_complete(tasks_listbox, display_tasks):
    """Toggle the completion status of the selected task."""
    selected_task = tasks_listbox.curselection()
    if selected_task:
        task_text = tasks_listbox.get(selected_task)
        task_name = task_text.split(" - ")[0]
        with sqlite3.connect("tasks.db") as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE tasks SET completed = NOT completed WHERE task = ?", (task_name,))
            conn.commit()
        display_tasks()
    else:
        messagebox.showwarning(
            "Warning", "Please select a task to mark as complete")


def display_tasks(tasks_listbox, update_status):
    """Display tasks in the listbox with color coding for completed and pending tasks."""
    tasks_listbox.delete(0, 'end')
    tasks = fetch_tasks()
    for task, completed in tasks:
        display_text = f"{task} - {'Completed' if completed else 'Pending'}"
        tasks_listbox.insert('end', display_text)
        last_index = tasks_listbox.size() - 1
        color = COLORS["task_completed"] if completed else COLORS["task_pending"]
        tasks_listbox.itemconfig(last_index, {'bg': color})
    update_status()
