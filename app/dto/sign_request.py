from dataclasses import dataclass
from dto.validatable import Validatable
from file_util import isFileExist


@dataclass
class SignRequest(Validatable):
    hashOption: str
    filePath: str
    privateKeyPath: str
    
    def validate(self):
        if not self.hashOption.isdigit():
            raise TypeError("hash algorithm option must be a number")

        if not isFileExist(self.filePath):
            raise Exception("file not found")

        if not isFileExist(self.privateKeyPath):
            raise Exception("private key not found")
