# -*- encoding: utf-8 -*-
"""
@File    : baseConfigOpe.py
@Time    : 2020/7/3 11:39
@Author  : zhangsongqing
@annotation： XXX
"""
import configparser

config = configparser.ConfigParser()
config.read("../properties.conf")
# config_lists = config.sections()
# options = config.options('mysql')
# print(options[0])
# print(type(options))
# print(options)
# values = config.values()
# for x in values:
#     print(x)


class BaseConfigOpe():
    def getConfigSection(self,Section):
        itemsList = config.items(Section)
        print(itemsList)
        dict = {}
        '''
        将获取到的配置文件list转为dict，
        可以根据key直接获取对应的配置项值
        '''
        for x in range(0, len(itemsList)):
            dict[(itemsList[x])[0]] = (itemsList[x])[1]
        return (dict)
