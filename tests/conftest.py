from datetime import  datetime
import json
import pytest


@pytest.fixture(scope='session')
def sample_msg_dict():
    return {
        "timestamp": datetime.now().replace(microsecond=0),  # suppress ms
        "power": 4500
    }

@pytest.fixture(scope='session')
def sample_msg_str(sample_msg_dict):
    msg_copy = sample_msg_dict.copy()
    msg_copy['timestamp'] = datetime.strftime(
        msg_copy['timestamp'],
        '%Y-%m-%d %H:%M:%S'
    )
    return json.dumps(msg_copy)
