import tkinter as tk
from tkinter import messagebox
import os

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x350")
        self.configure(bg="#f0f0f0")

        self.task_file = "tasks.txt"

        self.font = ("Arial", 12)
        self.bg_color = "#ffffff" 
        self.fg_color = "#333333"
        self.btn_bg_color = "#4CAF50"
        self.btn_fg_color = "#ffffff"
        self.input_bg_color = "#f7f7f7"
        self.input_fg_color = "#333333"

        self.input_box = tk.Entry(self, font=self.font, bg=self.input_bg_color, fg=self.input_fg_color, width=28, borderwidth=2)
        self.add_button = tk.Button(self, text="Add Task", font=self.font, bg=self.btn_bg_color, fg=self.btn_fg_color, command=self.add_task, borderwidth=2)
        self.delete_button = tk.Button(self, text="Delete Selected Task", font=self.font, bg=self.btn_bg_color, fg=self.btn_fg_color, command=self.delete_task, borderwidth=2)
        self.task_list = tk.Listbox(self, font=self.font, bg=self.bg_color, fg=self.fg_color, selectbackground="#d1e7dd", selectforeground=self.fg_color, width=35, height=10, borderwidth=2)
        
        self.input_box.pack(pady=10)
        self.add_button.pack(pady=5)
        self.delete_button.pack(pady=5)
        self.task_list.pack(pady=10)

        self.load_tasks()

        self.bind('<Return>', lambda event: self.add_task())

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task_text = self.input_box.get().strip()
        if task_text:
            self.task_list.insert(tk.END, task_text)
            self.input_box.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Cannot add an empty task!")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Error", "No task selected!")

    def load_tasks(self):
        if os.path.exists(self.task_file):
            with open(self.task_file, "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    self.task_list.insert(tk.END, task.strip())

    def save_tasks(self):
        tasks = self.task_list.get(0, tk.END)
        with open(self.task_file, "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def on_closing(self):
        self.save_tasks()
        self.destroy()

if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
