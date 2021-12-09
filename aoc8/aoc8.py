# 521
# 1016804

m=[x.replace('|','').split()for x in open('a')];H=range;F=filter;M=map;S=set;L=len;Y=[2,3,4];T=10
print(sum(M(lambda a:L([*F(lambda s:L(s)in[7]+Y,a[T:])]),m)))
h=[[*F(lambda x:0x37FF4BEF5AEDB75277>>(x+s*7)&1,H(7))]for s in H(T)]
def d(e,v=""):
 *t,=M(lambda s:S(s),e[:T]);x=S('abcdefg');r=S(x)
 for s in F(lambda s:L(s)==6,t):x&=s
 k=[(r&x,r-x)[i in Y]for i in H(7)]
 for s in t:
  *p,=F(lambda x:L(x)==L(s),h)
  if L(p)<2:k=[(k[i]-s,k[i]&s)[i in p[0]]for i in H(7)]
 for b in e[T:]:
  for i in H(T):
   if S(''.join(M(lambda s:''.join(k[s]),h[i])))==S(b):v+=str(i)
 return int(v)
print(sum(M(d,m)))

# 1222 1203 774 749 748 702 688 677 676 674 638 636 613 612 607 601 600 599