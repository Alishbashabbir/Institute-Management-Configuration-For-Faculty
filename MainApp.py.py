# Sumbitted by  : Alishba Shabbir
# Rollno        : F21BSEEN1E02010
# Section       : E1
# Semester      : 5th
# Project       : Faculty Configuration In Tkinter
# Submitted to  : Sir Nauman
# Department of : Software Engineering


import tkinter as tk
from tkinter import ttk, messagebox
import requests

class FacultyTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_item = None
        self.init_faculty_tab()

    def init_faculty_tab(self):
        faculty_frame = ttk.LabelFrame(self.parent, text="Faculty Information")
        faculty_frame.grid(row=0, column=0, padx=30, pady=10, sticky=tk.W)

        # Labels and Entries
        ttk.Label(faculty_frame, text="Faculty ID :").grid(row=0, column=0, padx=15, sticky=tk.W)
        self.faculty_id = ttk.Entry(faculty_frame)
        self.faculty_id.grid(row=0, column=1, padx=20, pady=5, sticky=tk.W+tk.E)
        
        ttk.Label(faculty_frame, text="Faculty Name :").grid(row=1, column=0,padx=15 , sticky=tk.W)
        self.faculty_name = ttk.Entry(faculty_frame)
        self.faculty_name.grid(row=1, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Faculty Dean :").grid(row=2, column=0, padx=15 ,sticky=tk.W)
        self.faculty_dean = ttk.Entry(faculty_frame)
        self.faculty_dean.grid(row=2, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        contact_info_label = ttk.Label(faculty_frame, text="Contact Info :-")
        contact_info_label.grid(row=3, column=0, padx=15 , pady=10 , sticky=tk.W)

        ttk.Label(faculty_frame, text="Telephone Number :").grid(row=4, column=0, padx=25 ,sticky=tk.W)
        self.phone = ttk.Entry(faculty_frame)
        self.phone.grid(row=4, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Email :").grid(row=5, column=0,padx=25 , sticky=tk.W)
        self.email = ttk.Entry(faculty_frame)
        self.email.grid(row=5, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Address :").grid(row=6, column=0, padx=25 ,sticky=tk.W)
        self.address = ttk.Entry(faculty_frame)
        self.address.grid(row=6, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)

        ttk.Label(faculty_frame, text="Teaching Subjects :").grid(row=7, column=0, padx=15 ,sticky=tk.W)
        self.teaching_subjects_text = tk.Text(faculty_frame, height=4, width=30)
        self.teaching_subjects_text.grid(row=7, column=1, padx=20 , pady=5 , sticky=tk.W+tk.E)


        # Buttons
        add_button = ttk.Button(faculty_frame, text="Add Faculty", command=self.add_faculty)
        add_button.grid(row=8, column=0, pady=10)

        update_button = ttk.Button(faculty_frame, text="Update Faculty", state=tk.DISABLED, command=self.update_faculty)
        update_button.grid(row=8, column=1, pady=10)

        show_data_button = ttk.Button(faculty_frame, text="Show Data", command=self.show_faculty_data)
        show_data_button.grid(row=9, column=0, pady=10)

        delete_button = ttk.Button(faculty_frame, text="Delete Faculty", state=tk.DISABLED, command=self.delete_faculty)
        delete_button.grid(row=9, column=1, pady=10)

        self.clear_button = ttk.Button(faculty_frame, text="Clear Entries", command=self.clear_entries)
        self.clear_button.grid(row=10, column=0, pady=10)

        separator = ttk.Label(self.parent, text="_______________________________________________________________________________________________________")
        separator.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)

        # Treeview for displaying faculty data
        faculty_show_data_label = ttk.Label(self.parent, text="Faculty Data Preview Area:", font=("Arial", 10))
        faculty_show_data_label.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

        self.tree = ttk.Treeview(self.parent, columns=("Faculty ID", "Faculty Name", "Faculty Dean", "Telephone", "Email", "Address", "Teaching Subjects"), show="headings")
        self.tree.heading("Faculty ID", text="Faculty ID")
        self.tree.heading("Faculty Name", text="Faculty Name")
        self.tree.heading("Faculty Dean", text="Faculty Dean")
        self.tree.heading("Telephone", text="Telephone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Teaching Subjects", text="Teaching Subjects")
        self.tree.grid(row=3, column=0, rowspan=8, padx=20, pady=10, sticky=tk.W)

        # Bind the treeview's selection event to a callback method
        self.tree.bind("<ButtonRelease-1>", lambda event: self.display_selected_data())

        # Save buttons as attributes for easy access
        self.add_button = add_button
        self.show_data_button = show_data_button
        self.update_button = update_button
        self.delete_button = delete_button

    def add_faculty(self):
        faculty_id = self.faculty_id.get()
        faculty_name = self.faculty_name.get()
        faculty_dean = self.faculty_dean.get()
        telephone = self.phone.get()
        email = self.email.get()
        address = self.address.get()
        subjects = self.teaching_subjects_text.get("1.0", tk.END)

        if not faculty_id or not faculty_name or not faculty_dean or not telephone or not email or not address:
            messagebox.showerror("Error", "Please fill in all the required fields.")
            return

        faculty_data = {
            "faculty_id": faculty_id,
            "faculty_name": faculty_name,
            "faculty_dean": faculty_dean,
            "telephone": telephone,
            "email": email,
            "address": address,
            "subjects": subjects
        }

        api_endpoint = "http://localhost:27017/faculty_db"

        try:
            response = requests.post(api_endpoint, json=faculty_data)
            if response.status_code == 201:
                messagebox.showinfo("Success", "Faculty added successfully.")
                self.show_faculty_data()
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Failed to add faculty: {response.text}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to add faculty: {e}")

    def show_faculty_data(self):
        api_endpoint = "http://localhost:27017/faculty_db"

        try:
            response = requests.get(api_endpoint)
            data = response.json()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in data:
                self.tree.insert("", tk.END, values=(
                    row["faculty_id"], row["faculty_name"], row["faculty_dean"],
                    row["telephone"], row["email"], row["address"], row["subjects"]
                ))

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch faculty data: {e}")

    def display_selected_data(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_data = self.tree.item(selected_item, "values")
            if selected_data and len(selected_data) == 7:
                self.update_button["state"] = tk.NORMAL
                self.delete_button["state"] = tk.NORMAL
                self.selected_item = selected_item

                self.faculty_id.delete(0, tk.END)
                self.faculty_id.insert(0, selected_data[0])

                self.faculty_name.delete(0, tk.END)
                self.faculty_name.insert(0, selected_data[1])

                self.faculty_dean.delete(0, tk.END)
                self.faculty_dean.insert(0, selected_data[2])

                self.phone.delete(0, tk.END)
                self.phone.insert(0, selected_data[3])

                self.email.delete(0, tk.END)
                self.email.insert(0, selected_data[4])

                self.address.delete(0, tk.END)
                self.address.insert(0, selected_data[5])

                # Update the Text widget with the selected subjects
                self.teaching_subjects_text.delete("1.0", tk.END)
                self.teaching_subjects_text.insert("1.0", selected_data[6])

                self.teaching_subjects_text.insert("1.0", selected_data[6])
            else:
                messagebox.showerror("Error", "Selected data does not have the expected format.")
                self.update_button["state"] = tk.DISABLED
                self.delete_button["state"] = tk.DISABLED
        else:
            self.update_button["state"] = tk.DISABLED
            self.delete_button["state"] = tk.DISABLED

    def update_faculty(self):
        selected_item = self.tree.selection()
        if selected_item:
            faculty_id = self.faculty_id.get()
            faculty_name = self.faculty_name.get()
            faculty_dean = self.faculty_dean.get()
            telephone = self.phone.get()
            email = self.email.get()
            address = self.address.get()
            subjects = self.teaching_subjects_text.get("1.0", tk.END)

            if not faculty_id or not faculty_name or not faculty_dean or not telephone or not email or not address:
                messagebox.showerror("Error", "Please fill in all the required fields.")
                return

            updated_faculty_data = {
                "faculty_id": faculty_id,
                "faculty_name": faculty_name,
                "faculty_dean": faculty_dean,
                "telephone": telephone,
                "email": email,
                "address": address,
                "subjects": subjects
            }

            update_api_endpoint = f"http://localhost:27017/faculty_db/{faculty_id}"

            try:
                response = requests.put(update_api_endpoint, json=updated_faculty_data)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Faculty updated successfully.")
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                    self.selected_item = None
                    self.clear_entries(selected_item)
                    self.show_faculty_data()
                else:
                    messagebox.showerror("Error", f"Failed to update faculty: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to update faculty: {e}")
        else:
            messagebox.showinfo("Update", "Please select a row to update.")

    def delete_faculty(self):
        selected_item = self.tree.selection()
        if selected_item:
            faculty_id = self.faculty_id.get()

            delete_api_endpoint = f"http://localhost:2707/faculty_db/{faculty_id}"

            try:
                response = requests.delete(delete_api_endpoint)
                if response.status_code == 200:
                    messagebox.showinfo("Success", "Faculty deleted successfully.")
                    self.tree.delete(selected_item)
                    self.update_button["state"] = tk.DISABLED
                    self.delete_button["state"] = tk.DISABLED
                else:
                    messagebox.showerror("Error", f"Failed to delete faculty: {response.text}")
            except requests.RequestException as e:
                messagebox.showerror("Error", f"Failed to delete faculty: {e}")
        else:
            messagebox.showinfo("Delete", "Please select a row to delete.")

    def clear_entries(self, selected_item=None):
        self.faculty_id.delete(0, tk.END)
        self.faculty_name.delete(0, tk.END)
        self.faculty_dean.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.teaching_subjects_text.delete("1.0", tk.END)

        if selected_item:
            self.tree.selection_remove(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    faculty_tab = FacultyTab(root)
    root.mainloop()
