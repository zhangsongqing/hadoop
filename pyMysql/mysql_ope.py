# -*- encoding: utf-8 -*-
"""
@File    : mysql_ope.py
@Time    : 2020/7/2 14:25
@Author  : zhangsongqing
@annotation： XXX
"""
import mysql.connector
import hadoop.config.configOpe as config
mysqldb = mysql.connector.connect(
    host = config.getMysqlIp(),
    user = config.getMysqlUser(),
    password = config.getMysqlPassword(),
    database = config.getMysqlDatabase()
)
mycursor = mysqldb.cursor()
#sql = "SHOW DATABASES;"
def showDatabases():
    mycursor.execute("show databases")
    dataBaseList = mycursor.fetchall()
    for x in dataBaseList:
        print("数据库有：",x)
# myresult = mycursor.execute("SHOW TABLES")
# #print(mycursor.fetchall())
#
# allTable = mycursor.fetchall()
# print("类型：",type(allTable))
# for x in allTable:
#     print(x)
# print("------------------------------")
# myresult = mycursor.execute("SHOW TABLES")
# print(type(mycursor.fetchone()))
# print(mycursor.fetchone())
# mycursor.execute("SELECT * FROM sites")
#
# myresult = mycursor.fetchall()  # fetchall() 获取所有记录
#
# for x in myresult:
#     print(x)
# for x in myresult:
# #     print(x)
if __name__ == '__main__':
    showDatabases()