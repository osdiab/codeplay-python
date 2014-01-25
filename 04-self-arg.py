class A:
    def methodOne(arg1, arg2):
        print 'arg1: {} | arg2: {}'.format(arg1, arg2)

    def methodTwo(self, arg1, arg2):
        print 'self: {} | arg1: {} | arg2: {}'.format(self, arg1, arg2)

    @staticmethod
    def staticMethodOne(arg1, arg2):
        print 'arg1: {} | arg2: {}'.format(arg1, arg2)

    @staticmethod
    def staticMethodTwo(self, arg1, arg2):
        print 'self: {} | arg1: {} | arg2: {}'.format(self, arg1, arg2)

a = A()
a.methodOne('a')
a.methodTwo('a', 'b')

A.staticMethodOne('a', 'b')
A.staticMethodTwo('a', 'b', 'c')
