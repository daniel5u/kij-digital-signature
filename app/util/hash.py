from enum import Enum
from constant import BUFFER_SIZE
import hashlib


class OperationOption(Enum):
    EXIT = 0
    SIGN = 1
    VERIFY = 2
    GENERATE_RSA_KEY_PAIR = 3


class HashOption(Enum):
    SHA1 = 0
    SHA224 = 1
    SHA256 = 2
    SHA384 = 3
    SHA512 = 4


class FileHasher:
    def __init__(self, bufferSize, hashObject):
        self.bufferSize = bufferSize
        self.hashObject = hashObject

    # https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
    def hashFile(self, path):
        with open(path, "rb") as f:
            while True:
                data = f.read(self.bufferSize)
                if not data:
                    break
                self.hashObject.update(data)

        return self.hashObject.digest()


def getHash(hashOption, filePath):
    if hashOption == HashOption.SHA1.value:
        sha1 = FileHasher(BUFFER_SIZE, hashlib.sha1())
        return sha1.hashFile(filePath)
    elif hashOption == HashOption.SHA224.value:
        sha224 = FileHasher(BUFFER_SIZE, hashlib.sha224())
        return sha224.hashFile(filePath)
    elif hashOption == HashOption.SHA256.value:
        sha256 = FileHasher(BUFFER_SIZE, hashlib.sha256())
        return sha256.hashFile(filePath)
    elif hashOption == HashOption.SHA384.value:
        sha384 = FileHasher(BUFFER_SIZE, hashlib.sha384())
        return sha384.hashFile(filePath)
    elif hashOption == HashOption.SHA512.value:
        sha512 = FileHasher(BUFFER_SIZE, hashlib.sha512())
        return sha512.hashFile(filePath)
    else:
        raise Exception("invalid hash algorithm option")