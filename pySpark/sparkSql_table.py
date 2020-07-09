# -*- encoding: utf-8 -*-
"""
@File    : sparkSql_table.py
@Time    : 2020/7/7 16:32
@Author  : zhangsongqing
@annotation： XXX
"""
from pyspark.sql import SparkSession
'''
1、创建连接
'''
spark=SparkSession \
        .builder \
        .appName('my_first_app_name') \
        .getOrCreate()
'''
2. 创建dataframe
2.1. 从变量创建
'''

# 生成以逗号分隔的数据
stringCSVRDD = spark.sparkContext.parallelize([
    (123, "Katie", 19, "brown"),
    (234, "Michael", 22, "green"),
    (345, "Simone", 23, "blue")
])
# 指定模式, StructField(name,dataType,nullable)
# 其中：
#   name: 该字段的名字，
#   dataType：该字段的数据类型，
#   nullable: 指示该字段的值是否为空
from pyspark.sql.types import StructType, StructField, LongType, StringType  # 导入类型

schema = StructType([
    StructField("id", LongType(), True),
    StructField("name", StringType(), True),
    StructField("age", LongType(), True),
    StructField("eyeColor", StringType(), True)
])

# 对RDD应用该模式并且创建DataFrame
swimmers = spark.createDataFrame(stringCSVRDD,schema)

# 利用DataFrame创建一个临时视图
swimmers.registerTempTable("swimmers")

# 查看DataFrame的行数
print(swimmers.count())
sqlDF = spark.sql("SELECT * FROM swimmers where id = 234")
sqlDF.show()
spark.stop()