import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinter import Tk, Button, filedialog, Label
from PIL import Image , ImageTk # For image processing
import os,time  # For handling file paths
import os
import csv
from tkinter import Tk, filedialog, messagebox
from tkinter import ttk  # For progress bar (optional)
from PIL import Image
  # For handling image orientation (optional)
import shutil
import os
global treck, image_label,labeltex
image_label=None
treck = False

global name
name=""
def upload_image(name):
    # Open file dialog and get image path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.gif")])

    # Check if user selected a file
    if file_path:
        try:
            # Open the image
            image = Image.open(file_path)

            # Extract filename and extension (assuming a valid path)
            filename, extension = os.path.splitext(file_path)

            # Create a new filename with a unique identifier (timestamp) to avoid overwrites
            new_filename = f"{filename}_{int(time.time())}{extension}"

            # Define the destination folder (replace with your actual path if needed)
            destination_folder = "C:/Users/DELL/Desktop/dorababu project/images"
            
            # Create the full destination path
            new_filename ="image"+str(time.time())
            # destination = os.path.join(destination_folder, new_filename)
            destination=destination_folder+"/"+name+".jpg"
            global image_name
            image_name=destination
            print(new_filename)
            print(destination)
           
            upload_button.config(bg="#90EE90", text="image uploaded", fg="white")

            # Save the image to the destination folder
            image.save(destination)
            print(f"Image uploaded successfully and saved as {destination}")
            labeltex.configure(text="Image uploaded successfully")
            treck=True
        except (OSError, IOError) as e:
            print(f"Error uploading image: {e}")

def delete_image(image_name):
    """
    Deletes the image with the specified name from the given folder.

    Args:
        image_name (str): The name of the image file to delete.

    Returns:
        bool: True if the image was successfully deleted, False otherwise.
    """
    # Specify the folder path where the images are located
    folder_path = r'C:\Users\DELL\Desktop\dorababu project\images'

    # Construct the full path to the image file
    image_path = os.path.join(folder_path, image_name)

    # Check if the image file exists
    if os.path.exists(image_path):
        try:
            # Attempt to delete the image file
            os.remove(image_path)
            print(f"Deleted image: {image_path}")
            return True
        except Exception as e:
            print(f"Error deleting image: {e}")
            return False
    else:
        print(f"Image not found: {image_path}")
        return False
    

def submit_form():
    name = name_entry.get()
    department = department_entry.get()
    roll = roll_entry.get()
    img=labeltex["text"]
    if name and department and roll and img!="No image":
        try:
            with open('atten.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, roll, department])
            tk.messagebox.showinfo("Success", "Student added successfully!")
            root.destroy()
        except FileNotFoundError:
            with open('atten.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Department", "Roll No"]) 
            submit_form()
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields and upload an image.")

def clear_form():
    name = name_entry.get()
    department = department_entry.get()
    roll = roll_entry.get()
    print(name !="" or department!="" or roll!="" and labeltex["text"]=="No image")
    if name =="" and department=="" and roll=="":
         messagebox.showwarning("check fields", "No data to remove")
    elif (name !="" or department!="" or roll!="" )and labeltex["text"]=="No image":
       
        if name !=""  :
            name_entry.delete(0, tk.END)
        if department!="":
            department_entry.delete(0, tk.END)
        if  roll!="":
            roll_entry.delete(0, tk.END)
    
    else:
        upload_button.config(bg="blue", text="upload image", fg="black")
        name_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)
        image_label.config(image=None)
        labeltex.configure(text="No image")
        delete_image(image_name)
        print("working")
        treck = False


def close_window():
    root.destroy()
def check():
    name = name_entry.get()
    department = department_entry.get()
    roll = roll_entry.get()
    if name !="" and department!="" and roll!="":
        upload_image(name+"_"+str(roll))
    else:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields and try to upload an image.")
def create_widgets(parent):
    
    name_label = tk.Label(parent, text="Name:", font=("Arial", 16))
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

    department_label = tk.Label(parent, text="Department:", font=("Arial", 16))
    department_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

    roll_label = tk.Label(parent, text="Roll No:", font=("Arial", 16))
    roll_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
    
    global name_entry, department_entry, roll_entry, image_label
    name_entry = tk.Entry(parent, font=("Arial", 16))
    name_entry.grid(row=0, column=1, padx=10, pady=10)
    
    roll_entry = tk.Entry(parent, font=("Arial", 16))
    roll_entry.grid(row=2, column=1, padx=10, pady=10)
    
    department_entry = tk.Entry(parent, font=("Arial", 16))
    department_entry.grid(row=1, column=1, padx=10, pady=10)

    global labeltex
    labeltex = Label(root, text="No image")
    labeltex.pack()
    print(labeltex["text"])
    name = name_entry.get()
    global upload_button
    upload_button = tk.Button(parent, text="Upload Image", command=check, bg="blue", fg="white")
    upload_button.grid(row=3, column=0, padx=10, pady=10)
 

    image_label = tk.Label(parent)
    image_label.grid(row=4, columnspan=2, padx=10, pady=10)

    submit_button = tk.Button(parent, text="Submit", font=("Arial", 16), command=submit_form, bg="green", fg="white")
    submit_button.grid(row=5, column=0, padx=10, pady=10)

    clear_button = tk.Button(parent, text="Clear", font=("Arial", 16), command=clear_form, bg="orange", fg="white")
    clear_button.grid(row=5, column=1, padx=10, pady=10)
    
    close_button = tk.Button(parent, text="Close", font=("Arial", 16), command=close_window, bg="red", fg="white")
    close_button.grid(row=6, columnspan=2, padx=10, pady=10, sticky='nsew')

def main():
    global root
    root = tk.Tk()
    root.title("Student Information Form")
    
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    
    create_widgets(frame)
    
    root.mainloop()
treck=False