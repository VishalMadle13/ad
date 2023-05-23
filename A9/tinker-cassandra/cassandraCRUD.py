from tkinter import *
from tkinter import messagebox

from cassandra.cluster import Cluster
cluster = Cluster()
con=cluster.connect('teknath33')



root=Tk()
root.geometry('400x350')
root.title("Employee Details")
root.configure(bg="cyan")

def add_course(): # new window definition
    def add_query():
        global root
        stat="INSERT INTO employee(emp_id,emp_name) VALUES ('"+E1.get()+"','"+E2.get()+"')"
        con.execute(stat)
        add.config(state=NORMAL)
        update.config(state=NORMAL)
        show.config(state=NORMAL)
        delete.config(state=NORMAL)
        newwin.destroy()
    newwin = Toplevel(root)
    newwin.geometry('400x350')
    add.config(state=DISABLED)
    newwin.title("Add New Employee")
    L1 = Label(newwin, text="Employee ID")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100,y=50)
    L2 = Label(newwin, text="Employee Name")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100,y=100)
    sub=Button(newwin,text="Add",command=add_query)
    sub.place(x=120,y=250)

def update_data(): # new window definition
    def UPDD():
        global root
        stat="UPDATE employee SET emp_name = '"+E1.get()+"' WHERE emp_id ='"+E2.get()+"'"
        con.execute(stat)
        add.config(state=NORMAL)
        newwin.destroy()

    newwin = Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Update Employee")
    add.config(state=NORMAL)

    L1 = Label(newwin, text="Employee Name")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=5)
    E1.place(x=100,y=50)

    L2 = Label(newwin, text="Employee ID")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=5)
    E2.place(x=100,y=100)


    sub=Button(newwin,text="Update",command=UPDD)
    sub.place(x=120,y=200)


def del_data():
    def delete():
        global root
        stat="DELETE FROM employee WHERE emp_id='"+E1.get()+"'"

        con.execute(stat)
        add.config(state=NORMAL)
        newwin.destroy()

    newwin=Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Delete Employee")
    add.config(state=NORMAL)
    L1 = Label(newwin, text="Employee ID")
    L1.place(x=10, y=50)
    E1 = Entry(newwin,bd=5)
    E1.place(x=100, y=50)
    sub = Button(newwin, text="Delete Employee", command=delete)
    sub.place(x=120, y=200)


def display():
    newwin=Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("STUDENT Details")
    stat="SELECT * FROM employee"
    rows=con.execute(stat)
    L1=Label(newwin,text="Employee ID")
    L1.grid(row=0,column=0)
    L2 = Label(newwin, text="Employee Name")
    L2.grid(row=0, column=1)

    i=1
    for row in rows:
        L1 = Label(newwin, text=row.emp_id)
        L1.grid(row=i, column=0)
        L2 = Label(newwin, text=row.emp_name)
        L2.grid(row=i, column=1)
        i+=1


add= Button(root,text='Add New Employee',command=add_course)
delete= Button(root,text='Delete Employee Entry',command=del_data)
update= Button(root,text='Update Employee Details',command=update_data)
show= Button(root,text='Show Employee Details',command=display)
add.place(x=50,y=50)
delete.place(x=50,y=100)
update.place(x=200,y=50)
show.place(x=200,y=100)

root.mainloop()