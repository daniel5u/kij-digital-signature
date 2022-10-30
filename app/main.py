import hashlib
import os

from app.constant import BUFFER_SIZE, RSA_KEY_PAIR_BITS, SIGNATURE_DIR_NAME, PRIVATE_KEY_FILE_NAME, \
    PUBLIC_KEY_FILE_NAME, KEY_PAIR_DIR_NAME
from crypto.rsa import PyCryptodomeRSA
from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from file_util import isFileExist, getFileName
from hash.hashlib import Hashlib
from view.main_view import MainView, CryptoHashFunctionOption, OperationOption


class App:
    def __init__(self):
        self.view = MainView()

    def validateSignRequest(self, signRequest: SignRequest):
        if not signRequest.chfOpt.isdigit():
            raise Exception("hash algorithm option must be a number")

        if not isFileExist(signRequest.filePath):
            raise Exception("file not found")

        if not isFileExist(signRequest.privateKeyPath):
            raise Exception("private key not found")

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
            sha1 = Hashlib(BUFFER_SIZE, hashlib.sha1())
            hashValue = sha1.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA224.value:
            sha224 = Hashlib(BUFFER_SIZE, hashlib.sha224())
            hashValue = sha224.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA256.value:
            sha256 = Hashlib(BUFFER_SIZE, hashlib.sha256())
            hashValue = sha256.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA384.value:
            sha384 = Hashlib(BUFFER_SIZE, hashlib.sha384())
            hashValue = sha384.hashFile(signRequest.filePath)

        elif chfOpt == CryptoHashFunctionOption.SHA512.value:
            sha512 = Hashlib(BUFFER_SIZE, hashlib.sha512())
            hashValue = sha512.hashFile(signRequest.filePath)

        else:
            print("ERROR: invalid hash algorithm option")
            return

        name = getFileName(signRequest.filePath)

        privateKey = PyCryptodomeRSA.importKey(signRequest.privateKeyPath)
        signature = PyCryptodomeRSA.sign(
            hashValue,
            'big',
            privateKey.d,
            privateKey.n
        )
        signatureFilename = f"{name}_signature"
        signaturePath = os.path.join("..", SIGNATURE_DIR_NAME, signatureFilename)
        PyCryptodomeRSA.exportSignature(
            signature,
            signaturePath
        )

        # print output
        print("")
        self.view.printSignResponse(SignResponse(
            chfOpt,
            signature,
            signaturePath
        ))
        print("")

    def verify(self):
        pass

    def genKeyPair(self, bits, dstDirPath):
        privateKey = PyCryptodomeRSA.generateKeyPair(bits)
        PyCryptodomeRSA.exportKey(privateKey, os.path.join(dstDirPath, PRIVATE_KEY_FILE_NAME))
        PyCryptodomeRSA.exportKey(privateKey.public_key(), os.path.join(dstDirPath, PUBLIC_KEY_FILE_NAME))
        print("")
        print("RSA key pair generated successfully")
        print("")

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
            elif operation == OperationOption.GENERATE_RSA_KEY_PAIR.value:
                self.genKeyPair(RSA_KEY_PAIR_BITS, os.path.join("..", KEY_PAIR_DIR_NAME))
            else:
                print("ERROR: invalid operation option")


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
