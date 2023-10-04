import numpy as np
# Define the transition probability matrix
P = np.array([[1/2, 1/4, 1/4],
              [1/3, 1/3, 1/3],
              [0, 1/2, 1/2]])
# Define the initial state X1 = 1, and the observed state X3 = 2
X1 = 1
X3 = 2
# Calculate P(X2 = 1 | X1 = 1, X3 = 2) using the Markov property
P_X2_given_X1_X3 = P[X1-1][0]  # Transition probability to state 1 from X1
# Print the result rounded to two decimal places
print(f"P(X2 = 1 | X1 = 1, X3 = 2) = {P_X2_given_X1_X3:.2f}")
