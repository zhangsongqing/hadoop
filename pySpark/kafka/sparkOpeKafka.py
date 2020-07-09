# -*- encoding: utf-8 -*-
"""
@File    : sparkOpeKafka.py
@Time    : 2020/7/9 14:14
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "NetworkWordCount")
sc.setLogLevel("OFF")
ssc = StreamingContext(sc, 1)

# 创建Kafka streaming
#line = KafkaUtils.createStream(ssc, "172.10.4.96:2181", 'test', {"jim_test": 1})
line = KafkaUtils.createDirectStream(ssc,['test'], {"jim_test": 1})
print('line:',type(line))

# 分词
words = line.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint()
print('wordCounts:',type(wordCounts))

ssc.start()
ssc.awaitTermination()
