# -*- encoding: utf-8 -*-
"""
@File    : file_read.py
@Time    : 2020/6/30 14:20
@Author  : zhangsongqing
@annotation： XXX
"""
'''
读取文件
    1、全部读取，read()，可指定大小
    2、每次读取一行，readline()，可指定大小，不足一行，按一行算
    3、一次读取所有行，readlines()，可指定大小，不足一行，按一行算
'''
#read()
# print("===================read()================")
# f = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r+",encoding="utf8")
# print(f.read(200))
# print("read类型：",type(f.read()))
# f.close()
#
# #readline()
# print("===================readline()================")
# f2 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# print(f2.readline())
# print("readline类型：",type(f2.readline()))
# f2.close()
# print("\n")
# #readline()
#
# print("===================2:readline()================")
# a2 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# # print(a2.readline())
# # print("readline类型：",type(a2.readline()))
# line = 1
# while line:
#     line = a2.readline()
#     print(line,end="")
# a2.close()
# print("\n")
#
# #readlines()
# print("===================readlines()================")
# f3 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# print(f3.readlines(200))
# print("readlines类型:",type(f3.readlines()))
# f3.close()
# print("\n")
# #直接对一个file对象使用for循环读每行数据
# print("===================直接对file对象遍历================")
# f4 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# print(type(f4))
# for line in f4:
#    print(line,end="")#end="",忽略换行符
# f4.close()
# print("\n")
#
#
# #一次读取多行，循环读取，直至读完
# print("===================1:一次读取多行，循环读取，直至读完================")
# f5 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# f6 = open(file="e.txt",mode="a+",encoding="utf8")
# lines = 1
# while lines:
#     lines = f5.readlines(300)#当设定大小不足一行字符，按一行读取
#     length = len(lines)
#     print("lines的长度：",length)
#     for i in range(0,length):
#         print(lines[i],end="")
#     #s = str(lines[0])
#     #print(s,end=" ")
#     #f6.write(str(lines[0]))
# f5.close()
# print("\n")
#
# #一次读取多行，循环读取，直至读完
# print("===================2:一次读取多行，循环读取，直至读完================")
# f7 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
# lines = 1
# while lines:
#     lines = f7.readlines(20)#当设定大小不足一行字符，按一行读取
#     #length = len(lines)
#     #print("lines的长度：",length)
#     for y in iter(lines):
#         print(y,end="")
# f7.close()
# print("\n")


#一次读取多行，循环读取，直至读完
print("===================3:一次读取多行，循环读取，直至读完================")
# f9 = open(file="G:\\pynamespace\\pyhadoop\\hadoop\\pyBase\\b.txt",mode="r",encoding="utf8")
f9 = open(file=r"G:\pynamespace\pyhadoop\hadoop\pyBase\b.txt",mode="r",encoding="utf8")
while 1:
    lines = f9.readlines(30)#当设定大小不足一行字符，按一行读取
    length = len(lines)
    if not lines:
        break
    for i in range(0,length):
        print(lines[i],end="")
f9.close()
