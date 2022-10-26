import hashlib
import os

from app.dto.sign_request import SignRequest
from app.dto.sign_response import SignResponse
from hash.hashlib import Hashlib
from view.main_view import MainView, CryptoHashFunctionOption, OperationOption

BUF_SIZE = 65536


class App:
    def __init__(self):
        self.view = MainView()

    def validateSignRequest(self, signRequest: SignRequest):
        if not signRequest.chfOpt.isdigit():
            raise Exception("hash algorithm option must be a number")

        if not os.path.isfile(signRequest.filePath):
            raise Exception("file not found")

    def sign(self):
        print("Hash algorithms:")
        self.view.printCryptoHashFunctionOptions()

        # get input
        signRequest = self.view.getSignRequest()

        # validate input
        try:
            self.validateSignRequest(signRequest)
        except Exception as e:
            print(f"ERROR: {e}")
            return

        chfOpt = int(signRequest.chfOpt)
        hashValue = ""

        # TODO: add more options
        if chfOpt == CryptoHashFunctionOption.SHA1.value:
            sha1 = Hashlib(BUF_SIZE, hashlib.sha1())
            hashValue = sha1.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA224.value:
            sha224 = Hashlib(BUF_SIZE, hashlib.sha224())
            hashValue = sha224.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA256.value:
            sha256 = Hashlib(BUF_SIZE, hashlib.sha256())
            hashValue = sha256.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA384.value:
            sha384 = Hashlib(BUF_SIZE, hashlib.sha384())
            hashValue = sha384.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA512.value:
            sha512 = Hashlib(BUF_SIZE, hashlib.sha512())
            hashValue = sha512.hashFile(signRequest.filePath)

        else:
            print("ERROR: invalid hash algorithm option")
            return

        # print output
        print("")
        self.view.printSignResponse(SignResponse(
            chfOpt,
            hashValue
        ))
        print("")

    def verify(self):
        pass

    def run(self):
        while True:
            print("Operations:")
            self.view.printOperations()

            operationStr = self.view.getOperation()
            if not operationStr.isdigit():
                print(f"ERROR: operation option must be a number")
                continue
            operation = int(operationStr)

            if operation == OperationOption.EXIT.value:
                return
            elif operation == OperationOption.SIGN.value:
                self.sign()
            elif operation == OperationOption.VERIFY.value:
                # TODO: implement
                self.verify()
            else:
                print("ERROR: invalid operation option")


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
