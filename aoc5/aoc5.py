# 7468
# 22364
a=[[*map(int,x.replace('->',',').split(','))]for x in open('a')]
t=1000;b=[0]*t*t;*d,=b;c=lambda x:(x>0)-(x<0);f=lambda s:s>1
def u(d,l):
 x,y,z,w=l;d[y*t+x]+=1
 while x!=z or y!=w:x-=c(x-z);y-=c(y-w);d[y*t+x]+=1
for l in a:u(b,l);x,y,z,w=l;(x!=z<t>y!=w)or u(d,l)
for i in d,b:print(sum(map(f,i)))

# 496 350 335 323 320 312 303 302 301 300 298 297