import tkinter as tk 
from tkinter import simpledialog, messagebox

def task():
    tasks = []  # Initialize an empty list to store tasks

    def add_task():
        task_name = simpledialog.askstring("Input", "Enter task:")
        if task_name:
            tasks.append(task_name)
            update_task_list()

    def update_task():
        task_name = simpledialog.askstring("Input", "Enter the task name you want to update:")
        if task_name in tasks:
            new_task = simpledialog.askstring("Input", "Enter new task:")
            if new_task:
                ind = tasks.index(task_name)
                tasks[ind] = new_task
                update_task_list()
        else:
            messagebox.showerror("Error", "Task not found.")

    def delete_task():
        task_name = simpledialog.askstring("Input", "Which task you want to delete:")
        if task_name in tasks:
            tasks.remove(task_name)
            update_task_list()
        else:
            messagebox.showerror("Error", "Task not found.")

    def view_tasks():
        messagebox.showinfo("Tasks", f"Total tasks: {tasks}")

    def update_task_list():
        task_list.delete(0, tk.END)
        for task in tasks:
            task_list.insert(tk.END, task)

    root = tk.Tk()
    root.title("Task Management App")

    tk.Label(root, text="----WELCOME TO THE TASK MANAGEMENT APP----").pack()

    tk.Button(root, text="Add Task", command=add_task).pack()
    tk.Button(root, text="Update Task", command=update_task).pack()
    tk.Button(root, text="Delete Task", command=delete_task).pack()
    tk.Button(root, text="View Tasks", command=view_tasks).pack()
    tk.Button(root, text="Exit", command=root.quit).pack()

    task_list = tk.Listbox(root)
    task_list.pack()

    root.mainloop()

task()
