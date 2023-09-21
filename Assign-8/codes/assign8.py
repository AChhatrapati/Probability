from scipy.stats import binom
# Total number of questions
n = 20
# Probability of getting a question correct (heads)
p = 0.5
# Calculate the probability of answering at least 12 questions correctly
probability = 1 - binom.cdf(11, n, p)
print(f"The probability of answering at least 12 questions correctly is {probability:.4f}")

