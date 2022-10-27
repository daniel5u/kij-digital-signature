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
        f = open(filePath, "r")
        return RSA.importKey(f.read())

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

