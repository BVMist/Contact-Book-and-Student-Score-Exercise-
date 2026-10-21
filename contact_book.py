#Contact book
#Stores contacts.
#Allows for adding, deletion, viewing and finding of contact.


contacts = {
    "Ayo Dami": 564,
    "Vanessa Black": 469,
    "Destiny Laditan": 361
}


def add():
    """Adds new contacts to the contacts dictionary."""
    try:
        num = int(input("Number(3 digits): ")) 
    except:
        print("Invalid input. Must be number.")
    if len(str(num))>3 or len(str(num))<3:
        print("Invalid number. Must be 3 digits.")
    else:
        name = input("Name: ").strip()
        contacts[num] = name
        print(num, "added to contacts.")
        
def delete():
        """Deletes contacts from the contact dictionary."""
        try:
            num = int(input("Number: "))
        except:
            print("Invalid input. Must be a number.")
        if num in contacts:
            del contacts[num]
            print(num, "deleted from contacts.")
        else:
            print("Number not saved to contact.")
            
def view():
    """Shows a list of all the contacts."""
    print("\n-----Contacts-----")
    for i, y in contacts.items():
        print(f"Name: {i}")     
        print(f"Number: {y}\n")    

def find():
    """Searches for name or number in the contacts dictionary."""
    try:
        by = int(input("By(1 for name, 2 for num): "))
    except:
        return "Invalid input, must be integer."
    if by == 1:    
        name = input("Name: ")
        msg = ""
        for i, y in contacts.items():
            if name.lower() in i.lower():
                msg += f"Name: {i}\n" 
                msg += f"Number: {y}\n\n"
        if msg == "":
            return "No such name found in contacts."
        else:
            return msg
    elif by == 2:
        try:
            num = int(input("Number: "))     
        except:
            return "Invalid input, must be integer."   
        msg = "" 
        for i, y in contacts.items():
            if str(num) in str(y):
                msg += f"Name: {i}\n"
                msg += f"Number: {y}\n\n"
        if msg == "":
            return "No such number found in contacts."   
        else:
            return msg                                    
                     
def main():
    """Main function"""
    while True:
        print("\n______Contact book______")     
        print("1. Add contact")   
        print("2. View contact")
        print("3. Delete contact")
        print("4. Find contact")
        print("5. Exit")
        try:
            action = int(input("What would you like to do(1,2, 3, 4 or 5): "))
        except:
            print("Invalid input.")
            continue
        match action:
            case 1:
                add()
            case 2:
                view()
            case 3:
                delete()
            case 4:
                result = find()
                print(result)
            case 5:
                exit()
                
main()                