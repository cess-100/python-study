class A(object):
    a = 0

    def __init__(self):
        self.b = 1


aa = A()
print(A.__dict__)
print(aa.__dict__)

# {'__module__': '__main__', 'a': 0, '__init__': <function A.__init__ at 0x000002B733C4FA60>,
# '__dict__': <attribute '__dict__' of 'A' objects>,
# '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# {'b': 1}
