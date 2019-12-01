# import RPi.GPIO as GPIO
import socket
import time
import paho.mqtt.client as mqtt

def irSend(decimalCode):
	# HOST='192.168.43.164'
	# PORT=4210
	# data=decimalCode+"\r"
	# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	# read=s.connect((HOST,PORT))
	# time.sleep(1)
	# read=s.sendto(bytes(data,'ascii'),(HOST,PORT))
	# time.sleep(2)
	# print("sent")
	# s.close()

	Broker = "test.mosquitto.org"
	Port = 1883
	data = decimalCode+"\r"

	def on_publish(client,userdata,result):
	    print("data published \n")
	    pass
	
	client = mqtt.Client()        
	client.on_publish = on_publish
	client.connect(Broker,Port)   
	time.sleep(1)
	client.publish("/remote/IRsignal",data)