#insert , update, delete



#insert_query="insert into student  values(104,'Sely')"
#update_query="update student set sname ='caca' where sname='Lala'"
delete_query="delete from student where sid='105'"

import mysql.connector
# try:
#    con = mysql.connector.connect(host='localhost'
#                                   , user='root',
#                                   passwd='',
#                                   database='test')
#    curs=con.cursor()   #create curosor
#    curs.execute(delete_query)  #execute query through curosor
#    con.commit()    #Commit transaction
#    con.close()
# except:
#    print("Failed Connetcting Database")


#Select Commands
try:
   con = mysql.connector.connect(host='localhost'
                                  , user='root',
                                  passwd='',
                                  database='test')
   curs=con.cursor()   #create curosor
   curs.execute("select * from orders")
   for row in curs:
       print(row[0],row[1],row[2])
   con.close()
except:
   print("Failed Connetcting Database")
print("finish")