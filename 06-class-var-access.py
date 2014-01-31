class A:
    _CONSTANT_VARIABLE = 5

    def foo(self):
        print 'self: {}'.format(self._CONSTANT_VARIABLE)
        print 'class: {}'.format(A._CONSTANT_VARIABLE)

a = A()
a.foo()
