from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from . import db

class Job(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    url = Column(String(120), unique=True, nullable=False)
    status = Column(Integer, nullable=False, default=1)
    interval = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Job {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'interval': self.interval,
            'created_at': self.created_at
        }