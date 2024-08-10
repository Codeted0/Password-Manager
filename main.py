from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)



#-----------------------------find password----------------------------------#



def find_pass():
    website = web_entry.get()
    try:
        with open("password_ata.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!", message="NO Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="ERROR", message=f"NO details for {website} exists!")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_entry.get()
    mail = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "Email": mail,
            "Password": password,
        }

    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("password_ata.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_ata.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("password_ata.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
image_png = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image_png)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

web_entry = Entry(width=31)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, '@gmail.com')
pass_entry = Entry(width=31)
pass_entry.grid(row=3, column=1)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
pass_button = Button(text='Generate', command=generate_pass)
pass_button.grid(row=3, column=2)
search_button = Button(text=' Search ', command=find_pass)
search_button.grid(row=1, column=2)

window.mainloop()
