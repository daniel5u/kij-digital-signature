from dataclasses import dataclass


@dataclass
class SignRequest:
    hashOption: str
    filePath: str
    privateKeyPath: str
