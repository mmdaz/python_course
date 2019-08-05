n = int(input('')) // 2
k = int((n+1) / 2)
for i in range(n):
    print((i+1) * '* ')
for i in range(n):
    print((n - i - 1)* '* ')
# n = int(input())
# for num1 in range(1, n+1):
#     for num2 in range(0, num1):
#         print("*", end="")
#     print("")
