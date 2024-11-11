import sqlite3


def init_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    with sqlite3.connect('tasks.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     task TEXT NOT NULL,
                     completed BOOLEAN NOT NULL DEFAULT 0)''')
        conn.commit()


def add_task_to_db(task):
    """Add a new task to the database."""
    with sqlite3.connect('tasks.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()


def delete_task_from_db(task):
    """Delete a task from the database."""
    with sqlite3.connect('tasks.db') as conn:
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE task = ?", (task,))
        conn.commit()


def fetch_tasks():
    """Fetch all tasks from the database."""
    with sqlite3.connect('tasks.db') as conn:
        c = conn.cursor()
        c.execute("SELECT task, completed FROM tasks")
        return c.fetchall()
