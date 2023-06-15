#!/usr/bin/env python3

import requests
import pprint

url = "https://cat-fact.herokuapp.com/facts"

resp = requests.get(url).json()

for x in resp:
    pprint.pprint(x["text"])
