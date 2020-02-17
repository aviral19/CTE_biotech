def rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbits(n - 2, k) * k + rabbits(n - 1, k)


f = open("rosalind_fib.txt", "r")

content = f.read()
content = content.split(" ")

n = int(content[0])
k = int(content[1])

print(rabbits(n, k))