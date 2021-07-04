
#Program to generate MD5 of string data.

import hashlib
given_string = b"HELLO, WORLD!"
given_string_2 = b"hello world!"

md5_value = hashlib.md5(given_string)
md5_value_2 = hashlib.md5(given_string_2)

print(md5_value.hexdigest())
print(md5_value_2.hexdigest())


# OUTPUT :

# 1f9bd06f0b9c061cb1079a2bc30ded89
# fc3ff98e8c6a0d3087d515c0473f8677

