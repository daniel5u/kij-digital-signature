from dto.verify_request import VerifyRequest
from dto.verify_response import VerifyResponse
from hash_util import getHash
from crypto.rsa import PyCryptodomeRSA


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

        publicKey = PyCryptodomeRSA.importKey(verifyRequest.publicKeyPath)
        signature = PyCryptodomeRSA.importSignature(verifyRequest.signaturePath)

        isMatch = PyCryptodomeRSA.verify(
            signature,
            hashValue,
            "big",
            publicKey.e,
            publicKey.n
        )

        return VerifyResponse(isMatch)