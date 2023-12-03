#!/usr/bin/python3

"""
A Python script that takes in a letter and sends a POST request to a specified URL
with the letter as a parameter. The script handles JSON responses and displays
appropriate messages based on the content of the response.
"""

import requests
import sys

def send_post_request(url, letter):
    # Send a POST request with the letter as a parameter
    response = requests.post(url, data={'q': letter})

    try:
        # Try to parse the JSON response
        json_response = response.json()
        if json_response:
            # If JSON is not empty, display id and name
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            # If JSON is empty
            print("No result")
    except ValueError:
        # If response is not a valid JSON
        print("Not a valid JSON")

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    send_post_request(url, letter)

