import tkinter as tk

class DailyRoutineGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Routine Generator")
        self.root.configure(bg="#3333FF")  # Lavender background color
        self.root.geometry("550x600")  # Increase the size of the GUI

        # Create project heading at the top
        self.project_heading = tk.Label(root, text="Daily Routine Generator", font=("Monospace", 24, "bold"), fg="BLACK", bg="#3333FF")
        self.project_heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create input fields and buttons
        self.task_label = tk.Label(root, text="Enter Task:", font=("Arial", 14), bg="#3333FF")
        self.task_label.grid(row=1, column=0, padx=10, pady=10)
        self.task_entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.task_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#ADD8E6", fg="black", font=("Arial", 14))
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a frame to hold the task list
        self.task_list_frame = tk.Frame(root, bg="#3333FF")
        self.task_list_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create column headings
        self.task_heading = tk.Label(self.task_list_frame, text="Task", font=("Arial", 14, "bold"), bg="#3333FF")
        self.task_heading.grid(row=0, column=0, padx=5, pady=5)

        # Create a listbox to display the tasks
        self.task_listbox = tk.Listbox(self.task_list_frame, width=40, height=10, font=("Arial", 14))
        self.task_listbox.grid(row=1, column=0, padx=5, pady=5)

        # Create buttons to mark tasks as done and delete tasks
        self.mark_done_button = tk.Button(root, text="Mark Done", command=self.mark_done, bg="#ADD8E6", fg="black", font=("Arial", 14))
        self.mark_done_button.grid(row=4, column=0, padx=10, pady=10)
        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task, bg="#ADD8E6", fg="black", font=("Arial", 14))
        self.delete_button.grid(row=4, column=1, padx=10, pady=10)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.display_tasks()
            self.task_entry.delete(0, tk.END)

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, task)

    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.tasks[selected_task_index[0]] = f"✓ {task}"
            self.display_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.display_tasks()

root = tk.Tk()
daily_routine_generator = DailyRoutineGenerator(root)
root.mainloop()