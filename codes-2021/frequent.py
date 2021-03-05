def frequency(numbers):
    res = {}
    for n in numbers:
        if res.get(n) is None:
            res[n] = 1
        else:
            res[n] += 1

    return res


print(frequency([10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]))
