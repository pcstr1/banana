from abc import ABC, abstractmethod
from style import Style

# 定义迭代器接口
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Style:
        pass

# 定义数据结构接口
class Data_struct(ABC):
    @abstractmethod
    def add(self, style) -> bool:
        pass

    @abstractmethod
    def pop(self) -> bool:
        pass

    @abstractmethod
    def getsize(self) -> int:
        pass   

    @abstractmethod
    def iterator(self) -> Iterator:
        pass   

class Array_style(Data_struct):
    def __init__(self, len) -> None:
        self.size = 0
        self.len = len
        self.array = [None] * len

    def add(self, style) -> bool:
        if self.size >= self.len:
            return False
        self.array[self.size] = style
        self.size += 1
        return True
    
    def pop(self) -> bool:
        if self.size == 0 or self.size >= self.len:
            return False
        self.array[self.size] = None
        self.size -= 1
        return True
    
    def getsize(self) -> int:
        return self.size
        
    def iterator(self) -> Iterator:
        return self.Array_iterator(self)
    
    class Array_iterator(Iterator):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            self.count = 0
            self.size = outer_instance.size

        def has_next(self) -> bool:
            return self.count < self.size
        
        def next(self) -> Style:
            self.count += 1
            return self.outer_instance.array[self.count - 1]