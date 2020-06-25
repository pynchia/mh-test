"""
Test the consumer

PLEASE NOTE: FOR DEMO PURPOSES ONLY. NOT ALL THE SCENARIOS ARE CATERED FOR
"""
import pytest
from unittest.mock import MagicMock, patch
from mh.broker.connectors.rabbit import Rabbit
from mh.broker.services.broker import Broker
from mh.pv.consumer import Processor


DUMB_FILENAME = 'dumb.txt'


def test_processor_opened_closed_output_file():
    mocked_file = MagicMock()
    with patch('mh.pv.consumer.open', return_value=mocked_file):
        with Processor(DUMB_FILENAME):
            pass
        mocked_file.close.assert_called_once()

@pytest.fixture(scope='module')
def sample_line_in_output_file(sample_msg_dict):
    return "{} meter={} pv={}, total={}\n".format(
        sample_msg_dict['timestamp'],
        sample_msg_dict['power'],
        10,
        sample_msg_dict['power']+10
    )

def test_msg_written_to_output_file(sample_msg_str, sample_line_in_output_file):
    def mocked_write(line):
        assert line == sample_line_in_output_file

    mocked_file = MagicMock()
    with patch('mh.pv.consumer.open', return_value=mocked_file), \
        patch('mh.pv.pv_power.PV.measure_power') as mock_measure:
        mock_measure.return_value = 10
        with Processor(DUMB_FILENAME) as processor:
            mocked_file.write.side_effect = mocked_write
            processor(sample_msg_str)  # i.e. call the consumer's callback
            mock_measure.assert_called_once()
            mocked_file.write.assert_called_once()
        mocked_file.close.assert_called_once()
