import uuid

class Order:
    def __init__(self,
                progressed_time: int, total_time: int
                ):
        self.__order_uuid = uuid.uuid4();
        self.__progressed_time = progressed_time;
        self.__total_time = total_time;
        
    def increment_progress(self):
        self.__progressed_time += 1;
        
    def set_progress(self, value: int):
        self.__progressed_time = value;
        
    def get_progress(self):
        return self.__progressed_time;
    
    def get_order_uuid(self):
        return self.__order_uuid;