#Kafka Installation-One node

#zookeeper part
sudo apt-get update
sudo apt-get install default-jre
sudo apt-get install default-jre


sudo adduser kafka sudo
sudo apt-get install default-jre
sudo useradd -m kafka


sudo adduser kafka sudo
sudo apt-get install zookeeperd


telnet localhost 2181
write ruok
show imok

#kafka part

wget http://www.us.apache.org/dist/kafka/0.8.2.2/kafka_2.9.2-0.8.2.2.tgz

tar xvzf kafka_2.9.2-0.8.2.2.tgz
cd kafka_2.9.2-0.8.2.2/
./bin/kafka-server-start.sh /home/beyhan/kafka_2.9.2-0.8.2.2/config/server.properties

#opened,open a another ssh

#Topic Part

cd kafka_2.9.2-0.8.2.2/

#create a topic

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

#write something
asd
asd


#open another ssh
cd kafka_2.9.2-0.8.2.2/
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic test	

##install

pip install kafka-python

##################################

#Just Open
./bin/kafka-server-start.sh /home/beyhan/kafka_2.9.2-0.8.2.2/config/server.properties

#producer part
--manual
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test 
--read from file
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test  --new-producer < /home/beyhan/test
###bunu dene
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test < /home/beyhan/foo.txt



#consumer part
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --from-beginning --topic test	

##################

kafka-topics --create --zookeeper zookeeper_server:2181 --topic wordcounttopic --partitions 1 --replication-factor 1











