#kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testtopic 
#kafka-console-consumer.sh --zookeeper localhost:2181 --bootstrap-server localhost:9092 --topic testtopic --from-beginning
#https://github.com/dpkp/kafka-python

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for index in range(1000):
	msg = "%s: %d" % ('message',index+1)
	producer.send('testtopic', msg)