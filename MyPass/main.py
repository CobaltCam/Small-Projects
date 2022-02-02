from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generate a password for the user. Bound to generate button.
def gen_password():
    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
                                                                                                                  'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]

    symbols = [
    '!', '@', '$', '#', '%', '&', '*', '(', ')', '-', '+', '/', '.', '=', '~'
    ]

    password_letters = [choice(letters) for _ in range(0, randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(0, randint(2, 6))]
    password_symbols = [choice(symbols) for _ in range(0, randint(2, 6))]
    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function used to save new credentials to mypass.txt. Bound to add_button.
def save_credentials():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showerror(title="Empty Field Error", message="You have left a field empty. Please fill in all"
                                                                "fields")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite:{website}\nEmail: "
                                                          f"{email}\nPassword: {password}")
    if is_ok:
        with open("mypass.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(pady=50, padx=50)

# Image
lock = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, )
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Create buttons
add_button = Button(text="Add", font=("Courier", 12, "bold"), width=36, command=save_credentials)
generate_button = Button(text="Generate", font=("Courier", 12, "bold"), command=gen_password)
add_button.grid(column=1, row=4, columnspan=2)
generate_button.grid(column=2, row=3, columnspan=2)

# Create labels/text
website_label = Label(text="Website:", font=("Courier", 12, "normal"))
email_label = Label(text="Email/Username:", font=("Courier", 12, "normal"))
password_label = Label(text="Password:", font=("Courier", 12, "normal"))
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Create Input boxes
website_entry = Entry(width=45)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=45)
email_entry.insert(0, "youremail@email.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

window.mainloop()
