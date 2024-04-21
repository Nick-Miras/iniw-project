import json
import tkinter as tk
import re


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
            "email": self.email,
            "phone": self.phone
        }


class Account_Creator:
    def create_admin(self, username, password, email, phone):
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
                raise ValueError("Invalid Email")
        except Exception as e:
            print("An error occurred:", e)

    def registration_Account_UI(self):
        try:
            root = tk.Tk()
            root.title("User Registration and Login")
            root.geometry("300x200")

            username_label = tk.Label(root, text="Username:")
            username_label.grid(row=3, column=1)
            username = tk.Entry(root)
            username.grid(row=3, column=2)

            password_label = tk.Label(root, text="Password:")
            password_label.grid(row=4, column=1)
            password = tk.Entry(root, show="*")
            password.grid(row=4, column=2)

            email_label = tk.Label(root, text="Email:")
            email_label.grid(row=5, column=1)
            email = tk.Entry(root)
            email.grid(row=5, column=2)

            phone_label = tk.Label(root, text="Phone Number:")
            phone_label.grid(row=6, column=1)
            phone = tk.Entry(root)
            phone.grid(row=6, column=2)

            register_button = tk.Button(root, text="Register", command=lambda: [root.destroy(),
                                                                                self.create_admin(username.get(),
                                                                                                  password.get(),
                                                                                                  email.get(),
                                                                                                  phone.get())])
            register_button.grid(row=8, column=2)

            root.mainloop()
        except Exception as e:
            print("An error occurred:", e)


def Account_Type():
    try:
        root = tk.Tk()
        root.geometry("500x300")
        root.title("Account Type")

        label = tk.Label(root, text="Account Type", font=('Arial_Black', 24))
        label.pack(padx=20, pady=20)

        admin = tk.Button(root, text="Admin",
                          command=lambda: [root.destroy(), Account_Creator().registration_Account_UI()], height=2,
                          width=10, font=('Arial_Black', 16))
        admin.pack(padx=20, pady=20)

        root.mainloop()
    except Exception as e:
        print("An error occurred:", e)


def main():
    try:
        root = tk.Tk()
        root.geometry("500x300")
        root.title("Menu")

        label = tk.Label(root, text="Menu", font=('Arial_Black', 24))
        label.pack(padx=20, pady=20)

        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)

        register_button = tk.Button(buttonframe, text="Register", command=lambda: [root.destroy(), Account_Type()],
                                    height=2, width=10, font=('Arial_Black', 16))
        login_button = tk.Button(buttonframe, text="Login", height=2, width=10, font=('Arial_Black', 16))

        login_button.grid(row=0, column=0)
        register_button.grid(row=0, column=1)

        buttonframe.pack(padx=100, pady=20, fill='x')
        root.mainloop()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

