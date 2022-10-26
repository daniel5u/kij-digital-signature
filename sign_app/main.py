from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
import hashlib
import os

BUF_SIZE = 65536


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


class SHA256(ICryptoHashFunction):
    def __init__(self, bufferSize):
        self.bufferSize = bufferSize

    # https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
    def hashFile(self, path):
        sha256 = hashlib.sha256()

        with open(path, 'rb') as f:
            while True:
                data = f.read(self.bufferSize)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()


class KeyPair:
    pass


@dataclass
class InputData:
    chfOpt: str
    filePath: str


@dataclass
class OutputData:
    chfOpt: str
    hashValue: str


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
        filePath = input("File path: ")
        return InputData(chfOpt, filePath)

    def printOutput(self, outputData: OutputData):
        print(f"Algorithm: {CryptoHashFunctionOption(outputData.chfOpt).name}")
        print(f"Hash: {outputData.hashValue}")


class SignApp:
    def __init__(self):
        self.view = MainView()

    def validateInput(self, inputData: InputData):
        if not inputData.chfOpt.isdigit():
            raise Exception("Hash algorithm option must be a number")

        if not os.path.isfile(inputData.filePath):
            raise Exception("File not found")

    def run(self):
        while True:
            print("Hash algorithms:")
            self.view.printCryptoHashFunctionOptions()
            inputData = self.view.getInput()
            isInputValid = True

            try:
                self.validateInput(inputData)
            except Exception as e:
                print(f"ERROR: {e}")
                isInputValid = False

            if not isInputValid:
                continue

            chfOpt = int(inputData.chfOpt)

            hashValue = ""

            if chfOpt == CryptoHashFunctionOption.SHA256.value:
                sha256 = SHA256(BUF_SIZE)
                hashValue = sha256.hashFile(inputData.filePath)

            print("")

            self.view.printOutput(OutputData(
                chfOpt,
                hashValue
            ))

            print("")


def main():
    app = SignApp()
    app.run()


if __name__ == '__main__':
    main()
