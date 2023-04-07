from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job as APJob
from ..models import Job

class CronJob:

    def __init__(self, scheduler : BackgroundScheduler):
        self.scheduler = scheduler
        self.scheduler.start()

    def add(self, function, job : Job):
        cron_job = self.scheduler.add_job(name=job.name, func=function, id=str(job.id), 
                                     seconds=job.interval, args=[job], trigger="interval")
        return self.job_dict(cron_job)

    def get(self, id):
        job = self.scheduler.get_job(id)
        return self.job_dict(job)
    
    def delete(self, id):
        self.scheduler.remove_job(id)

    def list(self):
        cron_jobs = self.scheduler.get_jobs()
        cron_jobs = list(map(lambda job : self.job_dict(job), cron_jobs))
        return cron_jobs
    
    def job_dict(self, job: APJob):
        return {
            'name': job.name,
            'id': int(job.id)
        }
