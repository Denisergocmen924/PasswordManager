import json

class PasswordsManager:

    def __init__(self, file_path):
        self.file_path = file_path


    def load_passwords(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []


    def save_passwords(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)


    def add_password(self):
        data = self.load_passwords()

        name = input("Enter the name: ")
        password = input("Enter the password: ")

        password = {
            "name": name,
            "password": password
        }

        data.append(password)
        self.save_passwords(data)

        print("Password added successfully.")


    def show_passwords(self):
        data = self.load_passwords()

        if not data:
            print("No passwords found.")
            return

        for i, pwd in enumerate(data, start=1):
            print(f"{i}. {pwd['name']} | {pwd['password']}\n")


    def search_password(self):
        data = self.load_passwords()

        name = input("Enter name to search: ")

        results = [pwd for pwd in data if pwd["name"].lower() == name.lower()]

        if not results:
            print("No passwords found.")
            return

        for i, pwd in enumerate(results, start=1):
            print(f"{i}. {pwd['name']} | {pwd['password']}\n")


    def delete_password(self):
        data = self.load_passwords()

        self.show_passwords()

        delete_choice = input("Enter the number of the password to delete (or q to cancel): ")

        if delete_choice.lower() == "q":
            print("Deletion cancelled.")
            return

        try:
            index = int(delete_choice) - 1
            removed = data.pop(index)
            self.save_passwords(data)
            print(f"{removed['name']} password deleted.")
        except(ValueError , IndexError):
            print("Invalid selection.")

manager = PasswordsManager("passwords.json")

while True:
    print("\n1. Add password")
    print("2. Show passwords")
    print("3. Search password")
    print("4. Delete password")
    print("5. Exit")

    menu_choice = input("Select an option: ")

    if menu_choice == "1":
        manager.add_password()

    elif menu_choice == "2":
        manager.show_passwords()

    elif menu_choice == "3":
        manager.search_password()

    elif menu_choice == "4":
        manager.delete_password()

    elif menu_choice == "5" or menu_choice.lower() == "q":
        break

    else:
        print("Invalid option.")