def  add_student():
    name = input("Enter name: ").strip()
    while not name.isalpha():
        print("❌ name must contain letters only")
        name = input("Enter name again")


    roll = input("Enter a roll number: ").strip()
    while not roll.isdigit():
        print("❌ roll number must contain digits only")
        roll = input("Enter roll number again: ").strip()

    if roll_exists(roll):
        print("❌ Roll number already exists!")
        return    
        

    age = input("Enter age: ").strip()
    while not age.isdigit():
        print("❌ age must contain number")
        age = input("Enter age again")


    course = input("Enter your course: ")

    print("\nyou entered:")
    print(f"name:{name}")
    print(f"roll:{roll}")
    print(f"age:{age}")
    print(f"course:{course}")

    confirm = input("you want save this?(yes/no):").strip().lower()

    if confirm!= "yes":
        print("❌  Data not saved. Please try again")
        return


    

    with open("students.txt", "a") as file:
        file.write(f"{name}, {roll}, {age}, {course}\n")

    print("✅ student added successfully")





def roll_exists(roll):
    try:
        with open("students.txt", "r") as file:
            for line in file:
                existing_roll = line.strip().split(",")[1].strip()
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
                print("No students found.")
                return
            
            print("\n" + "=" * 70)
            print(f"| {'NAME':<20} | {'ROLL NO':<12} | {'AGE':<5} | {'COURSE':<20} |")
            print("-" * 70)
            
            for line in lines:
                data = [x.strip() for x in line.strip().split(",")]
                if len(data) == 4:
                    name, roll, age, course = data
                    print(f"| {name:<20} | {roll:<12} | {age:<5} | {course:<20} |")
            
            print("=" * 70 + "\n")

    except FileNotFoundError:
        print("No data file found.") 



def search_student():
    roll_to_find = input("Enter roll number to search: ").strip()
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = [x.strip() for x in line.strip().split(",")]

                if roll == roll_to_find:
                    print("\nstudent found:")
                    print(f"name:{name}")
                    print(f"roll:{roll}")
                    print(f"age:{age}")
                    print(f"course:{course}")

                    found = True
                    break
        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No data file found.")

    

def update_student():
    roll_to_update = input("Enter roll number to update: ").strip()
    updated_lines = []
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = [x.strip() for x in line.strip().split(",")]

                if roll == roll_to_update:
                    print("Enter new details:")
                    name = input("New name: ").strip()
                    age = input("New age: ").strip()
                    course = input("New course: ").strip()

                    updated_lines.append(f"{name}, {roll}, {age}, {course}\n")
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
    roll_to_delete = input("Enter roll number to delete: ").strip()
    updated_line = []
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, age, course = [x.strip() for x in line.strip().split(",")]
                if roll!= roll_to_delete:
                    updated_line.append(line)
                else:
                    found = True

        if found:
            with open("students.txt", "w") as file:
                file.writelines(updated_line)
            print("Student deleted successfully")
        else:
            print("Student not found.")

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
        print("Invalid choice")                    
