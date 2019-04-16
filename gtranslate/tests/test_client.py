from unittest import TestCase, mock

from gtranslate.client import send_message, close_connection


class TestClient(TestCase):

    def test_send_message(self):
        mock_socket = mock.Mock()
        send_message("test message", "it", mock_socket)
        mock_socket.sendall.assert_called()

    def test_close_connection(self):
        mock_socket = mock.Mock()
        close_connection(mock_socket)
        mock_socket.close.assert_called()
