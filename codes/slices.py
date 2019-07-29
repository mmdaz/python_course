# s = "muhammad"
#
# print(s[2:6:1])
# print(s[2:6:2])
# print(s[6:2:-2])

x = "123456789"

print(int(x[:3]) + int(x[3:6]) + int(x[6:]))

s_1 = x[:3]
s_2 = x[3:6]
s_3 = x[6:]

i_1 = int(s_1)
i_2 = int(s_2)
i_3 = int(s_3)

print(i_1 + i_2 + i_3)