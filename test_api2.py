import unittest
import api2
import requests
import json
import sys

class TestFlaskApi(unittest.TestCase):
    def test_hello(self):
    	name = 'aircraft'
    	addresszip = 60046
    	api_url = 'http://127.0.0.1:5000/'
    	data = {'name':name,'addresszip':addresszip}
    	r = requests.post(url=api_url, data=data)
    	self.assertEqual(r.json(), {"id": "30","name": "jcf international aircraft","website": "http://jcfinternational.com","zip": "60046"})

if __name__ == "__main__":
    unittest.main()