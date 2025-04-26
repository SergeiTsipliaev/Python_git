import unittest
import os
from file_handler import FileHandler
from model import Contact
from exceptions import FileOperationError


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_contacts.json'
        self.file_handler = FileHandler(self.filename)
        self.contacts = [Contact(name="Alice", phone="1234567890")]

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_contacts(self):
        self.file_handler.save_contacts(self.contacts)
        self.assertTrue(os.path.exists(self.filename))

    def test_load_contacts(self):
        self.file_handler.save_contacts(self.contacts)
        loaded_contacts = self.file_handler.load_contacts()
        self.assertEqual(len(loaded_contacts), 1)
        self.assertEqual(loaded_contacts[0].name, "Alice")

    def test_load_contacts_file_not_found(self):
        with self.assertRaises(FileOperationError):
            self.file_handler.load_contacts()


if __name__ == '__main__':
    unittest.main()
