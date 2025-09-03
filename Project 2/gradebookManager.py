# Student Gradebook Manager
# Starter Template

# Dictionaries to store student information and grades
students = {}   # ID -> (first_name, last_name)
grades = {}     # ID -> [grade1, grade2, ...]

def add_student():
    """Add a new student to the gradebook."""
    student_id = input("Enter ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    # TODO: store the student's info in students dict
    # TODO: initialize an empty grades list for this student
    print("Student added!")

def add_grade():
    """Add a grade for an existing student."""
    student_id = input("Enter ID: ")
    # TODO: check if student exists
    # TODO: ask for a grade and add it to the student's grades list
    print("Grade added!")

def view_average():
    """View the average grade for a student."""
    student_id = input("Enter ID: ")
    # TODO: check if student exists
    # TODO: calculate and print the average grade
    print("Average for [student name]: [average]")

def list_all_students():
    """List all students with their average grade."""
    # TODO: loop over all students
    # TODO: print student name and average grade



while True:
    print("\nWelcome to the Gradebook Manager!")
    print("1. Add student")
    print("2. Add grade")
    print("3. View student average")
    print("4. List all students")
    print("5. Quit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        add_grade()
    elif choice == "3":
        view_average()
    elif choice == "4":
        list_all_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

