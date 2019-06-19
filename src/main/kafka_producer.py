import names
import uuid
from kafka import KafkaProducer
from json import dumps
from time import sleep


def create_producer(port):
    producer = KafkaProducer(bootstrap_servers=[port],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    for e in range(1000):
        data = {'name': names.get_full_name(), 'id': str(uuid.uuid4())}
        producer.send('names', value=data)
        sleep(1)


create_producer('localhost:9092')
