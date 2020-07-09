# -*- encoding: utf-8 -*-
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession

spark=None

def test():
    conf = SparkConf() \
        .set("javax.jdo.option.ConnectionURL", 'jdbc:mysql://172.10.4.77:3306/hive') \
        .set("javax.jdo.option.ConnectionDriverName", 'com.mysql.jdbc.Driver') \
        .set("javax.jdo.option.ConnectionUserName", 'root') \
        .set("javax.jdo.option.ConnectionPassword", 'password') \
        .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .set("spark.sql.parquet.writeLegacyFormat", "true") \
        .set("spark.sql.hive.convertMetastoreParquet", "false") \
        .set("hive.input.format", "org.apache.hadoop.hive.ql.io.CombineHiveInputFormat") \
        .set("mapred.max.split.size", "256000000") \
        .set("mapred.min.split.size.per.node", "100000000") \
        .set("mapred.min.split.size.per.rack", "100000000") \
        .set("hive.merge.mapfiles", "true") \
        .set("hive.merge.mapredfiles", "true") \
        .set("hive.merge.size.per.task", "256*1000*1000") \
        .set("hive.merge.smallfiles.avgsize", "16000000") \
        .set("hive.exec.reducers.bytes.per.reducer", "512000000") \
        .set("hive.exec.max.created.files", "100") \
        .set("spark.sql.adaptive.enabled", "true") \
        .set("spark.sql.adaptive.shuffle.targetPostShuffleInputSize", "128000000")
    conf.setMaster("local") \
        .setAppName("pyspark hive")

    spark = SparkSession \
        .builder \
        .config(conf=conf) \
        .enableHiveSupport()\
        .getOrCreate()

    spark.sql("use aijiami")
    spark.sql("show tables").show()

    print(spark)


if __name__ == '__main__':
    test()