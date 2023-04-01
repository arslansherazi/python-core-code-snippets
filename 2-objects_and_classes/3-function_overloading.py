"""
    Important Points::
    =>Python does not support function overloading
    =>If we define multiple functions with same name and different no of parameters then only the latest
      defined function can be called
    =>We can achieve function overloading using **kwargs or *args
"""


class Sum:
    sum = 0
    concat = ''

    def calculate_sum(self, data_type, *args):
        if data_type == 'int':
            for n in args:
                self.sum += n
            return self.sum
        elif data_type == 'str':
            for s in args:
                self.concat = self.concat + ' ' + s
            return self.concat


if __name__ == '__main__':
    obj = Sum()
    result = obj.calculate_sum('int', 2, 5, 7)
    print('Sum::', result)

    result = obj.calculate_sum('str', 'Arslan', 'Haider', 'Sherazi')
    print('Concatenation::', result)


