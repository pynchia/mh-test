"""
Test the Rabbit connector

PLEASE NOTE: FOR DEMO PURPOSES ONLY. NOT ALL THE SCENARIOS ARE CATERED FOR
"""

import logging
# import pika
# import pika.exceptions as exc
from unittest.mock import MagicMock, patch
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.connectors.api import PublishError


log = logging.getLogger()


def test_connector_publish(sample_msg_str):
    exchange_name = None
    routing_key_name = None
    message_queue = []  # the queue of messages, stored elsewhere

    def basic_publish(exchange,routing_key, body):
        nonlocal exchange_name, routing_key_name
        exchange_name = exchange
        routing_key_name = routing_key
        message_queue.append(body)

    with patch('mh.broker.connectors.rabbit.pika') as mock_pika:
        mock_pika.URLParameters.return_value = MagicMock()
        connection = MagicMock()
        mock_pika.BlockingConnection.return_value = connection
        channel = MagicMock()
        connection.channel.return_value = channel
        connector = Rabbit('broker_url')
        channel.basic_publish.side_effect = basic_publish
        connector.publish(sample_msg_str)
        assert len(message_queue) == 1
        assert message_queue[0] == sample_msg_str

def test_connector_subscribe(sample_msg_str):
    message_queue = []  # the queue of messages, stored elsewhere
    callback_f = None

    def basic_publish(exchange, routing_key, body):
        message_queue.append(body)

    def basic_consume(queue,callback, auto_ack):
        nonlocal callback_f
        callback_f = callback

    def processor(msg):  # the actual callback, the end-user processing the msg
        # print(f"\nprocessor: {msg}")
        assert msg == sample_msg_str

    with patch('mh.broker.connectors.rabbit.pika') as mock_pika:
        mock_pika.URLParameters.return_value = MagicMock()
        connection = MagicMock()
        mock_pika.BlockingConnection.return_value = connection
        channel = MagicMock()
        connection.channel.return_value = channel
        connector = Rabbit('broker_url')
        channel.basic_publish.side_effect = basic_publish
        connector.publish(sample_msg_str)
        assert len(message_queue) == 1
        assert message_queue[0] == sample_msg_str

        channel.basic_consume.side_effect = basic_consume
        connector.subscribe(processor)

        channel.start_consuming.side_effect = callback_f
