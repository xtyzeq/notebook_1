class A:
    def __init__(self, x, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Moves to next in MRO
        self.variable_1 = x
        print(f"A initialized with x = {self.variable_1}")

class B:
    def __init__(self, y, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Moves to next in MRO
        self.y = y
        print(f"B initialized with y = {self.y}")

class C(A, B):
    def __init__(self, parameter_1, y1):
        super().__init__(parameter_1, y1)  # Calls A → B → object
        print("C initialized")

c = C(10, 20)
print(c.x, c.y)  # Access attributes
