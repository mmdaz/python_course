from datetime import datetime


def not_during_the_night(func):
    def wrapper(*args, **kwargs):
        if 7 <= datetime.now().hour < 22:
            func(*args, **kwargs)
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


@do_twice
def greet(name):
    print("Hello {}!".format(name))


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi = return_greeting("Muhammad")

print(hi)
