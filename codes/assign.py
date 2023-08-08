import numpy as np
 
def AreaCalc(A, B, C):
    AB = A - B
    AC = A - C
#cross_product calculation
    cross_product = np.cross(AB,AC)
#magnitude calculation
    magnitude = np.linalg.norm(cross_product)

    area = 0.5 * magnitude

    return area

# Given vertices
A = np.array([1,-1])
B = np.array([-4,6])
C = np.array([-3,-5])
area_ABC = AreaCalc(A, B, C)
print("Area of triangle ABC:", area_ABC)
