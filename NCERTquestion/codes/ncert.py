# Given probabilities
# P(hindi) = P_H
# P(english) = P_E

P_H = 0.60
P_E = 0.40
P_both = 0.20

# (a) Probability that she reads neither Hindi nor English newspapers
P_neither = 1 - (P_H + P_E - P_both)
print("(a) Probability that she reads neither Hindi nor English newspapers:", P_neither)

# (b) Probability that she reads English newspaper given that she reads Hindi newspaper=P_E_H
P_E_H = P_both / P_H
print("(b) Probability that she reads English newspaper given Hindi newspaper:", P_E_H)

# (c) Probability that she reads Hindi newspaper given that she reads English newspaper=P_H_E
P_H_E = P_both / P_E
print("(c) Probability that she reads Hindi newspaper given English newspaper:", P_H_E)

