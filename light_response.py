import subprocess as sp
import time
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12      #GPIO 18

os.system('clear')
print('-------------------------------')
print('Welcome to COAP LIGHT RESPONSE')
print('-------------------------------')

def lighton():
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(2)

def lightoff():
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)

def response():
    cmd = ["python3 2c.py | cut -d ',' -f 3 | tail -2"]
    msg = str(sp.check_output(cmd, shell=True), 'utf-8')[0:-1]
    return msg


def loop():
    while(True):
        x=response()
        time.sleep(1)
        while((response() == '') or (response()==x)):
            time.sleep(1)
            continue
        y = response().strip()
        if y == 'light off':
            lightoff()
        elif y == 'light on':
            lighton()
        print('Client: {}'.format(y))

try:
    loop()
except KeyboardInterrupt:
    print('\nProgramme Terminated')
