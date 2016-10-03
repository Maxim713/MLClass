def sum_factorials(i):
    """
    :param i:
    :return sum of factorials:
    """
    sum_total, factorial_cur = 0, 1
    for x in range(1, i + 1):
        factorial_cur *= x
        sum_total += factorial_cur
    return sum_total

n = int(input())
print(sum_factorials(n))

