"""
    Important Points::
    => Monkey patching refers to dynamic (or run-time) modifications of a class or module.
    => In Python, we can change the behavior of code at run-time.
"""


class A:
    def func(self):
        print('func in class A')


class B:
    def monk_func(self):
        print('func in class B')


if __name__ == '__main__':
    a = A()
    a.func()

    # monkey patching
    A.func = B.monk_func
    obj = A()
    obj.func()