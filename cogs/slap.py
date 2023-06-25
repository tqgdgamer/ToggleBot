import discord
from discord import app_commands
from discord.ext import commands

class Slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("slap.py is active!")
    
    @app_commands.command(name = "slap", description="Virtually slap whoever you wish to slap.")
    async def slap(self, interaction: discord.Interaction, *, member: discord.Member, reason: str="*No reason provided.*"):

        reason = discord.Embed(
        description=f"{interaction.user.mention} slapped *{member.mention}* for **{reason}**",
        colour=discord.Colour.blurple()
        )
    
        await interaction.response.send_message(embed=reason)  

async def setup(client: commands.Bot):
    await client.add_cog(Slap(client), guilds=client.guilds)  