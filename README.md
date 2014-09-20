kafka-insight-tutorial
======================

Follow this tutorial to set up Kafka

Download Kafka from Apache

```shell
wget http://psg.mtu.edu/pub/apache/kafka/0.8.1.1/kafka_2.10-0.8.1.1.tgz
```


Un-targz the archive
```
tar xvzf kafka_2.10-0.8.1.1.tgz
cd kafka_2.10-0.8.1.1
```

Optional: Go to the folder and configure the server properties
```
nano config/server.properties
```
Change broker id if running multiple instances


Optional: launch a local zookeeper (skip if you already have a zookeeper instance)
```
bin/zookeeper-server-start.sh
```

Start Kafka
```
bin/kafka-server-start.sh
```

Set up a new topic
```
bin/kafka-topics.sh --create --topic mytopic --replication-factor 1 --partitions 1 --zookeeper 127.0.0.1:2181
```



Run the python scripts.
```
python producer.py

python consumer.py
```


