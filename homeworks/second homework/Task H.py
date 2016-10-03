n = int(input())
if (n % 10 == 1) and (n > 20 or n < 10):
    print(str(n) + " korova")
elif (n % 10 == 2 or n % 10 == 3 or n % 10 == 4) and (n > 20 or n < 10):
    print(str(n) + " korovy")
else:
    print(str(n) + " korov")