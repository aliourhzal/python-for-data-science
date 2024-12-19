class calculator:
#your code here

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        total = 0
        for i in range(len(V1)):
            total += V1[i] * V2[i]
        print(f"Dot product is: {total}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        new_vector = list([])
        for i in range(len(V1)):
            new_vector.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {new_vector}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        new_vector = list([])
        for i in range(len(V1)):
            new_vector.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is : {new_vector}")

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)