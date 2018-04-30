import unittest
import api
import requests
import json
import sys

class TestFlaskApi(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.json(), {'OK': 'yawoen.db is Updated!'})

if __name__ == "__main__":
    unittest.main()