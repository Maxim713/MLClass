n, m, k = int(input()), int(input()), int(input())
print("YES" if ((k % n == 0) or (k % m == 0)) and (k <= n*m) else "NO")
