# -*- encoding: utf-8 -*-
"""
@File    : pySparkCon.py
@Time    : 2020/7/3 14:11
@Author  : zhangsongqing
@annotation： XXX
"""
# import pyspark
# import os
# os.environ['SPARK_HOME'] = r"D:\spark-2.1.1-bin-hadoop2.7"  #（有用）
# from pyspark import SparkContext as sc
# from pyspark import SparkConf
# conf=SparkConf().setMaster('spark://node1.hadoop:7077').setAppName("miniProject")
# sc=sc(conf=conf)
#
# #（a）利用list创建一个RDD;使用sc.parallelize可以把Python list，NumPy array或者Pandas Series,Pandas DataFrame转成Spark RDD。
# rdd = sc.parallelize([1,2,3,4,5])
# #rdd
# #Output:ParallelCollectionRDD[0] at parallelize at PythonRDD.scala:480
#
# #（b）getNumPartitions()方法查看list被分成了几部分
# rdd.getNumPartitions()
# #Output:4

# import os
# from pyspark import SparkContext
# from pyspark import SparkConf
# # os.environ['SPARK_HOME'] = r"F:\big_data\spark-2.3.3-bin-without-hadoop"
# os.environ['SPARK_HOME'] = r"D:\spark-2.1.1-bin-hadoop2.7"
# # os.environ["HADOOP_HOME"] = r"F:\big_data\hadoop-2.6.5"
# # os.environ['JAVA_HOME'] = r"F:\Java\jdk1.8.0_144"
# print(0)
# conf = SparkConf().setMaster("spark://node1.hadoop:7077").setAppName("test")
# sc = SparkContext(conf=conf)
# print(1)
# logData = sc.textFile("file:///zywa/spark/spark-2.1.1-bin-hadoop2.7/test.sh").cache()
# print(2)
# print("num of a",logData)
# sc.stop()
# -*- coding:utf8-*-
# from pyspark import SparkConf, SparkContext
# import findspark
# findspark.init(r"D:\spark-2.1.1-bin-hadoop2.7")
# import os
# os.environ['PYSPARK_PYTHON']='D:\python3'
# #conf = SparkConf().setAppName("WordCount").setMaster('spark://node1.hadoop:7077')
# conf = SparkConf().setAppName("WordCount").setMaster('local[2]')
# sc = SparkContext(conf=conf)
# #inputFile = "hdfs://node1.hadoop:9000/README.md"
# inputFile = "a.txt"
# textFile = sc.textFile()
# #wordCount = textFile.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# print(textFile)
# resultColl = textFile.collect()
# for line in resultColl:
#     print(line)


from pyspark import SparkConf, SparkContext

# 创建SparkConf和SparkContext
conf = SparkConf().setMaster("local").setAppName("wordcount")
sc = SparkContext(conf=conf)

# 输入的数据
data = ["hello", "world", "hello", "word", "count", "count", "hello"]
inputFile = "hdfs://node1.hadoop:9000/README.md"
# 将Collection的data转化为spark中的rdd并进行操作
#rdd = sc.parallelize(data)
rdd = sc.textFile(inputFile)
countRdd = rdd.count()
print('countRdd:',countRdd)
from operator import add
#resultRdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
resultRdd = rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(add)
# rdd转为collecton并打印
resultColl = sorted(resultRdd.collect())
for line in resultColl:
    print(line)

# 结束
sc.stop()


