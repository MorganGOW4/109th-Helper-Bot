from typing import Literal
import discord
from discord.ext import commands
from discord import app_commands

class Eventlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="log", description="Log an event.")
    async def log(self, interaction: discord.Interaction, 
                    event_type: Literal["Border Patrol", 
                                        "City Patrol", 
                                        "Combat Training", 
                                        "Spar",
                                        "Defense Training", 
                                        "Raid Defense Training", 
                                        "Scrim", 
                                        "General Training", 
                                        "Tryout",
                                        "Special",
                                        "Other"
                                        ], 
                    host_username: str, 
                    attendees_usernames: str, 
                    mvp: str, 
                    proof: discord.Attachment,
                    supervisor_username: str = "N/A",
                    cohost_username: str = "N/A",
                    ptbd: str = "N/A" 
                    ):

        # Create an embed to display the event log information
        embed = discord.Embed(title=event_type, 
                      colour=discord.Colour(0xe74c3c), 
                      timestamp=discord.utils.utcnow()
                      )

        embed.set_image(url=proof)
        embed.set_footer(text="Success", icon_url="https://cdn.discordapp.com/emojis/1055493020025360506.webp?size=96")

        embed.add_field(name="Host:", value= host_username, inline=False)
        if supervisor_username != "N/A":
            embed.add_field(name="Supervisor:", value= supervisor_username, inline=False)
        if cohost_username != "N/A":
            embed.add_field(name="Cohost:", value= cohost_username, inline=False)
        embed.add_field(name="Attendees:", value= attendees_usernames, inline=False)
        embed.add_field(name="MVPs:", value= mvp, inline=False)
        embed.add_field(name="PTBD:", value= ptbd, inline=False)
        embed.add_field(name="Proof:", value="** **", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Eventlog(bot))