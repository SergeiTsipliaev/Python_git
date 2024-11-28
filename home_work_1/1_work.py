import os

from tabulate import tabulate
import json

humans = 'humans.json'

main_menu = [
    'Main menu',
    'Open contacts',
    'Add contact',
    'Search contact',
    'Change contact',
    'Delete contact',
    'Exit',
]


def show_menu():
    for i, item in enumerate(main_menu):
        if not i:
            print(25 * "-", "\n", item)
        else:
            print(f'\t{i}.{item}')
    

def validate_menu_input(msg, error_msg):
    while True:
        input_menu_number = input(msg)
        if input_menu_number.isdigit() and 0 < int(input_menu_number) < len(main_menu):
            return int(input_menu_number)
        print(error_msg)


def opening_contacts():
    with open(humans, "r", encoding="utf-8") as humans_data:
        data = json.load(humans_data)
        contacts = data.get("contacts", ["No contacts in file"])
        table = []
        for contact in contacts:
            table.append([
                int(contact.get("id")),
                contact.get("name"),
                contact.get("telephone"),
                contact.get("specialization")

            ])

        table_sorted = sorted(table, key=lambda x: x[0])

        headers = ["ID", "NAME", "TELEPHONE", "SPECIALIST"]

        print(tabulate(table_sorted, headers, tablefmt="grid"))


def add_contact():
    with open(humans, 'r', encoding='utf-8') as humans_data:
        data = json.load(humans_data)

    new_contact = {
        "name": input("Add name: ").capitalize(),
        "telephone": input("Add telephone number: "),
        "specialization": input("Add specialization: ").capitalize()
    }

    if data["contacts"]:
        max_id = max(int(contact["id"]) for contact in data["contacts"])
    else:
        max_id = 0

    new_contact["id"] = max_id + 1
    data["contacts"].append(new_contact)
    with open(humans, "w", encoding="utf-8") as humans_data:
        json.dump(data, humans_data, indent=4, ensure_ascii=False)
    print("\nCONTACT HAS BEEB ADDED")


def search_contact():
    with open(humans, "r", encoding="utf-8") as humans_data:
        data = json.load(humans_data)

        contact_id = input("Please write contact id: ")
        
        table = []
        for contact in data.get("contacts", []):
            if contact.get("id") == contact_id:
                table.append([
                    int(contact.get("id")),
                    contact.get("name"),
                    contact.get("telephone"),
                    contact.get("specialization")

                ])

        headers = ["ID", "NAME", "TELEPHONE", "SPECIALIST"]

        print(tabulate(table, headers, tablefmt="grid"))


def change_contact():
    with open(humans, "r", encoding="utf-8") as humans_data:
        data = json.load(humans_data)

    contact_id = input("Please input contact ID for change: ")

    contact = next((c for c in data.get("contacts", []) if str(c.get("id")) == contact_id), None)

    if not contact:
        print(f"Contact with ID = {contact_id} not found")
        return

    print("Contact data:")
    print(f"1. Name: {contact.get('name')}")
    print(f"2. Telephone: {contact.get('telephone')}")
    print(f"3. Specialization: {contact.get('specialization')}")

    fields = {
        "1": "name",
        "2": "telephone",
        "3": "specialization"
    }

    while True:
        field_choice = input("Please choice fields for change or '0' for exit: ")
        if field_choice == '0':
            print("\nYou Exited")
            break
        elif field_choice in fields:
            new_value = input(f"Please input new {fields[field_choice]} for {contact.get('name')}: ")
            contact[fields[field_choice]] = new_value
            print("Contact has been changed")
        else:
            print("Incorrect choice. Please, try again!")

    with open(humans, "w", encoding="utf-8") as humans_data:
        json.dump(data, humans_data, indent=4, ensure_ascii=False)



def delete_contact():
    with open(humans, "r", encoding="utf-8") as humans_data:
        data = json.load(humans_data)

    contact_id = input("Please input contact ID for delete:  ")

    contacts = data.get("contacts", [])
    contact_to_delete = next((c for c in contacts if str(c.get("id")) == contact_id), None)

    if not contact_to_delete:
        print(f"Contact with ID = {contact_id} not found")
        return

    confirm = input(f"Are you sure you want to delete the contact '{contact_to_delete.get('name')}'? (y/n): ")
    if confirm.lower() == 'y':
        contacts.remove(contact_to_delete)
        with open(humans, "w", encoding="utf-8") as humans_data:
            json.dump(data, humans_data, indent=4, ensure_ascii=False)
        print(f"\nContact:\n{contact_to_delete}\nhas been deleted .")
    else:
        print("\nDeletion canceled.")


def menu_start():
    while True:
        show_menu()
        menu_number = validate_menu_input(
            '\nSelect a menu item: ',
            f'\nPlease input number from 1 to {len(main_menu) - 1}'
        )
        if menu_number == 1:  # Opening file
            opening_contacts()

        elif menu_number == 2:
            add_contact()

        elif menu_number == 3:
            search_contact()

        elif menu_number == 4:
            change_contact()

        elif menu_number == 5:
            delete_contact()

        elif menu_number == 6:
            print("\nYOU EXITED")
            break

   
menu_start()
