import student_manager

student_manager.load_students_from_file()

while True:
    print("\n----Student Management System----\n")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    
    if choice == '1':
        student_manager.add_student()
    elif choice == '2':
        student_manager.display_students()
    elif choice == '3':
        student_manager.search_student()
    elif choice == '4':
        student_manager.update_student()
    elif choice == '5':
        student_manager.delete_student()
    elif choice == '6':
        print("\nExiting Program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1-6.")