from datetime import datetime
import json
import pytest
from mh.broker.services.message import Message, TIMESTAMP_FORMAT, MessageFormatError


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

@pytest.fixture
def sample_msg_dict_bad_value_type_timestamp():
    return {
        "timestamp": "I am rubbish",
        "power": 4500
    }

@pytest.fixture
def sample_msg_str_bad_value_type_timestamp(sample_msg_dict_bad_value_type_timestamp):
    msg_copy = sample_msg_dict_bad_value_type_timestamp.copy()
    return json.dumps(msg_copy)

@pytest.fixture
def sample_msg_dict_bad_value_type_power():
    return {
        "timestamp": datetime.now().replace(microsecond=0),  # suppress ms
        "power": 'I am a string'
    }

@pytest.fixture
def sample_msg_str_bad_value_type_power(sample_msg_dict_bad_value_type_power):
    msg_copy = sample_msg_dict_bad_value_type_power.copy()
    msg_copy['timestamp'] = datetime.strftime(
        msg_copy['timestamp'],
        '%Y-%m-%d %H:%M:%S'
    )
    return json.dumps(msg_copy)
