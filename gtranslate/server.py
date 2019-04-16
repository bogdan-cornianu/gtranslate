import socket
import logging
import os

from gtranslate import gapi


def start_server():
    server_address = '/tmp/gtranslate_uds_socket'
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        # delete socket file if it already exists
        if os.path.exists(server_address):
            os.unlink(server_address)
        sock.bind(server_address)
    except OSError as e:
        logging.info('exception {}'.format(e))
    sock.listen(1)
    logging.info('listening...')

    return sock.accept()


def read_message(connection):
    while True:
        data = connection.recv(4096)
        logging.info('received {!r}'.format(data))
        if data:
            translations = gapi.get_translation(data)
            send_message(connection, translations)
            logging.info('sending data back to the client')
        else:
            break


def send_message(connection, message):
    connection.sendall(message)
