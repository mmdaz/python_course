n = int(input())

digit_sum = 0

while n > 0:
    dig = n % 10
    digit_sum = digit_sum + dig
    n = n // 10

print("The total sum of digits is:", digit_sum)
