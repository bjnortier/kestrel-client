#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import picamera
import time
import os

while True:
    camera = picamera.PiCamera()
    camera.capture('img720x480.jpg')
    camera.close()
    requests.post(
        os.environ['KESTREL_API_URL'] + '/photos',
        files={'photo': open('img720x480.jpg', 'rb')},
        data={
            'camera_id': 'm200',
            'timestamp': time.time()*1000,
            'extension': 'jpg'
        })
    time.sleep(60)
