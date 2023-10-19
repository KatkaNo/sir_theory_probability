month_a = 2
month_all = 12
summa = month_a / month_all
n = 1
prev_sob = 1
while summa < 0.99:
    n += 1
    prev_sob *= (1 - month_a/month_all)
    summa += month_a / month_all * prev_sob
    print("n = {}, ver = {}".format(n, summa))