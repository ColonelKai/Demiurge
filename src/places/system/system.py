import json
from typing import Dict, List
from src.places.system import planet;

class System:
    @classmethod
    def __init__(self, name: str):
        self.name = name;
        self.planets = []
        

def sl_get_serialised(input: System):
    output = {};
    
    for p in input.planets:
        output.update(p.planet_name, planet.sl_get_serialised(p));
        
    return output;

def sl_get_deserialised(input: Dict[int, planet.Planet], name: str):
    output = System(name);
    
    for i, v in input.items():
        output.planets.append(planet.sl_get_deserialised(v, i));
    
    return output;

def save(input: System):
    with open(f"data_cont/systems/{input.name}.json", "w+") as file:
        json.dump(sl_get_serialised(input), file);

def load(name: str):
    with open(f"data_cont/systems/{name}.json", "r") as file:
        return sl_get_deserialised(json.load(file));