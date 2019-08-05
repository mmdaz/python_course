z = 5


def foo(y, x=2):
    global z
    z = 63
    global a
    a = 5
    print(locals())
    print(globals()['z'])
    print(x, y, z)


def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    print(prompt)
    for i in range(retries):
        ok = input()
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False

if __name__ == '__main__':
    ask_yn(prompt="start!!!\n", complaint="naaaaaaa")


