import json
import requests


# Set parameters to search information in a database
name = 'aircraft'
addresszip = 60046

# Building request
api_url = 'http://127.0.0.1:5000/'
data = {'name':name,'addresszip':addresszip}
r = requests.post(url=api_url, data=data)
print(r.text)