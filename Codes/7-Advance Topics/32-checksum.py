"""
    Important Notes::
    => when we do not have any primary key to uniquely identify something then we can create unique keys based on
       text which is called checksum
    => while creating checksum text will be considered case sensitive.
       for example::
       "pakistan" has different checksum than "Pakistan"
    => If two strings differ by even single character then both will have different checksums
    => checksum of a string will always same
"""
import hashlib


if __name__ == '__main__':
    str1 = 'pakistan'
    str2 = 'Pakistan'
    str3 = 'Pakistan Zindabad'
    str4 = 'PakistanZindabad'
    str5 = '34-A Lahore'
    str6 = '35-A Lahore'

    str1_checksum = hashlib.md5(str1.encode()).hexdigest()
    str2_checksum = hashlib.md5(str2.encode()).hexdigest()
    str3_checksum = hashlib.md5(str3.encode()).hexdigest()
    str4_checksum = hashlib.md5(str4.encode()).hexdigest()
    str5_checksum = hashlib.md5(str5.encode()).hexdigest()
    str6_checksum = hashlib.md5(str6.encode()).hexdigest()
    print(str1_checksum)
    print(str2_checksum)
    print(str3_checksum)
    print(str4_checksum)
    print(str5_checksum)
    print(str6_checksum)
