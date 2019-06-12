# Kafka-Spark Workshop

The following instructions are to setup a simple Kafka-Spark connection to further your understanding of Kafka and Spark. Currently, only the Kafka Docker container is set up. The next step would be to link a Spark container to the Kafka container so they can talk to each other.

**Download Docker:**

Download Docker if you have not done so already.

https://docs.docker.com/docker-for-mac/install/

**Download Pycharm:**

https://www.jetbrains.com/pycharm/

**Clone this repo:**
```
git clone https://github.com/garyjfong/Kafka-Spark-Workshop.git
```
**Create a Twitter Dev account:**

If you want to have your own access keys, sign up for a developer account. Otherwise, I will provide you with my access keys for the demonstration.

https://developer.twitter.com/en/apply-for-access


**Open a terminal window and pull and run the image, spotify/kafka:**
```
docker run -d -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST="localhost" --env ADVERTISED_PORT=9092 --name kafka -h kafka spotify/kafka
```
**Verify the container is running:**
```
docker ps
```
The terminal should print something like this:

![alt text][docker ps]

[docker ps]: https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/docker_ps.png


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
Replication factor is the number of replicas or copies of that topic within a cluster of Kafka brokers. 
Partitions specifies how many partitions the topic should be split up into. Partitioning a topic allows multiple consumers to read from the topic in parallel.

**Make sure the topic appears on the list of topics:**
```
bin/kafka-topics.sh --list --zookeeper localhost:2181
```
![alt text][topic list]

[topic list]:https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/list_topics.png

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

**With the Consumer terminal window still open, open the project repo as a project in Pycharm:**

Set the local interpreter to Python3.7

![alt text][set_local_interpreter_1]

[set_local_interpreter_1]:https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/set_local_interpreter_1.png

![alt text][set_local_interpreter_2]

[set_local_interpreter_2]:https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/set_local_interpreter_2.png

![alt text][set_local_interpreter_3]

[set_local_interpreter_3]:https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/set_local_interpreter_3.png

![alt text][set_local_interpreter_4]

[set_local_interpreter_4]:https://github.com/garyjfong/Kafka-Spark-Workshop/blob/master/main/resources/set_local_interpreter_4.png

Run the following command to properly install everything or click the 'install requirements' hint:
```
pip3 install -r requirements.txt
```

Open the kafka_producer.py

Go to Run -> Run... -> kafka_producer

View the Kafka consumer window. You should see a list of names being listed with ids. 

To exit any of the terminal operations, use ctrl+D or ctrl+C.

Run structured_streaming_spark.py to view Spark Streaming print out messages to the console. This is basically running a Spark Job on streaming data.

Create a new topic named twitter_topic.
Run twitter_stream_producer.py to read streams from the Twitter API. 

