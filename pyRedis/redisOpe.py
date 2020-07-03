# -*- encoding: utf-8 -*-
"""
@File    : redisOpe.py
@Time    : 2020/7/2 12:11
@Author  : zhangsongqing
@annotation： XXX
"""

import redis
redisClient = redis.Redis(host='106.55.163.16',port=6379,password='')
#redis 0 - 15 总共16个
v = redisClient.get("a")
s1 = str(v,encoding='utf-8')
print(s1)