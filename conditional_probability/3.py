B = 0
A = 0
C = 0
AB = 0
AC = 0
BC = 0
ABC = 0
ALL = 12**2
for i in range(1, 13):
    for j in range(1, 13):
        A_res = i % 2
        B_res = j % 2
        C_res = (i + j) % 2
        A += A_res
        B += B_res
        C += C_res
        AB += A_res * B_res
        AC += A_res * C_res
        BC += B_res * C_res
        ABC += A_res * B_res * C_res
print("Кол-во случаев:\nA = {}, B = {}, C = {}, AB = {}, AC = {}, BC = {}, ABC = {}".format(A, B, C, AB, AC, BC, ABC))