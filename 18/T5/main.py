import re

import requests

def get_request(path):
    return requests.get(path)


my_req = get_request('http://www.columbia.edu/~fdc/sample.html')

subheadings = re.findall(r'<h3.*>(?P<name>.*)</h3>', my_req.text)
print(subheadings)