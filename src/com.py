# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""
import time
import requests
import json
import src.detection.utils
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt_client
import ext.farmware_tools.device as device
import requests


def getToken(credentialFile):
    with open(credentialFile) as file:
        credential=json.loads(file.read())

    # Get your FarmBot Web App token.
    headers = {'content-type': 'application/json'}
    user = {'user': {'email': credential['email'], 'password': credential['password']}}
    response = requests.post('https://my.farmbot.io/api/tokens',
                            headers=headers, json=user)
    return response.json()


def send_mqtt_request(my_mqtt_host, my_device_id, my_token, message):
    client = mqtt_client.Client()
    client.username_pw_set(my_device_id, my_token)
    client.connect("brisk-bear.rmq.cloudamqp.com", 1883, 60)
    publish.single(
    'bot/{}/from_clients'.format(my_device_id),
    payload=json.dumps(message),
    hostname=my_mqtt_host,
    auth={
        'username': my_device_id,
        'password': my_token
        }
    )

# Simple version for the moment    
def get_last_pic_url(my_token, last_url=None):
    headers = {'Authorization': 'Bearer ' + my_token,
           'content-type': "application/json"}
    if last_url is not None:
        response = requests.get('https://my.farmbot.io/api/images', headers=headers)
        images = response.json()
        most_recent_image_url = images[0]['attachment_url']
        start = time.time()
        while most_recent_image_url == last_url:
            # PAUSE: waits for one second before trying again
            time.sleep(1)
            response = requests.get('https://my.farmbot.io/api/images', headers=headers)
            images = response.json()
            most_recent_image_url = images[0]['attachment_url']
            done = time.time()
            elapsed = done - start
            # If more than two minutes of waiting, there's probably an issue
            if elapsed >= 120:
                print("Couldn't get new url")
                return last_url
        return most_recent_image_url
    else:
        response = requests.get('https://my.farmbot.io/api/images', headers=headers)
        images = response.json()
        most_recent_image_url = images[0]['attachment_url']
        return most_recent_image_url


def move_relative(my_mqtt_server, my_device, my_token, x=0, y=0, z=0, speed=100):
    send_mqtt_request(my_mqtt_server, my_device, my_token, device.move_relative(x, y, z, speed))


def move_along_trajectory(my_mqtt_server, my_device, my_token, positions):
    # positions should be a list of 3 dimensionnals positions
    # TODO: Check whether home coressponds to [0, 0, 0]
    send_mqtt_request(my_mqtt_server, my_device, my_token, device.home('all'))
    positions.insert(0, [0, 0, 0])
    move_to_execute = positions[1:] - positions[:-1]
    for move in move_to_execute:
        send_mqtt_request(my_mqtt_server, my_device, my_token, device.move_relative(x=move[0], y=move[1], z=move[2]))
        send_mqtt_request(my_mqtt_server, my_device, my_token, device.take_photo())
    send_mqtt_request(my_mqtt_server, my_device, my_token, device.home('all'))


def balayage(my_mqtt_server, my_device, my_token):
    send_mqtt_request(my_mqtt_server, my_device, my_token, device.home('all'))
    for i in range(5):
            send_mqtt_request(my_mqtt_server, my_device, my_token, device.move_relative(50))
            send_mqtt_request(my_mqtt_server, my_device, my_token, device.take_photo())
    send_mqtt_request(my_mqtt_server, my_device, my_token, device.home('all'))

