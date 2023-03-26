from flask import Blueprint, jsonify, request, make_response
from apscheduler.schedulers.background import BackgroundScheduler

from .models import db
from .libs import worker
from .views import jobs_view

scheduler = BackgroundScheduler({})
scheduler.start()

jobs = Blueprint('jobs', __name__)

@jobs.route('/jobs/<id>', methods=['DELETE'])
def delete(id):
    scheduler.remove_job(id)
    return make_response('', 204)

@jobs.route('/jobs', methods=['POST'])
def create():

    url = request.get_json().get('url')
    name = request.get_json().get('name')
    interval = int(request.get_json().get('interval'))
    file_name = request.get_json().get('file_name')
    id = f"{name}-{interval}-seconds"

    scheduler.add_job(name=name, func=worker.job_function, args=[url, file_name], trigger='interval', seconds=interval, id=id)

    jobs = scheduler.get_jobs()
    return jobs_view.list_jobs(jobs)

@jobs.route('/jobs', methods=['GET'])
def list():
    jobs = scheduler.get_jobs()
    return jobs_view.list_jobs(jobs)