a, b, c = int(input()), int(input()), int(input())

if a >= b:
    a, b = b, a
if b >= c:
    c, b = b, c
if a >= b:
    a, b = b, a

print(str(a) + " " + str(b) + " " + str(c))
