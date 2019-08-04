s = "muhammad"

my_list = [1, "dsa", True]

# for ch in s:
#     print(ch, end=" ")

# for t in my_list:
#     print(type(t))

# for i in range(10):
#     print(i)

# word = input("enter sth:")
# counter = 0
#
# for ch in word:
#     print(counter, ":", ch)
#     counter += 1
#
# for i in range(len(word)):
#     print(i, ":", word[i])

# for i in range(1, 1001):
#     if i % 2 == 0:
#         print(i, ": even")
#     else:
#         print(i, ": odd")

# word = input("enter sth:\n")
# counter = 0
#
# while counter < len(word):
#     print(counter, ":", word[counter])
#     counter += 1

# s = "STELLAR"
#
# print(s.find("AR"))
#
# for ch in s:
#     if ch in "EL":
#         continue
#     print(ch, end="*")
#
# for i in range(10):
#     if i == 6:
#         break
#     print(i)

# number = int(input("enter your range number:"))
#
# numbers_list = []
#
# for i in range(number):
#     numbers_list.append(int(input("enter {}'th number".format(i + 1))))
#
# for number in numbers_list:
#     print("result : {}".format(number ** 2))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in matrix:
    for j in i:
        print(j)



# age = 10
#
# s = "exapmle: {age}, {test}, {test1}".format(test=45, age=age, test1="sd")
#
# print(s)