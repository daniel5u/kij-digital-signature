from dataclasses import dataclass


@dataclass
class VerifyRequest:
    hashOption: str
    filePath: str
    publicKeyPath: str
    signaturePath: str
