# Kafka-Spark Workshop

The following instructions are to setup a simple Kafka-Spark connection to further your understanding of Kafka and Spark. Currently, only the Kafka Docker container is setup. THe next step would be to link a Spark container to the Kafka container so they can talk to each other.

**Download Docker:**

Download Docker if you have not done so already.

https://docs.docker.com/docker-for-mac/install/

**Clone this repo:**
```
git clone https://github.com/garyjfong/Kafka-Spark-Workshop.git
```
**Open a terminal window and pull and run the image, spotify/kafka:**
```
docker run -d -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST="localhost" --env ADVERTISED_PORT=9092 --name kafka -h kafka spotify/kafka
```
**Verify the container is running:**
```
docker ps
```
**SSH into the docker container:**
```
docker exec -it kafka /bin/bash
```
An instance of Kafka and zookeeper is now running. You can create topics, create a producer, consume messages, etc. from the terminal. Often times, you would not do it straight from the terminal, a script would be much better, but this is an easy way to see how Kafka operates.

**Go into the Kafka folder:**
```
cd opt/kafka_2.11-0.10.1.0
```
**Create a topic:**
```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic names
```
You can specify the replication factor and number of partitions for each topic.

**Make sure the topic appears on the list of topics:**
```
bin/kafka-topics.sh --list --zookeeper localhost:2181
```
**Open a new terminal window/tab and go into the container again, cd into the kafka folder:**

Create a producer:
```
bin/kafka-console-producer.sh --broker-list kafka:9092 --topic names
```
**Open a new terminal window/tab and go into the container again, cd into the kafka folder:**

Create a consumer:
```
bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic names --from-beginning
```

If you type something and press return in the producer window, you should see the message being retrieved and shown in the consumer window. The Producer is sending messages to Kafka, which stores it in topics, then the messages can be consumed from those topics.

**With the terminal window still open and Kafka still running, open the project repo in Pycharm:**

Open the kafka_producer.py

Go to Run -> Run... -> kafka_producer

View the Kafka consumer window. You should see a list of names being listed with ids. 

To exit any of the terminal operations, use ctrl+D or ctrl+C.

Run structured_streaming_spark.py to view Spark Streaming print out messages to the console. This is basically running a Spark Job on streaming data.

Run twitter_stream_producer.py to read streams from the Twitter API. 

