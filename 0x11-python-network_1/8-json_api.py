#!/usr/bin/python3
"""Script that takes in a letter, sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    payload = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_data = response.json()

        if isinstance(json_data, list) and len(json_data) > 0:
            user = json_data[0]
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
