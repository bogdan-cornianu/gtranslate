import json
import os


def serialize(data):
    return json.dumps(data).encode('utf-8')


def deserialize(data):
    return json.loads(data)


def get_rate_limit():
    qps = os.environ.get('QUERIES_PER_SEC')
    return int(qps) if qps else 10
