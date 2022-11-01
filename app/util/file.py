import os
import traceback
from constant import ENABLE_LOG
import logging


def isFileExist(path):
    return os.path.isfile(path)

def getFileName(path):
    filename = os.path.basename(path)
    name, extension = os.path.splitext(filename)
    return name

def printException(e: Exception):
    logging.critical(e)
    
    if ENABLE_LOG:
        print(f"Trace: {traceback.format_exc()}")
