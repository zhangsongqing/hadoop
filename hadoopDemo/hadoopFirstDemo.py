# -*- encoding: utf-8 -*-
"""
@File    : hadoopFirstDemo.py
@Time    : 2020/6/24 09:12
@Author  : zhangsongqing
@annotation： XXX
"""
import pyhdfs
fs = pyhdfs.HdfsClient(hosts='172.10.4.95:50070',user_name='hadoop')
print(fs.get_home_directory())#返回这个用户的根目录
#返回可用的namenode节点
print(fs.get_active_namenode())
fs.mkdirs("/aa")
str = fs.copy_from_local(localsrc="./test.txt",dest="/aa/ssst.txt")
print(str)
    # with open(localsrc, "rb") as f:
    #     self.create(dest, f, **kwargs)
# from hdfs import Client
# client=Client(url="172.10.4.95:50070",root="/",timeout=1000,session=False)
# client.list("/")
# print(client.list("/"))

