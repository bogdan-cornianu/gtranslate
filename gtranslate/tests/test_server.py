from unittest import TestCase, mock

from gtranslate import server


class TestServer(TestCase):

    def test_send_message(self):
        mock_socket = mock.Mock()
        server.send_message(mock_socket, "test message")
        mock_socket.sendall.assert_called()
