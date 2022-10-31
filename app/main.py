from view.main_view import MainView, OperationOption
from command.sign import Sign
from command.verify import Verify
from command.generate_rsa_key_pair import GenerateRSAKeyPair


class App:
    def __init__(self):
        self.view = MainView()

    def sign(self):
        self.view.printHashOptions()

        signRequest = self.view.getSignRequest()

        try:
            signRequest.validate()
            signResponse = Sign.do(signRequest)
        except Exception as e:
            print(f"ERROR: {e}")
            return

        self.view.printSignResponse(signResponse)

    def verify(self):
        self.view.printHashOptions()

        verifyRequest = self.view.getVerifyRequest()

        try:
            verifyRequest.validate()
            verifyResponse = Verify.do(verifyRequest)
        except Exception as e:
            print(f"ERROR: {e}")
            return
        
        self.view.printVerifyResponse(verifyResponse)

    def genRsaKeyPair(self):
        GenerateRSAKeyPair.do()
        self.view.printGenRSAKeyPairResponse()

    def run(self):
        while True:
            self.view.printOperations()

            operationStr = self.view.getOperation()
            if not operationStr.isdigit():
                self.view.printInvalidOptionDataType()
                continue
            operation = int(operationStr)

            if operation == OperationOption.EXIT.value:
                return
            elif operation == OperationOption.SIGN.value:
                self.sign()
            elif operation == OperationOption.VERIFY.value:
                self.verify()
            elif operation == OperationOption.GENERATE_RSA_KEY_PAIR.value:
                self.genRsaKeyPair()
            else:
                self.view.printInvalidOptionType()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
