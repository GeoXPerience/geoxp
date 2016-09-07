'''This module handles CSV files.'''
import csv
import sys
from location import Location


def geocode_uploaded_file(input_file, output_file):
    csv_data = csv.reader(input_file, delimiter=';')
    next(csv_data)
    for address in csv_data:
        loc = Location(address)
        loc.write(output_file)


def main():
    '''This is functions is for testing purposes.'''
    with open('addresses.csv', 'rb') as input_file, open('output.csv', 'a') as output_file:
        geocode_uploaded_file(input_file, output_file)

if __name__ == '__main__':
    main()
