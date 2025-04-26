import unittest
from unittest.mock import MagicMock
from controller import Controller
from model import Contact
from exceptions import ContactNotFoundError, InvalidContactError


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()
        self.controller.view = MagicMock()
        self.controller.file_handler = MagicMock()

    def test_add_contact(self):
        self.controller.view.get_input.side_effect = ["Bob", "0987654321"]
        self.controller.add_contact()
        self.assertEqual(len(self.controller.phonebook.contacts), 1)
        self.assertEqual(self.controller.phonebook.contacts[0].name, "Bob")

    def test_add_invalid_contact(self):
        self.controller.view.get_input.side_effect = ["", ""]
        self.controller.add_contact()
        self.controller.view.display_message.assert_called_with("Name and phone cannot be empty.")

    def test_remove_contact(self):
        contact = Contact(name="Bob", phone="0987654321")
        self.controller.phonebook.add_contact(contact)
        self.controller.view.get_input.return_value = "Bob"
        self.controller.remove_contact()
        self.assertEqual(len(self.controller.phonebook.contacts), 0)

    def test_remove_nonexistent_contact(self):
        self.controller.view.get_input.return_value = "Charlie"
        self.controller.remove_contact()
        self.controller.view.display_message.assert_called_with("Contact with name 'Charlie' not found.")

    # Additional tests can be added for other controller methods


if __name__ == '__main__':
    unittest.main()
