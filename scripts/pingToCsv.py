import csv


def getTime(x):
    return x[11:19].strip()


def getPing(x):
    if "Request timeout" in x:
        return 0
    timeOffset = x.find("time") + 5
    time = x[timeOffset:].find(" ")
    return float(x[timeOffset:timeOffset + time].strip())


filepath = '../data/google_ping.txt'
line_num = 0
with open('../data/google_ping.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["date", "time", "ms"])
    with open(filepath) as fp:
        line = fp.readline()
        if line_num == 0:
            line = fp.readline()
        line_num = 1
        while line:
            employee_writer.writerow(["15-6-2020", getTime(line), getPing(line)])
            line = fp.readline()
            line_num += 1



