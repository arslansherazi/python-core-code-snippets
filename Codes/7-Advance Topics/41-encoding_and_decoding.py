"""
    Important Points::
    => Encoding is the process of putting a sequence of characters such as letters, numbers and other special characters
       into a specialized format for efficient transmission.
    => Decoding is the process of converting an encoded format
       back into the original sequence of characters
"""
import base64


if __name__ == '__main__':
    data = 'Pakistan Zindabad'
    # encoding
    encoded_data_utf8 = data.encode()
    encoded_data_base64 = base64.b64encode(data.encode())
    print(encoded_data_utf8)
    print(encoded_data_base64)

    # decoding
    decoded_data_utf8 = encoded_data_utf8.decode()
    decoded_data_base64 = base64.b64decode(encoded_data_base64)
    print(decoded_data_utf8)
    print(decoded_data_base64.decode())
