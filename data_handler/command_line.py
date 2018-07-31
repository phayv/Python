import argparse

from modules.phay_mods import *


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Show the number of violations in a given month')
    parser.add_argument('filename', help='Name of data file')
    parser.add_argument('month', help='Month to filter on')
    parser.add_argument('year', help='Year to filter on')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    result = count_risk_categories_by_month(
        read_file(args.filename), args.month, args.year)
    print(result)


if __name__ == '__main__':
    main()