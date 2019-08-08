def fact(n):
    if n <= 1:
        return 1
    sub_solution = fact(n - 1)
    solution = n * sub_solution
    return solution


def calculate_gcd(a, b):
    while b != 0:
        gcd = b
        b = a % b
        a = gcd
    return gcd


if __name__ == '__main__':
    s_1 = "asdf"
    s_2 = "asdf"
    l_1 = [1, 2, 3]
    l_2 = [1, 2, 3]
    print(l_1 == l_2)