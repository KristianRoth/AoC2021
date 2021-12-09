# 508
# 1564640
m=[int(c)for c in open('a').read()if c!='\n'];S=100
t=[[-1,0],[1,0],[0,-1],[0,1]]
def f(i):*r,=map(lambda c:(x:=c[0],y:=c[1],m[y*S+x]if x>-1<y<S>x else S)[2],[(i%S+x,i//S+y)for x,y in t]);x,y=t[r.index(min(r))];j=i+x+y*S;return f(j)if m[j]<m[i]else i
a=[f(x)for x in range(S*S)if m[x]!=9]
b=[*set(a)]
print(sum(map(lambda i:m[i],b))+len(b))
d={i:a.count(i)for i in set(a)}
a=[*d.values()]
a.sort()
print(a[-1]*a[-2]*a[-3])

# 643 555 543 514 514 484 446 422