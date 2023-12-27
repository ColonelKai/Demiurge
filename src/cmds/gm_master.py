import discord
from discord import Interaction, app_commands
from discord.ext import commands


gamemaster_role_id = 1189524504838406154;
    
gm_group = app_commands.Group(name="gm", description="Commands to be used by GMs.");

@gm_group.command(name="test")
async def test(interaction: Interaction):
    if(not interaction.guild.get_role(gamemaster_role_id) in interaction.user.roles):
        await interaction.response.send_message("You must have the `Game Master` role to use GameMaster commands.", ephemeral=True);
        return;