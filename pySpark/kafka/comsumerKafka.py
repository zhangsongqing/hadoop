# -*- encoding: utf-8 -*-
"""
@File    : comsumerKafka.py
@Time    : 2020/7/9 14:49
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def start():
    conf = SparkConf().set("spark.python.profile", "true").set("spark.io.compression.codec", "snappy").setMaster('local')
    conf.setAppName('spark-test')
    sc = SparkContext(conf=conf)
    ssc=StreamingContext(sc,6)

    brokers="172.10.4.96:9092,172.10.4.96:9091"
    topic='test'
    kafkaStreams = KafkaUtils.createDirectStream(ssc,[topic],kafkaParams={"metadata.broker.list": brokers})
    result=kafkaStreams.map(lambda x:(x[1],1)).reduceByKey(lambda x, y: x + y)
    kafkaStreams.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)
    result.pprint()
    ssc.start()
    ssc.awaitTermination()

offsetRanges = []

def storeOffsetRanges(rdd):
    global offsetRanges
    offsetRanges = rdd.offsetRanges()
    return rdd

def printOffsetRanges(rdd):
    for o in offsetRanges:
        print("%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset,o.untilOffset-o.fromOffset))

if __name__ == '__main__':
    start()
