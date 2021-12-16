# 925
# 342997120375

from math import*
m=int(open('a').read(),16);I=lambda s:int(s,2);S=lambda s,m:(m[:s],m[s:])
m=bin(m)[2:];m=(4-len(m)%4)%4*'0'+m;s=[0]
O=[sum,prod,min,max,0,lambda s:s[0]>s[1],lambda s:s[0]<s[1],lambda s:s[0]==s[1]]
def p(m):
 V,m=S(3,m);T,m=S(3,m);T=I(T);s[0]+=I(V);l=""
 while T==4:
  A,m=S(5,m);l+=A[1:]
  if A[0]!='1':return m,I(l)
 i,m=S(1,m);b=(15,11)[i=='1'];i,m=S(b,m);l=I(i);h=[];n=len(m)
 for i in range(l):
  m,j=p(m);h+=[j]
  if b==15>0<n-len(m)>=l:break
 return m,O[T](h)
m,a=p(m);print(s[0],a)

# 1788 1041 905 894 873 666 605 571 563 543 521 512 509 506

