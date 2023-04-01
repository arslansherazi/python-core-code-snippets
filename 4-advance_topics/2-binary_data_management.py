if __name__ == '__main__':
    #### Binary ####
    print('####Binary Conversion####')
    bin_num = input('Enter binary number::')
    # convert binary into decimal
    dec_num = int(bin_num, 2)
    print('Decimal => ', dec_num)
    # convert binary into octal
    octal_num = oct(dec_num)
    print('Octal => ', octal_num)
    # convert binary into hexa-decimal
    hex_num = hex(dec_num)
    print('Hexa-Decimal => ', hex_num)


    #### Decimal ####
    print('\n####Decimal Conversion####')
    dec_num = input('Enter decimal number::')
    # convert decimal into binary
    bin_num = bin(int(dec_num))
    print('Binary => ', bin_num)
    # convert decimal into octal
    octal_num = oct(int(dec_num))
    print('Octal => ', octal_num)
    # convert decimal into hexa-decimal
    hex_num = hex(int(dec_num))
    print('Binary => ', hex_num)


    #### Octal ####
    print('\n####Octal Conversion####')
    octal_num = input('Enter octal number::')
    # convert decimal into binary
    dec_num = int(octal_num, 8)
    bin_num = bin(dec_num)
    print('Binary => ', bin_num)
    # convert decimal into decimal
    print('Decimal => ', dec_num)
    # convert decimal into hexa-decimal
    hex_num = hex(dec_num)
    print('Hexa-Decimal => ', hex_num)


    #### Hexa Decimal ####
    print('\n####Hexa Conversion####')
    hex_num = input('Enter hexa-decimal number::')
    # convert decimal into binary
    dec_num = int(hex_num, 16)
    bin_num = bin(dec_num)
    print('Binary => ', bin_num)
    # convert decimal into decimal
    print('Decimal => ', dec_num)
    # convert decimal into octal
    octal_num = oct(dec_num)
    print('Octal => ', octal_num)
