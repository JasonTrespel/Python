#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import pprint

URL= "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=boolean"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for q in data:
        print(data["results"]["question"])



if __name__ == "__main__":
    main()
