if __name__ == '__main__':
    # list as value
    data = {
        'name': 'Arslan Haider Sherazi',
        'marks': [708, 905, 930, 3.42]
    }
    print(data['marks'][0])  # 0 = index of list
    for m in data['marks']:
        print(m, end=" ")

    # dictionary as value (dictionary of dictionary)
    data = {
        'category': 'Chemicals',
        'ph_levels': {
            'Vinegar': 2.2,
            'Tomatoes': 4.5
        }
    }
    print('\n')
    print(data['ph_levels']['Vinegar'])
    for chemical, ph_level in data['ph_levels'].items():
        print(chemical, ph_level)