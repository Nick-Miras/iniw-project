import tkinter as tk
import re
import json


class Account_Creator:
    @staticmethod
    def create_admin():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()

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

                root.destroy()  # Close the GUI window if email is valid
            else:
                invalid_email_label.config(text="Invalid Email")
        except Exception as e:
            print("An error occurred:", e)

    def registration_Account_UI(self):
        try:
            global root, username_entry, password_entry, email_entry, phone_entry, invalid_email_label

            root = tk.Tk()
            root.title("User Registration and Login")
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


if __name__ == "__main__":
    account_creator = Account_Creator()
    account_creator.registration_Account_UI()

