from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from util.hash import getHash, HashOption
from util.file import getFileName, printException
from constant import SIGNATURE_DIR_NAME, KEY_PAIR_DIR_NAME, PRIVATE_KEY_FILE_NAME
from crypto.rsa import PyCryptodomeRSA
import os


class Sign:
    @staticmethod
    def do(signRequest: SignRequest) -> SignResponse:
        hashOption = int(signRequest.hashOption)
        try:
            hashValue = getHash(
                hashOption,
                signRequest.filePath
            )
        except Exception as e:
            printException(e)
            return
        
        privateKeyPath = f"{KEY_PAIR_DIR_NAME}/{PRIVATE_KEY_FILE_NAME}"
        privateKey = PyCryptodomeRSA.importKey(privateKeyPath)

        signature = PyCryptodomeRSA.sign(
            hashValue,
            "big",
            privateKey.d,
            privateKey.n
        )
        
        signaturePath = os.path.join(
            SIGNATURE_DIR_NAME,
            f"{getFileName(signRequest.filePath)}_{HashOption(hashOption).name}"
        )

        PyCryptodomeRSA.exportSignature(
            signature,
            signaturePath
        )
        
        return SignResponse(
            signaturePath
        )