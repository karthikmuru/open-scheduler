# Open Scheduler

This is a Flask project that allows users to schedule jobs that will continuously check the status of a URL. This application is useful for anyone who wants to monitor the availability and response time of a website.

### Getting started

#### Requirements
- Python >= 3.10

#### Installation
```
pip install -r requirements.txt
python3 app.py
```

### API
- GET /jobs : List all the current jobs
- DELETE /jobs/<id> : Delete job by ID.
- POST /jobs : Create a new job.
  - Parameters
  ```
  {
    "url" : "URL to check the status of",
    "name" : "Name of the Job",
    "interval" : "No. of seconds between each status check request",
    "file_name" : "Name of the CSV file to store the logs."
  }
  ```
### TODO
  
- [x] Create a worker to check the status of given URL and log the time and status to the given log file. 
- [ ] Trigger a mail when the page status changes.
- [ ] Persist all job details in the database.
- [ ] Add support for accounts and users.
- [ ] Restart all running jobs when server is restarted.
- [ ] Dashboard to create and view the jobs and the logs.
- [ ] Execute a user defined task on the URL and create triggers for specific when certain events are observed.
