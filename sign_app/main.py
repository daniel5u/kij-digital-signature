from abc import ABC, abstractmethod


class IHashFunction(ABC):
    @abstractmethod
    def hashFile(self, path) -> str:
        raise NotImplementedError


class KeyPair:
    pass


class MainController:
    pass


class MainView:
    pass


def main():
    print("Hello World")


if __name__ == '__main__':
    main()
