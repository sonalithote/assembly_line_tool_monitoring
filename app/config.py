import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or 'postgresql://postgres:mypassword@localhost:5432/assembly_line_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KAFKA_BROKERS = os.environ.get('KAFKA_BROKERS') or 'localhost:9092'
    KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC') or 'tool_metrics'