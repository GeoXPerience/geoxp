'''This module handles CSV files.'''
import csv
import sys


def build_locations(csv_data):
    '''This function builds a lists of location objects.'''
    pass


def read_csv(file_name):
    '''This function reads a CSV file.'''
    with open(file_name, 'rb') as csv_file:
        header = csv.Sniffer().has_header(csv_file.read(4096))
        csv_file.seek(0)
        csv_data = csv.reader(csv_file)
        if header:
            next(csv_data)
        csv_as_list = [row for row in csv_data]

    return csv_as_list


def main():
    '''This is functions is for testing purposes.'''
    csv_data = read_csv(sys.argv[1])
    build_locations(csv_data)

if __name__ == '__main__':
    main()
