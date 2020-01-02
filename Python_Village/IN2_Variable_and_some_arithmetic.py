def hypo(filename):
    f = open(filename, "r")
    content: str = f.read()
    content = content.split(" ")

    hypotenuse = 0
    for i in range(len(content)):
        hypotenuse += int(content[i]) ** 2

    print(hypotenuse)


file = input()
hypo(file)
