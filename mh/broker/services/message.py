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
        except (json.JSONDecodeError, ValueError):
            raise MessageFormatError(f"Malformed message received: {msg}")
        return Message(**msg_d)

    def __str__(self):
        msg_d = self._asdict()
        msg_d['timestamp'] = datetime.strftime(self.timestamp, TIMESTAMP_FORMAT)
        return json.dumps(msg_d)
