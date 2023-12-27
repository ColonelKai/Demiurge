from enum import Enum

class ResourceType(Enum):
    POPULATION = 1
    
    # Extracted Raw Materials
    ICE = 101
    IRON = 102
    RAW_TITANIUM = 103
    URANIUM = 104
    HELIUM = 105
    
    # Produced Raw Materials
    PREM_AGRI_PRODUCE = 201
    AGRI_PRODUCE = 202
    POTABLE_WATER = 203
    CARBON = 204
    TITANIUM = 205
    MANPOWER = 206
    HUMAN_NERV_SYS = 207
    HUMAN_BIOMASS = 208
    
    # Basic Products
    FOODSTUFFS = 301
    RATIONS = 302
    BOTTLED_WATER = 303
    STEEL = 304
    OX_BIOCELL = 305
    BIOCIRCUITRY = 306
    URANIUM_FUEL_CELL = 307
    
    # Components
    STRUCTURAL_BEAMS = 401
    BUILDING_MATERIALS = 402
    SPACESHIP_HULL = 403
    SHIPLUNG = 404
    BIOCOMPUTER = 405

    # Advanced Components
    SERV_STATION_PARTS = 501
    STATION_PARTS = 502
    SUPER_STATION_PARTS = 503
    
    # Advanced Products
    ARMY_SUPPLIES = 601
    LIGHT_ARMS = 602
    SHIP_SUPPLIES = 603
    INFANTRY_MECH = 604
    CAVALRY_MECH = 605
    FORTRESS_MECH = 606