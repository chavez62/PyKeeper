import tkinter as tk
from database import init_db
from ui import setup_main_window, setup_frames, setup_widgets
from task_manager import display_tasks

# Initialize database
init_db()

# Set up the main window
root = setup_main_window()
input_frame, list_frame, button_frame = setup_frames(root)

# Set up widgets and get the tasks_listbox and status_bar
tasks_listbox, status_bar = setup_widgets(
    root, input_frame, list_frame, button_frame)

# Define an update_status function to update the status bar with the task count


def update_status():
    status_bar.config(text=f"{tasks_listbox.size()} tasks")


# Display initial tasks with the tasks_listbox and update_status function
display_tasks(tasks_listbox, update_status)

# Run the application
root.mainloop()
