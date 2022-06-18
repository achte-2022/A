# IMPORTING LIBRARIES
import tkinter
from tkinter import messagebox

# CONSTANTS
LOGO_FILE_PATH = "images/logo.png"
LOGO_HEIGHT = 200
LOGO_WIDTH = 200
PASSWORD_DATA_FILE = "data.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# SAVE PASSWORD
def save_password():
    website = website_entry.get()
    id = id_entry.get()
    password = password_entry.get()

    add_message = f"Details:\nEmail: {id}\nPassword: {password}"
    empty_message = "Do not leave fields blank!"

    if (len(website) == 0) or (len(password) == 0) or (len(id) == 0):
        messagebox.showwarning(title="Warning", message=empty_message)
    else:
        is_ok = messagebox.askokcancel(title=website, message=add_message)
        if is_ok:
            data_entry = f"{website} | {id} | {password} \n"
            with open(PASSWORD_DATA_FILE, "a") as file:
                file.write(data_entry)
            website_entry.delete(0, tkinter.END)
            id_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()
    return


# UI SETUP
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# CANVAS
canvas = tkinter.Canvas(width=LOGO_WIDTH, height=LOGO_HEIGHT)
logo = tkinter.PhotoImage(file=LOGO_FILE_PATH)
canvas.create_image(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, image=logo)
canvas.grid(row=0, column=1)

# WEBSITE LABEL
website_label = tkinter.Label(text="Website:")
website_label.focus()
website_label.grid(row=1, column=0)

# ID LABEL
id_label = tkinter.Label(text="Email/Username:")
id_label.grid(row=2, column=0)

# PASSWORD LABEL
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# WEBSITE ENTRY
website_entry = tkinter.Entry()
website_entry.grid(row=1, column=1)

# ID ENTRY
id_entry = tkinter.Entry()
id_entry.insert(0, "abc@xyz.com")
id_entry.grid(row=2, column=1)

# PASSWORD ENTRY
password_entry = tkinter.Entry()
password_entry.grid(row=3, column=1)

# PASSWORD GENERATOR BUTTON
password_button = tkinter.Button(text="Generate Password")
password_button.grid(row=3, column=2)

# ADD BUTTON
add_button = tkinter.Button(text="Add", command=save_password)
add_button.grid(row=4, column=1)

window.mainloop()
