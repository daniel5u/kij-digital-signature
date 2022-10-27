from dataclasses import dataclass


@dataclass
class SignRequest:
    chfOpt: str
    filePath: str
    privateKeyPath: str
