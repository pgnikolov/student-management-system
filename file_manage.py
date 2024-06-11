from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet


def delete_row(sheet: Worksheet, first_name_del: str, last_name_del: str):
    """
        Delete all rows from a worksheet in the given workbook.
    Args:
        sheet: The worksheet to delete from.
        first_name_del: Student's first name to delete.
        last_name_del: Student's last name to delete.
    Return:
        sheet without the deleted row.
    """

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=2):
        first_name = row[0].value
        last_name = row[1].value

        if first_name == first_name_del and last_name == last_name_del:
            # Delete the row if the first and last names match
            sheet.delete_rows(row[0].row)
            break  # Exit the loop after deleting the first matching row

    return sheet


def load_existing_file(file_path: str):
    """
    Loads an existing Excel file and returns the workbook and its sheets.

    Args:
        file_path (str): The path to the Excel file to be loaded.
    Returns:
        workbook
    """
    workbook = load_workbook(file_path)

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
