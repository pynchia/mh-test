"""
Test the Broker service

PLEASE NOTE: FOR DEMO PURPOSES ONLY. NOT ALL THE SCENARIOS ARE CATERED FOR
"""

import logging
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from unittest.mock import MagicMock, patch


log = logging.getLogger()


def test_service_publish(sample_msg_str):
    message_queue = []  # the queue of messages, stored elsewhere
    def publish(msg):
        message_queue.append(msg)

    mock_rabbit = MagicMock()
    with Broker(mock_rabbit) as broker:
        assert broker.connector == mock_rabbit

        mock_rabbit.publish.side_effect = publish
        broker.publish(sample_msg_str)
        mock_rabbit.publish.assert_called_once()
        assert message_queue.pop() == sample_msg_str
    mock_rabbit.close.assert_called_once()


def test_service_subscribe_and_consume(sample_msg_str):
    consumer = lambda msg: None  # what to call back, stored in the connector
    message_queue = []  # the queue of messages, stored elsewhere

    def processor(msg):  # the actual callback, the end-user processing the msg
        # print(f"\nprocessor: {msg}")
        assert msg == sample_msg_str
    def publish(msg):
        message_queue.append(msg)
    def subscribe(callback):
        nonlocal consumer
        consumer = callback
    def consume():
        msg = message_queue.pop(0)  # pop the oldest one in the queue
        consumer(msg)

    mock_rabbit = MagicMock()
    with Broker(mock_rabbit) as broker:
        assert broker.connector == mock_rabbit

        mock_rabbit.publish.side_effect = publish
        broker.publish(sample_msg_str)
        mock_rabbit.publish.assert_called_once()
    mock_rabbit.close.assert_called_once()

    mock_rabbit = MagicMock() # another broker for another consumer process
    with Broker(mock_rabbit) as broker:
        assert broker.connector == mock_rabbit

        mock_rabbit.publish.side_effect = publish
        broker.publish(sample_msg_str)
        mock_rabbit.publish.assert_called_once()

        mock_rabbit.subscribe.side_effect = subscribe
        mock_rabbit.consume.side_effect = consume
        broker.subscribe_and_consume(processor)
        mock_rabbit.subscribe.assert_called_once()
        mock_rabbit.consume.assert_called_once()
    mock_rabbit.close.assert_called_once()
