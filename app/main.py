import hashlib
import os

from app.constant import BUFFER_SIZE, RSA_KEY_PAIR_BITS, SIGNATURE_DIR_NAME, PRIVATE_KEY_FILE_NAME, \
    PUBLIC_KEY_FILE_NAME, KEY_PAIR_DIR_NAME
from app.file_hasher import FileHasher
from crypto.rsa import PyCryptodomeRSA
from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from file_util import isFileExist, getFileName
from view.main_view import MainView, HashOption, OperationOption


class App:
    def __init__(self):
        self.view = MainView()

    def validateSignRequest(self, signRequest: SignRequest):
        if not signRequest.hashOption.isdigit():
            raise TypeError("hash algorithm option must be a number")

        if not isFileExist(signRequest.filePath):
            raise Exception("file not found")

        if not isFileExist(signRequest.privateKeyPath):
            raise Exception("private key not found")

    def hash(self, hashOption, filePath):
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

    def sign(self):
        self.view.printHashOptions()

        signRequest = self.view.getSignRequest()

        try:
            self.validateSignRequest(signRequest)
        except Exception as e:
            print(f"ERROR: {e}")
            return

        try:
            hashValue = self.hash(
                int(signRequest.hashOption),
                signRequest.filePath
            )
        except Exception as e:
            print(f"ERROR: {e}")
            return

        privateKey = PyCryptodomeRSA.importKey(signRequest.privateKeyPath)

        signature = PyCryptodomeRSA.sign(
            hashValue,
            "big",
            privateKey.d,
            privateKey.n
        )

        signaturePath = os.path.join(
            "..",
            SIGNATURE_DIR_NAME,
            f"{getFileName(signRequest.filePath)}_signature"
        )

        PyCryptodomeRSA.exportSignature(
            signature,
            signaturePath
        )

        self.view.printSignResponse(SignResponse(
            signaturePath
        ))

    def verify(self):
        pass

    def genRsaKeyPair(self, bits, dstDirPath):
        privateKey = PyCryptodomeRSA.generateKeyPair(bits)
        PyCryptodomeRSA.exportKey(
            privateKey,
            os.path.join(
                dstDirPath,
                PRIVATE_KEY_FILE_NAME
            )
        )
        PyCryptodomeRSA.exportKey(
            privateKey.public_key(),
            os.path.join(
                dstDirPath,
                PUBLIC_KEY_FILE_NAME
            )
        )
        print("\nRSA key pair generated successfully\n")

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
                self.genRsaKeyPair(RSA_KEY_PAIR_BITS,
                                   os.path.join("..", KEY_PAIR_DIR_NAME))
            else:
                print("ERROR: invalid operation option")


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
