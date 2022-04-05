import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("xoxb-3171986363218-3285538170935-v1TQy2nwI9vo7fddnKN2EVdv"))
logger = logging.getLogger(__name__)

try:
    # Call the chat.postMessage method using the WebClient
    result = client.chat_postMessage(
        channel="#pybot", 
        text="Hello world"
    )
    logger.info(result)

except SlackApiError as e:
    logger.error(f"Error posting message: {e}")
