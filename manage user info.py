import json

# Initialize an empty contact list
contacts = []

def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        json.dump(contacts, file)

def load_contacts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_contact(name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(index, name, phone, email):
    if index >= 0 and index < len(contacts):
        contacts[index] = {'name': name, 'phone': phone, 'email': email}
    else:
        print("Invalid contact index. Contact not updated.")

def delete_contact(index):
    if index >= 0 and index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Deleted contact: {deleted_contact['name']}")

# Load contacts from a file (if available)
contacts = load_contacts_from_file('contacts.json')

while True:
    print("\nContact Management System")
    print("1. Add New Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save and Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email address: ")
        add_contact(name, phone, email)
        print("Contact added successfully.")

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        view_contacts()
        index = int(input("Enter the index of the contact to edit: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email address: ")
            edit_contact(index, name, phone, email)
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    elif choice == '4':
        view_contacts()
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            delete_contact(index)
        else:
            print("Invalid contact index.")

    elif choice == '5':
        save_contacts_to_file(contacts, 'contacts.json')
        print("Contacts saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
