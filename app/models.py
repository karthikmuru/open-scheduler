from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from . import db

class Job(db.Model):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)
    url = Column(String(120), unique=True, nullable=False)
    status = Column(Integer, nullable=False, default=1)
    interval = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Job {self.id}, {self.name}, {self.url}, {self.status}, {self.interval}, {self.created_at}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'interval': self.interval,
            'created_at': self.created_at
        }

class Log(db.Model):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    status = Column(Integer, nullable=False, default=503)
    time = Column(DateTime, default=datetime.utcnow)