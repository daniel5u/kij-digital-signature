from dataclasses import dataclass
from dto.validatable import Validatable
from util.file import isFileExist
from os.path import isabs
from constant import STORAGE_DIR_NAME


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
        
        self.isDigit(self.hashOption, fieldNames["hashOption"])
        self.fileExists(self.filePath, fieldNames["filePath"])
        self.fileHasExtension(self.filePath, fieldNames["filePath"], ".pdf")
