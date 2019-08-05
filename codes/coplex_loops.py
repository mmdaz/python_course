# numbers = [n ** 2 for n in range(20)]

numbers = [(n, n**2, n**3) for n in range(10) if n % 2 == 0]

print(numbers)