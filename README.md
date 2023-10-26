# Slack App: Component Mention Counts 🔥
A Slack App feature that helps users determine how often a component/element/word was mentioned within Slack messages. The feature provides the user with a number count of the times a specific component is mentioned and referenced. 

The project starts off by creating a new [Slack App](https://api.slack.com/automation/create) and workspace to build my app. I chose to create a new workspace! Within the application, scopes were used to give the new app permission to do things. Under the **OAuth & Permissions** tab in the sidebar, add scopes to the app. The scopes that will be necessary include: 
* `channels:read`: This scope allows the app to retrieve a list of all the public channels in a workspace in order to pick one to retrieve a message from.
* `channels:history`: This scope lets the app view all the messages within any public channel in a workspace.

https://github.com/debbieyuen/slack-app-mentions/assets/31296177/561341d2-7fbb-44fb-be9e-8d0d17b4a0b3

## Requirements
* [Slack CLI](https://api.slack.com/automation/quickstart)
* [Slack Pro Workspace](https://api.slack.com/start/overview)
* Python 3.12.0
* [Python Slack SDK 3.23.0](https://slack.dev/python-slack-sdk/)
* Slack Signing Secret key
* Bot User OAuth Access Token

## Python-Slack

In the root directory, create a **requirements.txt** file and add the following contents to the file.
```
slack_sdk>=3.0
slack_bolt>=1.6.1
certifi
```
Install the dependencies by running the following command from terminal. 
```bash
$ pip3 install -r requirements.txt
```

Use Certifi's functions to locate installed certificate authority (CA) bundles.
```Python
import ssl as ssl_lib
import certifi

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
```

## Slack API

<img width="1280" alt="Screenshot 2023-10-26 at 3 31 02 AM" src="https://github.com/debbieyuen/slack-app-mentions/assets/31296177/355ff60f-ad8b-4655-b7ed-41d73f7f621f">


## Set Up

Clone the repository
```bash
$ git clone https://github.com/debbieyuen/slack-app-mentions.git
```

Install Slack CLI (Mac)
```bash
# Run the automated installer from your terminal window:
$ curl -fsSL https://downloads.slack-edge.com/slack-cli/install.sh | bash

# Authorize the CLI in your workspace with the following command:
$ slack login

# Input an entry for a paid workspace
$ slack auth list
```

Retrieve your **Bot User OAuth Access Token** for your app from the [app management page](https://api.slack.com/apps). In your terminal, add your token to your environment variables.

```bash
$ export SLACK_BOT_TOKEN='xoxb-XXXXXXXXXXXX-xxxxxxxxxxxx-XXXXXXXXXXXXXXXXXXXXXXXX'
```
<img width="1280" alt="Screenshot 2023-10-26 at 2 57 37 AM" src="https://github.com/debbieyuen/slack-app-mentions/assets/31296177/987ea01d-b587-478d-a482-45d7e5530e14">

Retrieve your **Slack Signing Secret** key for your app from the [app management page](https://api.slack.com/apps). In your terminal, run the following command. 

```bash
$ export SLACK_SIGNING_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
<img width="631" alt="Screenshot 2023-10-26 at 3 01 21 AM" src="https://github.com/debbieyuen/slack-app-mentions/assets/31296177/61d43a85-5fc8-4216-9543-8b101b483f20">

Run the python file
```bash
$ python3 bot.py
```

On the [app management page](https://api.slack.com/apps), install the DebBot app in your workspace. Then, in Slack add the DeBot app to the `#general` channel.

<img width="1280" alt="Screenshot 2023-10-26 at 3 06 19 AM" src="https://github.com/debbieyuen/slack-app-mentions/assets/31296177/b6977381-5489-4bf4-9660-3992fa9d1cdc">

## Credits and References
* [Python Slack SDK Documentation](https://github.com/slackapi/python-slack-sdk)
* @karishay's [PythOnBoardingBot](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial) tutorial
* [The New Slack Platform](https://www.youtube.com/playlist?list=PLWlXaxtQ7fUYi7HPZMi0fUU7YbYZXemsp) YouTube series
* [Slack: Retrieving Messages](https://api.slack.com/messaging/retrieving)
* [Slack: Conversations API](https://api.slack.com/docs/conversations-api)
* [Slack: Using the Slack Web API](https://api.slack.com/web)
