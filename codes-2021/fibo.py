def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(i, a)
        a, b = b, a + b


print(fib(5))


