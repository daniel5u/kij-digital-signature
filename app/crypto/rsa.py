from Crypto.PublicKey import RSA
from PyPDF2 import PdfReader, PdfWriter
from constant import SIGNATURE_METADATA_KEY


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
        reader: PdfReader = PdfReader(originPath)
        writer: PdfWriter = PdfWriter()

        # Copy pdf from origin to destination
        for page in reader.pages:
            writer.add_page(page)

        # Add metadata from origin Pdf
        writer.add_metadata(reader.metadata)

        # Add Signature metadata to Destination Pdf File
        writer.add_metadata({
            PyCryptodomeRSA.getSignatureKey(): signature
        })

        # Export Signed PDF file
        with open(destinationPath, "wb+") as f:
            writer.write(f)

    @staticmethod
    def importSignature(filePath):
        with open(filePath, "r") as f:
            hexString = f.read()
            return int(hexString, 16)
    
    @staticmethod
    def importEmbeddedSignature(filePath):
        reader = PdfReader(filePath)
        metadata = reader.metadata
        
        try:
            signature = metadata[PyCryptodomeRSA.getSignatureKey()]
            if signature is None:
                raise Exception()
        except Exception as e:
            raise Exception(f"Embedded signature isn't found in the given file")
        
        return int(signature, 16)
    
    @staticmethod
    def getSignatureKey() -> str:
        return '/' + SIGNATURE_METADATA_KEY[0].upper() + SIGNATURE_METADATA_KEY[1:]
