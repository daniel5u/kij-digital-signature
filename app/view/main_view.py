from enum import Enum

from app.dto.sign_request import SignRequest
from app.dto.sign_response import SignResponse
from app.dto.verify_request import VerifyRequest

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
        self.hashOptions = {
            i.name: i.value for i in HashOption
        }

    def printOperations(self):
        for key, val in self.operationOptions.items():
            print(f"[{val}] {key}")

    def printHashOptions(self):
        print("Hash algorithms:")
        for key, val in self.hashOptions.items():
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
        print(f"Signature path: {signResponse.signaturePath}")
        print("")

    def getVerifyRequest(self) -> VerifyRequest:
        hashOption = input("Algorithm: ")
        filePath = input("File path: ")
        publicKeyPath = input("Public key path: ")
        signaturePath = input("Signature path: ")
        return VerifyRequest(
            hashOption,
            filePath,
            publicKeyPath,
            signaturePath
        )
