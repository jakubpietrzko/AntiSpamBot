import discord
from discord.ext import commands
from message_handler import on_message_handler
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
from config import TOKEN
@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message(message):
    await on_message_handler(message,bot) 

    await bot.process_commands(message)
bot.run(TOKEN)
