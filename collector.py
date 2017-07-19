# we can also use python-daemon, just to make it simple I have used while loop
#sudo apt-get update
#sudo apt-get install gcc python-dev python-pip
#sudo pip install psutil
#sudo pip install kafka-python
#https://github.com/giampaolo/psutil


#!/usr/bin/env python
import time
import socket
import datetime
import json
import psutil

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
   hostName = socket.gethostname()
   timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
   cpu = psutil.cpu_times().system
   virtualMemory = psutil.virtual_memory().total
   diskUsage = psutil.disk_usage('/').total
   msg1 = {'hostName':hostName,'timestamp':timestamp,'cpu':cpu,'virtualMemory':virtualMemory,'diskUsage':diskUsage}
   msg1 = json.dumps(msg1)
   print msg1
   producer.send('sampletopic',msg1)
   time.sleep(1)
