import json


def serialize(data):
    return json.dumps(data).encode('utf-8')


def deserialize(data):
    return json.loads(data)
