class A:
    def __init__(self, a): #here comes the value frm C class to a
        self.variable_1 = a #the value of a is assigned to variable_1
        print(f"A initialized with variable_1 = {self.variable_1}")

    def show(self):
        print(f"Method of A: variable_1 = {self.variable_1}") # accessing the value of variable_1

class B:
    def __init__(self, y):
        self.variable_2 = y
        print(f"B initialized with variable_2 = {self.variable_2}")

    def display(self):
        print(f"Method of B: variable_2 = {self.variable_2}")

class C(A, B):
    def __init__(self, ax, y1):
        A.__init__(self, y1)  # Explicitly calling A's init, and value of y1 will go into parameter of class a init (a)
        B.__init__(self, ax)  # Explicitly calling B's init,  and value of ax will go into parameter of class b init (b)
        print("C initialized")

    def show_all(self):
        self.show()     # Calls A's show()
        self.display()  # Calls B's display()
        print("Method of C")

c = C(10, 20) #10 will go to ax and 20 will go to y1
c.show_all()
