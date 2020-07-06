# -*- encoding: utf-8 -*-
"""
@File    : testspark.py
@Time    : 2020/7/3 15:13
@Author  : zhangsongqing
@annotation： XXX
"""
# from pyspark import SparkConf, SparkContext
# from pyspark.sql.functions import concat, concat_ws
#
# # 创建SparkConf和SparkContext
# conf = SparkConf().setMaster("local").setAppName("wordcount")
# sc = SparkContext(conf=conf)

# # 输入的数据
# data = ["hello", "world", "hello", "word", "count", "count", "hello"]
# #rdd = sc.parallelize(data, 2)
# rdd = sc.parallelize(data)
# rdd1 = rdd.collect()
# print('rdd1:',rdd1)
# print(type(rdd1))
# #glom()函数：将获取的数据根据指定并行度分为平行度数个list
# #[['hello', 'world', 'hello'], ['word', 'count', 'count', 'hello']]
# #print(rdd.flatMap(lambda x: x.split(",")).collect())
# #RDDAdd = rdd.flatMap(lambda x: x.split(",")).flatMap(lambda y: y.capitalize()).collect()
# #RDDAdd = rdd.flatMap(lambda x: x.split(",")).flatMap(lambda y: y.upper()).collect()
# for y in rdd1:
#     print(type(y))
#     print(y)
# RDDAdd = (rdd.flatMap(lambda x: x.split(','))).collect()
# print(type(RDDAdd))
# #rdd.flatMap(lambda x: x.split(",")).foreach(print)
# for x in RDDAdd:
#     print(type(x))
#     print(x)
# print(type(RDDAdd))
from pyspark.sql import SparkSession
# spark = SparkSession.builder \
#     .master("local") \
#     .appName("Word Count") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()
spark = SparkSession.builder.master('local').appName('wordcount').config("spark.some.config.option", "some-value").getOrCreate()
from pyspark.sql.functions import concat, concat_ws
data = [("hello", "world", "hello", "word", "count", "count", "hello"),("zsq", "world", "hello", "bbbbbbbbb", "count", "count", "hello")]
# df = spark.createDataFrame(data,['a','b','c','d','e','f','g'])
# print(df.collect())
# #df = spark.createDataFrame([('abcd','123zsq')], ['s', 'd'])
#
# # 1.直接拼接
# df.select(concat(df.a, df.d).alias('s')).show()
# # abcd123

# print(sorted(rdd.glom().collect()))
d = [{'name': 'Alice', 'age': 1},{'name': 'jack', 'age': 33}]
print(spark.createDataFrame(d).collect())