# -*- encoding: utf-8 -*-
"""
@File    : configOpe.py
@Time    : 2020/7/2 12:21
@Author  : zhangsongqing
@annotation： XXX
"""
import configparser

config = configparser.ConfigParser()
config.read("../properties.conf")
config_lists = config.sections()
options = config.options('mysql')
print(options[0])
print(type(options))
print(options)
values = config.values()
for x in values:
    print(x)
redisCon = config.items('redis')
print(redisCon)
dict = {}
'''
将获取到的配置文件list转为dict，
可以根据key直接获取对应的配置项值
'''
for x in range(0,len(redisCon)):
    dict[x].x[0]=(redisCon[x])[0]

print(type(redisCon))
print(config.items("redis")[0][1])
#print(config_lists)
#print(type(config_lists))
#print(str(config['mysql']['ip']))

def getMysqlIp():
    IP = config["mysql"]['ip']
    return str(IP)
def getMysqlPort():
    PORT = config["mysql"]['port']
    return str(PORT)
def getMysqlUser():
    USER = config["mysql"]['user']
    return str(USER)
def getMysqlPassword():
    PASSWORD = config["mysql"]['password']
    return str(PASSWORD)
def getMysqlDatabase():
    DATABASE = config["mysql"]['database']
    return str(DATABASE)

#print(config_lists['redis'])

if __name__ == '__main__':
    #print('test')
    getMysqlIp()
    #print("ssssssssssssssssss")
