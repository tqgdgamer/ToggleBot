import discord
from discord import app_commands
from discord.ext import commands

page1 = discord.Embed(
    title='Bot Help 1',
    description='Use the buttons below to switch pages',
    colour=discord.Colour.blue()
    )

page1.add_field(name='/help', value='Send a help page in the following channel you used this command in.', inline= False)
page1.add_field(name='/hello', value='The Bot says hello to the user.', inline= False)
page1.add_field(name='/links', value='Page of links', inline = False)
page1.add_field(name='/ping', value="Tells the bot ping", inline = False)
page1.add_field(name='/membercount', value="Tells the current membercount", inline = False)

page2 = discord.Embed(
    title='Bot Help 2',
    description='Page 2 (Commands with the prefix \'tg\' are not updated)',
    colour=discord.Colour.blue()
    )

page2.add_field(name='/clear (amount)', value="Deletes messages up to 999", inline = False)
page2.add_field(name='tg.unmute @user', value="Unmutes a specified user.", inline = False)
page2.add_field(name='tg.mute @user', value="Mutes the specified user.", inline = False)
page2.add_field(name='tg.kick @user', value="Kicks the specified user.", inline = False)
page2.add_field(name='tg.ban @user', value="Bans the specified user.", inline = False)
page2.add_field(name='tg.unban user#0000', value="Unbans the specified user", inline = False)

page3 = discord.Embed(
    title='Bot Help 3',
    description='Page 3',
    colour=discord.Colour.blue()
    )

page3.add_field(name='/pp @user', value="Randomly measures your pp size from a range of 1-6 inches.", inline= False)
page3.add_field(name='/potato', value="Send a potato gif", inline= False)
page3.add_field(name='/uwu', value="uwu?", inline=False)
page3.add_field(name='/slap @user', value="Slap a desired person", inline=False)
page3.add_field(name='/dict [word]', value="The goofy dictionary", inline=False)

page4 = discord.Embed(
    title='Bot Help 4',
    description='Page 4 (Not Updated)',
    colour=discord.Colour.blue()
    )

page4.add_field(name='tg.gsetup', value="Add a role for permissions to host giveaways. The role can be edited later by an adminstrator")
page4.add_field(name='tg.giveaway', value='Host a giveaway! Instructions with this command.')
page4.add_field(name='tg.reroll (channelID) (giveawayMessageID)', value='Reroll the giveaway to select a different winner.')


class helpButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        
    @discord.ui.button(label="1", style=discord.ButtonStyle.blurple, custom_id='persistent_view:HelpPage1')
    async def menu1(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(embed=page1)
        
    @discord.ui.button(label="2", style=discord.ButtonStyle.blurple, custom_id='persistent_view:HelpPage2')
    async def menu2(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(embed=page2)       
        
    @discord.ui.button(label="3", style=discord.ButtonStyle.blurple, custom_id='persistent_view:HelpPage3')
    async def menu3(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(embed=page3)        

    @discord.ui.button(label="4", style=discord.ButtonStyle.blurple, custom_id='persistent_view:HelpPage4')
    async def menu4(self, interaction: discord.Interaction,  button: discord.ui.Button):
        await interaction.response.edit_message(embed=page4)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help.py is active!")

    @app_commands.command(name = "help", description="A guidebook on how to use ToggleBot!")
    async def help(self, interaction: discord.Interaction):
    
        view = helpButton()
    
        await interaction.response.send_message(embed=page1,view=view, ephemeral=True)

async def setup(client: commands.Bot):
    await client.add_cog(Help(client), guilds=client.guilds)