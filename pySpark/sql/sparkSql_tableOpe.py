# -*- encoding: utf-8 -*-
"""
@File    : sparkSql_tableOpe.py
@Time    : 2020/7/8 11:47
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark.sql import SparkSession
from pyspark.sql.types import *
'''
1.创建spark程序入口对象
'''
spark = SparkSession.builder.master('local').config('a','b').getOrCreate()
sc = spark.sparkContext

'''
2、读取一个文件为RDD
'''
# Load a text file and convert each line to a Row.
lines = sc.textFile("file:///G:\pynamespace\pyhadoop\hadoop\pySpark\people.txt")
#print('lines:',type(lines))
parts = lines.map(lambda l: l.split(","))
# Each line is converted to a tuple.
people = parts.map(lambda p: (p[0], p[1].strip()))
#print('people:',people.collect())
# The schema is encoded in a string.
schemaString = "name age"

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)

# Apply the schema to the RDD.
schemaPeople = spark.createDataFrame(people, schema)

# Creates a temporary view using the DataFrame
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
results = spark.sql("SELECT name,age FROM people")

results.show()