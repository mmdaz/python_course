def read_int():
    """Read an integer from the user (better)."""
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops! Invalid input. Try again...")
    return x


if __name__ == '__main__':
    print(read_int())
