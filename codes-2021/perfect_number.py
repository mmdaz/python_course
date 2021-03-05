def is_prefect(n):
    tot = 0
    while n > 0:
        dig = n % 10
        tot = tot + dig
        n = n // 10
    print("The total sum of digits is:", tot)
    if tot == n:
        return True
    else:
        return False


is_prefect(12)
