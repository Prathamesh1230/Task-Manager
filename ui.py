import tkinter as tk
from tkinter import messagebox
import db

class TaskManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        
        # Title Input
        tk.Label(root, text="Task Title:").pack()
        self.title_entry = tk.Entry(root, width=40)
        self.title_entry.pack()

        # Description Input
        tk.Label(root, text="Description:").pack()
        self.desc_entry = tk.Entry(root, width=40)
        self.desc_entry.pack()

        # Buttons
        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        self.list_tasks_btn = tk.Button(root, text="View Tasks", command=self.list_tasks)
        self.list_tasks_btn.pack()

        self.tasks_listbox = tk.Listbox(root, width=50)
        self.tasks_listbox.pack()

        # Dropdown for updating status
        self.status_var = tk.StringVar(root)
        self.status_var.set("Pending")  # Default status
        self.status_menu = tk.OptionMenu(root, self.status_var, "Pending", "In Progress", "Completed")
        self.status_menu.pack()

        # Update Status Button
        self.update_status_btn = tk.Button(root, text="Update Status", command=self.update_status)
        self.update_status_btn.pack()

        # Delete Task Button
        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack()

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        if title:
            db.add_task(title, desc)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showerror("Error", "Task title cannot be empty")

    def list_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = db.get_tasks()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task[0]} - {task[1]} - {task[3]}")

    def update_status(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            task_id = selected_task.split(" - ")[0]
            new_status = self.status_var.get()
            db.update_task(task_id, new_status)
            messagebox.showinfo("Success", "Task status updated!")
            self.list_tasks()

    def delete_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            task_id = selected_task.split(" - ")[0]
            db.delete_task(task_id)
            messagebox.showinfo("Success", "Task deleted!")
            self.list_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
