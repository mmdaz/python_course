# t = (1, 2, "Muhammad", "Ali")
#
# print(t[1])
# print(len(t))
#
# a, b, c, d = t
#
# print(a, b, c, d)

l = ["Muhammad", "Ali", "Hasan"]

for index, value in enumerate(l):
    print("{} {}".format(index, value))

for i in range(len(l)):
    print("{} {}".format(i, l[i]))
