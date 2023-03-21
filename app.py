from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import utc
from datetime import datetime
import json
import time
from libs import worker
from views import jobs_view

app = Flask(__name__)
scheduler = BackgroundScheduler({})
scheduler.start()

@app.route('/jobs/<id>', methods=['DELETE'])
def delete(id):
    scheduler.remove_job(id)
    return

@app.route('/jobs', methods=['POST'])
def create():

    url = request.get_json().get('url')
    name = request.get_json().get('name')
    interval = int(request.get_json().get('interval'))
    file_name = request.get_json().get('file_name')
    id = f"{name}-{interval}-seconds"

    scheduler.add_job(name=name, func=worker.job_function, args=[url, file_name], trigger='interval', seconds=interval, id=id)

    jobs = scheduler.get_jobs()
    return jobs_view.list_jobs(jobs)

@app.route('/jobs', methods=['GET'])
def list():
    jobs = scheduler.get_jobs()
    return jobs_view.list_jobs(jobs)

## Remove job
# - ID

## Add job
# - ID
# - interval
# - URL
# - File Name

# scheduler.add_job(func=worker.job_function, args=["\n1 seconds", "https://www.qwewqr.org/"], trigger='interval', seconds=10)
# scheduler.add_job(func=worker.job_function, args=["\n1 seconds", "https://www.google.com/"], trigger='interval', seconds=7)
# scheduler.add_job(func=worker.job_function, args=["\n1 seconds", "https://www.wikipedia.org/"], trigger='interval', seconds=1)
