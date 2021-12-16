# 592
# 2897
m=[[int(x)for x in y]for y in open('a').read().splitlines()];S=100
g={(x,y):m[y][x]for x in range(S)for y in range(S)}
def f(s,t,h,j):
 q=[(h,s[0],s[1])]
 while q:
  q=[(h,x,y)for h,x,y in q if(x,y)not in j or j[(x,y)]>h];h,x,y=min(q);q.remove((h,x,y));j[(x,y)]=h
  if(x,y)==t:return j[(x,y)]
  for a,b in[c for c in((x,y+1),(x-1,y),(x+1,y),(x,y-1))if c in g]:q+=[(h+g[(a,b)],a,b)]
print(f((0,0),(S-1,S-1),0,{}))
for z in[lambda:(x+i*S,y),lambda:(x,y+i*S)]:
 n={}
 for x,y in g:
  for i in 1,2,3,4:n[z()]=(g[(x,y)]+i-1)%9+1
 g.update(n)
print(f((0,0),(S*5-1,S*5-1),0,{}))


# 950 760 632 586