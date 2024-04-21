import json
import tkinter as tk
import re

FONT_NAME = 'Arial_Black'
BUTTON_FONT_SIZE = 16
TITLE_FONT_SIZE = 24
BUTTON_FONT = (FONT_NAME, BUTTON_FONT_SIZE)
TITLE_FONT = (FONT_NAME, TITLE_FONT_SIZE)
COMMON_BUTTON_WIDTH = 10
COMMON_BUTTON_HEIGHT = 2
DATABASE_FILE_NAME = 'user_data.json'


#main menu button
class Account:
    def __init__(self, username, password, email, phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone


class Admin(Account):
    def __init__(self, username, password, email, phone):
        super().__init__(username, password, email, phone)
        self.admin_username = username
    def to_dict(self):
        return {
                "username": self.username,
                "password": self.password,
                "email": self.admin_email,
                "phone": self.admin_phone
                }


class BetterAccount:
    def __init__(self, username, password, email, phone):
        self.username = self.verify_username(username)
        self.password = self.verify_password(password)
        self.email = self.verify_email(email)
        self.phone = self.verify_phone(phone)

    @staticmethod
    def verify_username(username):
        return username

    @staticmethod
    def verify_password(password):
        return password

    @staticmethod
    def verify_email(email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            return email
        else:
            raise SyntaxError('Invalid Email')

    @staticmethod
    def verify_phone(phone):
        return phone

    def add_to_database(self, file_path=DATABASE_FILE_NAME):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
            
        data[self.username] = {
            "password": self.password,
            "email": self.email,
            "phone": self.phone
        }
        with open(file_path, "r") as file:
            json.dump(data, file)


#Account Creator for admin boiiii
class Account_Creator:
    @staticmethod
    def create_admin():
        admin_username = username_entry.get()
        admin_password = password_entry.get()
        admin_email = email_entry.get()
        admin_phone = phone_entry.get()

        try:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(email_pattern, admin_email):
                try:
                    with open("user_data.json",  "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}

                data[admin_username] = {
                    "password": admin_password,
                    "email": admin_email,
                    "phone": admin_phone
                }

                with open("user_data.json", "w") as file:
                    json.dump(data, file)

                root.destroy()
            else:
                invalid_email_label.config(text="Invalid Email")
        except Exception as e:
            print("An error occurred:", e)

    def registration_Account_UI_admin(self):
        try:
            global root, username_entry, password_entry, email_entry, phone_entry, invalid_email_label

            root = tk.Tk()
            root.title("Admin Registration")
            root.geometry("300x200")

            username_label = tk.Label(root, text="Username:")
            username_label.grid(row=3, column=1)
            username_entry = tk.Entry(root)
            username_entry.grid(row=3, column=2)

            password_label = tk.Label(root, text="Password:")
            password_label.grid(row=4, column=1)
            password_entry = tk.Entry(root, show="*")
            password_entry.grid(row=4, column=2)

            email_label = tk.Label(root, text="Email:")
            email_label.grid(row=5, column=1)
            email_entry = tk.Entry(root)
            email_entry.grid(row=5, column=2)

            invalid_email_label = tk.Label(root, text="", fg="red")
            invalid_email_label.grid(row=9, column=2)

            phone_label = tk.Label(root, text="Phone Number:")
            phone_label.grid(row=6, column=1)
            phone_entry = tk.Entry(root)
            phone_entry.grid(row=6, column=2)

            register_button = tk.Button(root, text="Register", command=self.create_admin)
            register_button.grid(row=10, column=2)

            root.mainloop()
        except Exception as e:
            print("An error occurred:", e)

    def login_admin(self):
        admin_username = username_entry.get()
        admin_password = password_entry.get()

        # Load user data from JSON file
        try:
            with open("user_data.json", "r") as file:
                data = json.load(file)
                if admin_username in data and data[admin_username]["password"] == admin_password:
                    result_label.config(text="Login successful!", fg="green")
                else:
                    result_label.config(text="Invalid username or password", fg="red")
        except FileNotFoundError:
            result_label.config(text="No registered users yet")
    #UI for admin log in
    def login_admin_UI(self):
        try:
            global root, username_entry, password_entry, email_entry, phone_entry,result_label
            root = tk.Tk()
            root.title("User Registration")
            root.geometry("300x200")

            username_label = tk.Label(root, text="Username:")
            username_label.grid(row=3, column=1)
            username_entry = tk.Entry(root)
            username_entry.grid(row=3, column=2)

            password_label = tk.Label(root, text="Password:")
            password_label.grid(row=4, column=1)
            password_entry = tk.Entry(root, show="*")
            password_entry.grid(row=4, column=2)

            result_label = tk.Label(root, text="")
            result_label.grid(row=5, column=2)

            login_button = tk.Button(root, text="Login", command=self.login_admin)
            login_button.grid(row=10, column=2)

            root.mainloop()
        except Exception as e:
            print("An error occurred:", e)


def Accunt_Type_register():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Account Type")

    label = tk.Label(root, text="Account Type", font=TITLE_FONT)
    label.pack(padx=20, pady=20)

    admin = tk.Button(
        root, 
        text="Admin",
        command=lambda: [root.destroy(), Account_Creator().registration_Account_UI_admin()], 
        height=2, 
        width=10, 
        font=BUTTON_FONT
    )
    employee = tk.Button(
        root, 
        text="Employee",
        command=lambda: [root.destroy(), Account_Creator()], 
        height=2, 
        width=10, 
        font=BUTTON_FONT
    )
    user = tk.Button(
        root, 
        text="User", 
        command=lambda: [root.destroy(), Account_Creator()], 
        height=2, 
        width=10,
        font=BUTTON_FONT
    )
    back = tk.Button(
        root, 
        text="<-", 
        command=lambda: [root.destroy(), main()],
        height=2,
        width=10, 
        font=BUTTON_FONT
    )

    admin.place(x=100, y=100, height=50, width=100)
    employee.place(x=210, y=100, height=50, width=100)
    user.place(x=320, y=100, height=50, width=100)
    back.place(x=10, y=260, height=30, width=60)

    root.mainloop()

def Accunt_Type_login():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Account Type")

    label = tk.Label(root, text="Account Type", font=TITLE_FONT)
    label.pack(padx=20, pady=20)

    admin = tk.Button(
        root, 
        text="Admin",
        command=lambda: [root.destroy(), Account_Creator().login_admin_UI()], 
        height=2, 
        width=10, 
        font=BUTTON_FONT
    )
    employee = tk.Button(
        root, 
        text="Employee", 
        command=lambda: [root.destroy(), Account_Creator()], 
        height=2, 
        width=10, 
        font=BUTTON_FONT
    )
    user = tk.Button(
        root,
        text="User",
        command=lambda: [root.destroy(), Account_Creator()],
        height=2,
        width=10,
        font=BUTTON_FONT
    )
    back = tk.Button(
        root,
        text="<-",
        command=lambda: [root.destroy(), main()],
        height=2,
        width=10,
        font=BUTTON_FONT
    )

    admin.place(x=100, y=100, height=50, width=100)
    employee.place(x=210, y=100, height=50, width=100)
    user.place(x=320, y=100, height=50, width=100)
    back.place(x=10, y=260, height=30, width=60)

    root.mainloop()


class Menu:
    def __init__(self, title, geometry, font):
        self.root = tk.Tk()
        root.geometry(geometry)
        root.title(title)

        label = tk.Label(root, text=title, font=font)
        label.pack(padx=20, pady=20)

    def add_button(self, command, button_text, x, y, height, width):
        button = tk.Button(
            self.root,
            text=button_text,
            command=lambda: [root.destroy(), command()],
            height=COMMON_BUTTON_HEIGHT,
            width=COMMON_BUTTON_WIDTH,
            font=BUTTON_FONT
        )
        button.place(x=x, y=y, h=height, w=width)

    def start(self):
        self.root.mainloop()


class Label:


class Mediator:


def save_accounts_to_json(accounts):
    # note: I love this function niw
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)


def main():
    account = []
    print(f"{account.__class__.__name__} account created successfully.")

    root = tk.Tk()

    root.geometry("500x300")
    root.title("Menu")

    label = tk.Label(root, text="Menu", font=TITLE_FONT)
    label.pack(padx=20, pady=20)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)

    register_button = tk.Button(
        buttonframe,
        text="Register",
        command=lambda: [root.destroy(), Accunt_Type_register()],
        height=2,
        width=10,
        font=BUTTON_FONT)
    login_button = tk.Button(
        buttonframe,
        text="Login",
        command=lambda: [root.destroy(), Accunt_Type_login()],
        height=2,
        width=10,
        font=BUTTON_FONT
    )

    login_button.grid(row=0, column=0)
    register_button.grid(row=0, column=1)

    buttonframe.pack(padx=100, pady=20, fill='x')
    root.mainloop()


if __name__ == "__main__":
    main()
