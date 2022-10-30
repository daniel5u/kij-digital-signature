from Crypto.PublicKey import RSA

class PyCryptodomeRSA:
    @staticmethod
    def generateKeyPair(bits):
        return RSA.generate(bits=bits)

    @staticmethod
    def exportKey(rsaKey, filePath):
        with open(filePath, "wb") as f:
            f.write(rsaKey.exportKey("PEM"))

    @staticmethod
    def importKey(filePath):
        with open(filePath, "r") as f:
            return RSA.importKey(f.read())

    # https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
    @staticmethod
    def sign(digest, byteorder, d, n):
        hash = int.from_bytes(digest, byteorder=byteorder)
        signature = pow(hash, d, n)
        return hex(signature)

    # TODO: check if this is correct
    @staticmethod
    def exportSignature(signature, filePath):
        with open(filePath, "w") as f:
            f.write(signature)

