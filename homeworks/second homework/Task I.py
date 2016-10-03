a, b, c, d = int(input()), int(input()), int(input()), int(input())

for x in range(0, 1001):
    if a*x*x*x + b*x*x + c*x + d == 0:
        print(x)
