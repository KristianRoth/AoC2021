# 1546
# 471
m=[int(a)for a in open('a').read()if a!='\n'];S=10;c=0
T=lambda s:[s+j for j in[-1,0,1]if 0<=s+j<S]
for r in range(S**S):
 if sum(m)==0:print(r);break
 *m,=map(lambda s:s+1,m)
 while max(m)>9:
  for i in range(S*S):
   if m[i]>9:
    c+=1;X,Y=i%S,i//S;m[i]=0
    for x,y in[(x,y)for x in T(X)for y in T(Y)]:m[(y)*S+x]+=(1,0)[0==m[y*S+x]or x==X<S>Y==y]
 if r==99:print(c)

# 589 487 484 482 464 415 411 403 401 372 370