class A:
    def public_method(self):
        print 'hello!'

    def __private_method(self):
        return 'wow!'

    def public_method_calls_private(self):
        print 'such {}'.format(self.__private_method())

a = A()
a.public_method()
a.public_method_calls_private()
print 'hack: {}'.format(a._A__private_method())
