import discord
from discord import Interaction, app_commands
from discord.ext import commands

from src.cmds.gm_commands.gm_system import cmd_gm_create_system


gamemaster_role_id = 1189524504838406154;

@app_commands.guild_only()
class GmGroup(app_commands.Group):
    
  # top group commands 
    @app_commands.command(name="test")
    async def test(self, interaction: Interaction):
        if(not interaction.guild.get_role(gamemaster_role_id) in interaction.user.roles):
            await interaction.response.send_message("You must have the `Game Master` role to use GameMaster commands.", ephemeral=True);
            return;
        
        
  # nested group commands
    system_group = app_commands.Group(name="system", description="For GMing systems.")
    
    @system_group.command(name="create")
    async def cmd_gm_create_system(self, interaction: Interaction, name: str):
        return await cmd_gm_create_system(self, interaction, name);