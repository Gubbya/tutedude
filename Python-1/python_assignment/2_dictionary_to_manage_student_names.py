# Dictionary to store students and their grades
student_grades = {} # Initialize an empty dictionary

while True: # Loop to keep the menu active
    # Display the menu options
    print("\n--- Student Grade Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1': # Add a new student and grade
        # Input student name and grade
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists with grade {student_grades[name]}")
        else:
            grade = input("Enter grade for the student: ")
            student_grades[name] = grade
            print(f"{name} added with grade {grade}")

    elif choice == '2': # Update an existing student's grade
        # Input student name to update
        name = input("Enter student name to update: ")
        if name in student_grades:
            new_grade = input("Enter the new grade: ")
            student_grades[name] = new_grade
            print(f"{name}'s grade updated to {new_grade}")
        else:
            print(f"Student '{name}' not found.")

    elif choice == '3':
        # Print all student grades
        # Check if there are any students in the dictionary
        if not student_grades:
            print("No students added yet.")
        else:
            print("\n--- Student Grades List ---")
            for name, grade in student_grades.items():
                print(f"Name: {name}, Grade: {grade}")

    elif choice == '4': # Exit the program
        # Exit the loop and end the program
        print("Exiting... Goodbye!")
        break

    else: # Handle invalid input
        # If the input is not valid, prompt the user again
        print("Invalid choice. Please select from 1 to 4.")