import mysql.connector
connn = mysql.connector.connect(user='root',password='',database='test')
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user(id,name) values(%s %s)',['1','Michael'])
print(cursor.rowcount)
#提交事务
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
print(cursor.fetchall())
cursor.close()
conn.close()