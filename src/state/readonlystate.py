
from enum import Enum

class ReadOnlyTypes(Enum):
    OFF = 0
    ON_NORMAL = 1
    STRICT = 2
    
st_read_only = ReadOnlyTypes.OFF;
