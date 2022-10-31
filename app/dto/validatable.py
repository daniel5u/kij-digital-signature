from abc import ABC, abstractmethod

class Validatable(ABC):
    
    @abstractmethod
    def validate(self):
        pass