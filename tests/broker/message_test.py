"""
Test the integrity and the functionality of the Message
"""

from datetime import datetime
import json
import pytest
from mh.broker.services.message import Message, TIMESTAMP_FORMAT, MessageFormatError


def test_message_parsing(sample_msg_dict, sample_msg_str):
    """
    Test the message parses the json string correctly
    """
    message = Message.parse(sample_msg_str)  # the fields have the right names
    assert type(message.timestamp) is datetime  # and types
    assert type(message.power) is int
    assert message._asdict() == sample_msg_dict  # it equates its origin

def test_message_parsing_fail_bad_keys(sample_msg_str_bad_keys):
    """
    Test the message fails correctly when parsing a message
    which contains the wrong keys (fields)
    """
    with pytest.raises(MessageFormatError):
        Message.parse(sample_msg_str_bad_keys)

def test_message_parsing_fail_bad_value_types(
    sample_msg_str_bad_value_type_timestamp,
    sample_msg_str_bad_value_type_power  # cannot parametrize with fixtures
):
    """
    Test the message fails correctly when parsing a message
    whose fields are of the wrong type
    """
    with pytest.raises(MessageFormatError):
        Message.parse(sample_msg_str_bad_value_type_timestamp)
    with pytest.raises(MessageFormatError):
        Message.parse(sample_msg_str_bad_value_type_power)

def test_message_format_as_string(sample_msg_dict, sample_msg_str):
    """
    Test the message converts to string correctly
    """
    message = Message(**sample_msg_dict)
    assert str(message) == sample_msg_str
