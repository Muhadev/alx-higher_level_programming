#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id
in the response header.Uses the packages requests and sys.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")
