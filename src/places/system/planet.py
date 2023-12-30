from enum import Enum
from typing import Dict
from src.places.planet.artifact import Artifacts
from src.nationlib import Nation
from src.places.planet import resources
from src.places.planet.wildlife import Wildlife


class PlanetType(Enum):
    STATION = 0
    
    EARTHLIKE_TROPICAL = 101
    EARTHLIKE_OCEAN = 102
    EARTHLIKE_CONTINENTAL = 103
    EARTHLIKE_FROZEN = 104
    EARTHLIKE_DESERT = 105
    EARTHLIKE_MOLTEN = 106
    EARTHLIKE_TOXIC = 107
    EARTHLIKE_ECUMENOPOLIS = 108
    GAS_GIANT = 201
    ICE_GIANT = 202
    DWARF = 301
    
    SUN = 999

class Planet:
    @classmethod
    def __init__(self, planet_name: str, planet_type: PlanetType):
        
        self.planet_name           = planet_name;
        self.planet_type           = planet_type;
        self.alleigence            = None;
        self.resources             = resources.Resources();
        self.wildlife              = Wildlife();
        self.volatility            = 0;
        self.radiation             = 0;
        self.unrest                = 0;
        self.artifacts             = Artifacts();
        self.volatility_resistance = 0;
        
def sl_get_serialised(input: Planet):
    return {
        "planet_type":input.planet_type.name,
        "volatility":input.volitility,
        "radiation":input.radiation,
        "unrest":input.unrest,
        "volatility_resistance":input.volatility_resistance,
        "resources":resources.sl_get_serialised(input.resources)
    }
    
def sl_get_deserialised(input: Dict, name: str):
    output = Planet(input["planet_type"], name);
    output.resource = resources.sl_get_deserialised(input["resources"]);
    
    output.volatility = input["volatility"];
    output.radiation = input["radiation"];
    output.unrest = input["unrest"];
    output.volatility_resistance = input["volatility_resistance"];
    
    return output;