import json
from student import Student

students = []
DATA_FILE = "students.json"

def load_students_from_file():
    """Loads student data from a JSON file."""
    global students
    try:
      with open(DATA_FILE, 'r') as f:
        students_data = json.load(f)
    
        students = [Student(**s) for s in students_data]
        print(f"Loaded {len(students)} student(s) from {DATA_FILE}.")
    except FileNotFoundError:
        print("No data file found. Starting with an empty student list.")
        students = []
    except json.JSONDecodeError:
        print(f"Error reading {DATA_FILE}. It might be corrupted or empty. Starting fresh.")
        students = []

def save_students_to_file():
    """Saves the current list of students to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        # Convert list of Student objects to a list of dictionaries
        students_data = [s.__dict__ for s in students]
        json.dump(students_data, f, indent=4)
        
def add_student():
    """Prompts user for student details and adds a new student."""
    name = input("Enter the name: ")
    try:
        roll_number = int(input("Enter the roll number: "))
    except ValueError:
        print("\nInvalid input for roll number. Please enter a number.")
        return

    for s in students:
        if s.roll_number == roll_number:
            print("\nThis roll number is already taken.")
            return

    try:
        marks = int(input("Enter the marks: "))
        fees = float(input("Enter the fees: "))
    except ValueError:
        print("\nInvalid input for marks or fees. Please enter numbers.")
        return

    grade = input("Enter the grade: ")

    s = Student(name, roll_number, marks, grade, fees)
    students.append(s)
    save_students_to_file()
    print("\nStudent Added Successfully!")

def display_students():
    """Displays the details of all students."""
    if not students:
        print("\nNo students found.")
        return

    print("\n----- Student List -----")
    for s in students:
        print(f"Name        : {s.name}")
        print(f"Roll Number : {s.roll_number}")
        print(f"Marks       : {s.marks}")
        print(f"Grade       : {s.grade}")
        print(f"Fees        : {s.fees}")
        print("-" * 30)

def search_student():
    """Searches for a student by roll number and displays their details."""
    if not students:
        print("\nNo students to search.")
        return

    try:
        search_roll = int(input("Enter the roll number of the student to search for: "))
    except ValueError:
        print("\nInvalid input. Please enter a number for the roll number.")
        return

    for s in students:
        if s.roll_number == search_roll:
            print("\n--- Student Found ---")
            print(f"Name        : {s.name}")
            print(f"Roll Number : {s.roll_number}")
            print(f"Marks       : {s.marks}")
            print(f"Grade       : {s.grade}")
            print(f"Fees        : {s.fees}")
            return

    print(f"\nNo student found with roll number {search_roll}.")

def update_student():
    """Updates the details of an existing student."""
    try:
        roll = int(input("Enter the roll number of the student to update: "))
    except ValueError:
        print("\nInvalid roll number. Please enter a number.")
        return

    for s in students:
        if s.roll_number == roll:
            try:
                s.name = input("Enter the new name: ")
                s.marks = int(input("Enter the new marks: "))
                s.grade = input("Enter the new grade: ")
                s.fees = float(input("Enter the new fees: "))
                print("\nStudent details updated successfully!")
                save_students_to_file()
            except ValueError:
                print("\nInvalid input for marks or fees. Please enter numbers.")
            return

    print(f"\nStudent with roll number {roll} not found.")

def delete_student():
    """Deletes a student from the system by roll number."""
    if not students:
        print("\nNo students to delete.")
        return

    try:
        roll_to_delete = int(input("Enter the roll number of the student to delete: "))
    except ValueError:
        print("\nInvalid input. Please enter a number for the roll number.")
        return

    student_to_remove = next((s for s in students if s.roll_number == roll_to_delete), None)

    if student_to_remove:
        students.remove(student_to_remove) 
        save_students_to_file()
        print(f"\nStudent with roll n umber {roll_to_delete} deleted successfully!")
    else:
        print(f"\nNo student found with roll number {roll_to_delete}.")
