# -*- encoding: utf-8 -*-
"""
@File    : sparkSql_ope.py
@Time    : 2020/7/6 14:50
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
'''
创建一个sparksql入口实例
'''
spark = SparkSession.builder.master('local')\
    .appName('testSql')\
    .config('spark.some.config.option','some-config')\
    .getOrCreate()

#sparkSession中包含sparkContext方法

sc = spark.sparkContext

#读取hdfs上一个文件
# rdd = sc.textFile('hdfs://node1.hadoop:9000/stu.txt')
# print('count:',rdd.count())
# print(type(rdd))
# rdd2 = rdd.map(lambda line: line.split(","))
# print(type(rdd2))


#执行collect()方法将rdd转为list
# resultRDD = rdd2.collect()
# print('resultRDD type:',type(resultRDD))
# print(resultRDD)
# #
# for y in resultRDD:
#     print(y)
#     for i in y:
#         print(i)
'''
通过sparkSession创建一个DataFrame,参数为一个RDD
df：dataframe
'''
# df = spark.createDataFrame(resultRDD)
#
# print("df.select('*').collect():",type(df.select('*').collect()))
# dfShow = df.select('*').collect()
# print(dfShow)

# from pyspark.sql import Row
# l = [('Alice', 1),('jack',88)]
# spark.createDataFrame(l).collect()
# spark.createDataFrame(l, ['name', 'age']).collect()

# rdd = sc.parallelize(l)
# Person = Row('name', 'age')
# person = rdd.map(lambda r: Person(*r))
# df2 = spark.createDataFrame(person)
# print(df2.collect())

# from pyspark.sql.types import *
# schema = StructType([
#    StructField("name", StringType(), True),
#    StructField("age", IntegerType(), True)])
# df3 = spark.createDataFrame(rdd, schema)
# print(df3.collect())


rdd = spark.read.text(r'hdfs://node1.hadoop:9000/stu.txt')
print(rdd.collect())
sc.stop()
spark.stop()
