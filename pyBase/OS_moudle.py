# -*- encoding: utf-8 -*-
"""
@File    : OS_moudle.py
@Time    : 2020/6/30 13:14
@Author  : zhangsongqing
@annotation： XXX
"""
import os
#得到当前文件的路径
print(os.getcwd())
print(os.curdir)

f = open(file="./a.txt",mode="a+",encoding="utf8")
#默认会写入到当前项目的文件夹下
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.write("这是一个测试文件")
# 关闭打开的文件
f.close()
