n = 12
prob = 1/n

for i in range(1, n):
    prob = prob * (n - i)/n
    #print(prob)

print(prob * 12)