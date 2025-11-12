import json
import os

# File where contacts will be saved
FILE_PATH = "contacts.json"

# Load existing contacts if the file exists
def load_contacts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(FILE_PATH, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' saved!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"{name} - {info['phone']} - {info['email']}")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
