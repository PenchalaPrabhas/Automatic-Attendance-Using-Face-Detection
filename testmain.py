import tkinter as tk

import hash
import remove1
import video
import help1
import up
# Create the main window
root11 = tk.Tk()
root11.title("Attendance System")
global entry
entry = tk.Entry(root11, show="*", bg="lightgray", fg="black")
entry.place(x=10, y=10)  
def attendance():
    video.facial_recognition()

def button_click():
    input_text = entry.get()
    print(input_text)
    z=hash.main(input_text)
    if z:
        up.create_gui()
def clear():
    entry.delete(0, 'end')
    
def checkinput(a):
    input_text = entry.get()
    print(input_text)
    z=hash.main(input_text)
    if z:
        if a=="register":
            help1.main()
        else:
            remove1.setup_remove_roll_gui()
def sender():
    checkinput("register")
def deleter():
    checkinput("register11")
screen_width = root11.winfo_screenwidth()
screen_height = root11.winfo_screenheight()

# Set the window dimensions to cover the entire screen
root11.geometry(f"{screen_width}x{screen_height}")
button = tk.Button(root11, text="add keys", command=button_click)

# Pack the button to the bottom right corner
button.pack(side="bottom", anchor="se", pady=10)

button2 = tk.Button(root11, text="clear", command=clear)

# Pack the button to the bottom right corner
button2.pack(side="bottom", anchor="se")

# Create a frame to hold the buttons
button_frame = tk.Frame(root11, bg="gray")
button_frame.place(relx=0.5, rely=0.5, anchor="center")

# Register button
register_button = tk.Button(button_frame, text="Register", font=("Arial", 24), bg="green", fg="white", padx=40, pady=20,command=sender)
register_button.grid(row=0, column=0, padx=50)

# Attendance button
attendance_button = tk.Button(button_frame, text="Attendance", font=("Arial", 24), bg="blue", fg="white", padx=40, pady=20, command=attendance)
attendance_button.grid(row=0, column=1, padx=50)

# Remove button
remove_button = tk.Button(button_frame, text="Remove", font=("Arial", 24), bg="red", fg="white", padx=40, pady=20,command=deleter)
remove_button.grid(row=0, column=2, padx=50)
# Set background color and text color


# Start the main event loop
root11.mainloop()