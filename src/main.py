# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""

# Make root
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import ext.farmware_tools as ft
import detection

import utils
import handshake

response=handshake.getToken(utils.dataFolder+'credential.json')
token=response['token']['encoded']
mqttHost=response['token']['unencoded']['mqtt']
deviceId=response['user']['device_id']

print(mqttHost)
print(deviceId)
exit(0)
# Inputs:
EMAIL = 'bstanciulescu@gmail.com'
PASSWORD = 'farmbot'

# Get your FarmBot Web App token.
headers = {'content-type': 'application/json'}
user = {'user': {'email': EMAIL, 'password': PASSWORD}}
response = requests.post('https://my.farmbot.io/api/tokens',
                         headers=headers, json=user)
TOKEN = response.json()['token']['encoded']



import json
import paho.mqtt.publish as publish
import paho.mqtt.client as client
# Generate this information by using `token_generation_example.py`.
# Now let's build an RPC command.
celery_script_rpc = {
    "kind": "rpc_request",
    "args": {
        "label": "cb78760b-d2f7-4dd1-b8ad-ce0626b3ba53"
    },
    "body": [{
        "kind": "toggle_pin",
        "args": {
            "pin_number": 13
        }
    }]
}

# Encode it as JSON...
json_payload = json.dumps(celery_script_rpc)

# Connect to the broker...
client = client.Client()
# ...using credentials from `token_generation_example.py`
client.username_pw_set(my_device_id, my_token)


# An event handler for sending off data:
def on_connect(client, userdata, flags, rc):
    print("CONNECTED! Sending data now...")
    # "bot/device_18/from_device" contains all of FarmBot's responses to
    # commands. It's JSON, like everything else. If FarmBot is running, we will
    # see a response from this channel.
    client.subscribe("bot/" + my_device_id + "/from_device")

    # Publish that payload as soon as we connect:
    client.publish("bot/" + my_device_id + "/from_clients", json_payload)


def on_message(client, userdata, msg):
    print("Got a message: ")
    print(msg.topic + " " + str(msg.payload))


# Attach event handler:
client.on_connect = on_connect
client.on_message = on_message

# Finally, connect to the server:
client.connect("brisk-bear.rmq.cloudamqp.com", 1883, 60)
print("Here we go...")

""" Sends a log message"""
#message = {
#    'kind': 'send_message',
#    'args': {
#        'message': 'Hello World!',
#        'message_type': 'success'
#    }
#}
""" Moves the farmbot"""
#message = {
#    'kind': "rpc_request",
#    'args': { 'label': "adslkjhfalskdha" },
#    'body': [
#      { 'kind': "move_relative", 'args': { 'x': 100, 'y': 105, 'z': -100, 'speed': 100 } }
#    ]
#}

""" Takes a picture """

message = {
    'kind': "take_photo",
    'args': {}
}  

# Send the command to the device.
publish.single(
    'bot/{}/from_clients'.format(my_device_id),
    payload=json.dumps(message),
    hostname=my_mqtt_host,
    auth={
        'username': my_device_id,
        'password': my_token
        }
    )

