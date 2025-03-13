Employee Management System

This is a simple command-line Employee Management System written in Python. It allows users to add, edit, delete, search, display, and save employee records in a file.

Features

Add Employee: Enter employee details and add them to the list.

Edit Employee: Modify existing employee information.

Delete Employee: Remove an employee from the list.

Search Employee: Find employees by surname and optionally save results to a file.

Display Employees: Filter employees by age or surname initial letter.

Save Data: Save all employee records to a file.

Load Data: Load employee records from a file at startup.

File Format

The employee records are stored in a CSV-like format:

Surname,Name,Age,Position

Example:

Smith,John,30,Manager
Doe,Jane,25,Developer

Usage

Run the script.

Enter the filename to load (or create a new file if it doesn’t exist).

Use the menu to interact with employee records.

Save changes before exiting.

Menu Options

1. Add Employee
2. Edit Employee
3. Delete Employee
4. Search Employee
5. Display Employee
6. Save
7. Exit

Error Handling

If the file does not exist, a new one is created.

Invalid inputs (e.g., incorrect index values) are handled with error messages.

If no employees exist, appropriate messages are displayed.

Requirements

Python 3.x

Running the Script

To run the script, use:

python script.py

Replace script.py with the actual filename of your script.

Notes

Make sure to save changes before exiting.

The program uses a simple dictionary structure to store employee data.

