import unittest
import sys

from testUtils.file import removeFileIfExists, isFileExists

sys.path.insert(0, 'app')
from command.generate_rsa_key_pair import GenerateRSAKeyPair
from util.hash import HashOption

from command.sign import Sign
from dto.sign_request import SignRequest
from dto.sign_response import SignResponse

from command.verify import Verify
from dto.verify_request import VerifyRequest
from dto.verify_response import VerifyResponse


KEYS = ['private_key.pem', 'public_key.pem']
PATH_TO_KEYS = './key_pair/'

PATH_TO_UNSIGNED_FILE = '../storage/hello.pdf'
PATH_TO_SIGNED_FILE = './storage/hello_SHA1.pdf'

class GenerateKeyTest(unittest.TestCase):
    def testGenerateNewRSAKeys(self):
        """
        Test generation of RSA key pairs
        """

        # 0. Clean previous keys if exist
        for key in KEYS:
            filePath = PATH_TO_KEYS + key
            removeFileIfExists(filePath)
            self.assertFalse(isFileExists(filePath))

        # 1. Generate key pair
        GenerateRSAKeyPair.do()
        for key in KEYS:
            filePath = PATH_TO_KEYS + key
            self.assertTrue(isFileExists(filePath))

class SignPdfTest(unittest.TestCase):
    def testSignSignatureToPdf(self):
        """
        Test embedding signature to pdf
        """

        #0. Clean previous signed pdf if exists
        removeFileIfExists(PATH_TO_SIGNED_FILE)
        self.assertFalse(isFileExists(PATH_TO_SIGNED_FILE)) 

        #1. Prepare SignRequest
        signRequest = SignRequest(str(HashOption.SHA1.value), PATH_TO_UNSIGNED_FILE)
        self.assertIsNone(signRequest.validate())

        #2. Sign
        signResponse = Sign.do(signRequest)
        self.assertTrue(isFileExists(PATH_TO_SIGNED_FILE))

if __name__ == '__main__':
    unittest.main()