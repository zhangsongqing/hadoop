# -*- encoding: utf-8 -*-
"""
@File    : excel_ope.py
@Time    : 2020/6/30 17:53
@Author  : zhangsongqing
@annotation： XXX
"""

'''
第一个参数为：行
第二个参数为：列
第三个参数为：单元格数据
'''
import xlwt
wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('智联python招聘信息')
ws.write(0, 0, label='序号')
ws.write(0, 1, label='招聘公司')
ws.write(0, 2, label='工资')
ws.write(0, 3, label='职业')
ws.write(0, 4, label='职位')
a = 1
list = [[1,2,3,4,5],[6,7,8,9,10]]
for index in list:
    # print(index)
    for x in index:
        for bot in range(0,len(index)):
            ws.write(a, x, label=str(index[bot]))#1,0，1
    if a < len(list):
       a += 1
ws.col(0).width = 1300
ws.col(4).width = 15999
ws.col(1).width = 13999
wb.save('pipi.xls')