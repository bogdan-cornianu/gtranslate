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
        connection, client_address = server.start_server()
        try:
            logger.info('connection from {}'.format(client_address))
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                logger.info('received {!r}'.format(data))
                if data:
                    logger.info('sending data back to the client')
                    server.send_message(connection, data)
                else:
                    logger.info('no data from {}'.format(client_address))
                    break
        finally:
            connection.close()


def main():
    with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
        start_server()
