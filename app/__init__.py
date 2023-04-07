from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()

from .libs.cron_job import CronJob
cron_job = CronJob(BackgroundScheduler({}))

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)

    migrate = Migrate(app, db)

    from .controllers import job
    app.register_blueprint(job.jobs)

    with app.app_context():
        enqueue_all_jobs()

    return app

def enqueue_all_jobs():

    from .models import Job
    from .libs.worker import job_function

    jobs = db.session.query(Job).all()
    print("Jobs enqueued :", len(jobs))
    
    for job in jobs:
        cron_job.add(job_function, job)