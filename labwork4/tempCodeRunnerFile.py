def add_contact(name, contact):
    with open("contacts.txt", "a") as f:
        f.write(f"{name}, {contact}\n")
def view_contacts():
    with open("contacts.txt", "r") as f:
        print(f.read())
def search_contact(name):
    found = False
    with open("contacts.txt", "r") as f:
        for line in f:
            if name.lower() in line.lower():
                print("Found:", line.strip())
                found = True
    if not found:
        print("Contact not found.")

while True: 
    print("Press 1 to add new contact")
    print("Press 2 to add view contacts")
    print("Press 3 to search for contacts")
    print("Press 4 to exit")
    choice = input("Enter your choice : ")
    try:
        if choice == '1':
            name = input("Enter name")
            contact = input("Enter contact")
            add_contact(name, contact)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact you want to search for ")
            search_contact(name)
        elif choice == '4':
            print("Exiting...")
            break
        else :
            print("Invalid choice")
    except Exception as e:
        print(e)



    