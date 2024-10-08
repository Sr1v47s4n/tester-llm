from nexa.input_handlers.telephony import TelephonyInputHandler
from dotenv import load_dotenv
from nexa.helpers.logger_config import configure_logger

logger = configure_logger(__name__)
load_dotenv()


class PlivoInputHandler(TelephonyInputHandler):
    def __init__(self, queues, websocket=None, input_types=None, mark_set=None, turn_based_conversation=False):
        super().__init__(queues, websocket, input_types, mark_set, turn_based_conversation)
        self.io_provider = 'plivo'

    async def call_start(self, packet):
        start = packet['start']
        self.call_sid = start['callId']
        self.stream_sid = start['streamId']
