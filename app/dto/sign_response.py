from dataclasses import dataclass


@dataclass
class SignResponse:
    chfOpt: int
    hashValue: str
