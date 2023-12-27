from src.data import general_state_data;
from discord import Interaction;
from discord import app_commands;
import discord;

@app_commands.command(
    name="status",
    description="Checks if the bot is up, and it's general status.")
async def status_command(interaction: discord.Interaction):
    embed=discord.Embed(title="Demiurge Status", description="Checks if the bot is up, and it's general status.", color=0x00ff1e)
    embed.add_field(name= "Ping", value=interaction.client.latency + " ms", inline = False);
    embed.add_field(name="Read-Only  Mode", value=str(general_state_data.load_readonlystate().name).capitalize(), inline=False)
    await interaction.response.send_message(embed=embed)
