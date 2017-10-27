import json

__author__ = 'George'

def makeFile():
    months_names = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    dict = {}

    file = open("/home/squeaky/months.txt", 'w+')
    for month_number in range (0, 12):
        month_name = months_names[month_number]

        dict[month_number + 1] = {}
        for day in range(1, months[month_number] + 1):
            dict[month_number + 1][day] = ""

    file.write(json.dumps(dict))

    file.close()

makeFile()