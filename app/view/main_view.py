from enum import Enum
import logging

from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from dto.verify_request import VerifyRequest
from dto.verify_response import VerifyResponse
from util.hash import OperationOption, HashOption


class MainView:
    def __init__(self):
        self.operationOptions = {
            i.name: i.value for i in OperationOption
        }
        self.hashOptions = {
            i.name: i.value for i in HashOption
        }
        logging.basicConfig(format="%(levelname)s: %(message)s")

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
        logging.error("operation option must be a number")
            
    def printInvalidOperation(self):
        logging.error("invalid operation option")
        
    def printGenRSAKeyPairResponse(self):
        logging.info("\nRSA key pair generated successfully\n")
