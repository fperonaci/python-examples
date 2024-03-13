from kafka import KafkaConsumer

consumer = KafkaConsumer(
  "test_topic",
  bootstrap_servers=["localhost:9094"],
  group_id="test_groud")

for msg in consumer:
  print(msg)
