from kafka import KafkaProducer

class KafkaProducerWrapper:
    def __init__(self, bootstrap_servers: str):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def send_message(self, topic: str, message: str):
        self.producer.send(topic, message.encode('utf-8'))

