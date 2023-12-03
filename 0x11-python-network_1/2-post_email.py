#!/usr/bin/python3

"""
This Python script accepts a URL and an email address as inputs, then proceeds to send a POST request to the provided URL, including the email address as a parameter. Afterward, it retrieves and displays the response body, decoded in utf-8 encoding
Args:
        email: Holds the email address
"""

import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        re = r.read().decode("utf-8")
        print(re)
