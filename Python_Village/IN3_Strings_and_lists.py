def stringslice(filename)
    f = open(filename,"r")
    content = f.readlines()
    print(content)
    rangelist = content[1].split(" ")

    for i in range(len(rangelist)):
        rangelist[i] = int(rangelist[i])

    print(content[0][rangelist[0]:rangelist[1]+1] + " " + content[0][rangelist[2]:rangelist[3]+1])

file = input()
stringslice(file)