import numpy as np

def CalculationOfArea(A, B, C):
    A = np.array(A)
    B = np.array(B)
    C = np.array(C)

    vectorAB = A - B
    vectorAC = A - C

    cross_product = np.cross(vectorAB, vectorAC)

    magnitude = np.linalg.norm(cross_product)

    area = 0.5 * magnitude

    return area

# Given vertices
A = [1, -1]
B = [-4, 6]
C = [-3, -5]

area_ABC = CalculationOfArea(A, B, C)
print("Area of triangle ABC:", area_ABC)
