def menu():
    root = tk.Tk()

    root.geometry("500x300")
    root.title("Menu")

    label = tk.Label(root, text="Menu", font=('Arial_Black', 24))
    label.pack(padx=20, pady=20)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)

    register_button = tk.Button(buttonframe, text="Register",command=lambda:account_type, height=2, width=10, font=('Arial_Black', 16))
    login_button = tk.Button(buttonframe, text="Login", height=2, width=10, font=('Arial_Black', 16))

    login_button.grid(row=0, column=0)
    register_button.grid(row=0, column=1)

    buttonframe.pack(padx=100,pady=20,fill='x')
    root.mainloop()

class Menu:

    def __init__(self):

        self.root = tk.Tk()

        self.geometry("500x300")
        self.title("Menu")

        self.label = tk.Label(self.root, text="Menu", font=('Arial_Black', 24))
        self.pack(padx=20, pady=20)

        buttonframe = tk.Frame(self.root)
        self.columnconfigure(0, weight=1)

        self.register_button = tk.Button(buttonframe, text="Register", height=2, width=10,
                                    font=('Arial_Black', 16))
        self.login_button = tk.Button(buttonframe, text="Login", height=2, width=10, font=('Arial_Black', 16))

        self.login_button.grid(row=0, column=0)
        self.register_button.grid(row=0, column=1)

        buttonframe.pack(padx=100, pady=20, fill='x')
        self.mainloop()




menu()


def register():
    username = username_entry.get()
    password = password_entry.get()
    try:
        email = email.entry.get()
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            try:
                with open("user_data.json", 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = {}

            data[username] = password
            data[email] = password

            with open("user_data.json", 'w') as file:
                json.dump(data, file)
        else:
            raise ValueError
    except ValueError:
        result_label.config(text="Invalid Email")
    result_label.config(text="Registration successful!")

    #UI for the register menu
    root = tk.Tk()

    root.title("User Registration")


    label = tk.Label(root, text="User Registration", font=('Arial_Black', 24))
    label.pack(padx=20, pady=20)

    username_label = tk.Label(root, text="Username:")
    username_entry = tk.Entry(root)
    password_label = tk.Label(root, text="Password:")
    password_entry = tk.Entry(root, show="*")
    email_label = tk.Label(root, text="Email:")
    email_entry = tk.Entry(root)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    register_button = tk.Button(buttonframe, text="Register", command=register)

    buttonframe.pack(padx=100, pady=20, fill='x')

    result_label = tk.Label(root, text="")

    username_label.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)
    email_label.grid(row=2, column=0)
    email_entry.grid(row=2, column=1)
    register_button.grid(row=3, column=0)
    result_label.grid(row=4, columnspan=2)

    class stats:
        def ___int___(self, hp, Dmg, Speed):
            self.hp = hp
            self.Dmg = Dmg
            slef.Speed = Speed

        def haste_effect(self):
            self.speed += 2

    character = stats(100, 20, 10)
    # this is not a userinput variables which means can be change on later codes
    # example for printing stats

    print(f"character speed: (character.speed)")

    # The output will be "character speed: 10"

    character.haste_effect()
    print(f"character speed: (character.speed)")
    # The output will be "character speed: 20"
import json
import tkinter as tk
import re


# main menu button
class Main_Menu:
    def __init__(self, option):
        self.root = tk.Tk()

        self.root.geometry("500x300")
        self.root.title("Menu")

        self.label = tk.Label(self.root, text="Menu", font=('Arial_Black', 24))
        self.label.pack(padx=20, pady=20)

        buttonframe = tk.Frame(self.root)
        buttonframe.columnconfigure(0, weight=1)

        self.register_button = tk.Button(buttonframe, text="Register",command=lambda: [self.root.destroy(), self.account_type()],height=2, width=10, font=('Arial_Black', 16))
        self.login_button = tk.Button(buttonframe, text="Login",command=lambda: [self.root.destroy(), self.account_type()], option="login",height=2, width=10, font=('Arial_Black', 16))

        self.login_button.grid(row=0, column=0)
        self.register_button.grid(row=0, column=1)

        buttonframe.pack(padx=100, pady=20, fill='x')
        self.root.mainloop()
        self.Option = option

    def account_type(self):
        self.root = tk.Tk()

        self.root.geometry("500x300")
        self.root.title("Account Type")

        self.label = tk.Label(self.root, text="Account Type", font=('Arial_Black', 24))
        self.label.pack(padx=20, pady=20)

        self.admin = tk.Button(self.root, text="Admin", height=2, width=10, font=('Arial_Black', 16))
        self.employee = tk.Button(self.root, text="Employee", height=2, width=10, font=('Arial_Black', 16))
        self.user = tk.Button(self.root, text="User",command=lambda: [self.root.destroy(), ], height=2, width=10, font=('Arial_Black', 16))
        self.back = tk.Button(self.root, text="<-", command=lambda: [self.root.destroy(), self.__init__()], height=2,width=10, font=('Arial_Black', 16))

        self.admin.place(x=100, y=100, height=50, width=100)
        self.employee.place(x=210, y=100, height=50, width=100)
        self.user.place(x=320, y=100, height=50, width=100)
        self.back.place(x=10, y=260, height=30, width=60)
Main_Menu()


def register_account_type(self):
    self.root = tk.Tk()

    self.root.geometry("500x300")
    self.root.title("Account Type")

    self.label = tk.Label(self.root, text="Account Type", font=('Arial_Black', 24))
    self.label.pack(padx=20, pady=20)

    self.admin = tk.Button(self.root, text="Admin", height=2, width=10, font=('Arial_Black', 16))
    self.employee = tk.Button(self.root, text="Employee", height=2, width=10, font=('Arial_Black', 16))
    self.user = tk.Button(self.root, text="User", command=lambda: [self.root.destroy(), self], height=2, width=10,
                          font=('Arial_Black', 16))
    self.back = tk.Button(self.root, text="<-", command=lambda: [self.root.destroy(), self.registration_Account_UI()],
                          height=2,
                          width=10, font=('Arial_Black', 16))

    self.admin.place(x=100, y=100, height=50, width=100)
    self.employee.place(x=210, y=100, height=50, width=100)
    self.user.place(x=320, y=100, height=50, width=100)
    self.back.place(x=10, y=260, height=30, width=60)

    self.root.mainloop()

