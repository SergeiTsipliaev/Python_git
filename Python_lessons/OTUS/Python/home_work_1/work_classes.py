from xml.etree.ElementPath import iterfind

from tabulate import tabulate
import json

humans = "humans.json"

main_menu = [
    "Main menu",
    "Open contacts",
    "Add contact",
    "Search contact",
    "Change contact",
    "Delete contact",
    "Exit",
]


class WriteOpenFile:

    def __init__(self, humans):
        self.json_file = humans
        self.data = json.load()


class Open(WriteOpenFile):

    def opening_contacts(self):
        with open(self.json_file, "r", encoding="utf-8") as humans_open:
            return json.load(humans_open)


add_contact = WriteOpenFile(humans)
