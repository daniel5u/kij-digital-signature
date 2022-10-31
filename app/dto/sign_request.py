from dataclasses import dataclass
from dto.validatable import Validatable
from file_util import isFileExist


@dataclass
class SignRequest(Validatable):
    hashOption: str
    filePath: str
    privateKeyPath: str
    
    def validate(self):
        fieldNames = {
            "hashOption": "Hash algorithm option",
            "filePath": "File",
            "privateKeyPath": "Private key",
        }
        
        self.isDigit(self.hashOption, fieldNames["hashOption"])
        self.fileExists(self.filePath, fieldNames["filePath"])
        self.fileExists(self.privateKeyPath, fieldNames["privateKeyPath"])
        self.fileHasExtension(self.filePath, fieldNames["filePath"], ".pdf")
        self.fileHasExtension(self.privateKeyPath, fieldNames["privateKeyPath"], ".pem")
