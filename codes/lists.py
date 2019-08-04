l_1 = [1, 2, True, "muhammad", -3.5, 2 > 3]

print(l_1)


# l_1 = l_1[:2] + l_1[3:]
# l_1[2] = None

l_1.remove(l_1[2])

print(l_1)




a = 6

l_2 = ['fd', 5, 10, False, a]

b = 7

l_3 = [l_1, l_2, b]

l_3.append(4)

print(l_3)
print(l_3.index(4))

l_3.remove(4)

print(l_3)

l_3.insert(2, 56)

print(l_3)

print(l_3[0].insert(0, 65498))

print(l_3)

l_3.insert(2, [1, 3])

print(l_3)


# print(l_1)
#
# print(l_1[2:])
#
# print(l_1[2::2])

# print(l_3)
# print(l_3[0][3:])




print(len(l_3))

print(2 in l_1 and 3 in l_1)

s = "muhammad"

print("m" in s)