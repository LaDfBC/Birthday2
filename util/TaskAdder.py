__author__ = 'George'
import requests

url = 'https://api.rememberthemilk.com/services/rest/'
def add_task(task_name, task_notes):
    response = requests.get(url, auth)