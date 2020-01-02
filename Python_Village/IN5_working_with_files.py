
f = open("rosalind_ini5.txt", "r")
content = f.readlines()
f2 = open("newfile.txt", "w")


for i in range(len(content)):
    if i%2 == 1:
        f2.write(content[i])

