from tkinter import *
from typing import Counter, NewType
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def create_password():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = [letters[i] for i in range(nr_letters) ] + [numbers[i] for i in range(nr_symbols)]+ [symbols[i] for i in range(nr_symbols)]
    random.shuffle(password_list)
    passwords_str = "".join(password_list)
    return passwords_str


def generator():
    change_password = messagebox.askyesno(title="Generator", message='Do you want to generate password')
    if change_password:
        password_entry.delete(0,END)
        password_entry.insert(0, create_password())



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_():
    web_save = website_entry.get().title()
    email_save = email_entry.get().lower()
    password_save = password_entry.get()

    new_data = {web_save: {
        "Email": email_save,
        "Password": password_save
    }
    }

    if len(web_save) == 0 or len(email_save) == 0 or len(password_save) == 0 :
        messagebox.askokcancel(title='Empty input', message='Make sure you dont have any empty field')

    #is_ok = messagebox.askokcancel(title='Save file', message=f'Email: {email_save} \n Passowrd: {password_save} \n Do you want to save? ')
    elif messagebox.askokcancel(title='Save file', message=f'Email: {email_save} \n Passowrd: {password_save} \n Do you want to save? '):
        try:
            with open(file='save_file.json', mode='r') as file:
                # file.write("Website: " + web_save + "  |  ")
                # file.write("Email: " + email_save + "  |  ")
                # file.write("Password: " + password_save + "|\n")
                data_save = json.load(file)

        except FileNotFoundError:
            with open(file='save_file.json', mode="w") as file:
                json.dump(new_data, file, indent=4)
                # website_entry.delete(0,END)
                # password_entry.delete(0,END)
                # email_entry.delete(0, END)


        else:
            data_save.update(new_data)
            with open(file='save_file.json', mode="w") as file:
                json.dump(data_save, file, indent=4)
                # website_entry.delete(0,END)
                # password_entry.delete(0,END)
                # email_entry.delete(0, END)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            email_entry.delete(0, END)

# ---------------------------- SEARCHING EMAIL/PASSWORD ------------------------------- #
def find_password():
    website_search = website_entry.get().title()
    try:
        with open(file='save_file.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message='No file has found')
    else:
        if website_search in data:
            email = data[website_search]['Email']
            password = data[website_search]['Password']
            messagebox.showinfo(title=website_search, message=f'Email: {email} \nPassword: {password} ')
        else:
            messagebox.showinfo(title="No website", message=f"No details for the {website_search} exists")
        

        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100,image=logo_img)
canvas.grid(column=1,row=0)

#Lables
websites_label = Label(text='Websites:')
websites_label.grid(column=0, row=1)


email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
# email_entry.insert(0, "tranchung163@gmail.com")

password_entry = Entry(width=21, show='*')
password_entry.grid(column=1, row=3)

#Button
password_generator = Button(text='Generate Password', command=generator)
password_generator.grid(column=2, row= 3)

Add_button = Button(text='Add',width=10, command=save_)
Add_button.grid(column=1, row=4)

search_button = Button(text='Search', width=10, command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()