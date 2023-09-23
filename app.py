# Import the tkinter module
import tkinter as tk

# Define a function to retrieve the text written by the user
def clicked():
    # Get the text from the input field and create a message
    res = "You wrote " + txt.get()
    # Set the label's text to the message
    lbl.config(text=res)

# Create the main window
root = tk.Tk()

# Set the title and size of the main window
root.title("Mind Reader")
root.geometry('350x200')

# Create and add a label to the main window
lbl = tk.Label(root, text="Think a word")
lbl.grid(column=0, row=0)

# Create and add a text entry field to the main window
txt = tk.Entry(root, width=10)
txt.grid(column=1, row=0)

# Create a button with specific text and a function to execute when clicked
btn = tk.Button(root, text="OK", fg="red", command=clicked)
# Set the button's location in the main window
btn.grid(column=2, row=0)

# Start the main tkinter loop
root.mainloop()
