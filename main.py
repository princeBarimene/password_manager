from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height = 200)



lock_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column=1, row=0)


#create labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


#create inputs
website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=26)
password_input.grid(column=1, row=3)


#creating buttons

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()


