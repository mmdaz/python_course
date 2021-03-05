"""
Woooooow!


"""

n = int(input())

# print("W{}w!".format("o" * n))

# a = ""
# for i in range(n):
#     a += "o"
#
# print("W{}w!".format(a))

letter = "W"
t = 0
while t < n:
    letter += "o"
    t += 1

print(letter + "w!")
