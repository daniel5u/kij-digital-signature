from dto.sign_request import SignRequest
from dto.sign_response import SignResponse
from hash_util import getHash, HashOption
from file_util import getFileName
from constant import SIGNATURE_DIR_NAME
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
            "./",
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