"""
    Important Points::
    => The salt is a randomly generated string that is joined with the password before hashing
    => The cost factor increases security by slowing down the hashing
    => The bcrypt algorithm only handles passwords up to 72 characters, any characters beyond that are ignored
    => cipher text is the encrypted text
    => plain text is the original text / decrypted text
    => AES is symmetric algorithm which use single key to encrypt and decrypt data
"""
import base64
import hashlib

import bcrypt
from cryptography.fernet import Fernet


if __name__ == '__main__':
    # simple encryption & decryption
    data = 'Pakistan Zindabad'
    secret_key = Fernet.generate_key()
    cipher_suite = Fernet(secret_key)
    cipher_text = cipher_suite.encrypt(data.encode())
    plain_text = cipher_suite.decrypt(cipher_text)
    print('Secret Key::', secret_key.decode())
    print('Cipher Text::', cipher_text.decode())
    print('Plain Text::', plain_text.decode())

    # encrypt and decrypt password using salt
    password = b'markboucher34'
    salt = bcrypt.gensalt(rounds=10)  # rounds is used to define cost for generating salt. default = 12
    hashed_password = bcrypt.hashpw(password, salt)
    print('Hashed Password::', hashed_password)
    if bcrypt.checkpw(password, hashed_password):
        print('Password matched')
    else:
        print('Password is invalid')

    # encrypt and decrypt long passwords
    password = b'uythndfer45wsed89765432aqwszxcvfredthyhswaqswertyuiokjhnbgdeswertcgbfdertyuj890qa'
    salt = bcrypt.gensalt()
    encoded_password = base64.b64encode(hashlib.sha256(password).digest())
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    print('Hashed Password::', hashed_password)
    if bcrypt.checkpw(encoded_password, hashed_password):
        print('Password matched')
    else:
        print('Password is invalid')

    # generate password hash using secret key
    password = 'Pakistan123456'
    password_hash_key = 'hh%%as3!!@89ujh$$%^11PPDD&&))@@hujnb345'
    password_hash = hashlib.pbkdf2_hmac(
        hash_name='sha256',
        password=password.encode(),
        salt=password_hash_key.encode(),
        iterations=10000
    )
    print('Password::', password)
    print('Password Hash::', password_hash)

