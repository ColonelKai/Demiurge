import json;

def __load():
    with open("data_cont/general_state_data.json", "r") as file:
        return json.load(file);

def load_readonlystate():
    from src.state import readonlystate;

    return  readonlystate.ReadOnlyTypes(__load()["read_only"])