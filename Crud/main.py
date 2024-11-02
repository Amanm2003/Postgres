# main.py
from crud import create_record, read_records, update_record, delete_record

def main():
    print("Entering the database:.......")
    options = (
        "Performing CRUD operations..\n"
        "Press 1: For Insertion\n"
        "Press 2: For Update values\n"
        "Press 3: For Reading the values\n"
        "Press 4: For Delete Operation\n"
        "Press 0: To Exit"
    )
    
    while True:
        print(options)
        try:
            num = int(input("Enter the operation you want to perform: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if num == 1:
            name = input("Enter the name: ")
            try:
                age = float(input("Enter the age: "))
                email = input("Enter the email: ")
                print("Inserting values.......")
                create_record(name, age, email)
                print("Value inserted successfully!")
            except ValueError:
                print("Invalid input for age. Please enter a valid number.")
        
        elif num == 2:
            try:
                id = int(input("Enter the id: "))
                name = input("Enter the name: ")
                age = float(input("Enter the age: "))
                email = input("Enter the email: ")
                print("Updating values.......")
                update_record(id, name, age, email)
                print("Value updated successfully!")
            except ValueError:
                print("Invalid input. Please ensure id and age are valid numbers.")
        
        elif num == 3:
            print("Reading...........")
            records = read_records()
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")
        
        elif num == 4:
            try:
                id = int(input("Enter the id: "))
                delete_record(id)
                print("Deleted successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid id.")
        
        elif num == 0:
            print("Exiting the database operations.")
            break
        
        else:
            print("Invalid operation. Please enter a number between 0 and 4.")


if __name__ == "__main__":
    main()
