from datetime import datetime
import json
import pytest
import random
from mh.broker.services.message import Message, TIMESTAMP_FORMAT
from mh.meter.generate import generate_msgs
from unittest.mock import Mock, patch


def test_format_of_messages():
    """
    Test the message expected format
    """
    for msg in it.islice(generate_msgs(), 0, 5):
        message = Message.parse(msg)  # check the json fields have the right names
        assert type(message.timestamp) is datetime
        assert type(message.power) is int

