# -*- encoding: utf-8 -*-
#coding=utf8
"""
@File    : sparkSql_hive.py
@Time    : 2020/7/7 17:13
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession

import os
import sys
import subprocess
import platform
import datetime
from datetime import date, timedelta
os.environ ['JAVA_HOME'] = 'E:\java\jdk\bin\java.exe'
#os.environ ['JAVA_HOME'] = '/usr/bin/java'
os.environ['SPARK_HOME'] = "D:\spark-2.1.1-bin-hadoop2.7"
#os.environ["PYSPARK_SUBMIT_ARGS"] = "--master local"
os.environ["PYSPARK_PYTHON"] = "D:\python3"

#def getSpark(path):
def getSpark():
    #_pro = getPro(path, "mysql.properties")
    #print(_pro)
    #_pro = {'javax.jdo.option.connectionurl':'jdbc:mysql://172.10.4.144:5480/hive?createDatabaseIfNotExist=true&amp;characterEncoding=UTF-8',
    #        'javax.jdo.option.connectiondrivername':'com.mysql.jdbc.Driver',
     #       'javax.jdo.option.connectionusername':'test2',
     #       'avax.jdo.option.connectionpassword':'D5u8SS+qCbT8'}
#?createDatabaseIfNotExist=true&amp;characterEncoding=UTF-8
    conf = SparkConf()\
        .set("javax.jdo.option.ConnectionURL", 'jdbc:mysql://172.10.4.77:3306/hive?createDatabaseIfNotExist=true')\
        .set("javax.jdo.option.ConnectionDriverName",'com.mysql.jdbc.Driver' )\
        .set("javax.jdo.option.ConnectionUserName", 'root')\
        .set("javax.jdo.option.ConnectionPassword", 'password')\
        .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")\
        .set("spark.sql.parquet.writeLegacyFormat", "true")\
        .set("spark.sql.hive.convertMetastoreParquet", "false")\
        .set("hive.input.format", "org.apache.hadoop.hive.ql.io.CombineHiveInputFormat")\
        .set("mapred.max.split.size", "256000000")\
        .set("mapred.min.split.size.per.node", "100000000")\
        .set("mapred.min.split.size.per.rack", "100000000")\
        .set("hive.merge.mapfiles", "true")\
        .set("hive.merge.mapredfiles", "true")\
        .set("hive.merge.size.per.task", "256*1000*1000")\
        .set("hive.merge.smallfiles.avgsize", "16000000")\
        .set("hive.exec.reducers.bytes.per.reducer", "512000000")\
        .set("hive.exec.max.created.files", "100")\
        .set("spark.sql.adaptive.enabled", "true")\
        .set("spark.sql.adaptive.shuffle.targetPostShuffleInputSize", "128000000")

    if "Linux" not in platform.system():
        print("xxx")
        conf.setMaster("local")\
            .setAppName("pyspark hive")
        print("xxx")

        spark=SparkSession \
            .builder \
            .config(conf=conf) \
            .getOrCreate()
    sc = spark.sparkContext

    # spark = SparkSession \
    #     .builder.master("local")\
    #     .appName('my_first_app_name') \
    #     .getOrCreate()

    # spark.sparkContext.setLogLevel("ERROR")
    #
    # # hive元数据信息初始化
    # spark.sql("use aijiami")
    # spark.sql("set hive.exec.dynamic.partition=true")
    # spark.sql("set hive.exec.dynamic.partition.mode=nonstrict")
    return spark

def test(spark: SparkSession):
    spark.sql("use aijiami")
    spark.sql("desc dw_opera_detail").show(100)


if __name__ == '__main__':
    spark = getSpark()
    print(getSpark())
    # test(spark)

