from tkinter import *
from tkinter import messagebox 
from tkinter import ttk #for tables
import cx_Oracle

try:
    con = cx_Oracle.connect('SYSTEM/oracle123@localhost/XEPDB1')
    print("succesfully connected")

    cursor = con.cursor()
    # print("cursor created successfully")
except:
    # print("There is a problem with Oracle", e)
    exit()

# update_name = ''

def display():
    # print('Display clicked')
    for i in tree.get_children():
        tree.delete(i)
    
    # display_button['state'] = DISABLED
    query = 'select * from shivani_ganesh'
    cursor.execute(query)


    res = cursor.fetchall()

    if(not res):
        messagebox.showwarning("Warning", "No records available")
    else:
        for r in res:
            # e = Entry(frame_display, width=20, fg='blue', font=('Arial',11)) 
            # e.pack(fill = X)
            # e.insert(END, r)
            # e.pack(side = 'right')
            # e.insert(END, r[1])
            # print(r)

            tree.insert("",END, values=r)
                 
        # pass
        tree.pack()


        

def deleteRecord():
    roll_no = int(delete_entry.get())
    query = f'select * from shivani_ganesh where rollNo = {roll_no}'
    cursor.execute(query)


    res = cursor.fetchall()

    if(not res):
        messagebox.showwarning("Warning", "Record not available")
        return
    # print(roll_no)
    query = f'delete from shivani_ganesh where rollNo={roll_no}'
    cursor.execute(query)
    messagebox.showinfo("Info", "Successfully deleted")
    cursor.execute('commit')
    display()

def update():
    try:
        roll_no = update_entry.get()
        query = f'select * from shivani_ganesh where rollNo = {roll_no}'
        cursor.execute(query)


        res = cursor.fetchall()

        if(not res):
            messagebox.showwarning("Warning", "Record not available")
            return
        
        nm = update_name_entry.get()

        query = f"update shivani_ganesh set name = '{nm}' where rollNo = {roll_no}"
        
        cursor.execute(query)
        cursor.execute('commit')

        messagebox.showinfo("Info", "Successfully updated")
        display()


    except:
        # print('Invalid input')
        messagebox.showwarning("Warning", "Invalid input")




def addRec():
    roll_no = int(roll_entry.get())
    query = f'select * from shivani_ganesh where rollNo = {roll_no}'
    cursor.execute(query)


    res = cursor.fetchall()

    if(res):
        messagebox.showwarning("Warning", "Record already available")
        return

    nm = name_entry.get()
    query = f"insert into shivani_ganesh values({roll_no},'{nm}')"
    cursor.execute(query)

    messagebox.showinfo("Info", "Successfully inserted")
    cursor.execute('commit')
    display()
    

root = Tk()
root.title("Oracle CRUD operations")
root.geometry('900x900')




title_label = Label(text = 'Oracle Student information',bg = 'blue',fg = 'YELLOW',padx = 15, pady = 15,font ="comicsans 30 bold")
title_label.pack(anchor = 'n', side = 'top', fill= 'x' )



# insert

frame_insert = Frame(root,borderwidth=15)
frame_insert.pack(anchor = 'n',fill=X)

insert_label = Label(frame_insert, text = 'Insertion' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'black')
insert_label.pack(fill = X)

# insert_button = Button(frame_insert,text = 'Insert', command = insert)
# insert_button.pack(side='top',anchor = 's',fill = BOTH)

roll_label = Label(frame_insert, text = 'Enter Roll No' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'red')
roll_label.pack(fill = X,anchor='n')

global roll_entry
roll_entry = Entry(frame_insert,width = 20)
roll_entry.pack(anchor='n')

name_label = Label(frame_insert, text = 'Enter name' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'red')
name_label.pack(fill = X,anchor='n')

global name_entry
name_entry = Entry(frame_insert,width = 20)
name_entry.pack(anchor='n')

# global submit_button
submit_button = Button(frame_insert,text = 'Submit', command = addRec,width = 20)  
submit_button.pack(anchor='n')

# 


frame_update = Frame(root,borderwidth=20)
frame_update.pack(anchor = 'nw',fill=X,side=LEFT)

update_label = Label(frame_update, text = 'Updation' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'black')
update_label.pack(fill = X)

update_entry_label = Label(frame_update, text = 'Enter roll No' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'red')
update_entry_label.pack(side = 'top', fill = X)

update_entry = Entry(frame_update,width = 20)
update_entry.pack(side='top', fill = X)



update_name_entry_label = Label(frame_update, text = 'Name' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'red')
update_name_entry_label.pack(side = 'top', fill = X)

update_name_entry = Entry(frame_update,width = 20)
update_name_entry.pack(side='top', fill = X)

update_button = Button(frame_update,text = 'Update', command = update)
update_button.pack(side='top',anchor = 's',fill = BOTH)


frame_delete = Frame(root,borderwidth=20)
frame_delete.pack(anchor = 'ne',fill=X,side=RIGHT)

delete_label = Label(frame_delete, text = 'Deletion' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'black')
delete_label.pack(fill = X)

delete_entry_label = Label(frame_delete, text = 'Enter roll No' , padx = 15 ,pady = 15, font = "comicsans 20", fg = 'red')
delete_entry_label.pack(side = 'top', fill = X)

delete_entry = Entry(frame_delete,width = 10)
delete_entry.pack(side='top', fill = X)

delete_button = Button(frame_delete,text = 'Delete Record', command = deleteRecord)
delete_button.pack(side='top',anchor = 's',fill = BOTH)

#

#display


frame_display = Frame(root,borderwidth = 20)
frame_display.pack(fill = X, anchor = 's',side = BOTTOM)

tree = ttk.Treeview(frame_display, column=("c1", "c2"), show='headings')
tree.column("#1", anchor=CENTER)

tree.heading("#1", text="Roll No")

tree.column("#2", anchor=CENTER)

tree.heading("#2", text="NAME")

display_label = Label(frame_display,text = 'Retrival', padx = 15, pady = 15,font = "comicsans 20", fg = 'black')
display_label.pack(fill=X)

# display_button = Button(frame_display,text = 'Display Records', command = display)
# display_button.pack(fill = X)

display()

root.mainloop()
