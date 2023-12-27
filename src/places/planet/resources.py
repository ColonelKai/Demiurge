from src.places.planet.resource_types import ResourceType


class Resource:
    @classmethod
    def __init__(self, resource_type: ResourceType, amount: int):
        self.resource_type = resource_type;
        self.amount = amount;        

class Resources:
    @classmethod
    def __init__(self):
        # create a dictionary with 0 resources for each.
        self.__resource_dict = {}
        for i in ResourceType:
            self.__resource_dict.update(i, 0);
    
    @classmethod
    def get_resource_count(self, resource_type: ResourceType):
        return self.__resource_dict.get(resource_type);
    
    @classmethod
    def set_resource_counter(self, resource_type: ResourceType, amount: int):
        self.__resource_dict.update(resource_type, amount);
    
    @classmethod
    def change_resource_count(self, resource_type: ResourceType, amount: int):
        self.__resource_dict.update(resource_type, self.__resource_dict.get(resource_type) + amount);
        


def sl_get_serialised(input: Resources) -> dict:
    dict = {}
    
    