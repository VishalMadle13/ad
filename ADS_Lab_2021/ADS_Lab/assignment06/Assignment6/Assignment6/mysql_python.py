import mysql.connector
from threading import Thread
import threading
import time
import _thread

def qsort(sets,left,right):

    print("thead {0} is sorting {1}".format(threading.current_thread(), sets[left:right]))

    i = left
    j = right
    pivot = sets[int((left + right)/2)]
    temp = 0
    while(i <= j):
         while(pivot > sets[i]):
             i = i+1
         while(pivot < sets[j]):
             j = j-1
         if(i <= j):
             temp = sets[i]     
             sets[i] = sets[j]
             sets[j] = temp
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    if (left < j):
        lthread = Thread(target = lambda: qsort(sets,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(sets,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return sets

output = []

def individualjoin(thread_name, input1, input2):
    item = []
    for i in input1:
        for j in input2:
            if i[0] == j[0]:
                item.append(i[0])
                item.append(i[1])
                item.append(j[1])
                output.append(item)
                item = []

#Parallel Join
def ParallelJoin(input1, input2):
    threads = ["thread1", "thread2", "thread3", "thread4", "thread5"]
    temp_threads = []
    for i in range(5):
        temp_threads.append(
            threading.Thread(
                target=individualjoin,
                args=(
                    threads[i],
                    input1,
                    input2
                ),
            )
        )
        temp_threads[i].start()

    for t in temp_threads:
        t.join()
    res = []
    [res.append(x) for x in output if x not in res]
    for item in res:
        sql = "INSERT INTO output VALUES (%s, %s, %s)"
        val = (str(item[0]), item[1], item[2])
        mycursor.execute(sql, val)

        mydb.commit()

#Database Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="2018BCGRP10",
    passwd="shruti",
    database="world"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM wce"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for item in myresult:
    print(item)

'''testing below'''
res_sorted = qsort(myresult, 0, len(myresult) - 1)
print(res_sorted)

for item in res_sorted:
    sql = "INSERT INTO wcesort VALUES (%s, %s, %s)"
    val = (item[0], item[1], item[2])
    mycursor.execute(sql, val)

    mydb.commit()

#PARALLEL JOIN
print("Now Joining the input1 and input2")

sql = "SELECT * FROM input1"

mycursor.execute(sql)

myresult1 = mycursor.fetchall()

sql = "SELECT * FROM input2"

mycursor.execute(sql)

myresult2 = mycursor.fetchall()

ParallelJoin(myresult1, myresult2)

for item in output:
    print(item)
