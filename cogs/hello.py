import discord
from discord import app_commands
from discord.ext import commands

class helloButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
    @discord.ui.button(label="Hi!", style=discord.ButtonStyle.blurple, custom_id='persistent_view:helloButton')
    async def menu1(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.send_message("Hi! I'm ToggleBot! To explore my command list... use **/help**", ephemeral=True)

class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("hello.py is active!")
    
    @app_commands.command(name = "hello", description="Meet the first slash command where the bot greets the user with a hello!")
    async def hello(self, interaction: discord.Interaction):

        view = helloButton()
        await interaction.response.send_message(f"Hello {interaction.user.mention}! This is the first slash command!", view=view)

async def setup(client: commands.Bot):
    await client.add_cog(Hello(client), guilds=client.guilds)