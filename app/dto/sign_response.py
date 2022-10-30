from dataclasses import dataclass


@dataclass
class SignResponse:
    hashOption: int
    encryptedHashValue: str
    signaturePath: str
