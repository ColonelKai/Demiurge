from typing import List
from src.places.system import planet;

class System:
    @classmethod
    def __init__(self, name: str, planets: List[planet.Planet]):
        self.name = name;
        self.planets = planets;