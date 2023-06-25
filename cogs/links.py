import discord
from discord.ext import commands
from discord import app_commands

class linksButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
    @discord.ui.button(label="ToggleBot Invite", style=discord.ButtonStyle.blurple, custom_id='persistent_view:LinkButton1')
    async def menu1(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(content="`>>>` https://discord.com/api/oauth2/authorize?client_id=914658457909600347&permissions=8&scope=bot `<<<`\n\n") 
        
    @discord.ui.button(label="Help Server", style=discord.ButtonStyle.blurple, custom_id='persistent_view:LinkButton2')
    async def menu2(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(content="> `>>>` https://discord.gg/Z2swYS8HWH\n\n") 
        
    @discord.ui.button(label="Tqgd's Socials", style=discord.ButtonStyle.blurple, custom_id='persistent_view:LinkButton3')
    async def menu3(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(content="> `>>>` https://youtube.com/ToggledGamer\n\n> `>>>` https://www.twitch.tv/toggledgamer\n\n> `>>>` https://twitter.com/Toggled12") 
        
class Links(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("links.py is active!")

    @app_commands.command(name="links", description="Useful links and promotions of the creator of ToggleBot.")
    async def links(self, interaction: discord.Interaction):
        view = linksButton()
        embed = discord.Embed(
            description = "Click the buttons below to view the desired link!",
            colour = discord.Colour.blue()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)

async def setup(client: commands.Bot):
    await client.add_cog(Links(client), guilds=client.guilds)