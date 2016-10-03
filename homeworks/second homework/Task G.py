a, b = int(input()), int(input())

if a == b == 0:
    print("INF")
elif not (a == 0) and (b % a == 0):
    print(-b//a)
else:
    print("NO")
