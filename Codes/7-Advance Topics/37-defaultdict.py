"""
    Important Points::
    => defaultdict is used to handle key not present error
    => if key is not present in defaultdict then it will be created with default value
    => if we access a key which is not present in defaultdict using get function then it will not created and returns
       None
"""
from collections import defaultdict


if __name__ == "__main__":
    # specifying default value using lambda function
    dd1 = defaultdict(lambda: 'default value')
    dd1['name'] = 'Arslan Haider Sherazi'
    dd1['age'] = 25
    print(dd1.get('name'))
    print(dd1.get('age'))
    print(dd1['cgpa'])
    print(dd1)

    # specifying default value using builtin class (str, float, int, list, dict, set, tuple)
    print('\n\n')
    dd2 = defaultdict(float)
    dd2['name'] = 'Arslan Haider Sherazi'
    dd2['age'] = 25
    print(dd2.get('name'))
    print(dd2.get('age'))
    print(dd2['cgpa'])
    print(dd2)