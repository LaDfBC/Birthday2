__author__ = 'George'

def makeFile():
    months_names = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    file = open("C:\\Users\\George\\PycharmProjects\\months.txt", 'w+')
    for month_number in range (0, 12):
        month_name = months_names[month_number]
        for day in range(1, months[month_number] + 1):
            file.write(str(month_name) + "_" + str(day) + " = " + str(month_number + 1) + ", " + str(day) + "," + '"",' + "\n")

    file.close()

makeFile()