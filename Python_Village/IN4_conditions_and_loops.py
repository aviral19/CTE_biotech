def sumofodd(filename):
    f = open(filename, "r")
    content: str = f.read()
    content = content.split(" ")
    for i in range(len(content)):
        content[i] = int(content[i])
    sumtotal = 0
    for i in range(content[0], content[1]+1):
        if i%2==1:
            sumtotal += i
    print(sumtotal)


f = input()
sumofodd(f)