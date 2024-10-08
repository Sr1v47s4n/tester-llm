from .base_agent import BaseAgent
from nexa.helpers.logger_config import configure_logger

logger = configure_logger(__name__)


class ExtractionContextualAgent(BaseAgent):
    def __init__(self, llm, prompt=None):
        super().__init__()
        self.llm = llm
        self.current_messages = 0
        self.is_inference_on = False
        self.has_intro_been_sent = False

    async def generate(self, history):
        logger.info("extracting json from the previous conversation data")
        json_data = await self.llm.generate(history, request_json=True)
        return json_data
