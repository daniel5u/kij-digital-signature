class FileHasher:
    def __init__(self, bufferSize, hashObject):
        self.bufferSize = bufferSize
        self.hashObject = hashObject

    # https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
    def hashFile(self, path):
        with open(path, 'rb') as f:
            while True:
                data = f.read(self.bufferSize)
                if not data:
                    break
                self.hashObject.update(data)

        return self.hashObject.digest()
