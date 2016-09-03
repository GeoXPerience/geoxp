#!/usr/bin/env python
import sys
import csv


def read_csv(file_name):
    with open(file_name, 'rb') as csv_file:
        csv_data = csv.reader(csv_file)
        csv_list = list(csv_data)


def main():
    read_csv(sys.argv[1])


if __name__ == '__main__':
    main()
