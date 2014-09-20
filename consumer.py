from kafka import *



mykafka = KafkaClient("localhost:9092")


consumer = SimpleConsumer(mykafka, "mygroup", "mytopic")


try:
	messages = consumer.get_messages(count=5000, block=False)
	for message in messages:
    		print(message)
except KeyboardInterrupt:
	pass


consumer.commit()

mykafka.close()
