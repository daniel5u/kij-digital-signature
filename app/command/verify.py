from dto.verify_request import VerifyRequest
from dto.verify_response import VerifyResponse
from util.hash import getHash
from crypto.rsa import PyCryptodomeRSA
from constant import KEY_PAIR_DIR_NAME, PUBLIC_KEY_FILE_NAME


class Verify:
    @staticmethod
    def do(verifyRequest: VerifyRequest) -> VerifyResponse:
        try:
            hashValue = getHash(
                int(verifyRequest.hashOption),
                verifyRequest.filePath
            )
        except Exception as e:
            print(f"ERROR: {e}")
            return

        publicKeyPath = f"{KEY_PAIR_DIR_NAME}/{PUBLIC_KEY_FILE_NAME}"
        publicKey = PyCryptodomeRSA.importKey(publicKeyPath)
        signature = PyCryptodomeRSA.importSignature(verifyRequest.signaturePath)

        isMatch = PyCryptodomeRSA.verify(
            signature,
            hashValue,
            "big",
            publicKey.e,
            publicKey.n
        )

        return VerifyResponse(isMatch)