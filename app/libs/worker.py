import os
import requests
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..models import Job, Log

engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
session = (sessionmaker(bind=engine))()

def job_function(job : Job):

    try:
        response = requests.get(job.url)
        status_code = response.status_code
    except:
        status_code = 503
    finally:
        # status_string = "%s,%s,%s\n" % (str(current_time), job.url, status_code)
        log = Log(job_id=job.id, status=int(status_code))
        session.add(log)
        session.commit()

    return