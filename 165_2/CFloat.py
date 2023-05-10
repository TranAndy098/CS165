from dataclasses import dataclass
import sys

@dataclass
class CFloat:
    val: float

    def __eq__(self, other) -> bool:
        return abs(self.val - other.val) <= sys.float_info.epsilon
    
    def __lt__(self, other) -> bool:
        return not (self == other) and self.val < other.val
    
    def __le__(self,other):
        return self.__eq__(other) or self.__lt__(other)
    
    def __gt__(self, other) -> bool:
        return not (self == other) and self.val > other.val
    
    def __ge__(self,other):
        return self.__eq__(other) or self.__gt__(other)