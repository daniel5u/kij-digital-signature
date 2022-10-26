import hashlib

from app.hash.interface import ICryptoHashFunction


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
