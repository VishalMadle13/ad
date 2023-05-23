import cx_Oracle

#import mysql.connector
try:
    #dsn_tns = cx_Oracle.makedsn('192.168.43.104','1521','XE')
    con = cx_Oracle.connect('SYSTEM/oracle123@localhost/XEPDB1')
    #con = mysql.connector.connect( "localhost","root","vish","world")
    # con = cx_Oracle.connect(user=r'python',password='123456',dsn = dsn_tns)
    print("succesfully connected")

    cursor = con.cursor()
    print("cursor created successfully")

    query = "create table shivani_ganesh43(name varchar(30),rollNo number)"

    cursor.execute(query)
    print("Table Created successful") 

    query = "insert into shivani_ganesh43 values('Shivani',78)"
    cursor.execute(query)
    print('Successfully inserted Shivani')

    query = "insert into shivani_ganesh43 values('Ganesh',80)"
    cursor.execute(query)
    
    print('Successfully inserted Ganesh')

    query = "insert into shivani_ganesh43 values('Arpita',98)"
    cursor.execute(query)
    print("successfully inserted Arpita")

    cursor.execute('COMMIT')

    query = 'select * from shivani_ganesh43'
    cursor.execute(query)

    res = cursor.fetchall()
    for r in res:
        print(r)
    # print('Successfully inserted Akash')


except : 
    print("There is a problem with Oracle")