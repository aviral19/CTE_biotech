f = open("rosalind_revc.txt", "r")

content = f.read()
str = list(content)

str.reverse()

for i in range(len(str)):
    if(str[i]) == "A":
        str[i] = "T"
    elif(str[i]) == "T":
        str[i] = "A"
    elif(str[i]) == "G":
        str[i] = "C"
    elif(str[i]) == "C":
        str[i] = "G"

new = ""
new = new.join(str)
print(new)
