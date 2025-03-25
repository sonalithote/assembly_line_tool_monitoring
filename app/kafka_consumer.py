from kafka import KafkaConsumer
import json
import threading
from .models import Tool, db

def start_kafka_consumer(app):
    def consume_messages():
        consumer = KafkaConsumer(
            'tool_metrics',
            bootstrap_servers=app.config['KAFKA_BROKERS'],
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        
        with app.app_context():
            for message in consumer:
                data = message.value
                tool = Tool.query.get(data['tool_id'])
                if tool:
                    tool.status = data['status']
                    tool.throughput = data.get('throughput')
                    tool.error_rate = data.get('error_rate')
                    db.session.commit()

    thread = threading.Thread(target=consume_messages)
    thread.daemon = True
    thread.start()
