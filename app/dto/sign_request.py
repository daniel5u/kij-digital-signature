from dataclasses import dataclass
from dto.validatable import Validatable
from os.path import isabs
from constant import STORAGE_DIR_NAME
from util.hash import HashOption


@dataclass
class SignRequest(Validatable):
    hashOption: str
    filePath: str
    
    def __init__(self, hashOption: int, filePath: str):
        self.hashOption = hashOption
        self.filePath = filePath
        
        if not isabs(self.filePath):
            self.filePath = f"{STORAGE_DIR_NAME}/{filePath}"
    
    def validate(self):
        fieldNames = {
            "hashOption": "Hash algorithm option",
            "filePath": "File",
        }
        
        self.isInEnum(self.hashOption, HashOption)
        self.isDigit(self.hashOption, fieldNames["hashOption"])
        self.fileExists(self.filePath, fieldNames["filePath"])
        self.fileHasExtension(self.filePath, fieldNames["filePath"], ".pdf")
