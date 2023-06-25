import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py is active!")
    
    @app_commands.command(name = "ping", description="Tells the ping of the bot!")
    async def ping(self, interaction: discord.Interaction):

        MessageEmbed = discord.Embed(
            description = f"**Pong!** {round(self.client.latency * 1000)}ms\n\n",
            colour = discord.Colour.blue()
        )
        
        await interaction.response.send_message(embed=MessageEmbed)

async def setup(client: commands.Bot):
    await client.add_cog(Ping(client), guilds=client.guilds)