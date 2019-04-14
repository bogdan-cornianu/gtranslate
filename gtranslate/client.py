import os
import sys
import socket
import json
import logging


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


def send_message(message, unix_socket):
    if not message or not unix_socket:
        logging.error('message or unix socket not specified.')
        return
    try:
        message = json.dumps(message).encode('utf-8')
        logging.info('sending {!r}'.format(message))
        unix_socket.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        reply = b''
        while amount_received < amount_expected:
            data = unix_socket.recv(16)
            reply += data
            amount_received += len(data)
        interm = json.loads(reply)
        logging.info('received {}'.format(interm))
    finally:
        logging.info('closing socket')
        unix_socket.close()
