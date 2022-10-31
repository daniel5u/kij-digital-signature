from enum import Enum

from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from dto.verify_request import VerifyRequest
from dto.verify_response import VerifyResponse
from hash_util import OperationOption, HashOption


class MainView:
    def __init__(self):
        self.operationOptions = {
            i.name: i.value for i in OperationOption
        }
        self.hashOptions = {
            i.name: i.value for i in HashOption
        }

    def printOperations(self):
        print("Operations:")
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
        return SignRequest(hashOption, filePath)

    def printSignResponse(self, signResponse: SignResponse):
        print("")
        print(f"Signature path: {signResponse.signaturePath}")
        print("")

    def getVerifyRequest(self) -> VerifyRequest:
        hashOption = input("Algorithm: ")
        filePath = input("File path: ")
        signaturePath = input("Signature path: ")
        return VerifyRequest(
            hashOption,
            filePath,
            signaturePath
        )
        
    def printVerifyResponse(self, verifyResponse: VerifyResponse):
        if verifyResponse.isMatch:
            print("Signature matched")
        else:
            print("Signature not matched")
            
    def printInvalidOptionDataType(self):
        print("ERROR: operation option must be a number")
            
    def printInvalidOperation(self):
        print("ERROR: invalid operation option")
        
    def printGenRSAKeyPairResponse(self):
        print("\nRSA key pair generated successfully\n")
