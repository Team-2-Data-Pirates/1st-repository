def greet_user():
    print("Hello user Welcome to PhoneBook App")

def welcome():
    choice = int(input('''Welcome to Phonebook App. Select Your option==>
            1. Create a new contact
            2. Display your existing Contacts
            3. View the contacts by Name
            4. Delete a contact
            5. Exit
              '''))
    return choice

def phonebook():
    #Created an empty dictionary
    contact = {}

    #To run phonebook app continuously
    while True:
        option = welcome()
        if option == 1:
            contact_name = input("Enter contact name in this 'First Name Last Name': ")
            contact_number = int(input("Enter contact Number: "))

            if contact_number in contact.values():
                print("Contact is already exist!!!")
            else:
                contact[contact_name] = contact_number

        if option == 2:
            if bool(contact) != False:
                for k,v in contact.items():
                    print("{} ==> {}".format(k,v))
            else:
                print("No Contacts exist!!! Your Phone book is Empty.")
                
        if option == 3:
            name = input("Enter the name of Contact details: ")
            if name in contact:
                print("{} ==> {}".format(name,contact[name]))
            else:
                print("No Contacts exist with {} as name".format(name))
            
        if option == 4:
            name = input("Enter the name of Contact details that you wish to delete: ")
            if name in contact:
                contact.pop(name)
                print("Contact got deleted")
            else:
                print("No Contacts exist with {} as name".format(name))
            
        if option == 5:
            print("Thanks for using our Phonebook App")
            break

greet_user()
if __name__ == '__main__':
    phonebook()
