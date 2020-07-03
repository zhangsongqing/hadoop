# -*- encoding: utf-8 -*-
"""
@File    : kafkaCom.py
@Time    : 2020/7/2 09:31
@Author  : zhangsongqing
@annotation： XXX
"""

from kafka import KafkaConsumer

# consumer = KafkaConsumer('test_rhj', bootstrap_servers=['172.10.4.96:9092'])
# for msg in consumer:
#     recv = "%s:%d:%d: key=%s value=%s" %(msg.topic, msg.partition, msg.offset, msg.key, msg.value)
#     print(recv)

consumer = KafkaConsumer('testDemo', bootstrap_servers=['172.10.4.96:9092'], auto_offset_reset='earliest')

for message in consumer:
    print(message)
    print("=======================================================")
    print("topic=%s:partition=%d:offset=%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

