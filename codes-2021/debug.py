def debug(func):
    def wrapper(*args, **kwargs):
        print("Function variables: ")
        print(args)
        print(kwargs)
        value = func(*args, **kwargs)
        print("function {} returned {}".format(func.__name__, value))
        return value

    return wrapper


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting(name="Muhammad", age=22)
