def gcd(a=1, b=1):
    smaller = a
    if a > b:
        smaller = b

    res_gcd = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            res_gcd = i

    return res_gcd


gcd()
