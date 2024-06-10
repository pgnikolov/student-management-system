from openpyxl import Workbook, load_workbook


def new_all_students_custom(sheet_name: str, file_name: str, columns: int):
    """
    Create Excel file and ask the user for amount of columns
    and their names.

    Args:
        sheet_name (str): Name of sheet in Excel workbook
        file_name (str): Name of file (example "all_2024" all students who start 2024)
        columns (int): Number of columns in Sheet

    Return:
         None
    """
    wb = Workbook()
    sheet = wb.active
    sheet.title = sheet_name

    for i in range(1, columns + 1):
        sheet.cell(row=1, column=i).value = input("Enter column title: ")

    wb.save(filename=file_name)


def new_all_students_default(file_name: str, sheet_name: str):
    """
    Creates a new Excel file with a default structure for adding student information.

    Args:
        file_name (str): The name of the file (for example - "all_2024.xlsx").
        sheet_name (str): The name of the sheet in the Excel workbook.

    Returns:
        None
    """
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'ALL-2024'

    sheet['A1'] = 'first_name'
    sheet['B1'] = 'last_name'
    sheet['C1'] = 'gender'
    sheet['D1'] = 'date_of_birth'
    sheet['E1'] = "parent"

    wb.save(filename=file_name)


def load_existing_file(file_path: str):
    """
    Loads an existing Excel file and returns the workbook and its sheets.

    Args:
        file_path (str): The path to the Excel file to be loaded.
    Returns:
        workbook
    """
    workbook = load_workbook(file_path)

    print(workbook.sheetnames)
    return workbook


def save_existing_file(workbook, file_name: str):
    """
    Saves the given workbook to the specified file.

    Args:
        workbook (Workbook): The workbook to be saved.
        file_name (str): The name of the file to save the workbook to.

    Returns:
        None
    """
    workbook.save(filename=file_name)
    print(f"Workbook saved as {file_name}")


def file_menu():
    """
    Main function to provide user interaction.
    """
    current_workbook = None
    available_sheets = None
    while True:
        # Display menu options
        print("1. Create new custom file")
        print("2. Create new default file")
        print("3. Load existing file")
        print("4. Save changes to an existing file")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sheetname = input("Enter a name for your sheet: ")
            filename = input("Enter a name for your file: ")
            amount_columns = int(input("How many columns do you want?: "))
            new_all_students_custom(sheetname, filename, amount_columns)
        elif choice == '2':
            filename = input("Enter name for your file: ")
            sheetname = input("Enter a name for your sheet: ")
            new_all_students_default(filename, sheetname)
        elif choice == '3':
            file_path = input("Enter a file path: ")
            result = load_existing_file(file_path)
            current_workbook = result['workbook']
            available_sheets = result['available_sheets']
            print(f"Workbook loaded with sheets: {', '.join(available_sheets.keys())}")
        elif choice == '4':
            if current_workbook is None:
                print("No workbook loaded. Please first load a workbook")
            else:
                file_name = input("Enter a file name with extension( .xlsx): ")
                save_existing_file(current_workbook, file_name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
