import tkinter as tk
from tkinter import ttk

class FacultyConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Faculty Configuration")

        # Creating notebook for tabs
        self.notebook = ttk.Notebook(root)

        # Tab for adding faculty
        self.add_faculty_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.add_faculty_tab, text="Add Faculty")

        # Tab for viewing faculty
        self.view_faculty_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_faculty_tab, text="View Faculty")

        # Adding notebook to the main window
        self.notebook.pack(expand=1, fill="both")

        # Initialize variables
        self.faculty_list = []

        # Adding faculty tab widgets
        self.add_faculty_widgets()

        # Adding view faculty tab widgets
        self.view_faculty_widgets()

    def add_faculty_widgets(self):
        # Label and Entry for Name
        tk.Label(self.add_faculty_tab, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.add_faculty_tab)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for Department
        tk.Label(self.add_faculty_tab, text="Department:").grid(row=1, column=0, padx=10, pady=10)
        self.department_entry = tk.Entry(self.add_faculty_tab)
        self.department_entry.grid(row=1, column=1, padx=10, pady=10)

        # Label and Entry for Position
        tk.Label(self.add_faculty_tab, text="Position:").grid(row=2, column=0, padx=10, pady=10)
        self.position_entry = tk.Entry(self.add_faculty_tab)
        self.position_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to add faculty
        tk.Button(self.add_faculty_tab, text="Add Faculty", command=self.add_faculty).grid(row=3, column=0, columnspan=2, pady=10)

    def view_faculty_widgets(self):
        # Treeview to display faculty information
        self.faculty_tree = ttk.Treeview(self.view_faculty_tab, columns=("Name", "Department", "Position"), show="headings")
        self.faculty_tree.heading("Name", text="Name")
        self.faculty_tree.heading("Department", text="Department")
        self.faculty_tree.heading("Position", text="Position")
        self.faculty_tree.pack(padx=10, pady=10)

    def add_faculty(self):
        # Get values from entry widgets
        name = self.name_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()

        # Add faculty to the list
        self.faculty_list.append({"Name": name, "Department": department, "Position": position})

        # Clear entry widgets
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)

        # Update the Treeview in the view faculty tab
        self.update_faculty_tree()

    def update_faculty_tree(self):
        # Clear existing items in the Treeview
        for item in self.faculty_tree.get_children():
            self.faculty_tree.delete(item)

        # Insert new faculty information into the Treeview
        for faculty in self.faculty_list:
            self.faculty_tree.insert("", "end", values=(faculty["Name"], faculty["Department"], faculty["Position"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = FacultyConfigApp(root)
    root.mainloop()
