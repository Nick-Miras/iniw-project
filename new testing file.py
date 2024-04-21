import json
import tkinter as tk
import re
#main menu button
class Account:
    def __init__(self, username, password, email, phone):
        self.username = username.get()
        self.password = password.get()
        self.email = email.get()
        self.phone = phone.get()

        try:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(email_pattern, email):
                try:
                    with open("user_data.json", "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}

                data[username] = {
                    "password": password,
                    "email": email,
                    "phone": phone
                }

                with open("user_data.json", "w") as file:
                    json.dump(data, file)
            else:
                raise ValueError
        except ValueError:
            self.result_label.config(text="Invalid Email")
            return

class Account_Type(Account):
    def register_account_type(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Account Type")

        self.label = tk.Label(self.root, text="Account Type", font=('Arial_Black', 24))
        self.label.pack(padx=20, pady=20)

        self.admin = tk.Button(self.root, text="Admin", height=2, width=10, font=('Arial_Black', 16))
        self.employee = tk.Button(self.root, text="Employee", height=2, width=10, font=('Arial_Black', 16))
        self.user = tk.Button(self.root, text="User", command=self.register, height=2, width=10, font=('Arial_Black', 16))
        self.back = tk.Button(self.root, text="<-", command=self.registration_Account_UI, height=2,
                              width=10, font=('Arial_Black', 16))

        self.admin.place(x=100, y=100, height=50, width=100)
        self.employee.place(x=210, y=100, height=50, width=100)
        self.user.place(x=320, y=100, height=50, width=100)
        self.back.place(x=10, y=260, height=30, width=60)

        self.root.mainloop()

# Create an instance of the Account_Type class


class Registrattion_menu:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("500x300")
        self.root.title("Menu")

        self.label = tk.Label(self.root, text="Menu", font=('Arial_Black', 24))
        self.label.pack(padx=20, pady=20)

        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)

        self.register_button = tk.Button(buttonframe, text="Register",command=lambda: [self.root.destroy(), self.registration_Account_UI()], height=2, width=10, font=('Arial_Black', 16))
        self.login_button = tk.Button(buttonframe, text="Login",command=lambda: [self.root.destroy()], height=2, width=10, font=('Arial_Black', 16))

        self.login_button.grid(row=0, column=0)
        self.register_button.grid(row=0, column=1)

        buttonframe.pack(padx=100,pady=20,fill='x')
        self.root.mainloop()
    def registration_Account_UI(self):
        self.root = tk.Tk()
        self.root.title("User Registration and Login")

        self.root.geometry("300x200")
        self.label = tk.Label(self.root, text="Account Registration", font=('Arial_Black', 24))
        self.label.grid(row=0,columnspan=3)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Password:")
        self.password = tk.Entry(self.root, show="*")
        self.email_label = tk.Label(self.root, text="Email:")
        self.email = tk.Entry(self.root)
        self.name_label = tk.Label(self.root, text="Name:")
        self.name = tk.Entry(self.root)
        self.phone_label = tk.Label(self.root, text="Phone Number:")
        self.phone = tk.Entry(self.root)

        self.register_button = tk.Button(self.root, text="Register", command=lambda:[self.root.destroy(), Account_Type()])

        self.result_label = tk.Label(self.root, text="")

        self.username_label.grid(row=3, column=1)
        self.username.grid(row=3, column=2)
        self.password_label.grid(row=4, column=1)
        self.password.grid(row=4, column=2)
        self.register_button.grid(row=8, column=2)
        self.email_label.grid(row=5, column=1)
        self.email.grid(row=5, column=2)
        self.password_label.grid(row=6, column=1)
        self.password.grid(row=6, column=2)
        self.phone_label.grid(row=7, column=1)
        self.phone.grid(row=7, column=2)

        self.root.mainloop()
Registrattion_menu()

def man():
