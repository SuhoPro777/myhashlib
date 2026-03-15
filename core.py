import hashlib

class Hasher:
    """Ma'lumotni hash qilish uchun sinf"""

    def __init__(self, data: str):
        self.data = data.encode('utf-8')

    def hash(self, algorithm: str = 'sha256') -> str:
        """Hash algoritmini tanlang: md5, sha1, sha256, sha512"""
        algorithmn = algorithm.lower()
        try:
            h = getattr(hashlib, algorithm)()
        except AttributeError:
            raise ValueError(f"Algorithm '{algorithm}' not supported")

        h.update(self.data)
        return h.hexdigest()