from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) > 0 and len(password) > 0 and len(email) > 0:
        is_ok = messagebox.askokcancel(title=website, message="These are the" 
                               f"details entered:\nEmail: {email}"
                               f"\n Password: {password}\n"
                               "Is this ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_input.get()} | {email_input.get()} |"
                                f"{password_input.get()}\n")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showerror(title="You dumbo", message="Don't leave any of the"
                             " fields empty!!!\nI get angry when u do!!!!!!!!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
manager_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=manager_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
