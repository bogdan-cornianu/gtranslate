import os
from unittest import TestCase, mock

from gtranslate import utils


class TestUtils(TestCase):

    def test_serialization(self):
        data = {"1": "123", "2": "456"}
        serialized_data = utils.serialize(data)
        self.assertEqual(serialized_data, b'{"1": "123", "2": "456"}')

    def test_deserialization(self):
        deserialized_data = utils.deserialize(b'{"1": "123", "2": "456"}')
        self.assertEqual(deserialized_data, {"1": "123", "2": "456"})

    @mock.patch.dict(os.environ, {"QUERIES_PER_SEC": "5"})
    def test_get_rate_limit_from_env(self):
        self.assertEqual(utils.get_rate_limit(), 5)

    def test_get_default_rate_limit(self):
        self.assertNotIn("QUERIES_PER_SEC", os.environ)
        self.assertEqual(utils.get_rate_limit(), 10)
