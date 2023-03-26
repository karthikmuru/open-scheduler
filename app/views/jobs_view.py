from apscheduler.job import Job

JOBS_ATTRIBUTES = ['id', 'name']

def list_jobs(jobs):
    data = list(map(_get_fields, jobs))
    return data

def get_job(job):
    return _get_fields(job)

def _get_fields(job):
    job_json = {}
    for job_attr in JOBS_ATTRIBUTES:
        job_json[job_attr] = getattr(job, job_attr)
    
    return job_json
