from kafka import *


mykafka = KafkaClient("localhost:9092")


producer = SimpleProducer(mykafka)


producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")
producer.send_messages("mytopic", "mymessage")

