import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import cogs.cookieclicker as cc
import cogs.links
import cogs.help
import cogs.hello

load_dotenv()

class ToggleBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix = 'tg.',
            intents = discord.Intents.all(),
            application_id = 914658457909600347)
        
        self.initial_extensions = [
            "cogs.help",
            "cogs.ping",
            "cogs.hello",
            "cogs.links",
            "cogs.cookieclicker",
            "cogs.membercount",
            "cogs.slap"
        ]
        

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await client.load_extension(f"cogs.{filename[:-3]}")
                    
                    client.add_view(cc.CCButton())
                    client.add_view(cogs.links.linksButton())
                    client.add_view(cogs.hello.helloButton())
                    client.add_view(cogs.help.helpButton())

                    print(f"Loaded {filename}")
                except Exception as e:
                    print(f"Unable to load {filename}")
                    print(f"[ERROR] {e}")        


    async def close(self):
        await super().close()
        await self.session.close()
       

    async def on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('/help'))
        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

        print("The bot is available for usage...")

client = ToggleBot()
client.remove_command("help")

TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)

