def add_contact(filename, name, phone):
    try:
        with open(filename, "a") as f:
            f.write(f"{name},{phone}\n")
    except Exception as e:
        print(f"Error: {e}")

def view_contacts(filename):
    try:
        with open(filename, "r") as f:
            contacts = f.readlines()
            for contact in contacts:
                print(contact.strip())
    except FileNotFoundError:
        print("Contacts file not found.")
    except Exception as e:
        print(f"Error: {e}")

def search_contact(filename, keyword):
    try:
        with open(filename, "r") as f:
            found = False
            for contact in f:
                if keyword.lower() in contact.lower():
                    print(contact.strip())
                    found = True
            if not found:
                print("No matching contact found.")
    except FileNotFoundError:
        print("Contacts file not found.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_contact("contacts.txt", name, phone)
    elif choice == "2":
        view_contacts("contacts.txt")
    elif choice == "3":
        keyword = input("Enter name or phone to search: ")
        search_contact("contacts.txt", keyword)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
