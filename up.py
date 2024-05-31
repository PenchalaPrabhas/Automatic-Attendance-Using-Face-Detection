
import pandas as pd
import hash
import tkinter as tk
from tkinter import messagebox
def create_gui():
    def button_click():                        #submit
       passc = entry.get()   # Get text from the label
       print(passc)
       if not passc:
            messagebox.showerror("Error", "Label is empty!")
       else:
        passc = entry.get()  # Get the value from the input field
        passcode=hash.hash_string(passc)
        print("Passcode entered:", passcode)
        try:
            df = pd.read_csv('codes.csv')
        except FileNotFoundError:
        
            df = pd.DataFrame(columns=['passcodes'])
        
        
        
        
        
        if passcode in df['passcodes'].values:
            messagebox.showerror("Error", "password is already There,choose another")
        else:
            messagebox.showinfo("task", "password is added")
            new_row = pd.DataFrame({'passcodes': [passcode]})
            df = pd.concat([df, new_row], ignore_index=True)
    
            df.to_csv('codes.csv', index=False)


       root.destroy()



    def clear_input():              #delete
     passcode_to_delete = entry.get()  # Get text from the label

     if not passcode_to_delete:
        messagebox.showerror("Error", "Label is empty!")
     else:
      passcode_to_delete=hash.hash_string(passcode_to_delete)
      try:
        # Read the CSV file
        df = pd.read_csv('codes.csv')

        # Check if the passcode exists in the DataFrame
        if passcode_to_delete in df['passcodes'].values:
            # Remove the row containing the passcode
            df = df[df['passcodes'] != passcode_to_delete]

            # Write the updated DataFrame back to the CSV file
            df.to_csv('codes.csv', index=False)
            messagebox.showinfo("Task done", "password deleted")
        else:
            messagebox.showerror("Error", "password not found")
      except FileNotFoundError:
        print("CSV file 'codes.csv' not found.")
     root.destroy()
    
    

    def on_enter(e):
        original_color = e.widget.cget("bg")  # Get the original background color
        e.widget.config(bg="lightblue")
        e.widget.bind("<Leave>", lambda event, color=original_color: on_leave(event, color))

    def on_leave(e, color):
        e.widget.config(bg=color)

    root = tk.Tk()
    root.title("Key Management")
    root.geometry("300x300")

    # Create a frame for better organization
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    # Create a label
    label = tk.Label(frame, text="Enter Passcode:")
    label.grid(row=0, column=0, sticky="w")

    # Create an entry field
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=10)

    # Create a button to submit passcode
    submit_button = tk.Button(frame, text="Add Key", command=button_click, bg="orange")
    submit_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
    submit_button.bind("<Enter>", on_enter)

    # Create a button to clear the input field
    clear_button = tk.Button(frame, text="Remove Key", command=clear_input, bg="lightgreen")
    clear_button.grid(row=2, column=0, columnspan=2, sticky="ew")
    clear_button.bind("<Enter>", on_enter)

    root.mainloop()

