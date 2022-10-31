import os


def isFileExist(path):
    return os.path.isfile(path)

def getFileName(path):
    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)
    return name
