import RPi.GPIO as gpio
from time import sleep
import datetime
import pyrebase
import json

CHANNEL = 6
SECONDS_TO_WATER = 10

with open('/home/pi/garduino/database_config.json', 'r') as config:
  database_config = json.load(config)

gpio.setmode(gpio.BCM)
gpio.setup(CHANNEL, gpio.OUT)

firebase = pyrebase.initialize_app(database_config)

database = firebase.database()

def waterPlant():
    gpio.output(CHANNEL, 0)
    sleep(SECONDS_TO_WATER)
    gpio.output(CHANNEL, 1)

now = datetime.datetime.now()
toWater = database.child("toWater").get().val()
if(toWater == True):
    waterPlant()
    print("Watered plant at: " + str(now)[:19])
    database.update({"toWater": False})