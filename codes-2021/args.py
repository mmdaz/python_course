def sum(*args):
    result = 0
    for n in args:
        result += n

    print(result)


machine_factory = 2


def product(*nums, scale=1):
    p = scale
    for n in nums:
        p *= n
    return p


product(1, 2, 3, 5, 78, 79)


def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))
    for k, v in speaker_info.items():
        print(k, v, sep=': ')


def foo():
    """
    Summary line: do nothing, but document it.
    Description: No, really, it doesn't do anything.
    """
    pass


print(format.__doc__)

# authorize("Muhammad", name="Muhammad", username="mmdaz", password="123456", email="a@b.com", city="Maragheh")
