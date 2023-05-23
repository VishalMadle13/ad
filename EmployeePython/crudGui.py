# for mysql
# pip install mysql-connector-python
# import mysql.connector
# conn = mysql.connector.connect(
#     host='your_host',
#     user='your_username',
#     password='your_password',
#     database='your_database'
# )

#  for oralce 
# pip install cx_Oracle 
# import cx_Oracle
# conn = cx_Oracle.connect(
#     'your_username/your_password@your_host:your_port/your_service_name'
# )

import tkinter as tk
import mysql.connector

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Pass@12345',
    database='2020BTECS00092',
    auth_plugin='mysql_native_password'
)


# Function to insert a new record
def create_record():
    emp_no = int(emp_no_entry.get())
    name = name_entry.get()
    address = address_entry.get()
    grade = int(grade_entry.get())
    salary = float(salary_entry.get())
    date_of_joining = date_of_joining_entry.get()

    cursor = conn.cursor()
    insert_query = """
    INSERT INTO Employees (EmpNo, Name, address, Grade, Salary, Date_of_joining)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    record = (emp_no, name, address, grade, salary, date_of_joining)
    cursor.execute(insert_query, record)
    conn.commit()
    cursor.close()

    clear_entries()
    display_records()

# Function to read records
def display_records():
    cursor = conn.cursor()
    select_query = "SELECT * FROM Employees"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    cursor.close()

    # Clear existing records
    for child in records_frame.winfo_children():
        child.destroy()

    # Display records
    for row in rows:
        record_text = f"EmpNo: {row[0]}, Name: {row[1]}, Address: {row[2]}, Grade: {row[3]}, Salary: {row[4]}, Date of Joining: {row[5]}"
        label = tk.Label(records_frame, text=record_text, bg="#f0f0f0", relief=tk.SOLID, padx=10, pady=5)
        label.pack(fill=tk.X)

# Function to clear entry fields
def clear_entries():
    emp_no_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    date_of_joining_entry.delete(0, tk.END)

# Function to update a record
def update_record():
    emp_no = int(emp_no_entry.get())
    salary = float(salary_entry.get())

    cursor = conn.cursor()
    update_query = """
    UPDATE Employees
    SET Salary = %s
    WHERE EmpNo = %s
    """
    record = (salary, emp_no)
    cursor.execute(update_query, record)
    conn.commit()
    cursor.close()

    clear_entries()
    display_records()

# Function to delete a record
def delete_record():
    emp_no = int(emp_no_entry.get())

    cursor = conn.cursor()
    delete_query = "DELETE FROM Employees WHERE EmpNo = %s"
    cursor.execute(delete_query, (emp_no,))
    conn.commit()
    cursor.close()

    clear_entries()
    display_records()

# Create the main window
window = tk.Tk()
window.title("Employee Management")

# Create labels and entry fields
emp_no_label = tk.Label(window, text="EmpNo:", font=("Helvetica", 12))
emp_no_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
emp_no_entry = tk.Entry(window, font=("Helvetica", 12))
emp_no_entry.grid(row=0, column=1, padx=10, pady=5)

name_label = tk.Label(window, text="Name:", font=("Helvetica", 12))
name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(window, font=("Helvetica", 12))
name_entry.grid(row=1, column=1, padx=10, pady=5)

address_label = tk.Label(window, text="Address:", font=("Helvetica", 12))
address_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
address_entry = tk.Entry(window, font=("Helvetica", 12))
address_entry.grid(row=2, column=1, padx=10, pady=5)

grade_label = tk.Label(window, text="Grade:", font=("Helvetica", 12))
grade_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
grade_entry = tk.Entry(window, font=("Helvetica", 12))
grade_entry.grid(row=3, column=1, padx=10, pady=5)

salary_label = tk.Label(window, text="Salary:", font=("Helvetica", 12))
salary_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
salary_entry = tk.Entry(window, font=("Helvetica", 12))
salary_entry.grid(row=4, column=1, padx=10, pady=5)

date_of_joining_label = tk.Label(window, text="Date of Joining:", font=("Helvetica", 12))
date_of_joining_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
date_of_joining_entry = tk.Entry(window, font=("Helvetica", 12))
date_of_joining_entry.grid(row=5, column=1, padx=10, pady=5)

# Create buttons
create_button = tk.Button(window, text="Create", font=("Helvetica", 12), command=create_record)
create_button.grid(row=6, column=0, padx=10, pady=10)

update_button = tk.Button(window, text="Update", font=("Helvetica", 12), command=update_record)
update_button.grid(row=6, column=1, padx=10, pady=10)

delete_button = tk.Button(window, text="Delete", font=("Helvetica", 12), command=delete_record)
delete_button.grid(row=6, column=2, padx=10, pady=10)

display_button = tk.Button(window, text="Display Records", font=("Helvetica", 12), command=display_records)
display_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Create a frame to display records
records_frame = tk.Frame(window, bg="#f0f0f0", relief=tk.SOLID)
records_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=10, sticky=tk.W+tk.E)

# Configure grid weights to make the entry fields and frame expandable
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(8, weight=1)

# Start the GUI application
window.mainloop()

# Close the database connection
conn.close()
