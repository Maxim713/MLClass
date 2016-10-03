a = int(input())
b = int(input())
a2 = int(input())
b2 = int(input())

if (abs(a - a2) == 2) and (abs(b - b2) == 1) or (abs(b - b2) == 2) and (abs(a - a2) == 1):
    print("YES")
else:
    print("NO")
