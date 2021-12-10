# 415953
# 2292863731
m=open('a').read().split()
p='([{<';s={')':3,']':57,'}':1197,'>':25137}
x=[];f=0
for w in m:
 a=eval("w"+".replace('%s','')"*4%((),[],{},'<>')*len(w))
 b=[x for x in a if x in s]
 if b:f+=s[b[0]]
 else:
  c=0
  for i in a[::-1]:c=c*5-~p.index(i)
  x+=[c]
x.sort()
print(f,x[len(x)//2])
# 1043 738 547 439 427 429 428 339 330 328 317 315 300 292 291 285