import discord
from discord.ext import commands
from discord import app_commands

client = commands.Bot(command_prefix="tg.", intents=discord.Intents.all())

client.clickCount = 0
clickCount = client.clickCount

class CCButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
    @discord.ui.button(label="🍪", style=discord.ButtonStyle.blurple, custom_id='persistent_view:CC')
    async def menu1(self, interaction: discord.Interaction,  button: discord.ui.Button):
        
        global clickCount
        clickCount += 1
        
        embed = discord.Embed(
            title='Cookie Clicker v1',
            description=f'You have clicked **{clickCount}** times!',
            colour=discord.Colour.blue()
        )
        
        await interaction.response.edit_message(embed=embed)
        
class CookieClicker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("cookieclicker.py is active!")

    @app_commands.command(name="cookieclicker", description="Click on a button for fun.")
    async def links(self, interaction: discord.Interaction):
        view = CCButton()
        embed = discord.Embed(
            title = "Click the 🍪 below to begin playing!",
            colour = discord.Colour.blue()
        )
        await interaction.response.send_message(embed=embed, view=view)

async def setup(client: commands.Bot):
    await client.add_cog(CookieClicker(client), guilds=client.guilds)