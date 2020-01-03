f = open("rosalind_rna.txt", "r")

content = f.read()
content = list(content)

for i in range(len(content)):
    if content[i] == "T":
        content[i] = "U"

new = ""
for x in content:
    new += x

print(new)