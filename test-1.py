import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from os import system
system("clear")

mqttbroker='broker.hivemq.com'
client=mqtt.Client("Temperature_Inside")
client.connect(mqttbroker,port=1883)

while True:
    RandNum=uniform(12.0, 21.9)
    RandNum=round(RandNum,2)
    client.publish("Temperlicam",RandNum)
    print(".",RandNum)
    time.sleep(2)
