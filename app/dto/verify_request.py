from dataclasses import dataclass
from dto.validatable import Validatable
from file_util import isFileExist


@dataclass
class VerifyRequest(Validatable):
    hashOption: str
    filePath: str
    publicKeyPath: str
    signaturePath: str
    
    def validate(self):
        if not self.hashOption.isdigit():
            raise TypeError("hash algorithm option must be a number")

        if not isFileExist(self.filePath):
            raise Exception("file not found")

        if not isFileExist(self.publicKeyPath):
            raise Exception("public key not found")

        if not isFileExist(self.signaturePath):
            raise Exception("signature not found")
