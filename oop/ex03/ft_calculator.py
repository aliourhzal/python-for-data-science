class calculator:

    def __init__(self, vector):
        self.vector = vector


    def __add__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)
    
    def __mul__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            return 
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
