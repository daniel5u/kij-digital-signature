from dataclasses import dataclass


@dataclass
class SignResponse:
    chfOpt: int
    encryptedHashValue: str
    signaturePath: str
