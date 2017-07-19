from kafka import KafkaConsumer
consumer = KafkaConsumer('testtopic',bootstrap_servers='localhost:9092')
for msg in consumer:
	print (msg)