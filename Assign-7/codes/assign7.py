def calculate_intersection_probability(p_A, p_B):
    # Calculate the probability of the intersection of A and B
    p_intersection = p_A * p_B
    return p_intersection
# Provide the probabilities of A and B
p_A = float(input("Enter the probability of event A: "))
p_B = float(input("Enter the probability of event B: "))
# Calculate and print the probability of the intersection
result = calculate_intersection_probability(p_A, p_B)
print(f"P(A ∩ B) = {result}")
