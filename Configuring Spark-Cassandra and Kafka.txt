##zookeper çalıştır
sudo service zookeeper status
##kafka çalıştır
./bin/kafka-server-start.sh /home/beyhan/kafka_2.9.2-0.8.2.2/config/server.properties
######TOPIC CREATED
kafka-topics.sh --create --zookeeper 127.0.0.1:2181 --topic topic_cassandraam --partitions 1 --replication-factor 1

##Streaming start

spark-submit --master local[2] --conf "spark.dynamicAllocation.enabled=false" --jars SPARK_HOME/lib/spark-examples.jar /home/beyhan/kafka_wordcount.py 127.0.0.1:2181 wordcounttopic

##Producer start manual
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic_cassandraam

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic_casssandra
write something
####Producer start manual
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic wordcounttopic < /home/beyhan/foo.txt


##Kafka ile alıp streaming ile işleyip cassandra database'e yazıyor.
./spark-submit --master local[2] --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.0,TargetHolding/pyspark-cassandra:0.1.5  /home/beyhan/kafcasstre.py topic_casssandra
##Wordcount
./spark-submit --master local[2] --packages org.apache.spark:spark-streaming-kafka_2.10:1.6.0,TargetHolding/pyspark-cassandra:0.1.5  /home/beyhan/streaming.py topic_casssandraam


