import json

students = []


def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    student = {
        "name": name,
        "roll": roll,
        "age": age,
        "department": department
    }

    students.append(student)
    print("Student Added Successfully!")


def view_students():
    print("\n===== All Students =====")
    
    if not students:
        print("No students found.")
        return

    for student in students:
        print("------------------------")
        print(f"Name: {student['name']}")
        print(f"Roll: {student['roll']}")
        print(f"Age: {student['age']}")
        print(f"Department: {student['department']}")
    print("------------------------")


def search_student():
    search_roll = input("Enter Roll Number to search: ")
    found = False

    for student in students:
        if student["roll"] == search_roll:
            print("\nStudent Found:")
            print("------------------------")
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Age: {student['age']}")
            print(f"Department: {student['department']}")
            print("------------------------")
            found = True
            break

    if not found:
        print("Student not found.")


def update_student():
    search_roll = input("Enter Roll Number to update: ")
    found = False

    for student in students:
        if student["roll"] == search_roll:
            print("\nStudent Found! Enter new details:")
            
            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["department"] = input("New Department: ")
            
            print("Student Updated Successfully!")
            found = True
            break

    if not found:
        print("Student not found.")


def delete_student():
    search_roll = input("Enter Roll Number to delete: ")
    found = False

    for student in students:
        if student["roll"] == search_roll:
            students.remove(student)
            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")


def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    print("Students saved successfully!")


def load_students():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
        print("Students loaded successfully!")
    except FileNotFoundError:
        print("No saved file found (students.json does not exist yet).")



def main():
    while True:
    
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Students to File")
        print("7. Load Students from File")
        print("8. Exit")

        
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_students()
        elif choice == "7":
            load_students()
        elif choice == "8":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()