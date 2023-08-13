import numpy as np

# Define a matrix with P, Q, and R as row vectors
P = np.array([1, 1, 1])
Q = np.array([1, -4, -3])
R = np.array([-1, 6, -5])

# Create the matrix
matrix = np.vstack((P, Q, R))

# Calculating the rank of the matrix
rank = np.linalg.matrix_rank(matrix)

# Check if the points are collinear
if rank == 2:
    print("The points A, B, and C are collinear.")
else:
    print("The points A, B, and C are not collinear.")
