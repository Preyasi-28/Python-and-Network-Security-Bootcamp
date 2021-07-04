
#Program to generate hashes of string data using three agorithms from hishlib.

#Using MD5:

import hashlib
h = hashlib.md5(b"HELLO WORLD!")
print(h.hexdigest())

#Using SHA1:

import hashlib
h = hashlib.sha1(b"HELLO WORLD!")
hex_dig = h.hexdigest()
print(hex_dig)

#Using OPENSSL:

import hashlib
h = hashlib.new("ripemd160")
h.update(b"HELLO WORLD!")
h.hexdigest()
print(h.hexdigest())


# OUTPUT :

# b59bc37d6441d96785bda7ab2ae98f75
# 9cf278fa132bb5c546c2f45f50d7ce7edd2cfe43
# 11facc95bf546e87a79708950c3e9dff15c29368
