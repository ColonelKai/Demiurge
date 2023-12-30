from discord import Interaction
from places.system import system
from src.cmds.gm_master import GmGroup;



@gm_group.command(name="create_system")
async def cmd_gm_create_system(interaction: Interaction, name: str):
    new_system = system.System(name);
    
    system.save(new_system);
    
    