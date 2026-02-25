students = {}

def load_data():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                try:
                    roll, name, marks = line.strip().split(",")
                    students[roll] = {
                        "Name": name,
                        "Marks": int(marks)
                    }
                except ValueError:
                    print("Skipping invalid record in file.")
    except FileNotFoundError:
        print("No existing file found.\n")

def save_data():
    try:
        with open("students.txt", "w") as file:
            for roll, details in students.items():
                file.write(f"{roll},{details['Name']},{details['Marks']}\n")
    except Exception as e:
        print("Error saving file:", e)

# Add Student
def add_student():
    try:
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll number already exists!\n")
            return

        name = input("Enter Name: ")

        marks = int(input("Enter Marks: "))   # May cause ValueError

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.\n")
            return

        students[roll] = {
            "Name": name,
            "Marks": marks
        }
        save_data()
        print("Student Added Successfully!\n")

    except ValueError:
        print("Invalid input! Marks must be a number.\n")

# Display Student
def display_students():
    if not students:
        print("No Student Records Found.\n")
    else:
        print("\nStudent Records:")
        for roll, details in students.items():
            print("Roll No:", roll)
            print("Name:", details["Name"])
            print("Marks:", details["Marks"])
            print("----------------------")

# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print("Student Found:")
        print("Name:", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
    else:
        print("Student Not Found.")
    print()

# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    if roll in students:
        del students[roll]
        save_data()
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found.")
    print()


load_data()

while True:
    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting Program...")
            break
        else:
            print("Invalid choice! Please select 1-5.\n")

    except ValueError:
        print("Invalid input! Please enter a number.\n")