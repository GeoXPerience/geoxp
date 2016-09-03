"""
CSV Handler.
"""
import csv
import sys


def read_csv(file_name):
    """Open CSV file."""
    with open(file_name, 'rb') as csv_file:
        header = csv.Sniffer().has_header(csv_file.read(1024))
        csv_file.seek(0)
        csv_data = csv.reader(csv_file)

        if header:
            next(csv_data)

        csv_dict = [row for row in csv_data]

    return csv_dict


def build_locations(csv_data):
    print(csv_data)


def main():
    """Main."""
    csv_data = read_csv(sys.argv[1])
    build_locations(csv_data)

if __name__ == '__main__':
    main()
