

import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = {}

        # Create GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Layout GUI components
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        self.address_label.grid(row=3, column=0)
        self.address_entry.grid(row=3, column=1)
        self.add_button.grid(row=4, column=0)
        self.view_button.grid(row=4, column=1)
        self.search_button.grid(row=5, column=0)
        self.update_button.grid(row=5, column=1)
        self.delete_button.grid(row=6, column=0)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        contact_list = ""
        for name, details in self.contacts.items():
            contact_list += f"{name}: {details['phone']}\n"
        messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            details = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found in the list.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found in the list.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Contact Not Found", "Contact not found in the list.")

root = tk.Tk()
contact_manager = ContactManager(root)
root.mainloop()

