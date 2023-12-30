from discord import Interaction
from src.places.system import system

async def cmd_gm_create_system(self, interaction: Interaction, name: str):
    new_system = system.System(name);
    
    system.save(new_system);