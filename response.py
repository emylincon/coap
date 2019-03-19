import subprocess as sp
import time

def response():
    cmd = ["python3 2c.py | cut -d ',' -f 3 | tail -2"]
    msg = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return msg


def loop():
    while(True):
        x=response()
        while(response() == '' or response()==x):
            time.sleep(2)
            continue
        print('Client: {}'.format(response()))

try:
    loop()
except KeyboardInterrupt:
    print('\nProgramme Terminated')
