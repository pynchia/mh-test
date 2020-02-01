from datetime import datetime
import json
from typing import NamedTuple


TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

class MessageFormatError(Exception):
    pass

class Message(NamedTuple):
    timestamp: datetime
    power: int

    @classmethod
    def parse(cls, msg):
        """
        Parse the incoming string msg into a structured message
        Return:
            the message
        """
        try:
            msg_d = json.loads(msg)
            msg_d['timestamp'] = datetime.strptime(msg_d['timestamp'], TIMESTAMP_FORMAT)
            message = Message(**msg_d)
            if type(message.power) is not int:
                raise TypeError
        except (json.JSONDecodeError, TypeError, ValueError):
            raise MessageFormatError(f"Malformed message received: {msg}")
        return message

    def __str__(self):
        """
        The msg is stringified as the json:
            '{
                "timestamp": timestamp (in the above format),
                "power": current power level
            }'
        """
        msg_d = self._asdict()
        msg_d['timestamp'] = datetime.strftime(self.timestamp, TIMESTAMP_FORMAT)
        return json.dumps(msg_d)
