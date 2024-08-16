
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    if contacts:
        print("\nContact List:")
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")


def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found = False
    
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    
    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Contact found. Enter new details (leave blank to keep current):")
            contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
            return
    
    print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    
    print("Contact not found.")


def contact_management():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice, please try again.")

contact_management()
