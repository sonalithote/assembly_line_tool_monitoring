from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sample_data = {
    'tool_id': 1,
    'status': 'active',
    'throughput': 150.0,
    'error_rate': 0.05
}

producer.send('tool_metrics', sample_data)
producer.flush()
