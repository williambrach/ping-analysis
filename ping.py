import platform    
from subprocess import Popen, PIPE
from datetime import datetime
import sys
import csv
import time
import argparse
import CONSTANTS

def testPing(addr,fileOut):
    """Start monitoring your ping in while cycle. Outputs are written into csv files.
    Keyword arguments:
    addr -- ip or domain of target entity
    fileOut -- fileoutput name (default is same as addr)
    """

    dt_string = datetime.today().strftime('%Y_%m_%d_%H_%M_')
    dt_stringFormated = datetime.today().strftime('%Y:%m:%d %H:%M')
    fileName = fileOut
    cmd = addr
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', cmd]
    pingSum = 0
    tries = 1
    fileOutPath = f'{CONSTANTS.REPORT_FILE_PATH+dt_string+fileName}_ping.csv'

    print(f'SAVING REPORT FROM [{dt_stringFormated}] TO -> {fileOutPath}')
    with open(fileOutPath, mode='w') as ping_file:
        excel_writer = csv.writer(ping_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        excel_writer.writerow(["date", "time", "ms"])
        while 1:
            p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")

            pingString = str(output).split("time")[1].split("ms")[0][1:]
            ping = int(pingString) if len(pingString) < 10 else -1
            x = datetime.now()
            timeX = x.strftime("%H:%M:%S")
            date = x.strftime("%d-%m-%Y")
            excel_writer.writerow([date, timeX, ping])
            pingSum += int(ping)
            avgPing = round(pingSum/tries,2)
            sys.stdout.write('\r')
            sys.stdout.write("Ping - {} (avg {}) ms".format(str(ping),
            str(avgPing)))
            sys.stdout.flush()
            tries += 1	
            time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description='Process arguments for ping analysis.')
    parser.add_argument('--ping', nargs='?',metavar="Target IP addr",required = True, help='Target ip address')
    parser.add_argument('-o', nargs='?',metavar="File destination", help='Output file')
    args = parser.parse_args()

    addr = args.ping
    fileOut = args.ping if args.o == None else args.o

    testPing(addr, fileOut)

if __name__ == "__main__":
    main()

