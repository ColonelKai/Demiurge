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
    
    
    from src.places.planet import resource_types;
    from src.places.planet import resources;
    
    print(resources.Resources());
    
    for i in resource_types.ResourceType:
        print(i)
    
print(os.getenv('DISCORD_TOKEN'))
bot.run(os.getenv('DISCORD_TOKEN'))