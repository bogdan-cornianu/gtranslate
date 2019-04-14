import sys
import argparse

from gtranslate import client


def main():
    parser = argparse.ArgumentParser(
        description='CLI for Google Translate'
    )
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        help='Input File')
    parser.add_argument('-l', '--language',
                        help='Language', default='en',
                        choices=('en', 'ro', 'it', 'de'))
    args = parser.parse_args()
    if args.file:
        conn = client.get_connection()
        client.send_message(args.file.readlines(), conn)
        client.read_message(conn)
        client.close_connection(conn)
    else:
        print("Please specify an input file.")
