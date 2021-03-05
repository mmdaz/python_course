def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
        ok = input(prompt)
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False


ask_yn(prompt="Hello!\n")

print("dasdasd", "dasdasdas", "dasdasd", 2, 45, 789645, 453453, 54545, "dsdasd", 41564)
