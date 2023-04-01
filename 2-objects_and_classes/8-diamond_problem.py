class A:
    def output(self):
        print('Class A')


class B(A):
    def output(self):
        print('Class B')


class C(A):
    def output(self):
        print("Class C")


class D(B, C):
    def func(self):
        print('Class D')


if __name__ == '__main__':
    d = D()
    d.output()  # Class B's output() function will be called as it is class D's first parent
