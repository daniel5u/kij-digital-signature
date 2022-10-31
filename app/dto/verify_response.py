from dataclasses import dataclass


@dataclass
class VerifyResponse:
    isMatch: bool
