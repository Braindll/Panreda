import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from os import system
system("clear")

mqttbroker='mqtt.eclipseprojects.io'
client=mqtt.Client("Guldan")
client.connect(mqttbroker,port=1883)

def goster(client,userdata,message):
    print("mesaj",str(message.payload.decode("utf-8")))

client.loop_start()
client.subscribe("Temperlicam")
client.on_message=goster
time.sleep(30)
client.loop_stop()