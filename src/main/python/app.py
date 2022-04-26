from dotenv import load_dotenv
from listPR import *
import os
# Use the package we installed
from slack_bolt import App

load_dotenv()

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
@app.message("hello")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

@app.command("/getprs")
def getPr(ack, say):
    ack()
    blocks = [{
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Requested Pull Request Data"
                }
		     }]
    data = trial()
    url = data[0]
    data.pop(0)
    for x in data:
        prNum = x[0]
        prName = x[1]
        prTime = x[2]
        prUrl = x[3]
        printedText = "*PR " + str(prNum) + "*: " + prName
        dateText = "`Requested at: " + prTime + "`"
        blocks.append({"type": "divider"})
        blocks.append({
			"type": "section",
		    "text": {
			    "type": "mrkdwn",
			    "text": printedText
		    }
	    })
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": dateText
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Link to PR",
                },
                "url": prUrl,
                "action_id": "button-action"
            }
         })
        say(blocks=blocks)
# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))