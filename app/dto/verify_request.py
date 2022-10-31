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
        fieldNames = {
            "hashOption": "Hash algorithm option",
            "filePath": "File",
            "publicKeyPath": "Public key",
            "signaturePath": "Signature",
        }
        
        self.isDigit(self.hashOption, fieldNames["hashOption"])
        self.fileExists(self.filePath, fieldNames["filePath"])
        self.fileExists(self.publicKeyPath, fieldNames["publicKeyPath"])
        self.fileExists(self.signaturePath, fieldNames["signaturePath"])
        self.fileHasExtension(self.filePath, fieldNames["filePath"], ".pdf")
        self.fileHasExtension(self.publicKeyPath, fieldNames["publicKeyPath"], ".pem")
        self.fileHasExtension(self.signaturePath, fieldNames["signaturePath"], "")
