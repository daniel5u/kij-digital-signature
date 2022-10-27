from abc import ABC, abstractmethod


class ICryptoHashFunction(ABC):
    @abstractmethod
    def hashFile(self, path) -> bytes:
        raise NotImplementedError
