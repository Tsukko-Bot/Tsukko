# Import Libraries...
import asyncio
import random, os, sys, discord, random, logging
from discord.ext import commands

# ... then grab the API token
def set_token():
    TOKENfile = open('token.txt', 'rt') # Opens "token.txt" as a read-only text file.
    TOKEN = TOKENfile.read() # Reads from the file...
    TOKENfile.close() # ... before proptly closing it.
    return TOKEN

try:
    TOKEN = set_token()
except FileNotFoundError:
    input('Please put an API token in token.txt. (Press ENTER/RETURN to continue...) ')
    TOKEN = set_token()


# Bot trivia

bot_trivia_secret = ['tsu/secret_bot_trivia is what you probably typed to get this. If not *shouting now* HELLO FROM THE STATUS!!!', 'Nobody really knows who the person in Tsukko\'s profile picture is. That\'s why they don\'t have a face.', 'This is for those UNDERTALE players. The color of "Tsukko"\'s shirt, striped brown and green, is actually Frisk\'s shirt with inverted colors. Interesting.', 'We call the person in Tsukko\'s profile picture "Tsukko", as we don\'t know their name. Note the inverted commas there.']
bot_playing_cycle = ['the game of life.', 'tsu/help', 'a game.']

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    commands_heading = 'Tsukko/Help',
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix = commands.when_mentioned_or('tsu/'), help_command = help_command) # initilizes the bot, setting the prefix to "tsu/".

async def status_task():
    while True:
        SAMEMESS = True
        try:
            oldmessage = botmessage
        except:
            oldmessage = None

        while SAMEMESS:
            richloop = random.randint(0, 9999)
            print(richloop)
            if richloop == 3945 or 4390:
                botmessage = bot_trivia_secret[(random.randint(0, len(bot_trivia_secret)) - 1)]
                print(botmessage)
            else:
                botmessage = bot_playing_cycle[(random.randint(0, len(bot_playing_cycle)) - 1)]
                print(botmessage)

            if oldmessage == botmessage:
                SAMEMESS = True
            else:
                SAMEMESS = False

        await bot.change_presence(activity=discord.Game(name=botmessage))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())

@bot.command()
async def info(ctx):
    '''Basic Bot Info.'''
    embed = discord.Embed(title="Tsukko", description="ツッコ (Tsukko) is a Discord bot for managing your Discord server.", color=000000) #,color=Hex code
    embed.add_field(name="Creator", value="[ByeMC#3276](https://byemc.xyz/)")
    embed.add_field(name="Invite", value="To invite Tsukko to your Discord server, please go to the [GitHub repo](https://github.com/tsukko-bot/tsukko#invites)")
    embed.set_image(url="https://static.byemc.xyz/tsukko/tsukko.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/264139669174878219/d8cff95d16b3f1f4ee8322f972878d76.webp")
    await ctx.send(embed=embed)

@bot.command()
async def secret_bot_trivia(ctx):
    bot_triv = bot_trivia_secret[(random.randint(0, len(bot_trivia_secret)) - 1)]
    embed = discord.Embed(title="~~Secret Bot Trivia~~", description="Ok, you found this fair and square, here's some bot trivia:", color=000000) #,color=Hex code
    embed.add_field(name="Trivia", value=str(bot_triv))
    embed.set_thumbnail(url="https://static.byemc.xyz/tsukko/tsukko.png")
    await ctx.send(embed=embed)


bot.run(str(TOKEN))



