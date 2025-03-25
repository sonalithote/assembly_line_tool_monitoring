from datetime import datetime
from . import db

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)
    throughput = db.Column(db.Float)
    error_rate = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'last_update': self.last_update.isoformat(),
            'throughput': self.throughput,
            'error_rate': self.error_rate
        }
