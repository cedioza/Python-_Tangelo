import hashlib 

class Encrypt:
    def __init__(self,data):
        self.data = data

    def encryptData(self):
        self.encrypt=hashlib.sha1(str.encode(self.data)).hexdigest()
        return self.encrypt