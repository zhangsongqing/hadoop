# -*- encoding: utf-8 -*-
"""
@File    : mysqlConfigOpe.py
@Time    : 2020/7/3 11:59
@Author  : zhangsongqing
@annotation： XXX
"""
from config import baseConfigOpe
config = baseConfigOpe.BaseConfigOpe()
'''
#返回一个mysql配置字典
配置项：
    ip
    port
    user
    password
'''
def getMysqlconf():
    mysqlDict = config.getConfigSection('mysql')
    print(mysqlDict)
    return mysqlDict

