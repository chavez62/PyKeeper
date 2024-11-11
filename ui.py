import tkinter as tk
from config import COLORS, FONT_MAIN, FONT_BUTTON
from task_manager import add_task, delete_task, toggle_complete, display_tasks, search_tasks


def setup_main_window():
    """Set up the main window and return the root Tk instance."""
    root = tk.Tk()
    root.title("Enhanced Task Tracker")
    root.geometry("500x600")
    root.config(bg=COLORS["bg_main"])
    return root


def setup_frames(root):
    """Create and organize frames in the main window."""
    input_frame = tk.Frame(root, bg=COLORS["bg_main"])
    input_frame.pack(pady=10)

    list_frame = tk.Frame(root, bg=COLORS["bg_main"])
    list_frame.pack(pady=10)

    button_frame = tk.Frame(root, bg=COLORS["bg_main"])
    button_frame.pack(pady=10)

    return input_frame, list_frame, button_frame


def setup_widgets(root, input_frame, list_frame, button_frame):
    """Set up widgets in their respective frames."""
    global task_entry

    # Input field for new tasks
    task_entry = tk.Entry(input_frame, width=40,
                          font=FONT_MAIN, relief=tk.SUNKEN, borderwidth=2)
    task_entry.pack(side=tk.LEFT, padx=5)

    # Add Task button
    add_button = tk.Button(input_frame, text="Add Task", command=lambda: add_task(task_entry, lambda: display_tasks(tasks_listbox, lambda: status_bar.config(text=f"{tasks_listbox.size()} tasks"))), font=FONT_BUTTON,
                           bg=COLORS["add_button"], fg="white")
    add_button.pack(side=tk.RIGHT)

    # Listbox for displaying tasks
    tasks_listbox = tk.Listbox(list_frame, width=50, height=15, font=FONT_MAIN,
                               selectmode=tk.SINGLE, relief=tk.SUNKEN, borderwidth=2)
    tasks_listbox.pack(pady=5)

    # Scrollbar for task listbox
    tasks_scrollbar = tk.Scrollbar(list_frame)
    tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tasks_listbox.config(yscrollcommand=tasks_scrollbar.set)
    tasks_scrollbar.config(command=tasks_listbox.yview)

    # Delete and Complete buttons
    delete_button = tk.Button(button_frame, text="Delete Task", command=lambda: delete_task(tasks_listbox, lambda: display_tasks(tasks_listbox, lambda: status_bar.config(text=f"{tasks_listbox.size()} tasks"))), font=FONT_BUTTON,
                              bg=COLORS["delete_button"], fg="white")
    delete_button.grid(row=0, column=0, padx=5)

    complete_button = tk.Button(button_frame, text="Mark as Completed", command=lambda: toggle_complete(tasks_listbox, lambda: display_tasks(tasks_listbox, lambda: status_bar.config(text=f"{tasks_listbox.size()} tasks"))), font=FONT_BUTTON,
                                bg=COLORS["complete_button"], fg="white")
    complete_button.grid(row=0, column=1, padx=5)

    # Search bar and status bar
    search_entry = tk.Entry(root, width=30, font=FONT_MAIN,
                            relief=tk.SUNKEN, borderwidth=2)
    search_entry.pack(pady=(10, 0))
    search_button = tk.Button(root, text="Search", command=lambda: search_tasks(search_entry, tasks_listbox), bg=COLORS["search_button"],
                              fg="white", font=FONT_BUTTON)
    search_button.pack(pady=5)

    status_bar = tk.Label(root, text="0 tasks",
                          relief=tk.SUNKEN, anchor=tk.W, font=FONT_BUTTON)
    status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    # Return `tasks_listbox` and `status_bar`
    return tasks_listbox, status_bar
