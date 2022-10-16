import discord
import json

class discordBot():
    def __init__(self, TOKEN, GUILDS):
        self.GUILDS = GUILDS
        self.TOKEN = TOKEN
        self.CLIENT = discord.Bot()
    def registerCommand(self, functionCommand):
        functionCommand(self.CLIENT, self.GUILDS)
    def registerEvent(self, functionEvent):
        functionEvent(self.CLIENT)
    def start(self):
        self.CLIENT.run(self.TOKEN)

TOKEN = json.load(open("configBot.json", "r"))["TOKEN"]
GUILDS = json.load(open("configBot.json", "r"))["GUILDS"]

discordBot().start()