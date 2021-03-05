a = input("Enter First Number: \n")

while not a.isnumeric():
    a = input("Please enter valid number: \n")

b = input("Enter Second Number: \n")

while not b.isnumeric():
    b = input("Please enter valid number: \n")


sum = int(a) + int(b)

if sum > 10:
    print("Sum of your numbers is greater than 10!")
elif sum < 10:
    print("Sum of your numbers is smaller than 10!")
else:
    print("Sum of your numbers is equal 10!")



