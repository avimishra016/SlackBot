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
@app.message("Get PR")
def getPr(message, say):
    say(getPRoutput())
# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))