from tkinter import *
from tkinter import messagebox

import mysql.connector

w=Tk()
w.title("world")
w.geometry("500x500")

def createTable():
	#Create a database or connect to database 
	con=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="world")
	#create cursor
	a=con.cursor()
	#create table, we use execute
	a.execute(""" CREATE TABLE student_data (name varchar(50) primary key, classYr varchar(10) not null, prn int)""")
	messagebox.showinfo("Information","Table created successfully...:)")
	#commit changes in the database
	con.commit()
	#close database connection
	con.close()

#create insert function for database
def insert():
	con=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="world")
	b=con.cursor()
	cnt=b.rowcount
	name= e1.get()
	classYr= e2.get()
	prn= e3.get()
	try:
		sql="""INSERT INTO student_data (name,classYr,prn) VALUES (%s, %s, %s)"""
		val=(name,classYr,prn)
		b.execute(sql,val)
		messagebox.showinfo("Information","Data inserted successfully...:)")
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		con.commit()
	except Exception as e:
		print(e)
		messagebox.showinfo("Information","Sorry, data didn't get inserted...:(")
		con.rollback()
	con.close()

def delete():
	con=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="world")
	c=con.cursor()
	try:
		if c.rowcount > 0:
			messagebox.showinfo("Information","Sorry, no data exists to delete...:(")
		else:
			sql1=""" DELETE FROM student_data WHERE name= %s"""
			val1=(e4.get(),)
			c.execute(sql1,val1)
			messagebox.showinfo("Information","Data deleted successfully...:)")
			e4.delete(0,END)
			con.commit()
	except Exception as ee:
		print(ee)
		messagebox.showinfo("Information","Sorry, data didn't get deleted...:(")
		con.rollback()
	con.close()






    

def show():
	con=mysql.connector.connect(host="localhost",user="root",passwd="mysql123",database="world")
	d=con.cursor()
	d.execute("""SELECT * FROM student_data""")
	res=d.fetchall()
	result=""
	a=1
	for arr in res:
		result+=str(a)+" : "+str(arr[0])+" - "+str(arr[1])+" - "+str(arr[2])+"\n"
		a+=1
	messagebox.showinfo("Information",result)
	con.commit()
	con.close()



btn1=Button(w, text="Create student_data table", command=createTable)
btn1.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

label=Label(w, text="Insert Student Data")
label.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

label=Label(w, text="Student Name")
label.grid(row=4, column=0)

e1=Entry(w, width=50)
e1.grid(row=4, column=1, padx=30)

label1=Label(w, text="Class Year")
label1.grid(row=7, column=0)

e2=Entry(w, width=50)
e2.grid(row=7, column=1, padx=30)

label2=Label(w, text="PRN No")
label2.grid(row=10, column=0)

e3=Entry(w, width=50)
e3.grid(row=10, column=1, padx=30)

btn2=Button(w, text="Insert", command=insert)
btn2.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

label=Label(w, text="Delete Student Data")
label.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

label2=Label(w, text="Name")
label2.grid(row=16, column=0)

e4=Entry(w, width=50)
e4.grid(row=16, column=1, padx=30)

btn3=Button(w, text="Delete Student Data", command=delete)
btn3.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=50)



btn4=Button(w, text="Display Data", command=show)
btn4.grid(row=26, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

w.mainloop()
