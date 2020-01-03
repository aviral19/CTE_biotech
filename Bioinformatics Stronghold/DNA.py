f = open("rosalind_dna.txt", "r")

content = f.read()

countA, countC, countG, countT = 0, 0, 0, 0

for letter in content:
    if letter == "A":
        countA += 1
    elif letter == "C":
        countC += 1
    elif letter == "G":
        countG += 1
    elif letter == "T":
        countT += 1

print(str(countA) + " " + str(countC) + " " + str(countG) + " " + str(countT))
