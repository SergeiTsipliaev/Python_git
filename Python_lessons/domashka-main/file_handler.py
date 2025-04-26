import json
from typing import List
from model import Contact
from exceptions import FileOperationError


class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def save_contacts(self, contacts: List[Contact]):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json_contacts = [contact.__dict__ for contact in contacts]
                json.dump(json_contacts, file, ensure_ascii=False, indent=4)
        except IOError as e:
            raise FileOperationError(f"Failed to save contacts: {e}")

    def load_contacts(self) -> List[Contact]:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                json_contacts = json.load(file)
                return [Contact(**data) for data in json_contacts]
        except IOError as e:
            raise FileOperationError(f"Failed to load contacts: {e}")
        except json.JSONDecodeError as e:
            raise FileOperationError(f"Invalid JSON format: {e}")
