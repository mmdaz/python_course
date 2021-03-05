def first_foo():
    print("this is from first foo")


def second_foo():
    print("this is from second foo")


def bar(func, retry=2):
    for i in range(retry):
        func()


bar(first_foo, 3)
bar(second_foo, 5)
