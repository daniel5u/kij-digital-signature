import binascii

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

# test
if __name__ == '__main__':
    privateKey = PyCryptodomeRSA.generateKeyPair(1024)
    publicKey = privateKey.public_key()

    # export private key
    PyCryptodomeRSA.exportKey(privateKey, "../../key_pair/private_key.pem")
    # export public key
    PyCryptodomeRSA.exportKey(publicKey, "../../key_pair/public_key.pem")

    importedPrivateKey = PyCryptodomeRSA.importKey("../../key_pair/private_key.pem")
    importedPublicKey = PyCryptodomeRSA.importKey("../../key_pair/public_key.pem")

    print(importedPrivateKey)
    print(importedPublicKey)

