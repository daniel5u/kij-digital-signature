from Crypto.PublicKey import RSA
from PyPDF2 import PdfReader, PdfWriter

class PyCryptodomeRSA:
    @staticmethod
    def generateKeyPair(bits):
        return RSA.generate(bits=bits)

    @staticmethod
    def exportKey(rsaKey, filePath):
        with open(filePath, "wb+") as f:
            f.write(rsaKey.exportKey("PEM"))

    @staticmethod
    def importKey(filePath):
        with open(filePath, "rb") as f:
            return RSA.importKey(f.read())

    # https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
    @staticmethod
    def sign(digest, byteorder, d, n):
        hash = int.from_bytes(digest, byteorder=byteorder)
        signature = pow(hash, d, n)
        return hex(signature)

    @staticmethod
    def verify(signature, digest, byteorder, e, n):
        hash = int.from_bytes(digest, byteorder=byteorder)
        hashFromSignature = pow(signature, e, n)
        return hash == hashFromSignature

    @staticmethod
    def exportSignature(signature, filePath):
        with open(filePath, "w+") as f:
            f.write(signature)

    # https://pypdf2.readthedocs.io/en/latest/user/metadata.html
    @staticmethod
    def embedSignatureToPdf(
        originPath: str,
        destinationPath: str,
        signature: str
    ):
        # TODO refactor this as constant, verify gonna need it
        SIGNATURE_METADATA_KEY = "/Signature"

        reader: PdfReader = PdfReader(originPath)
        writer: PdfWriter = PdfWriter()

        # Copy pdf from origin to destination
        for page in reader.pages:
            writer.addPage(page)

        # Add metadata from origin Pdf
        writer.addMetadata(reader.getDocumentInfo())

        # Add Signature metadata to Destination Pdf File
        writer.add_metadata({
            SIGNATURE_METADATA_KEY: signature
        })

        # Export Signed PDF file
        with open(destinationPath, "wb+") as f:
            writer.write(f)


    @staticmethod
    def importSignature(filePath):
        with open(filePath, "r") as f:
            hexString = f.read()
            return int(hexString, 16)