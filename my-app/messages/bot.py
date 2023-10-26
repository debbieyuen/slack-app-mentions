import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to
channel_id = "C062XBL7XUL"

try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)

    conversation_history = result["messages"]
    count = 0
    toString = " "
    while count < 3: 
        messages = result["messages"][count]
        count += 1
        toString += str(messages["text"])
    
    print(toString.split())
    array = toString.split()
    counting = 0;
    for element in array: 
        if element == "slider":
            counting += 1
        if element == "slider.is":
            counting += 1
        if element == "*AndroidBaseSlider*":
            counting += 1
        if element == "SlideView":
            counting += 1
            print(f"Slide count: {counting}")
        

except SlackApiError as e:
    print("Error creating conversation: {}".format(e))

