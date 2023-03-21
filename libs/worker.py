import requests
import time

def job_function(url, file_name):

    current_time = time.ctime()

    try:
        response = requests.get(url)
        status_code = response.status_code
    except:
        status_code = -1
    finally:
        status_string = "%s,%s,%s\n" % (str(current_time), url, status_code)

    write_to_file(f'{file_name}.csv', status_string)

    return

def write_to_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)