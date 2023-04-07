from flask import render_template, make_response, request
from sqlalchemy import exc
from apscheduler.job import Job
from apscheduler.jobstores.base import JobLookupError

from . import jobs
from ... import db, cron_job
from ...models import Job
from ...libs.worker import job_function

@jobs.route('/jobs/<id>', methods=['DELETE'])
def delete(id : int):
    job = db.session.query(Job).filter_by(id=id).first()
    db.session.delete(job)
    db.session.commit()

    cron_job.delete(id)
    return make_response('', 204)

@jobs.route('/jobs', methods=['POST'])
def create():
    url = request.get_json().get('url')
    name = request.get_json().get('name')
    interval = int(request.get_json().get('interval'))

    job = Job(name=name, url=url, interval=interval)
    db.session.add(job)
    db.session.commit()

    print(job)
    return cron_job.add(job_function, job)

@jobs.route('/jobs', methods=['GET'])
def index():
    return cron_job.list()


@jobs.errorhandler(exc.IntegrityError)
def handle_duplicates(error):
    return make_response('Dupl', 400)

@jobs.errorhandler(JobLookupError)
def handle_job_lookup_error(error):
    return make_response({"message": "Job not found",
                          "error": str(error)}, 404)