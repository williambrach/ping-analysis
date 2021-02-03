import platform    
import subprocess  
from subprocess import Popen, PIPE
import datetime
import sys
import csv
import time


addr = sys.argv[1]
param = '-n' if platform.system().lower()=='windows' else '-c'
command = ['ping', param, '1', "google.sk"]
with open(f'{addr}_ping.csv', mode='w') as ping_file:
    excel_writer = csv.writer(ping_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    excel_writer.writerow(["date", "time", "ms"])
    while 1:
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        ping = str(output).split("time")[1].split("ms")[0][1:]
        x = datetime.datetime.now()
        time = x.strftime("%H:%M:%S")
        date = x.strftime("%d-%m-%Y")
        excel_writer.writerow([date, time, ping])
        time.sleep(1)


