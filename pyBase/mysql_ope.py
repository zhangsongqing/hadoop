# -*- encoding: utf-8 -*-
"""
@File    : mysql_ope.py
@Time    : 2020/6/30 17:29
@Author  : zhangsongqing
@annotation： XXX
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="106.55.163.16",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="123456",  # 数据库密码
    database="orderdb"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)
#sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
#val = ("RUNOOB", "https://www.runoob.com")
#mycursor.execute(sql, val)#一次插入单条数据

# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]

#mycursor.executemany(sql, val)#一次插入多条数据

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)
#mydb.commit()  # 数据表内容有更新，必须使用到该语句
#print(mycursor.rowcount, "记录插入成功。")