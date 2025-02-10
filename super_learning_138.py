class A:
    def __init__(self, x, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Moves to next in MRO
        self.variable_1 = x
        print(f"A initialized with x = {self.variable_1}")

class B:
    def __init__(self, y, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Moves to next in MRO
        self.variable_2 = y
        print(f"B initialized with y = {self.variable_2}")

class C(B, A): # yaha par again position B will fetch the value of x, and A will fetch the value of y1
    def __init__(self, y1, x): # 10 gya y1 and 20 gya x "call by position"
        super().__init__(x, y1)  # yaha par no positon, call by name 
        print("C initialized")

c = C(10, 20) # value 10 goes to y and 20 goes to x
print(c.variable_1, c.variable_2)  # Access attributes
