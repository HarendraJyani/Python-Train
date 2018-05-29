from itertools import combinations_with_replacement

s,a = input().split()
l = []
for i in range(len(s)):
    l.append(s[i])
l.sort()
p = list(combinations_with_replacement(l,int(a)))
for i in range(len(p)):
    for j in range(int(a)):
        if(j==int(a)-1):
            print(p[i][j])
        else:
            print(p[i][j],end="")
