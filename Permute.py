from itertools import permutations
s,a = input().split()
l = []
a = int(a)
for i in range(len(s)):
    l.append(s[i])
l.sort()
p = list(permutations(l,a))
for i in range(len(p)):
    for j in range(a):
        if j == a-1:
            print(p[i][j])
        else:
            print(p[i][j],end="")
