# coding:utf-8
"""Tests for latlong package."""
from django.test import TestCase
import csv
from location import Location
from csv_handler import geocode_uploaded_file
from collections import namedtuple
# Create your tests here.


class TestCalls(TestCase):
    """Test cases for page."""

    def test_should_return_status_200(self):
        """Test for status 200 when loading page."""
        response = self.client.get('/', follow=True)
        self.assertEqual(200, response.status_code)

    def test_should_return_csv_with_lat_lon(self):
        """Test if loaded page returns csv."""
        with open('test_files/addresses.csv', 'rb') as input_file, \
                open('test_files/output.csv', 'w+') as output_file:
            geocode_uploaded_file(input_file, output_file)

            # Rewind files
            input_file.seek(0)
            output_file.seek(0)

            in_data = csv.reader(input_file, delimiter=';')
            out_data = csv.reader(output_file, delimiter=';')

            next(in_data)

            for in_address in in_data:
                out_address = next(out_data)
                loc_in = Location(in_address)
                Geocode = namedtuple('Geocode', 'lat, long')
                g = Geocode(lat=float(out_address[3]),
                            long=float(out_address[4]))
                print loc_in
                loc_out = Location(out_address, geoloc=g)
                self.assertEqual(loc_in, loc_out)

    def test_zip_formatting(self):
        """Test the output for different zip formating."""
        a1 = ["Rua camburiu", 508, "05058-020"]
        a2 = ["Rua camburiu", 508, "05058020"]

        l1 = Location(a1)
        l2 = Location(a2)

        self.assertIsNotNone(l1.geoloc)
        self.assertIsNotNone(l2.geoloc)

        self.assertEqual(l1, l2)
