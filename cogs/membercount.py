import discord
from discord import app_commands
from discord.ext import commands

class Membercount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("membercount.py is active!")
    
    @app_commands.command(name = "membercount", description="Gives you the member count of your server!")
    async def membercount(self, interaction: discord.Interaction):

        guild = interaction.guild
        emoji = " "
    
        if guild.member_count < 100:
            emoji = "<:Oof:1102389709310804008>"

        if guild.member_count >= 100 and guild.member_count <= 1000:
            emoji = "⭐"

        if guild.member_count > 1000:
            emoji = "<:Great:1102390466906963999>"

        MessageEmbed = discord.Embed(
            description = f"The member count for **{guild.name}** is **{guild.member_count}**! " + emoji + "\n\n",
            colour = discord.Colour.blue()
        )
        await interaction.response.send_message(embed=MessageEmbed)

async def setup(client: commands.Bot):
    await client.add_cog(Membercount(client), guilds=client.guilds)