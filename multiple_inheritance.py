class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()


c = C()
print(c.prop1)
print(c.prop2)
print(c.name)