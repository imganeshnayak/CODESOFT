#import packages
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
#create entry box
ent = tk.Entry(root, width=63, borderwidth=5, bg="grey",font=("Arial",10,"bold"))
ent.grid(row=0, column=1)

#ask us3r to enter task
def addTask():
    try:
        lst.insert(tk.END, txt,).reverse()
        ent.delete(0, tk.END)
    except:
        ent.delete(0, tk.END)

#check for empty input
def check():
     global txt
     txt = ent.get()
     if txt == "":
         messagebox.showerror("Error", "Please enter a task")
     else:
         addTask()

from tkinter import simpledialog

def edit_selected_task():
    # Get the selected index
    selected_index = lst.curselection()
    
    if selected_index:
        # Get the selected text
        selected_task = lst.get(selected_index)
        
        # Open a dialog to edit the text
        new_text = simpledialog.askstring("Edit Text", "Enter new text", initialvalue=selected_task)
        
        if new_text is not None:
            # Update the Listbox with the new text
            lst.delete(selected_index)
            lst.insert(selected_index, new_text)



#clear all the tasks
def clear():
    lst.delete(0, tk.END)

#delete the selected task
def deleteTask():
    try:
        temp=lst.curselection()        

        lst.delete(temp)
    except:
        pass

    #create window
root.geometry("550x600")
root.title("TO-DO List")

#create list box
lst = tk.Listbox(root, width=50, height=20, borderwidth=4,bg="pink",font=("Arial",13,"bold"),fg="black",)
lst.grid(row=1, column=1)

#create button frame
btn_frame = tk.Frame(root)
btn_frame.grid(row=5, column=1)

#add task button
add_btn = tk.Button(root, width=10, text="Add Task", command=check,bg="green")
add_btn.grid(column=2,row=0)

#edit button
edit_button = tk.Button(btn_frame, text="Edit Selected Task", bg="purple",command=edit_selected_task)
edit_button.pack(side=tk.LEFT,pady=10,padx=10)

#delete button
del_btn = tk.Button(btn_frame, width=10, text="Delete", command=deleteTask,bg="blue")
del_btn.pack(side=tk.LEFT,pady=10,padx=10)

#clear button
clr_btn = tk.Button(btn_frame, width=10, text="Clear all", command=clear,bg="red")
clr_btn.pack(side=tk.LEFT,pady=10,padx=10)
root.mainloop()
