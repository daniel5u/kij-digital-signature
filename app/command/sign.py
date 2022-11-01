import os

from constant import KEY_PAIR_DIR_NAME, PRIVATE_KEY_FILE_NAME, STORAGE_DIR_NAME
from crypto.rsa import PyCryptodomeRSA
from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from util.file import getFileName, printException
from util.hash import getHash, HashOption


class Sign:
    @staticmethod
    def do(signRequest: SignRequest) -> SignResponse:
        hashOption = int(signRequest.hashOption)
        hashValue = getHash(
            hashOption,
            signRequest.filePath
        )
        
        privateKeyPath = f"{KEY_PAIR_DIR_NAME}/{PRIVATE_KEY_FILE_NAME}"
        privateKey = PyCryptodomeRSA.importKey(privateKeyPath)

        signature = PyCryptodomeRSA.sign(
            hashValue,
            "big",
            privateKey.d,
            privateKey.n
        )
        
        signaturePath = os.path.join(
            STORAGE_DIR_NAME,
            f"{getFileName(signRequest.filePath)}_{HashOption(hashOption).name}.pdf"
        )

        PyCryptodomeRSA.embedSignatureToPdf(
            signRequest.filePath,
            signaturePath,
            signature
        )
        
        return SignResponse(
            signaturePath
        )