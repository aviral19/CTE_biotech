from collections import defaultdict
f = open("rosalind_ini6.txt", "r")

content = f.read()
content = content.split(' ')

test_dict = defaultdict(int)

for i in range(len(content)):
    if content[i] in test_dict.keys():
        test_dict[content[i]] += 1
    else:
        test_dict[content[i]] = 1

for key, value in test_dict.items():
    print (str(key) +" "+  str(value))