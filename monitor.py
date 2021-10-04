import requests
import RPi.GPIO as GPIO
import time


port = 4
TARGET_URL = 'http://httpbin.org/status/500'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(port, GPIO.OUT)

try:
    while 1:
        r = requests.get(TARGET_URL)

        if r.status_code >= 400:
            GPIO.output(port, GPIO.HIGH)
        else:
            GPIO.output(port, GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()
