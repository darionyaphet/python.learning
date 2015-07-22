import hashlib

hash = hashlib.md5()
hash.update("darion.johannes.yaphet")

hash.digest()
print hashlib.new("md5", "darion.johannes.yaphet").hexdigest()

