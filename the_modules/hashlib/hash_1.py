import hashlib

m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
