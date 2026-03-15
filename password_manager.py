import json

class PasswordsManager:

    def __init__(self, file_path):
        self.file_path = file_path


    def load_accounts(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


    def save_accounts(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)


    def add_account(self):
        data = self.load_accounts()

        site = input("Enter the site: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        account = {
            "site": site,
            "username": username,
            "password": password
        }

        data.append(account)
        self.save_accounts(data)

        print("Account added successfully.")


    def show_accounts(self):
        data = self.load_accounts()

        if not data:
            print("No accounts found.")
            return

        for i, acc in enumerate(data, start=1):
            print(f"{i}. {acc['site']} | {acc['username']} | {acc['password']}\n")


    def search_account(self):
        data = self.load_accounts()

        site = input("Enter site to search: ")

        results = [acc for acc in data if acc["site"].lower() == site.lower()]

        if not results:
            print("No accounts found.")
            return

        for i, acc in enumerate(results, start=1):
            print(f"{i}. {acc['site']} | {acc['username']} | {acc['password']}\n")


    def delete_account(self):
        data = self.load_accounts()

        self.show_accounts()

        delete_choice = input("Enter the number of the account to delete (or q to cancel): ")

        if delete_choice.lower() == "q":
            print("Deletion cancelled.")
            return

        try:
            index = int(delete_choice) - 1
            removed = data.pop(index)
            self.save_accounts(data)
            print(f"{removed['site']} account deleted.")
        except(ValueError , IndexError):
            print("Invalid selection.")

manager = PasswordsManager("accounts.json")

while True:
    print("\n1. Add account")
    print("2. Show accounts")
    print("3. Search account")
    print("4. Delete account")
    print("5. Exit")

    menu_choice = input("Select an option: ")

    if menu_choice == "1":
        manager.add_account()

    elif menu_choice == "2":
        manager.show_accounts()

    elif menu_choice == "3":
        manager.search_account()

    elif menu_choice == "4":
        manager.delete_account()

    elif menu_choice == "5":
        break

    else:
        print("Invalid option.")