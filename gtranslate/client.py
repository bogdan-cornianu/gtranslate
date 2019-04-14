import os
import sys
import socket
import logging
import time

from gtranslate import utils

logging.basicConfig(filename='gtranslate_client.log', level=logging.DEBUG)


def get_connection():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect to the unix socket where the server is listening
    server_address = '/tmp/gtranslate_uds_socket'
    logging.info('connecting to {}'.format(server_address))
    try:
        sock.connect(server_address)
    except socket.error as msg:
        logging.exception(msg)
        sys.exit(1)

    return sock


def send_message(message, language, unix_socket):
    if not message or not unix_socket:
        logging.error('message or unix socket not specified.')
        return
    try:
        message = utils.serialize({"message": message, "language": language})
        logging.info('sending {!r}'.format(message))
        unix_socket.sendall(message)

    finally:
        logging.info('closing socket')
        # unix_socket.close()


def read_message(unix_socket):
    unix_socket.setblocking(0)
    timeout = 20
    total_data = b''
    data = ''
    begin = time.time()
    while True:
        # if some data arrived, break after timeout
        if total_data and time.time() - begin > timeout:
            break
        # increase waiting time if no data arrived
        elif time.time() - begin > timeout * 2:
            break
        try:
            data = unix_socket.recv(4096)
            if data:
                total_data += data
                begin = time.time()
            else:
                time.sleep(0.1)
        except:
            pass

    translated = utils.deserialize(total_data)
    print("Translating, please wait...")
    print(translated)
    logging.info('received {}'.format(translated))


def close_connection(connection):
    logging.info('closing socket')
    connection.close()
