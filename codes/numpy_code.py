# import numpy as np
# import matplotlib.pyplot as plt

# # Z = np.ones((10,10))
# # Z[1:-1, 1:-1] = 0
# # print(Z)
# # # print(Z.mean())
#
# # print(0 * np.nan)
# # print(np.nan == np.nan)
# # print(np.inf > np.nan)
# # print(np.nan > np.inf)
# # print(np.nan - np.nan)
# # print(0.3 == 3 * 0.1)
#
# # print(3 * 0.1)
#
# Z = np.arange(11)
# Z[(3 < Z) & (Z <= 8)] *= -1
# print(Z)
# t = np.linspace(0, 2 * np.pi, 50)
# x = np.sin(t)
# y = np.cos(t)
#
# # plt.figure()
#
# plt.plot(x)
#
# plt.show()

import numpy as np

# s = np.random.binomial(5000, 6/5000, 1000)
# count, bins, ignored = plt.hist(s, 30)
# plt.show()


# b = a.reshape((3, 3))
#
# print(b)
#
# print(b * 10 + 4)

# a = np.array([1, 2, 3, 4, 5])


# print(a.any())


# print(a.sum(axis=-1))

# b = np.arange(10)
#
# c = np.linspace(0, 1, 5)
#
# print(a)
# print(b)
# print(c)

# a = np.array([2, 5, 6, 3, 6, 3, 4, 1]).reshape((2, 4))

# np.savetxt('test.txt', a)

a = np.loadtxt('test.txt', delimiter=',')
print(a)

#
# print(np.sort(a, axis=None))

import matplotlib.pyplot as plt

# x = 2 * np.pi / 100 * np.arange(100)
#
# y = np.sin(x)
# plt.plot(x, y)
#
# y += np.random.normal(0, 0.05, size=100)
# plt.plot(x, y)

# x = np.linspace(-np.pi, np.pi, 200)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.title("My first plot")
# plt.plot(x, y1, "r-")
# plt.plot(x, y2, color="blue", linewidth=2.0, linestyle=":")
# plt.ylabel('y value')
# plt.xlabel('x value')
# n = 1024
# X = np.random.normal(0,1,n)
# Y = np.random.normal(0,1,n)
# plt.scatter(X,Y,s=1)
# plt.savefig("figure5.pdf")

# plt.savefig("figure1.png")

plt.show()

