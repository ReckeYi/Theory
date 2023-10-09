class Parent1:
    def __init__(self):
        super().__init__()
        self.smart = "smart"
        self.hair_color = "light"


class Parent2:
    def __init__(self):
        super().__init__()
        self.pretty = "pretty"
        self.hair_color = "Dark"


class Child(Parent2, Parent1):
    def __init__(self):
        super().__init__()

    def traits(self):
        print(self.smart)
        print(self.pretty)
        print(self.hair_color)


child = Child()
child.traits()
