import RPi.GPIO as gpio
from time import sleep

channel = 6

gpio.setmode(gpio.BCM)
gpio.setup(channel, gpio.OUT)

gpio.output(channel, 0)
sleep(10)
gpio.output(channel, 1)
gpio.cleanup