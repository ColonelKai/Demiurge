from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
import discord
import os

load_dotenv()
guild=discord.Object(os.getenv('GUILD'))

def register(bot: commands.Bot):
    # Commands
    from src.cmds import (
        ping,
        gm_master
        );
    
    command_list = [
        ping.status_command,
        gm_master.GmGroup()
    ]
    
    for i in command_list:
        bot.tree.add_command(i, guild=guild);
