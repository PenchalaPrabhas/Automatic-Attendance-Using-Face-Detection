import tkinter as tk
import csv
from tkinter import messagebox
import sys
import os
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
    
def remove_roll():
    roll_to_remove = roll_entry.get()
    checkk = True
    try:
        updated_data = []
        with open('atten.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            samp=True
            for row in reader:
                if row[1] == roll_to_remove and samp:  # Assuming roll is in the second column
                    checkk = False
                    samp=False
                    tk.messagebox.showinfo("Success", "Roll Number removed successfully!")
                    rmimg=row[0]+"_"+roll_to_remove+".jpg"
                    print(rmimg)
                    delete_image(rmimg)
                    
                else:
                    updated_data.append(row)
            
        # Rewrite the original file with the updated data
        with open('atten.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_data)

        # Clear entry field and display a success message
        roll_entry.delete(0, tk.END)
        if checkk:
            tk.messagebox.showinfo("Sorry", "the roll number is not there")
        root.destroy()
        
    except FileNotFoundError:
        tk.messagebox.showerror("Error", "File 'atten.csv' not found!")
        sys.exit()

def setup_remove_roll_gui():
    global root
    root = tk.Tk()
    root.title("Remove Roll from CSV")

    # Create label and entry field for roll
    roll_label = tk.Label(root, text="Enter Roll No:", font=("Arial", 16))
    roll_label.grid(row=0, column=0, padx=10, pady=10)

    global roll_entry
    roll_entry = tk.Entry(root, font=("Arial", 16))
    roll_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create remove button
    remove_button = tk.Button(
        root, text="Remove Roll Number", font=("Arial", 16), command=remove_roll
    )
    
    remove_button.grid(row=1, columnspan=2, padx=10, pady=10)

    root.mainloop()

