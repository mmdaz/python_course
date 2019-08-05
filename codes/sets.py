n = int(input("enter your range:\n"))

in_list = []

for i in range(n):
    in_list.append(input())

print(in_list)

set_from_list = set(in_list)

duplicated_list = list(set_from_list)

print(duplicated_list)