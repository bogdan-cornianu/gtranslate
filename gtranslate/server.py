import socket
import logging
import os


def start_server():
    server_address = '/tmp/gtranslate_uds_socket'
    logging.info('starting server...')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    logging.info('starting up on {}'.format(server_address))
    try:
        if os.path.exists(server_address):
            os.unlink(server_address)
        sock.bind(server_address)
    except OSError as e:
        logging.info('exception {}'.format(e))
    sock.listen(1)
    logging.info('listening...')

    return sock.accept()


def send_message(connection, message):
    connection.sendall(message)
