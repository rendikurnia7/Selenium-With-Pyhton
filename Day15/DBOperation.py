#insert , update, delete

import pymysql
import mysql.connector

con=pymysql.connect(host="localhost",port=80,user="root",passwd="",database="test")

curs=con.cursor()   #create curosor
#curs.execute("insert into student  values(104,'Kim')")  #execute query through curosor

#con.commit()    #Commit transaction
con.close()

print("finish")