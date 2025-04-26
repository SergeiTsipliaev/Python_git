# controller.py

from model import Phonebook, Contact
from view import View
from exceptions import ContactNotFoundError, InvalidContactError, FileOperationError
from file_handler import FileHandler


class Controller:
    def __init__(self):
        self.phonebook = Phonebook()
        self.view = View()
        self.file_handler = FileHandler('contacts.json')

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_input("Select an option: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.remove_contact()
            elif choice == '3':
                self.find_contact()
            elif choice == '4':
                self.list_contacts()
            elif choice == '5':
                self.save_contacts()
            elif choice == '6':
                self.load_contacts()
            elif choice == '7':
                self.view.display_message("Exiting the phonebook. Goodbye!")
                break
            else:
                self.view.display_message("Invalid option. Please try again.")

    def add_contact(self):
        name = self.view.get_input("Enter name: ")
        phone = self.view.get_input("Enter phone: ")
        try:
            contact = Contact(name, phone)
            self.phonebook.add_contact(contact)
            self.view.display_message("Contact added successfully.")
        except InvalidContactError as e:
            self.view.display_message(str(e))

    def remove_contact(self):
        name = self.view.get_input("Enter the name of the contact to remove: ")
        try:
            self.phonebook.remove_contact(name)
            self.view.display_message("Contact removed successfully.")
        except ContactNotFoundError as e:
            self.view.display_message(str(e))

    def find_contact(self):
        name = self.view.get_input("Enter the name of the contact to find: ")
        try:
            contact = self.phonebook.find_contact(name)
            self.view.display_contact(contact)
        except ContactNotFoundError as e:
            self.view.display_message(str(e))

    def list_contacts(self):
        contacts = self.phonebook.list_contacts()
        self.view.display_contacts(contacts)

    def save_contacts(self):
        try:
            self.file_handler.save_contacts(self.phonebook.contacts)
            self.view.display_message("Contacts saved successfully.")
        except FileOperationError as e:
            self.view.display_message(str(e))

    def load_contacts(self):
        try:
            contacts = self.file_handler.load_contacts()
            self.phonebook.contacts = contacts
            self.view.display_message("Contacts loaded successfully.")
        except FileOperationError as e:
            self.view.display_message(str(e))
