# -*- encoding: utf-8 -*-
"""
@File    : kafkaProduct.py
@Time    : 2020/7/2 09:28
@Author  : zhangsongqing
@annotation： XXX
"""

import json
import datetime,time
from kafka import KafkaProducer
#
# producer = KafkaProducer(bootstrap_servers='172.10.4.96:9092')
#
# msg_dict = {
#     "sleep_time": 10,
#     "db_config": {
#         "database": "test_1",
#         "host": "xxxx",
#         "user": "root",
#         "password": "root"
#     },
#     "table": "msg",
#     "msg": "Hello World"
# }
# msg = json.dumps(msg_dict)
# producer.send('test_rhj', msg, partition=0)
# producer.close()

producer=KafkaProducer(bootstrap_servers='172.10.4.96:9092')
for i in range(111):
    future = producer.send('testDemo', json.dumps(
        {"method": "get", "step": i, "type": "test", "testName": "kafka",
         "cid": "{0}".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
         "info": "demo{}".format(1)}).encode())
    record_metadata = future.get(timeout=10)
    print(record_metadata, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(3)