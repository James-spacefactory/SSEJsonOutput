# imports
import sys
import json
import time
import requests
import sseclient
from termcolor import colored

# All credentials are stored in a GIT IGNORED file
import credentials as cd
access_token = cd.access_token

class SSEClient:
    def __init__(self, _access_token):
        self.url = 'https://api.particle.io/v1/devices/events?access_token=' + _access_token
        self.client = None
        self.event = None
        self.data = None

    def start_sse(self):
        self.client = sseclient.SSEClient(self.url)
        for event in self.client:
            if event.data != "" and event.data != " ":
                self.event = event.event
                self.data = event.data
                self.data = json.loads(self.data)
                j = json.loads(self.data["data"])
                print()
                print(colored(self.event, 'green'))
                print(colored(self.data["coreid"], 'blue'))
                print(json.dumps(j, sort_keys=True, indent=4))

while True:
    try:
        s = SSEClient(access_token)
        s.start_sse()
    except:
        pass
