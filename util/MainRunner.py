__author__ = 'George'

import datetime
from util import SendEmail, TaskAdder
from data import Dailies

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']


def get_current_message():
    now = datetime.datetime.now()

    month = str(now.month)
    day = str(now.day)

    return Dailies.Message.year_dict.get(month).get(day)[0]

def get_next_message():
    now = datetime.datetime.now() - datetime.timedelta(days=1)

    month = str(now.month)
    day = str(now.day)

    return Dailies.Message.year_dict.get(month).get(day)

def run():
    message = get_current_message()
    SendEmail.send_message(message[0], "george.mausshardt@gmail.com", "Daily Love From Puddin'")

    if(message[1] is not None):
        TaskAdder.add_item(message[1])

    SendEmail.send_message(get_next_message()[0], "george.mausshardt@gmail.com", 'Check tomorrow\'s message')


