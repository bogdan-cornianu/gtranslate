import socket
import sys
import os
import logging

import daemon

from gtranslate import server


logging.basicConfig()
file_logger = logging.FileHandler("./gtd.log", "w")
logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)


def start_server():
    while True:
        connection, _ = server.start_server()
        try:
            server.read_message(connection)
        finally:
            connection.close()


def main():
    with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
        start_server()


if __name__ == '__main__':
    main()
