#!/usr/bin/python3
"""Script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_data = response.json()

        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except ValueError:
        print("Not a valid JSON")
