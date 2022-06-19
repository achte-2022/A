# IMPORTING LIBRARIES
import tkinter
from tkinter import messagebox
import random
# import pyperclip
import json


# CONSTANTS
LOGO_FILE_PATH = "images/logo.png"
LOGO_HEIGHT = 200
LOGO_WIDTH = 200
PASSWORD_DATA_FILE = "data.json"
ORANGE = "#F15412"
BLACK = "#000000"
BLUE = "#34B3F1"
FONT = ("Courier", 15, "bold")
LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# PASSWORD GENERATOR
def password_generator():
    password_entry.delete(0, tkinter.END)
    num_letters = random.randint(6, 10)
    num_symbols = random.randint(2, 6)
    num_numbers = random.randint(2, 6)

    letter_list = [random.choice(LETTERS) for i in range(num_letters)]
    symbol_list = [random.choice(SYMBOLS) for i in range(num_symbols)]
    number_list = [random.choice(NUMBERS) for i in range(num_numbers)]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)
    return


# SAVE PASSWORD
def save_password():
    website = website_entry.get().title()
    id = id_entry.get()
    password = password_entry.get()

    data_json = {
        website: {
            "Email": id,
            "Password": password,
        }
    }
    add_message = f"Details:\nEmail: {id}\nPassword: {password}"
    empty_message = "Do not leave the fields blank!"

    if (len(website) == 0) or (len(password) == 0) or (len(id) == 0):
        messagebox.showwarning(title="Warning", message=empty_message)
    else:
        is_ok = messagebox.askokcancel(title=website, message=add_message)
        if is_ok:
            try:
                with open(PASSWORD_DATA_FILE, "r") as file:
                    data = json.load(file)
                    data.update(data_json)

                with open(PASSWORD_DATA_FILE, "w") as file:
                    json.dump(data, file, indent=4)
            except:
                with open(PASSWORD_DATA_FILE, "w") as file:
                    json.dump(data_json, file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                id_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
                website_entry.focus()
    return


# SEARCH DATA
def find_password():
    website = website_entry.get().title()
    empty_message = "Do not leave the fields blank!"
    no_file_message = ".JSON File not found."
    key_message = "No Data Found."
    if len(website) == 0:
        messagebox.showwarning(title="Warning", message=empty_message)
    else:
        try:
            with open(PASSWORD_DATA_FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Warning", message=no_file_message)
        else:
            try:
                data_entry = data[website]
            except KeyError:
                messagebox.showwarning(title="Warning", message=key_message)
            else:
                id = data_entry["Email"]
                password = data_entry["Password"]
                entry_message = f"Details:\nEmail: {id}\nPassword: {password}"
                messagebox.showinfo(title="Entry Found", message=entry_message)
    return


# UI SETUP
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=BLUE)

# CANVAS
canvas = tkinter.Canvas(
    width=LOGO_WIDTH, height=LOGO_HEIGHT, bg=BLUE, highlightthickness=0
)
logo = tkinter.PhotoImage(file=LOGO_FILE_PATH)
canvas.create_image(LOGO_WIDTH / 2, LOGO_HEIGHT / 2, image=logo)
canvas.grid(row=0, column=1)

# WEBSITE LABEL
website_label = tkinter.Label(text="Website:", font=FONT, bg=BLUE, fg=ORANGE)
website_label.focus()
website_label.grid(row=1, column=0)

# ID LABEL
id_label = tkinter.Label(text="Email/Username:", font=FONT, bg=BLUE, fg=ORANGE)
id_label.grid(row=2, column=0)

# PASSWORD LABEL
password_label = tkinter.Label(text="Password:", font=FONT, bg=BLUE, fg=ORANGE)
password_label.grid(row=3, column=0)

# WEBSITE ENTRY
website_entry = tkinter.Entry(width=40)
website_entry.grid(row=1, column=1)

# ID ENTRY
id_entry = tkinter.Entry(width=40)
id_entry.insert(0, "abc@xyz.com")
id_entry.grid(row=2, column=1)

# PASSWORD ENTRY
password_entry = tkinter.Entry(width=40)
password_entry.grid(row=3, column=1)

# PASSWORD GENERATOR BUTTON
password_button = tkinter.Button(
    text="Generate Password", command=password_generator, font=FONT, bg=BLUE, fg=BLACK
)
password_button.grid(row=4, column=2)

# ADD BUTTON
add_button = tkinter.Button(
    text="Add", command=save_password, font=FONT, bg=BLUE, fg=BLACK
)
add_button.grid(row=4, column=1)

# SEARCH BUTTON
search_button = tkinter.Button(
    text="SEARCH", command=find_password, font=FONT, bg=BLUE, fg=BLACK
)
search_button.grid(row=2, column=2)

window.mainloop()
