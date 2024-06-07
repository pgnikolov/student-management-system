import students as st


def main():
	"""
	Main function to provide user interaction.
	"""
	while True:
		# Display menu options
		print("\nStudent Management System")
		print("1. Add Student")
		print("2. Update Student")
		print("3. Delete Student")
		print("4. Search Student")
		print("5. List All Students")
		print("6. Exit")

		# Prompt user for their choice
		choice = input("Enter your choice: ")

		if choice == '1':
			first_name = input("Enter the first name of the student: ").capitalize()
			last_name = input("Enter the last name of the student: ").capitalize()
			age = int(input("Enter the age of the student: "))
			sex = input("Enter the sex of the student (Male/Female): ").capitalize()
			email = input("Enter the email of the student: ").lower()
			subjects_lst = ["Mathematics", "Literature", "IT", "History", "Geography", "Philosophy", "Biology", "Physics",
						"Chemistry", "Sport", "Art"]
			grades = [float(input(f"Enter grade for {subjects_lst[i]}: ")) for i in range(len(subjects_lst))]
			subjects = {subject: grade for subject in subjects_lst for grade in grades}

			st.add_student(first_name, last_name, age, sex, email, subjects)
		elif choice == '2':
			first_name = input("Enter the first name of the student to update: ").capitalize()
			last_name = input("Enter the last name of the student to update: ").capitalize()
			name = f"{first_name} {last_name}"  # Use full name as the key
			st.update_student(name)
		elif choice == '3':
			first_name = input("Enter the first name of the student to update: ").capitalize()
			last_name = input("Enter the last name of the student to update: ").capitalize()
			name = f"{first_name} {last_name}"  # Use full name as the key
			st.delete_student(name)
		elif choice == '4':
			first_name = input("Enter the first name of the student to update: ").capitalize()
			last_name = input("Enter the last name of the student to update: ").capitalize()
			name = f"{first_name} {last_name}"  # Use full name as the key
			st.search_student(name)
		elif choice == '5':
			st.list_all_students()
		elif choice == '6':
			# Exit the program
			break
		else:
			print("Invalid choice, please try again.")


if __name__ == "__main__":
	main()
