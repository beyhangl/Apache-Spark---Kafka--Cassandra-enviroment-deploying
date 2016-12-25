from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import pyspark_cassandra
from pyspark_cassandra import streaming
from datetime import datetime
from pyspark.sql import SQLContext, Row
from py4j.protocol import Py4JJavaError

###This streaming takes data from Apache Kafka and makes basic analyse. After analyse save it to Cassandra database.

def getSqlContextInstance(sparkContext):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(sparkContext)
    return globals()['sqlContextSingletonInstance']


# Create a StreamingContext with batch interval of 3 second
conf=SparkConf().setAppName("asd").set("spark.cassandra.connection.host", "127.0.0.1")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, 3)

topic = "topic_cassandraam"
kafkaStream = KafkaUtils.createStream(ssc, "localhost:2181", "topic", {topic: 4})

def process(time, rdd):
    
    try:
        
        # Get the singleton instance of SparkSession
        sqlContext = getSqlContextInstance(rdd.context)
        
        # Convert RDD[String] to RDD[Row] to DataFrame
        #d.map(lambda w: Row(word=w))
        
        df = sqlContext.createDataFrame(rdd)
        #df.registerTempTable("words")
        
        #wordCountsDataFrame = sqlContext.sql("select * from words")
        #sqlContext.read.format("org.apache.spark.sql.cassandra").options(table="pushsms", keyspace="test").load().show()
        myrdd = df.rdd.map(tuple)
        #rdd.collect()

        myrdd.saveToCassandra("test", "basicdr")
    except:
        pass

lines = kafkaStream.map(lambda x: x[1])
result =lines.map(lambda line: line.split(",")).filter(lambda line: len(line)>1).map(lambda line: (line[0],line[2],line[21],line[22]))
#resultCDR = result.toDF(['Time','ANumber','ServingCellorSAC','ServingLAC'])

result.foreachRDD(process)
ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
