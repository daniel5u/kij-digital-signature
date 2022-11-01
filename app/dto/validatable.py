from abc import ABC, abstractmethod
from os.path import exists

class Validatable(ABC):
    
    @abstractmethod
    def validate(self):
        pass
    
    def isDigit(self, x, varName: str):
        if not x.isdigit():
            raise TypeError(f"{varName} must be a number")
        
    def fileExists(self, filePath: str, varName: str):
        if not exists(filePath):
            raise Exception(f"{varName} not found")
        
    def fileHasExtension(self, filePath: str, varName: str, extension: str):
        if not filePath.endswith(extension):
            raise Exception(f"{varName} extension isn't equal to '{extension}'")

    def isInEnum(self, varName: int, container):
        values = set(item.value for item in container)

        if int(varName) not in values:
            raise Exception(f"{varName} is not a valid {container} value")