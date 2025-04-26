import unittest
from model import Phonebook, Contact
from exceptions import ContactNotFoundError, InvalidContactError


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook()
        self.contact = Contact(name="Alice", phone="1234567890")
        self.phonebook.add_contact(self.contact)

    def test_add_contact(self):
        self.assertIn(self.contact, self.phonebook.contacts)

    def test_remove_contact(self):
        self.phonebook.remove_contact("Alice")
        self.assertNotIn(self.contact, self.phonebook.contacts)

    def test_remove_nonexistent_contact(self):
        with self.assertRaises(ContactNotFoundError):
            self.phonebook.remove_contact("Bob")

    def test_find_contact(self):
        contact = self.phonebook.find_contact("Alice")
        self.assertEqual(contact, self.contact)

    def test_find_nonexistent_contact(self):
        with self.assertRaises(ContactNotFoundError):
            self.phonebook.find_contact("Bob")

    def test_invalid_contact(self):
        with self.assertRaises(InvalidContactError):
            Contact(name="", phone="")

    def test_list_contacts(self):
        contacts = self.phonebook.list_contacts()
        self.assertEqual(len(contacts), 1)


if __name__ == '__main__':
    unittest.main()
