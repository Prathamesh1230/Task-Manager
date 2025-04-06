import db
import ui
import tkinter as tk

if __name__ == "__main__":
    db.init_db()
    root = tk.Tk()
    app = ui.TaskManagerUI(root)
    root.mainloop()
