from abc import ABC,abstractmethod

class MyClass(ABC):
    @abstractmethod
    def start_engine(self):
        print('parent,..')
    @property
    @abstractmethod
    def rate(self):
        pass
        
    
    
class Move(MyClass):
    
    def __init__(self,r):
        self.r = r
        
    def start_engine(self):
        super().start_engine()
        print('its startinggggg')
    
    def accelerate(self):
        print('moving.....')

    @property
    def rate(self):

        return self.r * 2
        
p = Move(4)
p.start_engine()
p.accelerate()
print(p.rate)




