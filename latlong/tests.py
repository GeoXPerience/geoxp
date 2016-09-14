from django.test import TestCase
from csv_handler import *
# Create your tests here.

class TestCalls(TestCase):

    def test_should_return_status_200(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(200, response.status_code)

    def test_should_return_csv_with_lat_lon(self):
        #with open('addresses.csv', 'rb') as input_file, open('output.csv', 'a') as output_file:
        #geocode_uploaded_file(input_file, output_file)
        response = self.client.get('/', follow=True)
        self.assertEqual(False, True)
