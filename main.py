
class Student:

    def __init__(self, name,roll_number, marks,grade, fees):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.grade = grade
        self.fees = fees
        
students = []


def add_student():  
 

    name = input("Enter the name:")
    try:
      roll_number = int(input("Enter the roll_number:"))
      marks = int(input("Enter the marks:"))
      fees = float(input("Enter the fees:"))
    except ValueError:  
        print("\ninvalid input for roll number marks, or fees Please enter numbers.")
        return
    grade = input("Enter thr grade:")
    s = Student(name, roll_number, marks, grade, fees)
    students.append(s)
    print("\nStudent Added Successfully!")

def display_students():
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
    if not students:
        print("\nNo students to search.")
        return
    
    try:
        search_roll = int(input("Enter the roll number of the student to search for: "))
    except ValueError:
        print("Invalid input. Please enter a number for the roll number.")
        return

    for s in students:
        if s.roll_number == search_roll:
            print("\n--- Student Found ---")
            print(f"Name        : {s.name}")
            print(f"Roll Number : {s.roll_number}")
            print(f"Marks       : {s.marks}")
            print(f"Grade       : {s.grade}")
            print(f"Fees        : {s.fees}")
            return # Exit the function once the student is found

    print(f"\nNo student found with roll number {search_roll}.")

def update_student():   
    try:
        roll = int(input("Enter the update roll number:")) 
    except ValueError:
        print("Envalid roll number")
        return 
    for s in students:
        if s.roll_number == roll:
            s.name = input("Enter the new name:")
            s.marks = input("Enter the new marks:")
            s.grade = input("Enter the new grade:")
            s.fees = input("Enter the new fees:")

            print("Update successfully!")
            return 
        print("student not found.")
                


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()

    elif choice == '5':      
        print("Exiting Program. Goodbye!")
        break
    else: 
        print("Invalid choice. Please enter a number between 1 and 4.")       
         
  