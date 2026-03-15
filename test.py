from myhashlib import Hasher

data = "Salom, dunyo!"
hasher = Hasher(data)

print("MD5: ", hasher.hash("md5"))
print("SHA1: ", hasher.hash("sha1"))
print("SHA256: ", hasher.hash("sha256"))
print("SHA512: ", hasher.hash("sha512"))
