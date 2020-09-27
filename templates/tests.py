import json

import requests
from django.test import TestCase

from templates import views


class TemplateTest(TestCase):

    def test_post_templates(self):
        client_10_response = requests.post('http://127.0.0.1:8000/te/customer/10/templates/')
        self.assertEqual(
            views.insert(10), json.loads(client_10_response.text)['result'])

    def test_get_templates(self):
        client_10_response = requests.get('http://127.0.0.1:8000/te/customer/10/templates/')
        self.assertEqual(
            views.display(10), json.loads(client_10_response.text)['result'])
