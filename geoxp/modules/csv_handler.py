import sys
import csv


def read_csv(file_name):
    with open(file_name, 'rb'):
        csv_file = csv.reader(file_name)
        csv_data = list(csv_file)
        print csv_data


def main():
    read_csv(sys.argv[1])

if __name__ == '__main__':
    main()
