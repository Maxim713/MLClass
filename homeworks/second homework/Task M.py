t10, t1 = 0, 0
n = int(input())
t60 = n // 60
n %= 60
if n > 34:
    t60 += 1
else:
    t10 = n // 10
    n %= 10
    if n > 8:
        t10 += 1
    else:
        t1 = n
print(str(t1) + " " + str(t10) + " " + str(t60))
