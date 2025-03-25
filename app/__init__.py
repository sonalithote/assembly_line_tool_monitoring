from .config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    with app.app_context():
        from . import routes
        db.create_all()
        
        # Start Kafka consumer
        from .kafka_consumer import start_kafka_consumer
        start_kafka_consumer(app)
        
    return app
