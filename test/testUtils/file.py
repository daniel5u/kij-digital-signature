import os

def removeFileIfExists(filePath: str) -> None:
    try:
        os.remove(filePath)
    except OSError:
        pass

def isFileExists(filePath: str) -> bool:
    return os.path.isfile(filePath)