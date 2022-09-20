import RPi.GPIO as gpio
from time import sleep
import datetime

CHANNEL = 6
WATERING_TIME = "11:59:50 AM"
SECONDS_TO_WATER = 10

gpio.setmode(gpio.BCM)
gpio.setup(CHANNEL, gpio.OUT)

def waterPlant():
    gpio.output(CHANNEL, 0)
    sleep(SECONDS_TO_WATER)
    gpio.output(CHANNEL, 1)

while(true):
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    if(current_time == WATERING_TIME):
        waterPlant()
        print("Watered plant at: " + now)