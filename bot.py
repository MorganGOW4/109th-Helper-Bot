import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load secret token from your hidden .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot intents (permissions)
intents = discord.Intents.default()
intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)