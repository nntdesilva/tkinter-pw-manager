from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)


def clear_inputs():
    website_input.delete(0, 'end')
    password_input.delete(0, 'end')


def save_details():
    website = website_input.get()
    email = email_input.get()
    pw = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": pw
        }
    }
    if not len(website) or not len(pw):
        messagebox.showwarning(title="Warning", message="Some fields are empty!")
    else:
        try:
            with open('details.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('details.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('details.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            clear_inputs()


def find_password():
    website = website_input.get()
    if not len(website):
        messagebox.showwarning(title="Warning", message="Enter website name")
    else:
        try:
            with open('details.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found")
        else:
            result = data.get(website)
            if result:
                messagebox.showinfo(title=website, message=f"Email: {result['email']}\nPassword: {result['password']}")
            else:
                messagebox.showerror(title="Uh, Oh", message=f"No details for {website} exists")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
# website input
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
# search button
gen_pw = Button(text="Search", width=13, command=find_password)
gen_pw.grid(row=1, column=2)
# email/username label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
# email/username input
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "nilakshinavoda97@gmail.com")
# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
# password input
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
# generate pw button
gen_pw = Button(text="Generate Password", command=generate_password)
gen_pw.grid(row=3, column=2)
# add button
add = Button(text="Add", width=36, command=save_details)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
