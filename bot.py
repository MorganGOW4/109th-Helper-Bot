import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load secret token from your hidden .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
 
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True # Required to read messages
        super().__init__(command_prefix="!", intents=intents)

    # The setup hook is called before the bot connects to Discord
    async def setup_hook(self):
        # Loop through all files in the cogs directory
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                # Load the cog using dot notation (e.g., cogs.general)
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}!")
    guild_object = discord.Object(id=1542137386375319642)
    bot.tree.copy_global_to(guild=guild_object)
    await bot.tree.sync(guild=guild_object)

bot.run(TOKEN)