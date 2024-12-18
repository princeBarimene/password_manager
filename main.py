from tkinter import *
from tkinter import messagebox
from random import randint,choice, shuffle
import pyperclip
import json



global website




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    letters_list = [choice(letters) for char in range(randint(8, 10))]

    symbols_list = [choice(symbols) for char in range(randint(2, 4))]

    numbers_list = [choice(numbers) for char in range(randint(2, 4))]


    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)


    password_input.insert(0,password)
    pyperclip.copy(password)


    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password":password,
        }
    }

    if not website or not password:
        messagebox.showerror(title="Opps", message="Please do not leave any fields empty!")

    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
                

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent = 4)
        
        else:
            data.update(new_data)

            with open("data.json", mode="w") as file:
                json.dump(data,file, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)



# search the database and retrieve info#


def find_password():
    website = website_input.get()

    try:
        with open("data.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:        
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")

       




def clear_entry():
    website_input.delete(0,END)
    password_input.delete(0,END)
      
    
       


            

    

    

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
website_input = Entry(width=26)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"olubari.prince.g@gmail.com")

password_input = Entry(width=26)
password_input.grid(column=1, row=3)


#creating buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password,width=15)
search_button.grid(column=2, row=1)

clear_button = Button(text="Clear", width=42, command=clear_entry)
clear_button.grid(column=1, row=5, columnspan=2)





window.mainloop()


