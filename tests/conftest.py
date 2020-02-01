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

@pytest.fixture(scope='session')
def sample_msg_dict_bad_keys():
    return {
        "timestamp": datetime.now().replace(microsecond=0),  # suppress ms
        "bar": 4500
    }

@pytest.fixture(scope='session')
def sample_msg_str_bad_keys(sample_msg_dict_bad_keys):
    msg_copy = sample_msg_dict_bad_keys.copy()
    msg_copy['timestamp'] = datetime.strftime(
        msg_copy['timestamp'],
        '%Y-%m-%d %H:%M:%S'
    )
    return json.dumps(msg_copy)

@pytest.fixture(scope='session')
def sample_msg_dict_bad_value_types():
    return {
        "timestamp": datetime.now().replace(microsecond=0),  # suppress ms
        "power": 'I am a string'
    }

@pytest.fixture(scope='session')
def sample_msg_str_bad_value_types(sample_msg_dict_bad_value_types):
    msg_copy = sample_msg_dict_bad_value_types.copy()
    msg_copy['timestamp'] = datetime.strftime(
        msg_copy['timestamp'],
        '%Y-%m-%d %H:%M:%S'
    )
    return json.dumps(msg_copy)
