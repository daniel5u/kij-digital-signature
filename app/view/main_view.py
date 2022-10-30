from enum import Enum

from app.dto.sign_request import SignRequest
from app.dto.sign_response import SignResponse


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


class MainView:
    def __init__(self):
        self.operationOptions = {
            i.name: i.value for i in OperationOption
        }
        self.cryptoHashFunctionOptions = {
            i.name: i.value for i in HashOption
        }

    def printOperations(self):
        for key, val in self.operationOptions.items():
            print(f"[{val}] {key}")

    def printCryptoHashFunctionOptions(self):
        for key, val in self.cryptoHashFunctionOptions.items():
            print(f"[{val}] {key}")

    def getOperation(self):
        return input("Operation: ")

    def getSignRequest(self) -> SignRequest:
        hashOption = input("Algorithm: ")
        filePath = input("File path: ")
        privateKeyPath = input("Private key path: ")
        return SignRequest(hashOption, filePath, privateKeyPath)

    def printSignResponse(self, signResponse: SignResponse):
        print("")
        print(
            f"Algorithm: {HashOption(signResponse.hashOption).name}")
        print(f"Encrypted hash: {signResponse.encryptedHashValue}")
        print(f"Signature path: {signResponse.signaturePath}")
        print("")
