a = int(input())
b = int(input())

# if b == 0:
#     raise Exception("Invalid Input b: {}".format(b))

try:
    print(a / b)
except ZeroDivisionError as e:
    print(e)

print("Done!")

a = []

for i in range(5):
    a.append(input())
