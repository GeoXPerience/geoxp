#!/usr/bin/env python
import csv
import geocoder
import sys

def read_csv(file_name):
    # Tratar primeira linha
    csv_data = None

    with open(file_name, 'rb') as csv_file:
        csv_data = csv.reader(csv_file)

def main():
    csv_data = read_csv(sys.argv[1])

if __name__ == '__main__':
    main()
