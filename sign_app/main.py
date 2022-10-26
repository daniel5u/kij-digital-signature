from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class CryptoHashFunctionOption(Enum):
    SHA1 = 0
    SHA224 = 1
    SHA256 = 2
    SHA384 = 3
    SHA512 = 4


class ICryptoHashFunction(ABC):
    @abstractmethod
    def hashFile(self, path) -> str:
        raise NotImplementedError


class KeyPair:
    pass


class MainController:
    pass


@dataclass
class InputData:
    chfOpt: str
    path: str


class MainView:
    def __init__(self):
        self.cryptoHashFunctionOptions = {
            i.name: i.value for i in CryptoHashFunctionOption
        }

    def printCryptoHashFunctionOptions(self):
        for key, val in self.cryptoHashFunctionOptions.items():
            print(f"[{val}] {key}")

    def getInput(self) -> InputData:
        chfOpt = input("Algorithm: ")
        path = input("File path: ")
        return InputData(chfOpt, path)


class SignApp:
    def __init__(self):
        self.view = MainView()

    def run(self):
        while True:
            print("Hash algorithms:")
            self.view.printCryptoHashFunctionOptions()
            input = self.view.getInput()
            print("")


def main():
    app = SignApp()
    app.run()


if __name__ == '__main__':
    main()
