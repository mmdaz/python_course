d = {"Muhammad": 100, "Ali": 2, "Hasan": 3}

# for key in d.keys():
#     print(key)
#
# for value in d.values():
#     print(value)

for item in d.items():
    print("key: {}, Value: {}".format(item[0], item[1]))
