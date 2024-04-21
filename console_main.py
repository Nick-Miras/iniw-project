import json
import uuid


class Command:
    @staticmethod
    def execute(account):
        pass


class UserCommand:
    @staticmethod
    def execute(account):
        print(f"User {account.username} viewing profile.")


class AdminCommand:
    @staticmethod
    def execute(account):
        # Implement admin-specific user management logic
        print(f"Admin {account.username} managing users.")


class EmployeeCommand:
    @staticmethod
    def execute(account):
        print(f"Employee {account.username} clocking in.")


class NicksAccount:
    def __init__(self, username, password, id_=None, command=None):
        self.username = username
        self.password = password
        self.id_ = id_
        self.command = command

    def do_something(self):
        self.command.execute(self)

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'id': self.id_
        }


class Account:
    def __init__(self, username, password, id_=None):
        self.username = username
        self.password = password
        self.id_ = id_


class Admin(Account):
    def manage_users(self):
        # Implement admin-specific user management logic
        print(f"Admin {self.username} managing users.")

    def generate_id(self):
        return '0001_12312312'


class User(Account):
    def view_profile(self):
        # Implement user-specific profile viewing logic
        print(f"User {self.username} viewing profile.")

    def generate_id(self):
        return '0000_' + str(uuid.uuid1())


class Employee(Account):
    def clock_in(self):
        # Implement employee-specific clock-in logic
        print(f"Employee {self.username} clocking in.")

    def generate_id(self):
        return '0002_12312312'


class Manager(Admin):
    def generate_id(self):
        return '0004_12312312'


class SuperVisor(Account):

    def generate_id(self):
        return '0003_12312312'


class SecurityManager(Manager):
    def manage_security(self):
        # Implement admin-specific user management logic
        print(f"Admin {self.username} managing users.")
    def generate_id(self):
        return '0003_12312312'


class EmployeeManager(Manager):
    def generate_id(self):
        return '0003_12312312'


class AccountCreator:
    @staticmethod
    def create_admin():
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        admin_id = input("Enter admin ID: ")
        return NicksAccount(admin_username, admin_password, admin_id, AdminCommand)

    @staticmethod
    def create_user():
        user_username = input("Enter user username: ")
        user_password = input("Enter user password: ")
        user_id = input("Enter user ID: ")
        return NicksAccount(user_username, user_password, user_id, UserCommand)

    @staticmethod
    def create_employee():
        employee_username = input("Enter employee username: ")
        employee_password = input("Enter employee password: ")
        employee_id = input("Enter employee ID: ")
        return NicksAccount(employee_username, employee_password, employee_id, EmployeeCommand)


def create_account(account_type, command):
    username = input(f"Enter {account_type} username: ")
    password = input(f"Enter {account_type} password: ")
    id_ = input(f"Enter {account_type} ID: ")
    return NicksAccount(username, password, id_, command)


def save_account_to_json(account, account_type):
    with open(f"database/{account_type}.json", 'a') as file:
        json.dump(account.to_dict(), file)
        file.write('\n')


def login():
    account_type = input("Choose account type to login (admin/user/employee): ").lower()

    with open(f"database/{account_type}.json", 'r') as file:
        accounts = [json.loads(line) for line in file]

    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in accounts:
        if account['username'] == username and account['password'] == password:
            print(f"Login successful as {account['username']}")
            return account_type, account
    print("Login failed. Invalid username or password or account type.")
    return None


# Main function
def main():
    choice = input("Do you want to create an account (c) or login (l)? ").lower()

    if choice == 'c':
        account_type = input("Choose account type (admin/user/employee): ").lower()

        if account_type == "admin":
            account = create_account("admin", AdminCommand)
        elif account_type == "user":
            account = create_account("user", UserCommand)
        elif account_type == "employee":
            account = create_account("employee", EmployeeCommand)
        else:
            print("Invalid account type. Please choose from admin/user/employee.")
            return

        print(f"{account_type} account created successfully.")
        save_account_to_json(account, account_type)

    elif choice == 'l':
        account_type, account = login()
        if account is not None:
            account_class = NicksAccount(account['username'], account['password'])
            if account_type == "admin":
                account_class.command = AdminCommand
                account_class.do_something()
            elif account_type == "user":
                account_class.command = UserCommand
                account_class.do_something()
            elif account_type == "employee":
                account_class.command = EmployeeCommand
                account_class.do_something()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()