# IMPORTING LIBRARIES
from email.mime import image
import tkinter
from turtle import width

# CONSTANTS
LOGO_FILE_PATH = "images/logo.png"
LOGO_HEIGHT = 200
LOGO_WIDTH = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# UI SETUP
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# CANVAS
canvas = tkinter.Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT)
logo = tkinter.PhotoImage(file=LOGO_FILE_PATH)
canvas.create_image(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, image=logo)
canvas.grid(row=0, column=1)

# WEBSITE LABEL
website_label = tkinter.Label(text="Website")
website_label.grid(row=1, column=0)

# WEBSITE ENTRY
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# ID LABEL
id_label = tkinter.Label(text="Email/Username:")
id_label.grid(row=2, column=0, columnspan=1)

# ID ENTRY
id_entry = tkinter.Entry(width=21)
id_entry.grid(row=2, column=1)

# PASSWORD LABEL
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# PASSWORD ENTRY
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

# PASSWORD BUTTON
password_button = tkinter.Button(text="Generate Password")
password_button.grid(row=3, column=2)

# ADD BUTTON
add_button = tkinter.Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
