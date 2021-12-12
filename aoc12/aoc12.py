# 4495
# 131254
k='start'
def e(g,r,o=0):
 c=r[-1];l=[*filter(lambda s:s.islower()and s!=k,r)];j=[];f=len(l)-len(set(l));p=[x for x in g if c in x]
 if len(p)==0 or(f==2 and o):return[]
 if c=='end':return[r]
 for n in p:j+=e(g if c.isupper()or f==0!=o and c!=k else[x for x in g if c not in x],r+[n[n.index(c)^1]],o)
 return j
for i in 0,1:print(len(e([x.rstrip().split('-')for x in open('a')],[k],i)))

# 812 625 516 459 398 387