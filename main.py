# Import Libraries...
import random, os, sys, discord
from discord.ext import commands

# ... then grab the API token
def set_token():
    TOKENfile = open('token.txt', 'rt') # Opens "token.txt" as a read-only text file.
    TOKEN = TOKENfile.read() # Reads from the file...
    print(TOKEN)
    TOKENfile.close() # ... before proptly closing it.
    return TOKEN

try:
    TOKEN = set_token()
except FileNotFoundError:
    input('Please put an API token in token.txt. (Press ENTER/RETURN to continue...) ')
    TOKEN = set_token()

bot = commands.Bot(command_prefix='tsu/') # initilizes the bot, setting the prefix to "tsu/".

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Tsukko", description="ツッコ (Tsukko) is a Discord bot for managing your Discord server.", color=000000) #,color=Hex code
    embed.add_field(name="Creator", value="[ByeMC#3276](https://byemc.xyz/)")
    embed.add_field(name="Invite", value="To invite Tsukko to your Discord server, please go to the [GitHub repo](https://github.com/tsukko-bot/tsukko#invites)")
    embed.set_image(url="https://static.byemc.xyz/tsukko/tsukko.png")
    await ctx.send(embed=embed)
    
bot.run(str(TOKEN))
