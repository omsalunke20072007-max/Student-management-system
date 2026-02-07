def  add_student():
    name = input("Enter name: ").strip()
    while not name.isalpha():
        print("❌ name must contain latter only")
        name = input("Enter name again")


    roll = int(input("Enter a roll number"))
    while not roll.isdigit():
        print("❌ only number contain")
        roll = input("Enter roll number again")


    age = input("Enter age").strip()
    while not age.isdigit():
        print("❌ age must contain number")
        age = input("Enter age again")


    course = input("enter your course")

    print("\nyou entered:")
    print(f"name:{name}")
    print(f"roll:{roll}")
    print(f"age:{age}")
    print(f"course:{course}")

    confirm = input("you want save this?(yes/no):").strip().lower()

    if confirm!= "yes":
        print("❌  data not save. Please try again")
        return


    

    with open("students.txt", "a") as file:
        file.write(f"{name}, {roll}, {age}, {course}\n")

    print("✅ student add successfully")





def roll_exists(roll):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                existing_roll = line.strip().split(",")[1]
                if existing_roll == roll:
                    return True
                
    except FileNotFoundError:
        return False
    
    return False
        


def view_students():
    try:
        with open("students.txt", "r") as file:

            lines = file.readlines()

            if not lines:
                print("no student found.")
                return
            
            print("\n==== student list ====") 
            for line in lines:
                name, roll, age, course = line.strip().split(",") #This line splits one student record from the file into roll, name, age, and course variables.
                print(f"name: {name}| roll: {roll}| age: {age}| couse: {course}")

    except FileNotFoundError:# It prevents the program from crashing if the data file does not exist.
        print("No data file found") 



def search_student():
    roll_to_find = input("enter roll number to search:")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = line.strip(). split(",")

                if roll == roll_to_find:
                    print("\nstudent found:")
                    print(f"name:{name}")
                    print(f"roll:{roll}")
                    print(f"age:{age}")
                    print(f"course:{course}")

                    found = True
                    break
        if not found:
            print("student not found")

    except FileNotFoundError:
        print("No data file found.")

    

def update_student():
    roll_to_update = input("Enter roll number to update: ")
    updated_lines = []
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = line.strip().split(",")

                if roll == roll_to_update:
                    print("Enter new details:")
                    name = input("New name: ")
                    age = input("New age: ")
                    course = input("New course: ")

                    updated_lines.append(f"{name},{roll},{age},{course}\n")
                    found = True
                else:
                    updated_lines.append(line) 

        if found:
            with open("students.txt", "w") as file:

                file.writelines(updated_lines) # writes the updated student record along with all unchanged student records into the new file.

            print("Student updated successfully.")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No data file found.")






def delete_student():
    roll_to_delete = input("Enter roll numbrt to delete:")
    updated_line = []
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = line.strip().split(",")
                if roll!= roll_to_delete:
                    updated_line.append(line)
                else:
                    found = True

        if found:
            with open("students.txt", "w") as file:
                file.writelines(updated_line)
            print("Student deleted successfully")
        else:
            print("student not found:")

    except FileNotFoundError:
        print("No data file found.")           


    

while True:
    print("\n==== student management system ====")
    print("1. Add student")
    print("2. view student")
    print("3. search student")
    print("4. update student")
    print("5. delete_student")
    print("6. Exit")

    choice = input("Enter your choice:").strip()

    if not choice.isdigit():
        print("Please enter numbers only")

    elif choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice =="3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exit 👋")
        break

    else:
        print("Invalide choice")                    

        
            
