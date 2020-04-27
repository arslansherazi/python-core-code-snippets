"""
    Important Points::
    =>Dictionary contains key:value pairs of data
    =>Dictionary is unordered. The order of key:value pairs that is defined by us will not be maintained by interpreter
    =>keys can be int, float or str
    =>values can be int, float, str, list, tuple, set or dictionary
"""
if __name__ == '__main__':
    student = {
        'roll_no': 13,
        'name': 'Arslan Haider Sherazi',
        'cgpa': 3.42
    }
    print(student['name'])  # accessing dictionary value using key

    countries = {
        1: 'Pakistan',
        2: 'Iran',
        3: 'Bangladesh',
        4: 'Nepal'
    }
    print(countries[1])

    ph_levels = {
        2.2: 'Vineger',
        3.9: 'Pickles'
    }
    print(ph_levels[3.9])