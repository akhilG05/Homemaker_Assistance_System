from django.contrib.auth.models import User
from accounts.models import RPiUser
from mobile.models import Message,Contact
import serial
# import RPi.GPIO as GPIO
import os,time
# import Adafruit_DHT

# GPIO.setmode(GPIO.BOARD)

# sensor = Adafruit_DHT.DHT11
# pin = 4

# def temperature():
# 	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
# 	return '{0:0.1f}'.format(temperature)
# 	print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

# def humidity():
# 	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
# 	return '{0:0.1f}'.format(humidity)

# temperature = temperature()
# humidity = humidity()
