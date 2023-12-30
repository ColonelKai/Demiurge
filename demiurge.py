from discord.ext import commands
from discord import app_commands
from src.data import general_state_data;
from dotenv import load_dotenv
from src.cmds import registry
import asyncio
import discord
import os


load_dotenv()
intents = discord.Intents.default();
intents.message_content = True;

bot = commands.Bot(intents=intents, command_prefix="du$")

@bot.event
async def on_ready():
    registry.register(bot);
    await bot.tree.sync(guild=discord.Object(os.getenv('GUILD')));
    print("Ready to Go.");
  
    
bot.run(os.getenv('DISCORD_TOKEN'))