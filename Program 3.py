
#Add salting and iterations to our hashes.

import uuid
import hashlib
 
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')


# OUTPUT :

# Please enter a password: e.g., 123456
# The string to store in the db is: 388f6ee7aa01d044e7fb3d1b1c5c17844eb9dd4a7f0a793c2d41cd1237b970c1:a852a1fcff8a4fbd91791755a3f89fda
# Now please enter the password again to check: 123456
# You entered the right password

# Please enter a password: e.g., 123456
# The string to store in the db is: 2bc4fd6d2b8c06c63a50a789c4b7b87b2df552e53773246b4eb2cb28fefcf05d:0fa50adb5e434974814878697dfba723
# Now please enter the password again to check: 12345
# I am sorry but the password does not match
