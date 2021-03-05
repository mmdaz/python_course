# squares = []
# for i in range(10):
#     if i % 2 == 0:
#         squares.append(i ** 2)
#
# new_squares = [x ** 2 for x in range(10) if x % 2 == 0]
#
# print(new_squares)
# print(squares)

sentence = "I am Muhammad!"

print([word.lower() for word in sentence.split()])
