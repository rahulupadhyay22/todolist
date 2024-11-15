import tkinter as tk
from tkinter import ttk, simpledialog, messagebox


def task():
    tasks = []  # List of tasks, each as a dictionary with task name, priority, and status

    def add_task():
        task_name = simpledialog.askstring("Input", "Enter task:")
        if task_name:
            priority = simpledialog.askstring("Input", "Enter priority (High, Medium, Low):")
            if priority and priority.lower() in ["high", "medium", "low"]:
                tasks.append({"name": task_name, "priority": priority.capitalize(), "status": "Pending"})
            else:
                messagebox.showerror("Error", "Invalid priority. Please enter High, Medium, or Low.")
        else:
            messagebox.showerror("Error", "Task name cannot be empty.")
        update_task_list()

    def update_task():
        task_name = simpledialog.askstring("Input", "Enter the task name you want to update:")
        for task in tasks:
            if task["name"] == task_name:
                new_task = simpledialog.askstring("Input", "Enter new task name:")
                if new_task:
                    task["name"] = new_task
                else:
                    messagebox.showerror("Error", "New task name cannot be empty.")
                update_task_list()
                return
        messagebox.showerror("Error", "Task not found.")
        update_task_list()

    def delete_task():
        task_name = simpledialog.askstring("Input", "Enter the task name to delete:")
        for task in tasks:
            if task["name"] == task_name:
                tasks.remove(task)
                update_task_list()
                return
        messagebox.showerror("Error", "Task not found.")
        update_task_list()

    def mark_completed():
        task_name = simpledialog.askstring("Input", "Enter the task name to mark as completed:")
        for task in tasks:
            if task["name"] == task_name:
                task["status"] = "Completed"
                update_task_list()
                return
        messagebox.showerror("Error", "Task not found.")
        update_task_list()

    def filter_tasks(priority):
        filtered_tasks = [task for task in tasks if task["priority"] == priority]
        task_list.delete(0, tk.END)
        for task in filtered_tasks:
            task_list.insert(tk.END, f"{task['name']} ({task['priority']}, {task['status']})")

    def clear_all_tasks():
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            tasks.clear()
        update_task_list()

    def search_task():
        query = simpledialog.askstring("Search", "Enter task name to search:")
        if query:
            for task in tasks:
                if query.lower() in task["name"].lower():
                    messagebox.showinfo("Search Result", f"Found: {task['name']} ({task['priority']}, {task['status']})")
                    update_task_list()
                    return
            messagebox.showerror("Error", "Task not found.")
        update_task_list()

    def update_task_list():
        task_list.delete(0, tk.END)
        for task in tasks:
            task_list.insert(tk.END, f"{task['name']} ({task['priority']}, {task['status']})")

    # Root window
    root = tk.Tk()
    root.title("Enhanced Task Management App")
    root.geometry("600x500")
    root.configure(bg="#f4f4f4")

    # Header
    header_frame = tk.Frame(root, bg="#3b5998")
    header_frame.pack(fill=tk.X)
    tk.Label(header_frame, text="Enhanced Task Management App", font=("Helvetica", 18, "bold"),
             fg="white", bg="#3b5998", pady=10).pack()

    # Task List
    list_frame = tk.Frame(root, bg="#f4f4f4")
    list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
    task_list = tk.Listbox(list_frame, font=("Helvetica", 12), bg="white", fg="black",
                           selectbackground="#3b5998", selectforeground="white", height=15)
    task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=task_list.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    task_list.config(yscrollcommand=scrollbar.set)

    # Buttons
    button_frame = tk.Frame(root, bg="#f4f4f4")
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="Add Task", command=add_task, style="TButton").grid(row=0, column=0, padx=10, pady=5)
    ttk.Button(button_frame, text="Update Task", command=update_task, style="TButton").grid(row=0, column=1, padx=10, pady=5)
    ttk.Button(button_frame, text="Delete Task", command=delete_task, style="TButton").grid(row=0, column=2, padx=10, pady=5)
    ttk.Button(button_frame, text="Mark Completed", command=mark_completed, style="TButton").grid(row=0, column=3, padx=10, pady=5)
    ttk.Button(button_frame, text="Search Task", command=search_task, style="TButton").grid(row=0, column=4, padx=10, pady=5)
    ttk.Button(button_frame, text="Clear All Tasks", command=clear_all_tasks, style="TButton").grid(row=1, column=0, padx=10, pady=5)
    ttk.Button(button_frame, text="Filter High Priority", command=lambda: filter_tasks("High"), style="TButton").grid(row=1, column=1, padx=10, pady=5)
    ttk.Button(button_frame, text="Filter Medium Priority", command=lambda: filter_tasks("Medium"), style="TButton").grid(row=1, column=2, padx=10, pady=5)
    ttk.Button(button_frame, text="Filter Low Priority", command=lambda: filter_tasks("Low"), style="TButton").grid(row=1, column=3, padx=10, pady=5)
    ttk.Button(button_frame, text="Exit", command=root.quit, style="TButton").grid(row=1, column=4, padx=10, pady=5)

    # Style
    style = ttk.Style(root)
    style.configure("TButton", font=("Helvetica", 10, "bold"), padding=5)
    style.configure("TFrame", background="#f4f4f4")

    update_task_list()  # Initial update of the task list
    root.mainloop()


task()
