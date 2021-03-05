# date = "06-11-2020"
# separated = date.split(sep="-")
#
# print(separated)
# for s in separated:
#     print(s)

# result = ", ".join(["Muhammad", "Ali", "Hasan"])
# print("join: ", result)
# print("Split: ", result.split(", "))


name = "Muhammad"
age = 22

print("My name is {name} and My age is {age} {} {}".format(1, 2, name=name, age=age))

print("My name is {name}, My age is {age}".format(name=name, age=age))

print("My name is " + name + ", My age is", str(age))

captains = [1, 2]

print("first caps: {caps[0]}, second caps: {caps[1]}".format(caps=captains))
