from dataclasses import dataclass, field
from typing import List
from exceptions import ContactNotFoundError, InvalidContactError


@dataclass
class Contact:
    name: str
    phone: str

    def __post_init__(self):
        if not self.name or not self.phone:
            raise InvalidContactError("Name and phone cannot be empty.")


class Phonebook:
    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, name: str):
        contact = self.find_contact(name)
        self.contacts.remove(contact)

    def find_contact(self, name: str) -> Contact:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        raise ContactNotFoundError(f"Contact with name '{name}' not found.")

    def list_contacts(self) -> List[Contact]:
        return self.contacts
