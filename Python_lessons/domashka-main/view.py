# view.py

class View:
    @staticmethod
    def display_menu():
        print("=== Phonebook Menu ===")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Find Contact")
        print("4. List Contacts")
        print("5. Save Contacts")
        print("6. Load Contacts")
        print("7. Exit")

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def display_message(message: str):
        print(message)

    @staticmethod
    def display_contact(contact):
        print(f"Name: {contact.name}, Phone: {contact.phone}")

    @staticmethod
    def display_contacts(contacts):
        if not contacts:
            print("No contacts found.")
            return
        for contact in contacts:
            View.display_contact(contact)
