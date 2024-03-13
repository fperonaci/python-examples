from kafka import KafkaProducer

producer = KafkaProducer(
  bootstrap_servers=["localhost:9094"])

producer.send("test_topic", key=b'10', value=b'13')

producer.flush()
