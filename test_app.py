#!/usr/bin/env python
import unittest

from app import app


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_request_response(self):
        response = self.app.get('/')
        self.assertEqual(response.data, '<p>Hello, World</p>')

    def test_json_request_response(self):
        response = self.app.get('/', headers={'Accept': 'application/json'})
        self.assertEqual(response.data, '{"message": "Good morning"}')


if __name__ == "__main__":
    unittest.main()
