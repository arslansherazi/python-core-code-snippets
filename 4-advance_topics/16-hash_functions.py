"""
    Important Points::
    * variable_length_input => hash function => fixed_length_output
    * same hash value will be generated for same input on every run
"""
import hashlib


if __name__ == '__main__':
    password = input('Enter Password::')

    # MD5
    hashed_password_md5_object = hashlib.md5(password.encode('utf-8'))
    print(hashed_password_md5_object.hexdigest())

    # SH1
    hashed_password_sh1_object = hashlib.sha1(password.encode('utf-8'))
    print(hashed_password_sh1_object.hexdigest())

    # SHA224
    hashed_password_sha224_object = hashlib.sha224(password.encode('utf-8'))
    print(hashed_password_sha224_object.hexdigest())

    # SHA256
    hashed_password_sha256_object = hashlib.sha256(password.encode('utf-8'))
    print(hashed_password_sha256_object.hexdigest())

    # SHA384
    hashed_password_sha384_object = hashlib.sha384(password.encode('utf-8'))
    print(hashed_password_sha384_object.hexdigest())

    # SHA512
    hashed_password_sha512_object = hashlib.sha512(password.encode('utf-8'))
    print(hashed_password_sha512_object.hexdigest())