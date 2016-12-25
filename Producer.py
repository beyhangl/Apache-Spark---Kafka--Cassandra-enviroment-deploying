from kafka import KafkaProducer
from kafka.errors import KafkaError
import os
import timeit
####This producer function takes data from a folder and push it to producer of Apache Kafka. After that Spark Streaming takes this data(consumer) analyse it and save it to cassandra database.



start = timeit.default_timer()

producer = KafkaProducer(bootstrap_servers='localhost:9092')

data='2016-11-16 15:24:44,905388828700,,,905428695600,1,1422,1,6039,0:00:00:000,31092,2,1,1,0,7516,1400,54054,9590554,0,3181,13402,286034005047317,2AC29D6A,3578050287321657,0,,0,16,,9,,3,0,0,,,,,,,,,0,'
count=0
producer.send('topic_cassandraam',data)

os.chdir("/home/beyhan/cdr")
for file in os.listdir("/home/beyhan/cdr"):
   if file.endswith(".txt"):
        f = open(file, "r")
        lines = f.readlines()
        #print(lines)
        for line in lines:
                count=count+1
                producer.send('topic_cassandraam',line)
#       print file
#       print "\n".join(lines)
        f.close()
        os.remove(file)

print count
stop = timeit.default_timer()
print stop - start