with open("test.txt", "r+") as f:
    content = f.readlines()
    for c in content:
        separated = c.split()
        name = separated[0]
        wins = int(separated[1])
        loses = int(separated[2])
        scores = "\n{name}: {score} ".format(name=separated[0], score=100 * wins / (wins + loses))
        f.write(scores)

