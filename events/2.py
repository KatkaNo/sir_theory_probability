a = []
for i in range(37):
    a.append(0)

for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            a[i + j + k] += 1
            #print(i+j+k, a[i+j+k])

print("сумма : кол-во наборов")
sum = 0
for i in range(3, 37):
    print(i, ':', a[i])
    sum += a[i]

print("сумма : вероятность")
for i in range(3, 37):
    print(i, ":", a[i] / sum)